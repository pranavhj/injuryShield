#!/usr/bin/env bash
# check-decisions.sh — guards the research corpus against self-contradiction.
# Run before committing research changes:  bash scripts/check-decisions.sh
#
# Checks:
#   1. Every known-stale file still carries its supersession banner
#   2. No reversed decision is stated as live fact outside an allowed context
#   3. No research file is newer than DECISIONS.md (a finding may be unrecorded)
# Exit 0 = clean, 1 = problems found.

cd "$(dirname "$0")/.." || exit 1
FAIL=0
echo "=== Decision consistency check ==="
echo

# --- 1. Stale files must carry banners ---
echo "[1] Supersession banners"
STALE_FILES="research/archive/sensor-architecture.md
research/archive/academic-papers.md
research/archive/competitors.md
research/archive/ecosystem-business-model.md
research/archive/market-sizing.md"

while IFS= read -r f; do
    [ -z "$f" ] && continue
    if [ ! -f "$f" ]; then
        printf "    MISSING FILE  %s\n" "$f"; FAIL=1; continue
    fi
    if head -5 "$f" | grep -q "SUPERSEDED\|READ WITH CORRECTIONS\|LOW VALUE"; then
        printf "    ok            %s\n" "$f"
    else
        printf "    NO BANNER     %s\n" "$f"; FAIL=1
    fi
done <<< "$STALE_FILES"
echo

# --- 2. Reversed decisions must not appear as live claims ---
# Each entry: "pattern|human description"
echo "[2] Reversed decisions — ADVISORY (grep cannot tell history from live claims)"
REVERSED='5-pod core|Core is 2 pods, not 5
\$35/pod|pricing is ~$249 for a 2-pod Core kit
hardware-as-subscription|model is outright sale'

# Scan only CURRENT files. Archive is bannered; DECISIONS/TRACKER/VIABILITY/LOG
# deliberately record reversals; scripts contain the patterns themselves.
SCAN=$(ls *.md research/*.md 2>/dev/null | grep -v "^DECISIONS.md")

while IFS= read -r line; do
    [ -z "$line" ] && continue
    pat="${line%%|*}"; desc="${line##*|}"
    hits=$(grep -niI "$pat" $SCAN 2>/dev/null         | grep -vi "SUPERSEDED\|Reversed\|~~\|KILLED\|retired\|no longer\|not viable\|old \|was impossible\|Never\|no apparel\|No edge") 
    if [ -n "$hits" ]; then
        printf "    review        %s
" "$desc"
        echo "$hits" | head -3 | sed 's/^/                  /'
    else
        printf "    ok            %s
" "$desc"
    fi
done <<< "$REVERSED"
echo

# --- 3. DECISIONS.md must not be older than the research it summarises ---
echo "[3] DECISIONS.md freshness"
if [ ! -f DECISIONS.md ]; then
    echo "    MISSING       DECISIONS.md does not exist"; FAIL=1
else
    newer=$(find research problems market -name "*.md" -not -path "*/archive/*" -newer DECISIONS.md 2>/dev/null)
    if [ -n "$newer" ]; then
        echo "    STALE         these changed after DECISIONS.md was last updated:"
        echo "$newer" | sed 's/^/                  /'
        echo "                  -> if any of them changed a decision, record it in DECISIONS.md"
        FAIL=1
    else
        echo "    ok            DECISIONS.md is current"
    fi
fi
echo

# --- 4. Corpus size ---
echo "[4] Corpus size"
current=$(ls research/*.md 2>/dev/null | wc -l)   # archive/ excluded by glob
total=$(cat $(find . -name '*.md' -not -path './.git/*') 2>/dev/null | wc -l)
printf "    %s research files, %s total lines\n" "$current" "$total"
if [ "$current" -gt 15 ]; then
    echo "    OVER CAP      >15 research files. Fold findings into existing files."
    FAIL=1
fi
echo

if [ "$FAIL" -eq 0 ]; then
    echo "=== CLEAN === (section [2] is advisory — eyeball it, do not auto-trust)"
else
    echo "=== ISSUES FOUND — review above before committing ==="
fi
exit $FAIL
