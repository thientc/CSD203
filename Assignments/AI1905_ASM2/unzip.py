import zipfile
from pathlib import Path

p = Path(r'.').glob('**/*.zip')
files = [x for x in p if x.is_file()]
for f in files:
    with zipfile.ZipFile(f.name, 'r') as zip_ref:
        zip_ref.extractall('.')
