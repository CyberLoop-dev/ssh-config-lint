#!/usr/bin/env python3
"""Read-only checks for risky OpenSSH client configuration."""
from __future__ import annotations
import argparse, json, shlex, sys
from collections import defaultdict
from pathlib import Path

RISKY = {
    "stricthostkeychecking": {"no", "off"},
    "userknownhostsfile": {"/dev/null", "none"},
    "forwardagent": {"yes"},
    "passwordauthentication": {"yes"},
    "permitlocalcommand": {"yes"},
}

def audit(text: str):
    issues=[]; aliases=defaultdict(list); scope="global"
    for number, raw in enumerate(text.splitlines(),1):
        line=raw.strip()
        if not line or line.startswith("#"): continue
        try: parts=shlex.split(line, comments=True)
        except ValueError:
            issues.append({"line":number,"scope":scope,"directive":"","message":"Malformed quoting"})
            continue
        if not parts: continue
        key=parts[0].lower(); values=parts[1:]
        if key=="host":
            scope=" ".join(values) or "(empty Host)"
            for alias in values:
                if not any(c in alias for c in "*?!"):
                    aliases[alias.casefold()].append(number)
            continue
        if key=="match":
            scope="Match "+" ".join(values)
            continue
        if not values: continue
        value=" ".join(values).strip().lower()
        if key in RISKY and value in RISKY[key]:
            issues.append({"line":number,"scope":scope,"directive":parts[0],
                "message":f"Risky setting: {parts[0]} { ' '.join(values) }"})
    for alias, lines in aliases.items():
        if len(lines)>1:
            for line in lines[1:]:
                issues.append({"line":line,"scope":alias,"directive":"Host","message":f"Duplicate Host alias: {alias} (also at line {lines[0]})"})
    return sorted(issues,key=lambda x:x["line"])

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file",type=Path,default=Path.home()/".ssh"/"config")
    ap.add_argument("--json",action="store_true"); args=ap.parse_args()
    try: text=args.file.expanduser().read_text(encoding="utf-8")
    except OSError as exc: print(f"error: {exc}",file=sys.stderr); return 2
    issues=audit(text)
    if args.json: print(json.dumps({"issue_count":len(issues),"issues":issues},indent=2))
    else:
        print(f"SSH Config Lint: {len(issues)} issue(s)")
        for item in issues: print(f"line {item['line']} [{item['scope']}] {item['message']}")
        if not issues: print("No configured risky options found.")
    return 1 if issues else 0
if __name__=="__main__": raise SystemExit(main())
