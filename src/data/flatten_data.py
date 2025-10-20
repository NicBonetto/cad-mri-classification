import os
import shutil
from pathlib import Path

# Initialize project paths
DATA_ROOT = Path('data/raw')
FLAT_ROOT = Path('data/flat')
FLAT_NORMAL = FLAT_ROOT / 'normal'
FLAT_SICK = FLAT_ROOT / 'sick'

FLAT_NORMAL.mkdir(parents=True, exist_ok=True)
FLAT_SICK.mkdir(parents=True, exist_ok=True)

ext = '.jpg'

print('Flattening data/raw')

for dirpath, dirnames, filenames in os.walk(DATA_ROOT):
    dirpath = Path(dirpath)
    label = None

    if 'Normal' in dirpath.parts:
        label = 'normal'
        target_dir = FLAT_NORMAL
    elif 'Sick' in dirpath.parts:
        label = 'sick'
        target_dir = FLAT_SICK
    else:
        continue

    for file in filenames:
        if file.startswith('.') or Path(file).suffix.lower() != ext:
            continue

    # Build labeled filename
    rel_parts = dirpath.relative_to(DATA_ROOT).parts
    rel_name = '_'.join(rel_parts) + '_' + file

    src_path = dirpath / file
    if not src_path.exists():
        print('Warning: file does not exist, skipping', src_path)
        continue

    dest = target_dir / rel_name
    shutil.copy2(dirpath / file, dest)

print('Flattening complete!')

