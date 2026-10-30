from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
missing = []
for path in root.rglob('*.tex'):
    for command, target in re.findall(r"\\(input|include)\{([^}]+)\}", path.read_text()):
        candidate = root / target
        if not candidate.suffix:
            candidate = candidate.with_suffix('.tex')
        if not candidate.exists():
            missing.append((str(path.relative_to(root)), target))
print('Missing input/include targets:', missing)
raise SystemExit(bool(missing))
