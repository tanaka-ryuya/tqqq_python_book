import os
from dotenv import load_dotenv
import subprocess

# .env 読み込み
load_dotenv()

title = os.getenv("TITLE")
author = os.getenv("AUTHOR")
language = os.getenv("LANGUAGE", "ja")
cover = os.getenv("COVER")

# 結合対象の Markdown ファイル（0.md ~ 10.md）
filenames = [f"{i}.md" for i in range(11)]
with open("all.md", "w", encoding="utf-8") as outfile:
    for fname in filenames:
        with open(fname, "r", encoding="utf-8") as infile:
            outfile.write(infile.read() + "\n\n")

# pandoc コマンド構築
cmd = [
    "pandoc", "all.md", "-o", "all.epub",
    "--metadata", f"title={title}",
    "--metadata", f"author={author}",
    "--metadata", f"language={language}",
    "--epub-cover-image", cover,
    "--toc"
]

# 実行
print("Running Pandoc...")
result = subprocess.run(cmd, capture_output=True, text=True)

# 成否の出力
if result.returncode == 0:
    print("✅ all.epub が生成されました！")
else:
    print("❌ エラー発生:")
    print(result.stderr)