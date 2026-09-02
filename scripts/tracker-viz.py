#!/usr/bin/env python3
"""
tracker-viz.py — Interactive tracker visualization + editor

Modes:
    python scripts/tracker-viz.py                  # start server on :5111
    python scripts/tracker-viz.py --port 8080      # custom port
    python scripts/tracker-viz.py --open            # start + open browser
    python scripts/tracker-viz.py --static          # static HTML (read-only)
    python scripts/tracker-viz.py --static --open   # static + open

Features:
  - Dark mode, high-contrast colors
  - Full CRUD: create/edit/delete tasks, sections, subsections
  - Add/remove dependencies (shift-click or form)
  - Collapsible sections (double-click to toggle)
  - Undo/redo (Ctrl+Z / Ctrl+Shift+Z)
  - Auto-save layout positions to localStorage
  - Git auto-commit on save
  - Save writes back to TRACKER.md + TRACKER-DEPS.json
"""

import re
import json
import copy
import subprocess
import argparse
import logging
import webbrowser
import time
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DEFAULT_TRACKER = PROJECT_ROOT / "problems" / "TRACKER.md"
DEFAULT_DEPS = PROJECT_ROOT / "problems" / "TRACKER-DEPS.json"

# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

TASK_RE = re.compile(
    r"^-\s+\[(.)\]\s+\*\*([A-Z]\d+(?:\.\d+[a-z]?)*)\*\*\s+(.+)$"
)
SECTION_RE = re.compile(r"^##\s+(P\d+):\s*(.+)$")
SUBSECTION_RE = re.compile(r"^###\s+(P\d+\.\d+[a-z]?):\s*(.+)$")
REF_RE = re.compile(r"P\d+\.\d+[a-z]?(?:\.\d+[a-z]?)?")

STATUS_CHAR = {
    "open": " ", "done": "x", "in_progress": "~",
    "blocked": "!", "killed": "K", "needs_research": "?",
}
STATUS_NAME = {v: k for k, v in STATUS_CHAR.items()}
STATUS_LABELS = {
    "open": "Open", "done": "Done", "in_progress": "In Progress",
    "blocked": "Blocked", "killed": "Killed", "needs_research": "Needs Research",
}

# Dark-mode color palettes (GitHub Dark inspired)
SECTION_COLORS = {
    "P0": {"bg": "#2a1519", "border": "#f85149", "label": "Existential"},
    "P1": {"bg": "#0d2240", "border": "#58a6ff", "label": "Evidence"},
    "P2": {"bg": "#2a2210", "border": "#e3b341", "label": "Hardware"},
    "P3": {"bg": "#0d2818", "border": "#3fb950", "label": "Attachment"},
    "P4": {"bg": "#1e1535", "border": "#bc8cff", "label": "Business"},
    "P5": {"bg": "#0d2a2a", "border": "#39d2c0", "label": "UX"},
    "P6": {"bg": "#2a1e10", "border": "#f0883e", "label": "Scope"},
    "P7": {"bg": "#1c2025", "border": "#8b949e", "label": "Regulatory"},
    "P8": {"bg": "#2a1525", "border": "#f778ba", "label": "Experiments"},
}

STATUS_COLORS = {
    "open":           {"bg": "#1c2128", "border": "#8b949e", "text": "#c9d1d9"},
    "done":           {"bg": "#0d2818", "border": "#3fb950", "text": "#a5d6a7"},
    "in_progress":    {"bg": "#0d2240", "border": "#58a6ff", "text": "#90caf9"},
    "blocked":        {"bg": "#341a00", "border": "#f0883e", "text": "#ffcc80"},
    "killed":         {"bg": "#3b1119", "border": "#f85149", "text": "#ffa4a2"},
    "needs_research": {"bg": "#1e1535", "border": "#bc8cff", "text": "#d2b3ff"},
}


def _short_title(desc):
    title_clean = re.sub(r"\*\*", "", desc)
    sent_end = re.search(r"[.!?]\s", title_clean)
    if sent_end and sent_end.start() < 80:
        return title_clean[: sent_end.start() + 1]
    elif len(title_clean) > 60:
        return title_clean[:57] + "..."
    return title_clean


