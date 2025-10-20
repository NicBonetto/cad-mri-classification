import os
from pathlib import Path
import csv

DATA_ROOT = Path('data/')

classes = ['normal', 'sick']
output_csv = DATA_ROOT / 'labels.csv'

rows = []

for class_name in classes:
    class_dir = DATA_ROOT / 'flat' / class_name
    for img_file in class_dir.glob('*'):
        if img_file.is_file():
            rows.append([str(img_file.relative_to(DATA_ROOT)), class_name])

with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['filename', 'label'])
    writer.writerows(rows)

print('labels.csv created')
