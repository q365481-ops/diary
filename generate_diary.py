
from pathlib import Path
import re
import json

# YYYY-MM-DD.html 形式の日記を探す
pattern = re.compile(r"^\d{4}-\d{2}-\d{2}\.html$")

files = [
    p.name
    for p in Path(".").iterdir()
    if p.is_file() and pattern.fullmatch(p.name)
]

files.sort(reverse=True)

# トップページから読み込む一覧を作成
Path("diary-list.json").write_text(
    json.dumps(files, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print(f"{len(files)}件の日記を登録しました")