class TrackerModel:
    """In-memory model of TRACKER.md with round-trip serialization and undo."""

    MAX_UNDO = 50

    def __init__(self, tracker_path, deps_path):
        self.tracker_path = Path(tracker_path)
        self.deps_path = Path(deps_path)
        self.blocks = []
        self.tasks = {}
        self.sections = []
        self.deps = []
        self.dirty = False
        self.load_time = 0
        self._undo_stack = []
        self._redo_stack = []
        self.reload()

    def _snapshot(self):
        """Return a deep copy of mutable state for undo."""
        return {
            "blocks": copy.deepcopy(self.blocks),
            "tasks": copy.deepcopy(self.tasks),
            "sections": copy.deepcopy(self.sections),
            "deps": copy.deepcopy(self.deps),
        }

    def _restore(self, snap):
        """Restore state from a snapshot."""
        self.blocks = snap["blocks"]
        self.tasks = snap["tasks"]
        self.sections = snap["sections"]
        self.deps = snap["deps"]
        self.dirty = True

    def _push_undo(self):
        """Save current state to undo stack before a mutation."""
        self._undo_stack.append(self._snapshot())
        if len(self._undo_stack) > self.MAX_UNDO:
            self._undo_stack.pop(0)
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            return {"ok": False, "error": "Nothing to undo"}
        self._redo_stack.append(self._snapshot())
        self._restore(self._undo_stack.pop())
        return {"ok": True}

    def redo(self):
        if not self._redo_stack:
            return {"ok": False, "error": "Nothing to redo"}
        self._undo_stack.append(self._snapshot())
        self._restore(self._redo_stack.pop())
        return {"ok": True}

    def reload(self):
        self.blocks = []
        self.tasks = {}
        self.sections = []
        self.dirty = False
        self.load_time = time.time()
        self._undo_stack.clear()
        self._redo_stack.clear()
        self._parse_tracker()
        self._load_deps()
        log.info("Loaded %d tasks, %d sections, %d deps",
                 len(self.tasks), len(self.sections), len(self.deps))

    def _parse_tracker(self):
        if not self.tracker_path.exists():
            raise FileNotFoundError(f"Not found: {self.tracker_path}")
        lines = self.tracker_path.read_text(encoding="utf-8").splitlines()
        current_section = None
        current_subsection = None
        current_task_id = None
        raw_buf = []
        in_p_section = False

        def flush_raw():
            if raw_buf:
                self.blocks.append({"type": "raw", "lines": list(raw_buf)})
                raw_buf.clear()

        for line in lines:
            sm = SECTION_RE.match(line)
            if sm:
                flush_raw(); current_task_id = None
                sid, stitle = sm.group(1), sm.group(2).strip()
                current_section = sid; current_subsection = None; in_p_section = True
                self.blocks.append({"type": "section", "id": sid, "title": stitle, "raw": line})
                self.sections.append({"id": sid, "title": re.sub(r"\s*—.*$", "", stitle), "subsections": []})
                continue

            if re.match(r"^##\s+", line) and not SECTION_RE.match(line):
                flush_raw(); current_task_id = None
                current_section = None; current_subsection = None; in_p_section = False
                raw_buf.append(line); continue

            ssm = SUBSECTION_RE.match(line)
            if ssm and in_p_section:
                flush_raw(); current_task_id = None
                ssid, sstitle = ssm.group(1), ssm.group(2).strip()
                current_subsection = ssid
                self.blocks.append({"type": "subsection", "id": ssid, "title": sstitle, "parent": current_section, "raw": line})
                if self.sections:
                    self.sections[-1]["subsections"].append({"id": ssid, "title": re.sub(r"\s*—.*$", "", sstitle)})
                continue

            tm = TASK_RE.match(line) if in_p_section else None
            if tm:
                flush_raw()
                status_char, tid, desc = tm.group(1), tm.group(2), tm.group(3).strip()
                current_task_id = tid
                self.tasks[tid] = {
                    "id": tid, "status": STATUS_NAME.get(status_char, "open"),
                    "title": _short_title(desc), "first_desc": desc, "description": desc,
                    "section": current_section, "subsection": current_subsection, "continuation": [],
                }
                self.blocks.append({"type": "task", "id": tid}); continue

            if current_task_id and line.startswith("  ") and line.strip():
                t = self.tasks[current_task_id]
                t["continuation"].append(line)
                t["description"] += " " + line.strip()
                continue

            current_task_id = None; raw_buf.append(line)
        flush_raw()

    def _load_deps(self):
        if self.deps_path.exists():
            with open(self.deps_path, "r", encoding="utf-8") as f:
                self.deps = json.load(f)
        else:
            self.deps = []
        task_ids = set(self.tasks.keys())
        dep_keys = {(d["source"], d["target"]) for d in self.deps}
        for task in self.tasks.values():
            for ref in REF_RE.findall(task["description"]):
                if ref != task["id"] and ref in task_ids and (task["id"], ref) not in dep_keys:
                    self.deps.append({"source": task["id"], "target": ref, "reason": "inline ref", "auto": True})
                    dep_keys.add((task["id"], ref))

    def serialize_tracker(self) -> str:
        lines = []
        for block in self.blocks:
            if block["type"] == "raw":
                lines.extend(block["lines"])
            elif block["type"] in ("section", "subsection"):
                lines.append(block["raw"])
            elif block["type"] == "task":
                task = self.tasks.get(block["id"])
                if task:
                    sc = STATUS_CHAR.get(task["status"], " ")
                    lines.append(f"- [{sc}] **{task['id']}** {task['first_desc']}")
                    lines.extend(task["continuation"])
        return "\n".join(lines) + "\n"

    def save(self):
        if self.tracker_path.exists():
            if self.tracker_path.stat().st_mtime > self.load_time:
                return {"ok": False, "error": "File modified externally. Reload first."}

        content = self.serialize_tracker()
        tmp = self.tracker_path.with_suffix(".md.tmp")
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(self.tracker_path)

        manual_deps = [d for d in self.deps if not d.get("auto")]
        tmp_d = self.deps_path.with_suffix(".json.tmp")
        with open(tmp_d, "w", encoding="utf-8") as f:
            json.dump(manual_deps, f, indent=2)
        tmp_d.replace(self.deps_path)

        self.dirty = False
        self.load_time = time.time()

        # Git auto-commit
        git_msg = self._git_commit()
        log.info("Saved TRACKER.md (%d tasks) + TRACKER-DEPS.json (%d deps)",
                 len(self.tasks), len(manual_deps))
        return {"ok": True, "git": git_msg}

    def _git_commit(self):
        """Auto-commit tracker files if in a git repo."""
        try:
            tracker_rel = str(self.tracker_path.relative_to(PROJECT_ROOT)).replace("\\", "/")
            deps_rel = str(self.deps_path.relative_to(PROJECT_ROOT)).replace("\\", "/")
            subprocess.run(
                ["git", "add", tracker_rel, deps_rel],
                cwd=str(PROJECT_ROOT), capture_output=True, timeout=10,
            )
            result = subprocess.run(
                ["git", "commit", "-m", "tracker-viz: update tracker"],
                cwd=str(PROJECT_ROOT), capture_output=True, text=True, timeout=10,
            )
            if result.returncode == 0:
                log.info("Git: committed tracker changes")
                return "committed"
            elif "nothing to commit" in result.stdout:
                return "no changes"
            else:
                log.warning("Git commit failed: %s", result.stderr.strip())
                return f"failed: {result.stderr.strip()[:100]}"
        except Exception as e:
            log.warning("Git commit error: %s", e)
            return f"error: {e}"

    # --- Mutations (all push undo) ---

    def update_task_status(self, task_id, new_status):
        if task_id not in self.tasks:
            return {"ok": False, "error": f"Task {task_id} not found"}
        if new_status not in STATUS_CHAR:
            return {"ok": False, "error": f"Invalid status: {new_status}"}
        self._push_undo()
        self.tasks[task_id]["status"] = new_status
        self.dirty = True
        return {"ok": True}

    def update_task_description(self, task_id, new_desc):
        if task_id not in self.tasks:
            return {"ok": False, "error": f"Task {task_id} not found"}
        self._push_undo()
        task = self.tasks[task_id]
        task["description"] = new_desc
        task["first_desc"] = new_desc
        task["continuation"] = []
        task["title"] = _short_title(new_desc)
        self.dirty = True
        return {"ok": True}

    def delete_task(self, task_id):
        if task_id not in self.tasks:
            return {"ok": False, "error": f"Task {task_id} not found"}
        self._push_undo()
        del self.tasks[task_id]
        self.blocks = [b for b in self.blocks if not (b["type"] == "task" and b["id"] == task_id)]
        self.deps = [d for d in self.deps if d["source"] != task_id and d["target"] != task_id]
        self.dirty = True
        return {"ok": True}

    def create_task(self, section, subsection, status, description):
        prefix = subsection or section
        if not prefix:
            return {"ok": False, "error": "Section required"}
        self._push_undo()
        existing = [tid for tid in self.tasks if tid.startswith(prefix + ".")]
        max_num = 0
        for tid in existing:
            m = re.match(r"(\d+)", tid[len(prefix) + 1:])
            if m:
                max_num = max(max_num, int(m.group(1)))
        new_id = f"{prefix}.{max_num + 1}"
        if new_id in self.tasks:
            new_id = f"{prefix}.{max_num + 2}"

        task = {
            "id": new_id, "status": status or "open", "title": _short_title(description),
            "first_desc": description, "description": description,
            "section": section, "subsection": subsection, "continuation": [],
        }
        self.tasks[new_id] = task

        insert_idx = len(self.blocks)
        target = subsection or section
        found = False; last_task = None
        for i, block in enumerate(self.blocks):
            if block["type"] in ("section", "subsection") and block["id"] == target:
                found = True
            elif found:
                if block["type"] == "task" and self.tasks.get(block["id"], {}).get("subsection") == subsection and self.tasks.get(block["id"], {}).get("section") == section:
                    last_task = i
                elif block["type"] in ("section", "subsection"):
                    break
        if last_task is not None:
            insert_idx = last_task + 1
        elif found:
            for i, block in enumerate(self.blocks):
                if block["type"] in ("section", "subsection") and block["id"] == target:
                    insert_idx = i + 1; break

        self.blocks.insert(insert_idx, {"type": "task", "id": new_id})
        self.dirty = True
        return {"ok": True, "id": new_id}

    def create_section(self, section_id, title):
        if any(s["id"] == section_id for s in self.sections):
            return {"ok": False, "error": f"Section {section_id} already exists"}
        self._push_undo()
        raw_line = f"## {section_id}: {title}"
        self.sections.append({"id": section_id, "title": title, "subsections": []})
        insert_idx = len(self.blocks)
        for i, block in enumerate(self.blocks):
            if block["type"] == "raw":
                if any("Research Index" in l for l in block["lines"]):
                    insert_idx = i; break
        self.blocks.insert(insert_idx, {"type": "raw", "lines": ["", "---", ""]})
        self.blocks.insert(insert_idx + 1, {"type": "section", "id": section_id, "title": title, "raw": raw_line})
        self.blocks.insert(insert_idx + 2, {"type": "raw", "lines": [""]})
        self.dirty = True
        return {"ok": True}

    def create_subsection(self, parent_section, sub_id, title):
        parent = next((s for s in self.sections if s["id"] == parent_section), None)
        if not parent:
            return {"ok": False, "error": f"Section {parent_section} not found"}
        if any(ss["id"] == sub_id for ss in parent["subsections"]):
            return {"ok": False, "error": f"Subsection {sub_id} already exists"}
        self._push_undo()
        raw_line = f"### {sub_id}: {title}"
        parent["subsections"].append({"id": sub_id, "title": title})
        insert_idx = len(self.blocks)
        found = False
        for i, block in enumerate(self.blocks):
            if block["type"] == "section" and block["id"] == parent_section:
                found = True
            elif found and block["type"] == "section":
                insert_idx = i; break
        self.blocks.insert(insert_idx, {"type": "raw", "lines": [""]})
        self.blocks.insert(insert_idx + 1, {"type": "subsection", "id": sub_id, "title": title, "parent": parent_section, "raw": raw_line})
        self.dirty = True
        return {"ok": True}

    def add_dep(self, source, target, reason):
        if any(d["source"] == source and d["target"] == target for d in self.deps):
            return {"ok": False, "error": "Dependency already exists"}
        self._push_undo()
        self.deps.append({"source": source, "target": target, "reason": reason})
        self.dirty = True
        return {"ok": True}

    def remove_dep(self, source, target):
        before = len(self.deps)
        self._push_undo()
        self.deps = [d for d in self.deps if not (d["source"] == source and d["target"] == target)]
        if len(self.deps) == before:
            self._undo_stack.pop()
            return {"ok": False, "error": "Dependency not found"}
        self.dirty = True
        return {"ok": True}

    # --- Computed data ---

    def compute_phases(self):
        blockers = {tid: set() for tid in self.tasks}
        for d in self.deps:
            if d["source"] in blockers:
                blockers[d["source"]].add(d["target"])
        def depth(tid, visited=None):
            if visited is None: visited = set()
            if tid in visited: return 0
            visited.add(tid)
            t = self.tasks.get(tid)
            if not t or t["status"] in ("done", "killed"): return 0
            ob = [b for b in blockers[tid] if self.tasks.get(b, {}).get("status") not in ("done", "killed")]
            return 1 + max((depth(b, visited.copy()) for b in ob), default=0) if ob else 1
        labels = {0: "Done", 1: "Ready Now", 2: "Next Up", 3: "Mid-term", 4: "Later"}
        return {tid: (0, "Done") if self.tasks[tid]["status"] in ("done", "killed") else (min(depth(tid), 4), labels.get(min(depth(tid), 4), "Later")) for tid in self.tasks}

    def to_frontend_data(self):
        phases = self.compute_phases()
        elements = []
        for section in self.sections:
            sid = section["id"]
            c = SECTION_COLORS.get(sid, {"bg": "#1c2128", "border": "#8b949e", "label": sid})
            # Compute section progress
            sec_tasks = [t for t in self.tasks.values() if t["section"] == sid]
            done_count = sum(1 for t in sec_tasks if t["status"] in ("done", "killed"))
            total = len(sec_tasks)
            pct = round(done_count / total * 100) if total else 0
            elements.append({"data": {
                "id": sid, "label": f"{sid}: {section['title']}", "type": "section",
                "bg": c["bg"], "borderColor": c["border"],
                "progress": pct, "doneCount": done_count, "totalCount": total,
            }})
            for sub in section["subsections"]:
                elements.append({"data": {
                    "id": sub["id"], "label": f"{sub['id']}: {sub['title']}",
                    "parent": sid, "type": "subsection", "bg": c["bg"], "borderColor": c["border"],
                }})
        for tid, task in self.tasks.items():
            parent = task["subsection"] or task["section"]
            sc = STATUS_COLORS.get(task["status"], STATUS_COLORS["open"])
            pn, pl = phases.get(tid, (1, "Ready Now"))
            nt = task["title"][:42] + "..." if len(task["title"]) > 45 else task["title"]
            elements.append({"data": {
                "id": tid, "label": f"{tid}: {nt}", "shortLabel": tid, "title": task["title"],
                "description": task["description"], "status": task["status"],
                "statusLabel": STATUS_LABELS.get(task["status"], task["status"]),
                "section": task["section"], "subsection": task["subsection"] or "",
                "parent": parent, "type": "task", "phase": pn, "phaseLabel": pl,
                "bg": sc["bg"], "borderColor": sc["border"], "textColor": sc["text"],
            }})
        for i, dep in enumerate(self.deps):
            elements.append({"data": {
                "id": f"e{i}", "source": dep["source"], "target": dep["target"],
                "reason": dep.get("reason", ""), "auto": dep.get("auto", False),
            }})
        stats = {"total": len(self.tasks), "by_status": {}, "by_phase": {}}
        for t in self.tasks.values():
            stats["by_status"][t["status"]] = stats["by_status"].get(t["status"], 0) + 1
        for _, (_, pl) in phases.items():
            stats["by_phase"][pl] = stats["by_phase"].get(pl, 0) + 1

        return {
            "elements": elements, "stats": stats, "sections": self.sections,
            "dirty": self.dirty,
            "canUndo": len(self._undo_stack) > 0,
            "canRedo": len(self._redo_stack) > 0,
        }


