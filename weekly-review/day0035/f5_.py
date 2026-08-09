from pathlib import Path

base = Path("data")
file_path = base / "students" / "scores.json"

print(base)
print(file_path)
print(file_path.name)
print(file_path.suffix)
print(file_path.parent)