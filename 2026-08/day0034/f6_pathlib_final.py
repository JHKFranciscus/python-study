from pathlib import Path

base_dir = Path("records")
file_path = base_dir / "study.txt"

base_dir.mkdir(exist_ok=True)
file_path.write_text("python pathlib study", encoding="utf-8")

print(file_path.exists())
print(file_path.is_file())
print(file_path.name)
print(file_path.suffix)
print(file_path.read_text(encoding="utf-8"))

# 예상 결과
# 1. exists():
# True
# 2. is_file():
# True
# 3. name:
# study.txt
# 4. suffix:
# .txt
# 5. read_text():
# python pathlib study