# ---------------------------------------------------------------------------
# Flask server
# ---------------------------------------------------------------------------

def run_server(tracker_path, deps_path, port, open_browser):
    from flask import Flask, jsonify, request, Response
    app = Flask(__name__)
    model = TrackerModel(tracker_path, deps_path)

    @app.route("/")
    def index():
        return Response(generate_html(), mimetype="text/html")

    @app.route("/api/data")
    def api_data():
        return jsonify(model.to_frontend_data())

    @app.route("/api/task/<path:task_id>/status", methods=["POST"])
    def api_status(task_id):
        return jsonify(model.update_task_status(task_id, request.get_json().get("status")))

    @app.route("/api/task/<path:task_id>/description", methods=["POST"])
    def api_desc(task_id):
        return jsonify(model.update_task_description(task_id, request.get_json().get("description")))

    @app.route("/api/task/<path:task_id>", methods=["DELETE"])
    def api_delete(task_id):
        return jsonify(model.delete_task(task_id))

    @app.route("/api/task", methods=["POST"])
    def api_create():
        b = request.get_json()
        return jsonify(model.create_task(b.get("section"), b.get("subsection"), b.get("status", "open"), b.get("description", "")))

    @app.route("/api/section", methods=["POST"])
    def api_section():
        b = request.get_json()
        return jsonify(model.create_section(b.get("id"), b.get("title")))

    @app.route("/api/subsection", methods=["POST"])
    def api_subsection():
        b = request.get_json()
        return jsonify(model.create_subsection(b.get("parent"), b.get("id"), b.get("title")))

    @app.route("/api/dep", methods=["POST"])
    def api_add_dep():
        b = request.get_json()
        return jsonify(model.add_dep(b.get("source"), b.get("target"), b.get("reason", "")))

    @app.route("/api/dep", methods=["DELETE"])
    def api_rm_dep():
        b = request.get_json()
        return jsonify(model.remove_dep(b.get("source"), b.get("target")))

    @app.route("/api/save", methods=["POST"])
    def api_save():
        return jsonify(model.save())

    @app.route("/api/reload", methods=["POST"])
    def api_reload():
        model.reload(); return jsonify({"ok": True})

    @app.route("/api/undo", methods=["POST"])
    def api_undo():
        return jsonify(model.undo())

    @app.route("/api/redo", methods=["POST"])
    def api_redo():
        return jsonify(model.redo())

    if open_browser:
        import threading
        threading.Timer(0.8, lambda: webbrowser.open(f"http://localhost:{port}")).start()

    log.info("Server on http://localhost:%d", port)
    app.run(host="127.0.0.1", port=port, debug=False)


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

