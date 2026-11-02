from pathlib import Path

base = Path(".")
prompt_path = base / "prompt.txt"

prompt = prompt_path.read_text(encoding="utf-8")

for txt in base.glob("*.txt"):
    if txt.resolve() == prompt_path.resolve():
        continue  # don't append prompt.txt to itself

    # Optionally ensure the file ends with a newline before appending
    needs_newline = txt.stat().st_size > 0 and not txt.read_bytes().endswith(b"\n")

    with txt.open("a", encoding="utf-8") as f:
        if needs_newline:
            f.write("\n")
        f.write(prompt)