def generate_html(static_data=None):
    ds = "inline" if static_data else "api"
    ij = json.dumps(static_data) if static_data else "null"

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tracker</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#0d1117;display:flex;height:100vh;overflow:hidden;color:#c9d1d9}}
::selection{{background:#264f78;color:#fff}}
::-webkit-scrollbar{{width:8px}}
::-webkit-scrollbar-track{{background:#161b22}}
::-webkit-scrollbar-thumb{{background:#30363d;border-radius:4px}}
::-webkit-scrollbar-thumb:hover{{background:#484f58}}

#sidebar{{width:320px;min-width:320px;background:#161b22;border-right:1px solid #30363d;display:flex;flex-direction:column;z-index:10}}
#sidebar-header{{padding:10px 14px;border-bottom:1px solid #21262d;display:flex;align-items:center;justify-content:space-between}}
#sidebar-header h1{{font-size:14px;font-weight:700;color:#e6edf3}}
.hdr-actions{{display:flex;gap:5px}}
.hdr-btn{{padding:4px 10px;border:1px solid #30363d;background:#21262d;border-radius:5px;font-size:11px;cursor:pointer;color:#c9d1d9;font-weight:500}}
.hdr-btn:hover{{background:#30363d;border-color:#484f58}}
.hdr-btn.primary{{background:#238636;border-color:#2ea043;color:#fff}}
.hdr-btn.primary:hover{{background:#2ea043}}
.hdr-btn.warn{{background:#9e6a03;border-color:#bb8009;color:#fff}}
.hdr-btn.danger{{background:#da3633;border-color:#f85149;color:#fff}}
.hdr-btn:disabled{{opacity:0.4;cursor:default}}

#search-box{{padding:8px 14px;border-bottom:1px solid #21262d}}
#search-box input{{width:100%;padding:6px 10px;border:1px solid #30363d;border-radius:5px;font-size:12px;outline:none;background:#0d1117;color:#c9d1d9}}
#search-box input:focus{{border-color:#58a6ff;box-shadow:0 0 0 2px rgba(88,166,255,0.15)}}
#search-box input::placeholder{{color:#484f58}}

#filters{{padding:8px 14px;border-bottom:1px solid #21262d;overflow-y:auto;flex-shrink:0;max-height:38vh}}
#filters h3{{font-size:9px;text-transform:uppercase;letter-spacing:.7px;color:#484f58;margin:8px 0 3px}}
#filters h3:first-child{{margin-top:0}}
.fi{{display:flex;align-items:center;gap:5px;padding:2px 0;font-size:11px;cursor:pointer;user-select:none;color:#8b949e}}
.fi:hover{{color:#c9d1d9}}
.fi input{{width:13px;height:13px;cursor:pointer;accent-color:#58a6ff}}
.fd{{width:9px;height:9px;border-radius:50%;flex-shrink:0}}
.fc{{margin-left:auto;font-size:9px;color:#484f58;background:#21262d;padding:0 5px;border-radius:8px}}

.sidebar-sec{{padding:8px 14px;border-bottom:1px solid #21262d;display:flex;flex-wrap:wrap;gap:4px}}
.lb{{padding:3px 8px;border:1px solid #30363d;background:#21262d;border-radius:4px;font-size:10px;cursor:pointer;color:#8b949e}}
.lb:hover{{background:#30363d;color:#c9d1d9}}
.lb.active{{background:#0d2240;border-color:#58a6ff;color:#58a6ff}}

#detail-panel{{padding:12px 14px;overflow-y:auto;flex:1;font-size:12px;line-height:1.5}}
#detail-panel.empty{{display:flex;align-items:center;justify-content:center;color:#484f58;font-style:italic;font-size:11px}}
.dh{{display:flex;align-items:center;gap:6px;margin-bottom:6px;flex-wrap:wrap}}
.di{{font-size:16px;font-weight:700;color:#e6edf3}}
.db{{font-size:9px;padding:2px 6px;border-radius:10px;font-weight:600;text-transform:uppercase;letter-spacing:.3px}}
.ds{{font-size:10px;color:#484f58;margin-bottom:6px}}
.dt{{font-size:12px;font-weight:600;margin-bottom:4px;color:#e6edf3}}
.dd{{font-size:11px;color:#8b949e;line-height:1.6;word-break:break-word}}
.dd strong{{color:#c9d1d9}}
.dd code{{background:#21262d;padding:1px 4px;border-radius:3px;font-size:10px}}

.deps{{margin-top:10px;padding-top:8px;border-top:1px solid #21262d}}
.deps h4{{font-size:9px;text-transform:uppercase;letter-spacing:.5px;color:#484f58;margin-bottom:3px}}
.dl{{display:inline-block;padding:1px 6px;margin:2px 1px;background:#0d2240;color:#58a6ff;border-radius:3px;font-size:10px;font-weight:600;cursor:pointer}}
.dl:hover{{background:#1a3a5c}}
.dr{{font-size:9px;color:#484f58;font-style:italic}}
.dx{{font-size:10px;color:#f85149;cursor:pointer;margin-left:2px;font-weight:700}}
.dx:hover{{color:#ff7b72}}

.ec{{margin-top:10px;padding-top:8px;border-top:1px solid #21262d}}
.ec h4{{font-size:9px;text-transform:uppercase;letter-spacing:.5px;color:#484f58;margin-bottom:6px}}
.er{{margin-bottom:6px}}
.er label{{display:block;font-size:10px;color:#8b949e;margin-bottom:2px;font-weight:600}}
.er select,.er input,.er textarea{{width:100%;padding:5px 8px;border:1px solid #30363d;border-radius:4px;font-size:11px;font-family:inherit;background:#0d1117;color:#c9d1d9}}
.er textarea{{resize:vertical;min-height:60px}}
.ebtns{{display:flex;gap:6px;margin-top:6px}}
.eb{{padding:4px 12px;border:1px solid #30363d;background:#21262d;border-radius:4px;font-size:11px;cursor:pointer;color:#c9d1d9}}
.eb.save{{background:#238636;border-color:#2ea043;color:#fff}}
.eb.del{{background:#da3633;border-color:#f85149;color:#fff}}
.adr{{display:flex;gap:4px;margin-top:6px;align-items:center}}
.adr input{{flex:1;padding:4px 6px;border:1px solid #30363d;border-radius:3px;font-size:10px;background:#0d1117;color:#c9d1d9}}
.adb{{padding:3px 8px;background:#238636;color:#fff;border:none;border-radius:3px;font-size:10px;cursor:pointer}}

#canvas-container{{flex:1;position:relative;background:#0d1117}}
#cy{{width:100%;height:100%}}
.grid-bg{{position:absolute;top:0;left:0;right:0;bottom:0;background:radial-gradient(circle,#21262d 1px,transparent 1px);background-size:24px 24px;pointer-events:none;opacity:0.4}}

#view-modes{{position:absolute;top:10px;left:10px;display:flex;gap:4px;z-index:10}}
.vb{{padding:5px 10px;border:1px solid #30363d;background:#161b22;border-radius:6px;font-size:11px;cursor:pointer;box-shadow:0 1px 3px rgba(0,0,0,0.3);font-weight:500;color:#8b949e}}
.vb:hover{{background:#21262d;color:#c9d1d9}}
.vb.active{{background:#0d2240;border-color:#58a6ff;color:#58a6ff}}

#toolbar{{position:absolute;top:10px;right:10px;display:flex;flex-direction:column;gap:3px;z-index:10}}
.tb{{width:32px;height:32px;border:1px solid #30363d;background:#161b22;border-radius:6px;font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 3px rgba(0,0,0,0.3);color:#8b949e}}
.tb:hover{{background:#21262d;color:#c9d1d9}}
.tb.active{{background:#0d2240;border-color:#58a6ff;color:#58a6ff}}
.ts{{height:1px;background:#21262d;margin:1px 4px}}

#zoom-ind{{position:absolute;bottom:10px;right:10px;background:rgba(22,27,34,0.9);padding:3px 8px;border-radius:5px;font-size:10px;color:#484f58;border:1px solid #30363d;z-index:10;pointer-events:none}}
#edge-tt{{display:none;position:absolute;background:rgba(22,27,34,0.95);color:#c9d1d9;padding:3px 8px;border-radius:4px;font-size:10px;pointer-events:none;z-index:20;white-space:nowrap;border:1px solid #30363d}}

#dep-modal{{display:none;position:absolute;z-index:50;background:#161b22;border:1px solid #30363d;border-radius:8px;padding:14px 18px;box-shadow:0 4px 16px rgba(0,0,0,0.4);min-width:280px;color:#c9d1d9}}
#dep-modal h3{{font-size:13px;margin-bottom:8px;color:#e6edf3}}
#dep-modal .dmr{{margin-bottom:6px;font-size:12px}}
#dep-modal .dmr span{{font-weight:600;color:#58a6ff}}
#dep-modal input{{width:100%;padding:5px 8px;border:1px solid #30363d;border-radius:4px;font-size:11px;margin-top:2px;background:#0d1117;color:#c9d1d9}}
#dep-modal .dmb{{display:flex;gap:6px;margin-top:8px}}
#dep-modal .dm{{padding:4px 12px;border:1px solid #30363d;background:#21262d;border-radius:4px;font-size:11px;cursor:pointer;color:#c9d1d9}}
#dep-modal .dm.pri{{background:#238636;border-color:#2ea043;color:#fff}}

#ntm{{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.6);z-index:60;align-items:center;justify-content:center}}
#ntm.visible{{display:flex}}
#ntf{{background:#161b22;border-radius:10px;padding:20px 24px;min-width:380px;box-shadow:0 8px 32px rgba(0,0,0,0.4);border:1px solid #30363d}}
#ntf h2{{font-size:15px;margin-bottom:12px;color:#e6edf3}}
.nr{{margin-bottom:8px}}
.nr label{{display:block;font-size:11px;color:#8b949e;margin-bottom:2px;font-weight:600}}
.nr select,.nr input,.nr textarea{{width:100%;padding:6px 10px;border:1px solid #30363d;border-radius:5px;font-size:12px;font-family:inherit;background:#0d1117;color:#c9d1d9}}
.nr textarea{{resize:vertical;min-height:80px}}
.nb{{display:flex;gap:8px;margin-top:12px}}
.nn{{padding:6px 16px;border:1px solid #30363d;background:#21262d;border-radius:5px;font-size:12px;cursor:pointer;color:#c9d1d9}}
.nn.pri{{background:#238636;border-color:#2ea043;color:#fff}}

#help-ov{{display:none;position:absolute;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.6);z-index:100;align-items:center;justify-content:center}}
#help-ov.visible{{display:flex}}
#help-c{{background:#161b22;border-radius:10px;padding:20px 28px;max-width:400px;box-shadow:0 8px 32px rgba(0,0,0,0.4);border:1px solid #30363d}}
#help-c h2{{font-size:14px;margin-bottom:10px;color:#e6edf3}}
#help-c table{{width:100%;font-size:11px}}
#help-c td{{padding:2px 0;color:#8b949e}}
#help-c td:first-child{{font-weight:600;color:#c9d1d9;width:130px}}
#help-c kbd{{background:#21262d;border:1px solid #30363d;border-radius:3px;padding:1px 4px;font-family:monospace;font-size:10px;color:#c9d1d9}}

#toast{{display:none;position:absolute;bottom:50px;left:50%;transform:translateX(-50%);background:#161b22;color:#c9d1d9;padding:8px 20px;border-radius:6px;font-size:12px;z-index:50;box-shadow:0 2px 8px rgba(0,0,0,0.4);border:1px solid #30363d}}
#toast.show{{display:block}}
#toast.error{{border-color:#f85149;color:#ffa4a2}}
#toast.success{{border-color:#2ea043;color:#a5d6a7}}
</style></head><body>

<div id="sidebar">
  <div id="sidebar-header">
    <h1>Tracker</h1>
    <div class="hdr-actions">
      <button class="hdr-btn" id="btn-undo" title="Undo (Ctrl+Z)" disabled>&#8617;</button>
      <button class="hdr-btn" id="btn-redo" title="Redo (Ctrl+Shift+Z)" disabled>&#8618;</button>
      <button class="hdr-btn" id="btn-new" title="New Task (N)">+ Task</button>
      <button class="hdr-btn primary" id="btn-save" title="Save (Ctrl+S)">Save</button>
    </div>
  </div>
  <div id="search-box"><input type="text" id="si" placeholder="Search tasks..." /></div>
  <div id="filters">
    <h3>Status</h3><div id="sf"></div>
    <h3>Phase</h3><div id="pf"></div>
    <h3>Section</h3><div id="xf"></div>
  </div>
  <div class="sidebar-sec">
    <button class="lb active" data-layout="dagre-lr">L-R</button>
    <button class="lb" data-layout="dagre-tb">T-D</button>
    <button class="lb" data-layout="cose">Force</button>
  </div>
  <div id="detail-panel" class="empty">Click a node for details</div>
</div>

<div id="canvas-container">
  <div class="grid-bg"></div>
  <div id="cy"></div>
  <div id="view-modes">
    <button class="vb active" data-view="grouped">Grouped</button>
    <button class="vb" data-view="flat">Flat</button>
  </div>
  <div id="toolbar">
    <button class="tb" id="t-zi">+</button>
    <button class="tb" id="t-zo">&#8722;</button>
    <button class="tb" id="t-fit">&#11036;</button>
    <div class="ts"></div>
    <button class="tb active" id="t-dep">&#8634;</button>
    <button class="tb" id="t-cmp">A</button>
    <div class="ts"></div>
    <button class="tb" id="t-help">?</button>
  </div>
  <div id="zoom-ind">100%</div>
  <div id="edge-tt"></div>
  <div id="dep-modal">
    <h3>Add Dependency</h3>
    <div class="dmr"><span id="dm-s"></span> depends on <span id="dm-t"></span></div>
    <div class="dmr"><input id="dm-r" placeholder="Reason (optional)" /></div>
    <div class="dmb">
      <button class="dm pri" id="dm-add">Add</button>
      <button class="dm" id="dm-swap">Swap</button>
      <button class="dm" id="dm-x">Cancel</button>
    </div>
  </div>
  <div id="toast"></div>
  <div id="help-ov">
    <div id="help-c">
      <h2>Keyboard Shortcuts</h2>
      <table>
        <tr><td><kbd>Scroll</kbd></td><td>Zoom</td></tr>
        <tr><td><kbd>Drag</kbd></td><td>Pan canvas</td></tr>
        <tr><td><kbd>Click</kbd></td><td>Select node</td></tr>
        <tr><td><kbd>Shift+Click</kbd></td><td>Add dependency</td></tr>
        <tr><td><kbd>Dbl-click</kbd> section</td><td>Collapse/expand</td></tr>
        <tr><td><kbd>F</kbd></td><td>Fit all</td></tr>
        <tr><td><kbd>D</kbd></td><td>Dep highlight</td></tr>
        <tr><td><kbd>C</kbd></td><td>Compact labels</td></tr>
        <tr><td><kbd>N</kbd></td><td>New task</td></tr>
        <tr><td><kbd>Del</kbd></td><td>Delete selected task</td></tr>
        <tr><td><kbd>Ctrl+Z</kbd></td><td>Undo</td></tr>
        <tr><td><kbd>Ctrl+Shift+Z</kbd></td><td>Redo</td></tr>
        <tr><td><kbd>Ctrl+S</kbd></td><td>Save</td></tr>
        <tr><td><kbd>1</kbd>-<kbd>9</kbd></td><td>Zoom to P0-P8</td></tr>
      </table>
      <p style="margin-top:10px;font-size:10px;color:#484f58">Click to close</p>
    </div>
  </div>
</div>

<div id="ntm"><div id="ntf">
  <h2>New Task</h2>
  <div class="nr"><label>Section</label><select id="nts"></select></div>
  <div class="nr"><label>Subsection</label><select id="ntss"><option value="">— none —</option></select></div>
  <div class="nr"><label>Status</label><select id="ntst">
    <option value="open">Open</option><option value="in_progress">In Progress</option>
    <option value="needs_research">Needs Research</option><option value="blocked">Blocked</option>
  </select></div>
  <div class="nr"><label>Description</label><textarea id="ntd" placeholder="Task description..."></textarea></div>
  <div class="nb"><button class="nn pri" id="ntgo">Create</button><button class="nn" id="ntc">Cancel</button></div>
</div></div>

<script src="https://unpkg.com/cytoscape@3.30.4/dist/cytoscape.min.js"></script>
<script src="https://unpkg.com/dagre@0.8.5/dist/dagre.min.js"></script>
<script src="https://unpkg.com/cytoscape-dagre@2.5.0/cytoscape-dagre.js"></script>
<script>
const DS='{ds}',ID={ij};
let compact=false,hlDeps=true,curView='grouped',selNode=null,gSections=[],dirty=false,lastData=null;
const SKEY='tracker-viz-'+window.location.pathname;
const SC={json.dumps(STATUS_COLORS)};
const XC={json.dumps({k:v["border"] for k,v in SECTION_COLORS.items()})};
const XL={json.dumps({k:v["label"] for k,v in SECTION_COLORS.items()})};

async function api(m,p,b){{const o={{method:m,headers:{{'Content-Type':'application/json'}}}};if(b)o.body=JSON.stringify(b);return(await fetch(p,o)).json()}}
function toast(msg,cls){{const t=document.getElementById('toast');t.textContent=msg;t.className='show '+(cls||'');setTimeout(()=>t.className='',2500)}}
function markDirty(){{dirty=true;const b=document.getElementById('btn-save');b.classList.add('warn');b.textContent='Save *'}}
function markClean(){{dirty=false;const b=document.getElementById('btn-save');b.classList.remove('warn');b.textContent='Save'}}

// Cytoscape
const cy=cytoscape({{
  container:document.getElementById('cy'),elements:[],minZoom:0.05,maxZoom:5,wheelSensitivity:0.3,boxSelectionEnabled:false,
  style:[
    {{selector:'node[type="section"]',style:{{'shape':'roundrectangle','background-color':'data(bg)','border-color':'data(borderColor)','border-width':2,'border-opacity':0.7,'background-opacity':0.35,'label':'data(label)','text-valign':'top','text-halign':'center','font-size':16,'font-weight':700,'color':'data(borderColor)','text-margin-y':12,'padding':30,'compound-sizing-wrt-labels':'include'}}}},
    {{selector:'node[type="subsection"]',style:{{'shape':'roundrectangle','background-color':'data(bg)','border-color':'data(borderColor)','border-width':1.5,'border-opacity':0.4,'border-style':'dashed','background-opacity':0.2,'label':'data(label)','text-valign':'top','text-halign':'center','font-size':12,'font-weight':600,'color':'#8b949e','text-margin-y':8,'padding':20,'compound-sizing-wrt-labels':'include'}}}},
    {{selector:'node[type="task"]',style:{{'shape':'roundrectangle','width':'label','height':'label','padding':'8px','background-color':'data(bg)','border-color':'data(borderColor)','border-width':2.5,'label':'data(label)','text-valign':'center','text-halign':'center','font-size':10,'font-weight':500,'color':'data(textColor)','text-wrap':'wrap','text-max-width':'200px','min-zoomed-font-size':4}}}},
    {{selector:'node[type="task"]:selected',style:{{'border-color':'#58a6ff','border-width':3.5,'box-shadow-blur':12,'box-shadow-color':'rgba(88,166,255,0.3)','box-shadow-opacity':1}}}},
    {{selector:'edge',style:{{'width':1.5,'line-color':'#30363d','target-arrow-color':'#30363d','target-arrow-shape':'triangle','curve-style':'bezier','arrow-scale':0.8,'opacity':0.6}}}},
    {{selector:'edge.highlighted',style:{{'line-color':'#58a6ff','target-arrow-color':'#58a6ff','width':2.5,'opacity':1,'z-index':10}}}},
    {{selector:'.dimmed',style:{{'opacity':0.08}}}},
    {{selector:'.hidden',style:{{'display':'none'}}}},
    {{selector:'.neighbor-highlight',style:{{'border-color':'#58a6ff','border-width':3}}}},
    {{selector:'.collapsed-section',style:{{'width':180,'height':40,'background-opacity':0.6,'font-size':12}}}},
  ],
}});

// Zoom
const zEl=document.getElementById('zoom-ind');
function uZoom(){{zEl.textContent=Math.round(cy.zoom()*100)+'%'}}
cy.on('zoom',uZoom);

// localStorage helpers
function saveLayout(){{
  try{{
    const pos={{}};cy.nodes('[type="task"]').forEach(n=>{{pos[n.id()]=n.position()}});
    const state={{pos,zoom:cy.zoom(),pan:cy.pan(),collapsed:Array.from(collapsedSections),view:curView,layout:document.querySelector('.lb.active')?.dataset.layout||'dagre-lr'}};
    localStorage.setItem(SKEY,JSON.stringify(state));
  }}catch(e){{}}
}}
function loadLayout(){{
  try{{
    const s=JSON.parse(localStorage.getItem(SKEY));
    if(!s)return false;
    if(s.collapsed)s.collapsed.forEach(id=>collapsedSections.add(id));
    if(s.pos){{cy.nodes('[type="task"]').forEach(n=>{{if(s.pos[n.id()])n.position(s.pos[n.id()])}})}}
    if(s.zoom)cy.zoom(s.zoom);
    if(s.pan)cy.pan(s.pan);
    if(s.view&&s.view!==curView){{const btn=document.querySelector(`.vb[data-view="${{s.view}}"]`);if(btn)btn.click()}}
    if(s.layout){{const lb=document.querySelector(`.lb[data-layout="${{s.layout}}"]`);if(lb){{document.querySelectorAll('.lb').forEach(b=>b.classList.remove('active'));lb.classList.add('active')}}}}
    return true;
  }}catch(e){{return false}}
}}
cy.on('dragfree','node[type="task"]',()=>saveLayout());
cy.on('zoom pan',()=>{{clearTimeout(window._saveTm);window._saveTm=setTimeout(saveLayout,500)}});

// Collapsible sections
const collapsedSections=new Set();
function toggleCollapse(secId){{
  if(collapsedSections.has(secId)){{collapsedSections.delete(secId)}}
  else{{collapsedSections.add(secId)}}
  applyCollapse();saveLayout();
}}
function applyCollapse(){{
  cy.batch(()=>{{
    cy.nodes('[type="section"]').forEach(sec=>{{
      const sid=sec.data('id');
      if(collapsedSections.has(sid)){{
        sec.addClass('collapsed-section');
        const d=sec.data();
        sec.style('label',`${{sid}}: ${{XL[sid]||sid}} (${{d.totalCount||'?'}} tasks, ${{d.progress||0}}%)`);
        getDesc(sec).forEach(n=>n.addClass('hidden'));
        sec.children().forEach(c=>{{if(c.data('type')==='subsection')c.addClass('hidden')}});
      }}else{{
        sec.removeClass('collapsed-section');
        sec.style('label',sec.data('label'));
        getDesc(sec).forEach(n=>n.removeClass('hidden'));
        sec.children().forEach(c=>{{if(c.data('type')==='subsection')c.removeClass('hidden')}});
      }}
    }});
    cy.edges().forEach(e=>{{
      e[(e.source().hasClass('hidden')||e.target().hasClass('hidden'))?'addClass':'removeClass']('hidden');
    }});
  }});
  applyFilters();
}}

// Load data
async function loadData(){{
  const data=DS==='inline'?ID:await(await fetch('/api/data')).json();
  lastData=data;gSections=data.sections||[];
  cy.elements().remove();cy.add(data.elements);
  const restored=loadLayout();
  if(!restored){{
    cy.layout({{name:'dagre',rankDir:'LR',nodeSep:30,edgeSep:10,rankSep:70,padding:40,animate:false}}).run();
    cy.fit(undefined,40);
  }}
  applyCollapse();buildFilters(data.stats);populateNTF();uZoom();updateUndoButtons(data);
}}
loadData();

function updateUndoButtons(data){{
  document.getElementById('btn-undo').disabled=!(data&&data.canUndo);
  document.getElementById('btn-redo').disabled=!(data&&data.canRedo);
}}

// Filters
function buildFilters(stats){{
  const sf=document.getElementById('sf'),pf=document.getElementById('pf'),xf=document.getElementById('xf');
  sf.innerHTML='';pf.innerHTML='';xf.innerHTML='';
  const sd={{open:'#8b949e',done:'#3fb950',in_progress:'#58a6ff',blocked:'#f0883e',killed:'#f85149',needs_research:'#bc8cff'}};
  const sl={{open:'Open',done:'Done',in_progress:'In Progress',blocked:'Blocked',killed:'Killed',needs_research:'Research'}};
  ['open','in_progress','done','blocked','killed','needs_research'].forEach(s=>{{
    const c=stats.by_status[s]||0;if(!c)return;
    const l=document.createElement('label');l.className='fi';
    l.innerHTML=`<input type="checkbox" checked data-ft="status" data-fv="${{s}}"/><span class="fd" style="background:${{sd[s]}}"></span>${{sl[s]}}<span class="fc">${{c}}</span>`;
    sf.appendChild(l);
  }});
  const pd={{Done:'#3fb950','Ready Now':'#58a6ff','Next Up':'#f0883e','Mid-term':'#bc8cff',Later:'#f85149'}};
  ['Done','Ready Now','Next Up','Mid-term','Later'].forEach(p=>{{
    const c=stats.by_phase[p]||0;if(!c)return;
    const l=document.createElement('label');l.className='fi';
    l.innerHTML=`<input type="checkbox" checked data-ft="phase" data-fv="${{p}}"/><span class="fd" style="background:${{pd[p]||'#8b949e'}}"></span>${{p}}<span class="fc">${{c}}</span>`;
    pf.appendChild(l);
  }});
  cy.nodes('[type="section"]').forEach(n=>{{
    const sid=n.data('id'),c=cy.nodes(`[type="task"][section="${{sid}}"]`).length;
    const l=document.createElement('label');l.className='fi';
    l.innerHTML=`<input type="checkbox" checked data-ft="section" data-fv="${{sid}}"/><span class="fd" style="background:${{XC[sid]||'#8b949e'}}"></span>${{sid}}: ${{XL[sid]||sid}}<span class="fc">${{c}}</span>`;
    xf.appendChild(l);
  }});
  document.querySelectorAll('#filters input').forEach(cb=>cb.addEventListener('change',applyFilters));
}}

function gc(ft){{return new Set([...document.querySelectorAll(`input[data-ft="${{ft}}"]:checked`)].map(i=>i.dataset.fv))}}
function getDesc(node){{const r=[];function c(n){{n.children().forEach(ch=>{{if(ch.data('type')==='task')r.push(ch);else c(ch)}})}}c(node);return r}}
function applyFilters(){{
  const ss=gc('status'),ps=gc('phase'),sc=gc('section');
  cy.batch(()=>{{
    cy.nodes('[type="task"]').forEach(n=>{{
      const inCollapsed=collapsedSections.has(n.data('section'));
      const show=ss.has(n.data('status'))&&ps.has(n.data('phaseLabel'))&&sc.has(n.data('section'))&&!inCollapsed;
      n[show?'removeClass':'addClass']('hidden');
    }});
    cy.nodes('[type="section"],[type="subsection"]').forEach(n=>{{
      if(n.data('type')==='section'&&collapsedSections.has(n.data('id')))return;
      if(n.data('type')==='subsection'&&collapsedSections.has(n.data('id')?.split('.')[0])){{n.addClass('hidden');return}}
      const t=getDesc(n);n[t.every(x=>x.hasClass('hidden'))?'addClass':'removeClass']('hidden');
    }});
    cy.edges().forEach(e=>e[(e.source().hasClass('hidden')||e.target().hasClass('hidden'))?'addClass':'removeClass']('hidden'));
  }});
}}

// Search
document.getElementById('si').addEventListener('input',function(){{
  const q=this.value.trim().toLowerCase();
  cy.batch(()=>{{
    if(!q){{cy.elements().removeClass('dimmed');return}}
    cy.nodes('[type="task"]').forEach(n=>n[(n.data('id').toLowerCase().includes(q)||(n.data('title')||'').toLowerCase().includes(q)||(n.data('description')||'').toLowerCase().includes(q))?'removeClass':'addClass']('dimmed'));
    cy.nodes('[type="section"],[type="subsection"]').forEach(n=>{{const t=getDesc(n);n[(t.length>0&&t.every(x=>x.hasClass('dimmed')))?'addClass':'removeClass']('dimmed')}});
    cy.edges().forEach(e=>e[(e.source().hasClass('dimmed')&&e.target().hasClass('dimmed'))?'addClass':'removeClass']('dimmed'));
  }});
}});

// Detail panel
const dp=document.getElementById('detail-panel');
function showDetail(node){{
  const d=node.data();if(d.type!=='task')return;selNode=node;
  const sc=SC[d.status]||SC['open'];
  const inc=node.incomers('edge').map(e=>({{id:e.source().data('id'),reason:e.data('reason')||'',auto:e.data('auto')}}));
  const out=node.outgoers('edge').map(e=>({{id:e.target().data('id'),reason:e.data('reason')||'',auto:e.data('auto')}}));
  let dh='<div class="deps"><h4>Depends on &rarr;</h4>';
  if(out.length)out.forEach(x=>{{dh+=`<span class="dl" data-t="${{x.id}}">${{x.id}}</span>`;if(x.reason&&x.reason!=='inline ref')dh+=`<span class="dr">${{x.reason}}</span>`;if(!x.auto)dh+=`<span class="dx" data-s="${{d.id}}" data-t="${{x.id}}">&times;</span>`;dh+=' '}});
  else dh+='<span style="color:#30363d;font-size:10px">none</span>';
  dh+='<h4>&larr; Blocks</h4>';
  if(inc.length)inc.forEach(x=>{{dh+=`<span class="dl" data-t="${{x.id}}">${{x.id}}</span>`;if(x.reason&&x.reason!=='inline ref')dh+=`<span class="dr">${{x.reason}}</span>`;if(!x.auto)dh+=`<span class="dx" data-s="${{x.id}}" data-t="${{d.id}}">&times;</span>`;dh+=' '}});
  else dh+='<span style="color:#30363d;font-size:10px">none</span>';
  dh+=`<div class="adr"><input id="adt" placeholder="P#.#.# (depends on)"/><input id="adr" placeholder="reason" style="flex:0.7"/><button class="adb" id="adg">+</button></div></div>`;
  const dc=d.description.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>').replace(/`([^`]+)`/g,'<code>$1</code>');
  const so=['open','in_progress','done','blocked','killed','needs_research'].map(s=>`<option value="${{s}}" ${{s===d.status?'selected':''}}>${{({{open:'Open',in_progress:'In Progress',done:'Done',blocked:'Blocked',killed:'Killed',needs_research:'Research'}})[s]}}</option>`).join('');

  dp.className='';dp.innerHTML=`
    <div class="dh"><span class="di">${{d.id}}</span><span class="db" style="background:${{sc.bg}};color:${{sc.text}};border:1px solid ${{sc.border}}">${{d.statusLabel}}</span><span class="db" style="background:#21262d;color:#8b949e;border:1px solid #30363d">${{d.phaseLabel}}</span></div>
    <div class="ds">${{d.section}}${{d.subsection?' &rsaquo; '+d.subsection:''}}</div>
    <div class="dt">${{d.title}}</div>
    <div class="dd">${{dc}}</div>
    <div class="ec"><h4>Edit</h4>
      <div class="er"><label>Status</label><select id="es">${{so}}</select></div>
      <div class="er"><label>Description</label><textarea id="ed">${{d.description.replace(/</g,'&lt;')}}</textarea></div>
      <div class="ebtns"><button class="eb save" id="eap">Apply</button><button class="eb del" id="edl">Delete</button></div>
    </div>
    ${{dh}}`;

  dp.querySelectorAll('.dl').forEach(el=>el.addEventListener('click',()=>{{const t=cy.getElementById(el.dataset.t);if(t.length){{cy.animate({{center:{{eles:t}},duration:300}});t.select();showDetail(t);if(hlDeps)hlConn(t)}}}}));
  dp.querySelectorAll('.dx').forEach(el=>el.addEventListener('click',async()=>{{if(DS==='inline')return;const r=await api('DELETE','/api/dep',{{source:el.dataset.s,target:el.dataset.t}});if(r.ok){{markDirty();await rGraph();toast('Dep removed','success')}}else toast(r.error,'error')}}));
  document.getElementById('eap')?.addEventListener('click',async()=>{{
    if(DS==='inline'){{toast('Read-only','error');return}}
    const ns=document.getElementById('es').value,nd=document.getElementById('ed').value;
    if(ns!==d.status){{const r=await api('POST',`/api/task/${{d.id}}/status`,{{status:ns}});if(!r.ok){{toast(r.error,'error');return}}}}
    if(nd!==d.description){{const r=await api('POST',`/api/task/${{d.id}}/description`,{{description:nd}});if(!r.ok){{toast(r.error,'error');return}}}}
    markDirty();await rGraph();toast('Updated '+d.id,'success');
  }});
  document.getElementById('edl')?.addEventListener('click',async()=>{{
    if(DS==='inline')return;
    if(!confirm(`Delete ${{d.id}}?`))return;
    const r=await api('DELETE',`/api/task/${{d.id}}`);
    if(r.ok){{markDirty();selNode=null;dp.className='empty';dp.textContent='Click a node for details';await rGraph();toast('Deleted '+d.id,'success')}}
    else toast(r.error,'error');
  }});
  document.getElementById('adg')?.addEventListener('click',async()=>{{
    if(DS==='inline')return;
    const t=document.getElementById('adt').value.trim(),r=document.getElementById('adr').value.trim();
    if(!t)return;const res=await api('POST','/api/dep',{{source:d.id,target:t,reason:r}});
    if(res.ok){{markDirty();await rGraph();toast('Dep added','success')}}else toast(res.error,'error');
  }});
}}

async function rGraph(){{
  const data=DS==='inline'?ID:await(await fetch('/api/data')).json();
  lastData=data;gSections=data.sections||[];
  const positions={{}};cy.nodes().forEach(n=>positions[n.id()]=n.position());
  cy.elements().remove();cy.add(data.elements);
  cy.nodes().forEach(n=>{{if(positions[n.id()])n.position(positions[n.id()])}});
  applyCollapse();buildFilters(data.stats);updateUndoButtons(data);
  if(selNode){{const n=cy.getElementById(selNode.data('id'));if(n.length){{n.select();showDetail(n);if(hlDeps)hlConn(n)}}}}
  saveLayout();
}}

function hlConn(node){{
  cy.batch(()=>{{
    cy.elements().removeClass('dimmed highlighted neighbor-highlight');
    if(!node||node.data('type')!=='task')return;
    const conn=new Set([node.id()]);
    function walk(n,dir){{(dir==='up'?n.incomers('edge'):n.outgoers('edge')).forEach(e=>{{const o=dir==='up'?e.source():e.target();if(!conn.has(o.id())&&o.data('type')==='task'){{conn.add(o.id());e.addClass('highlighted');walk(o,dir)}}}})}}
    walk(node,'up');walk(node,'down');node.connectedEdges().addClass('highlighted');
    cy.nodes('[type="task"]').forEach(n=>{{if(!conn.has(n.id()))n.addClass('dimmed');else if(n.id()!==node.id())n.addClass('neighbor-highlight')}});
    cy.nodes('[type="section"],[type="subsection"]').forEach(n=>{{const t=getDesc(n);if(t.length>0&&t.every(x=>x.hasClass('dimmed')))n.addClass('dimmed')}});
    cy.edges().forEach(e=>{{if(!e.hasClass('highlighted'))e.addClass('dimmed')}});
  }});
}}

cy.on('tap','node[type="task"]',evt=>{{
  if(evt.originalEvent.shiftKey&&selNode&&selNode.data('id')!==evt.target.data('id')){{showDepModal(selNode.data('id'),evt.target.data('id'),evt.renderedPosition);return}}
  showDetail(evt.target);if(hlDeps)hlConn(evt.target);
}});
cy.on('tap',evt=>{{if(evt.target===cy){{selNode=null;dp.className='empty';dp.textContent='Click a node for details';cy.elements().removeClass('dimmed highlighted neighbor-highlight')}}}});
cy.on('dblclick','node[type="section"]',evt=>toggleCollapse(evt.target.data('id')));
cy.on('mouseover','edge',evt=>{{const r=evt.target.data('reason');if(r){{const p=evt.renderedPosition||evt.position;const tt=document.getElementById('edge-tt');tt.textContent=`${{evt.target.data('source')}} → ${{evt.target.data('target')}}: ${{r}}`;tt.style.left=(p.x+15)+'px';tt.style.top=(p.y-10)+'px';tt.style.display='block'}}}});
cy.on('mouseout','edge',()=>document.getElementById('edge-tt').style.display='none');

// Dep modal
function showDepModal(s,t,pos){{const m=document.getElementById('dep-modal');document.getElementById('dm-s').textContent=s;document.getElementById('dm-t').textContent=t;document.getElementById('dm-r').value='';m.style.left=(pos.x+330)+'px';m.style.top=pos.y+'px';m.style.display='block';document.getElementById('dm-r').focus()}}
document.getElementById('dm-add').addEventListener('click',async()=>{{const s=document.getElementById('dm-s').textContent,t=document.getElementById('dm-t').textContent,r=document.getElementById('dm-r').value.trim();const res=await api('POST','/api/dep',{{source:s,target:t,reason:r}});document.getElementById('dep-modal').style.display='none';if(res.ok){{markDirty();await rGraph();toast('Dep added','success')}}else toast(res.error,'error')}});
document.getElementById('dm-swap').addEventListener('click',()=>{{const s=document.getElementById('dm-s'),t=document.getElementById('dm-t');[s.textContent,t.textContent]=[t.textContent,s.textContent]}});
document.getElementById('dm-x').addEventListener('click',()=>document.getElementById('dep-modal').style.display='none');

// View modes — full rebuild to avoid Cytoscape re-parenting bugs
document.querySelectorAll('.vb').forEach(btn=>{{btn.addEventListener('click',async()=>{{
  document.querySelectorAll('.vb').forEach(b=>b.classList.remove('active'));btn.classList.add('active');curView=btn.dataset.view;
  if(!lastData)lastData=DS==='inline'?ID:await(await fetch('/api/data')).json();
  const elems=JSON.parse(JSON.stringify(lastData.elements));
  if(curView==='flat'){{
    const filtered=elems.filter(e=>{{if(e.data&&(e.data.type==='section'||e.data.type==='subsection'))return false;if(e.data&&e.data.type==='task')delete e.data.parent;return true}});
    cy.elements().remove();cy.add(filtered);
  }}else{{cy.elements().remove();cy.add(elems);applyCollapse()}}
  const lt=document.querySelector('.lb.active')?.dataset.layout||'dagre-lr';let opts;
  if(lt==='dagre-tb')opts={{name:'dagre',rankDir:'TB',nodeSep:30,edgeSep:10,rankSep:60,padding:40,animate:false}};
  else if(lt==='dagre-lr')opts={{name:'dagre',rankDir:'LR',nodeSep:30,edgeSep:10,rankSep:70,padding:40,animate:false}};
  else opts={{name:'cose',padding:40,animate:false,nodeRepulsion:8000,idealEdgeLength:120}};
  cy.layout(opts).run();cy.fit(undefined,40);applyFilters();saveLayout();
}})}});

// Layout
document.querySelectorAll('.lb').forEach(btn=>{{btn.addEventListener('click',()=>{{
  document.querySelectorAll('.lb').forEach(b=>b.classList.remove('active'));btn.classList.add('active');
  const lt=btn.dataset.layout;let opts;
  if(lt==='dagre-tb')opts={{name:'dagre',rankDir:'TB',nodeSep:30,edgeSep:10,rankSep:60,padding:40,animate:true,animationDuration:400}};
  else if(lt==='dagre-lr')opts={{name:'dagre',rankDir:'LR',nodeSep:30,edgeSep:10,rankSep:70,padding:40,animate:true,animationDuration:400}};
  else opts={{name:'cose',padding:40,animate:true,animationDuration:500,nodeRepulsion:8000,idealEdgeLength:120}};
  cy.layout(opts).run();saveLayout();
}})}});

// New task
function populateNTF(){{const s=document.getElementById('nts');s.innerHTML='';gSections.forEach(sec=>s.innerHTML+=`<option value="${{sec.id}}">${{sec.id}}: ${{sec.title}}</option>`);updateNTSS()}}
function updateNTSS(){{const sid=document.getElementById('nts').value,ss=document.getElementById('ntss');ss.innerHTML='<option value="">— none —</option>';const sec=gSections.find(s=>s.id===sid);if(sec)sec.subsections.forEach(s=>ss.innerHTML+=`<option value="${{s.id}}">${{s.id}}: ${{s.title}}</option>`)}}
document.getElementById('nts')?.addEventListener('change',updateNTSS);
document.getElementById('btn-new').addEventListener('click',()=>{{document.getElementById('ntm').classList.add('visible');document.getElementById('ntd').value='';document.getElementById('ntd').focus()}});
document.getElementById('ntc').addEventListener('click',()=>document.getElementById('ntm').classList.remove('visible'));
document.getElementById('ntgo').addEventListener('click',async()=>{{
  if(DS==='inline')return;
  const sec=document.getElementById('nts').value,sub=document.getElementById('ntss').value,st=document.getElementById('ntst').value,desc=document.getElementById('ntd').value.trim();
  if(!desc){{toast('Description required','error');return}}
  const r=await api('POST','/api/task',{{section:sec,subsection:sub||null,status:st,description:desc}});
  document.getElementById('ntm').classList.remove('visible');
  if(r.ok){{markDirty();await rGraph();toast('Created '+r.id,'success');const n=cy.getElementById(r.id);if(n.length){{cy.animate({{center:{{eles:n}},duration:300}});n.select();showDetail(n)}}}}
  else toast(r.error,'error');
}});
document.getElementById('ntm').addEventListener('click',evt=>{{if(evt.target===document.getElementById('ntm'))document.getElementById('ntm').classList.remove('visible')}});

// Toolbar
document.getElementById('t-zi').addEventListener('click',()=>cy.animate({{zoom:cy.zoom()*1.3,duration:200}}));
document.getElementById('t-zo').addEventListener('click',()=>cy.animate({{zoom:cy.zoom()/1.3,duration:200}}));
document.getElementById('t-fit').addEventListener('click',()=>cy.animate({{fit:{{padding:40}},duration:300}}));
document.getElementById('t-dep').addEventListener('click',()=>{{hlDeps=!hlDeps;document.getElementById('t-dep').classList.toggle('active',hlDeps);if(!hlDeps)cy.elements().removeClass('dimmed highlighted neighbor-highlight')}});
document.getElementById('t-cmp').addEventListener('click',()=>{{compact=!compact;document.getElementById('t-cmp').classList.toggle('active',compact);cy.batch(()=>cy.nodes('[type="task"]').forEach(n=>{{n.style('label',compact?n.data('shortLabel'):n.data('label'));n.style('text-wrap',compact?'none':'wrap');if(!compact)n.style('text-max-width','200px')}}))}});
document.getElementById('t-help').addEventListener('click',()=>document.getElementById('help-ov').classList.toggle('visible'));
document.getElementById('help-ov').addEventListener('click',()=>document.getElementById('help-ov').classList.remove('visible'));

// Save + Undo/Redo
document.getElementById('btn-save').addEventListener('click',async()=>{{
  if(DS==='inline'){{toast('Read-only','error');return}}
  const r=await api('POST','/api/save');
  if(r.ok){{markClean();toast('Saved'+(r.git?' (git: '+r.git+')':''),'success');await rGraph()}}else toast(r.error,'error');
}});
document.getElementById('btn-undo').addEventListener('click',async()=>{{
  if(DS==='inline')return;const r=await api('POST','/api/undo');
  if(r.ok){{markDirty();await rGraph();toast('Undone','success')}}else toast(r.error,'error');
}});
document.getElementById('btn-redo').addEventListener('click',async()=>{{
  if(DS==='inline')return;const r=await api('POST','/api/redo');
  if(r.ok){{markDirty();await rGraph();toast('Redone','success')}}else toast(r.error,'error');
}});

// Keyboard
document.addEventListener('keydown',evt=>{{
  const inInput=evt.target.tagName==='INPUT'||evt.target.tagName==='TEXTAREA'||evt.target.tagName==='SELECT';
  if((evt.ctrlKey||evt.metaKey)&&evt.key==='s'){{evt.preventDefault();document.getElementById('btn-save').click();return}}
  if((evt.ctrlKey||evt.metaKey)&&evt.key==='z'){{evt.preventDefault();if(evt.shiftKey)document.getElementById('btn-redo').click();else document.getElementById('btn-undo').click();return}}
  if(inInput)return;
  switch(evt.key){{
    case 'f':case 'F':cy.animate({{fit:{{padding:40}},duration:300}});break;
    case '+':case '=':cy.animate({{zoom:cy.zoom()*1.3,duration:200}});break;
    case '-':cy.animate({{zoom:cy.zoom()/1.3,duration:200}});break;
    case 'd':case 'D':document.getElementById('t-dep').click();break;
    case 'c':case 'C':document.getElementById('t-cmp').click();break;
    case 'n':case 'N':document.getElementById('btn-new').click();break;
    case 'Delete':if(selNode&&DS!=='inline')document.getElementById('edl')?.click();break;
    case 'Escape':
      cy.elements().unselect().removeClass('dimmed highlighted neighbor-highlight');selNode=null;
      dp.className='empty';dp.textContent='Click a node for details';
      document.getElementById('help-ov').classList.remove('visible');
      document.getElementById('ntm').classList.remove('visible');
      document.getElementById('dep-modal').style.display='none';
      document.getElementById('si').value='';document.getElementById('si').dispatchEvent(new Event('input'));
      break;
    case '?':document.getElementById('help-ov').classList.toggle('visible');break;
    default:const num=parseInt(evt.key);if(!isNaN(num)&&num>=0&&num<=8){{const s=cy.getElementById('P'+num);if(s.length)cy.animate({{fit:{{eles:s,padding:40}},duration:400}})}}
  }}
}});

window.addEventListener('beforeunload',evt=>{{if(dirty){{evt.preventDefault();evt.returnValue=''}}}});
</script></body></html>"""


# ---------------------------------------------------------------------------
# Static generation
# ---------------------------------------------------------------------------

def generate_static(tracker_path, deps_path, output_path, open_browser):
    model = TrackerModel(tracker_path, deps_path)
    html = generate_html(static_data=model.to_frontend_data())
    Path(output_path).write_text(html, encoding="utf-8")
    log.info("Generated static %s (%d tasks)", output_path, len(model.tasks))
    if open_browser:
        webbrowser.open(str(output_path))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Tracker visualization + editor")
    p.add_argument("--tracker", default=str(DEFAULT_TRACKER))
    p.add_argument("--deps", default=str(DEFAULT_DEPS))
    p.add_argument("--port", type=int, default=5111)
    p.add_argument("--open", action="store_true")
    p.add_argument("--static", action="store_true")
    p.add_argument("--output", default=str(PROJECT_ROOT / "tracker-viz.html"))
    args = p.parse_args()

    if args.static:
        generate_static(args.tracker, args.deps, args.output, args.open)
    else:
        run_server(args.tracker, args.deps, args.port, args.open)


if __name__ == "__main__":
    main()
