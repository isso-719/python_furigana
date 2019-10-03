from pathlib import Path
terms = {"for": 0, "if": 0, "else": 0}
path = Path()
for filepath in path.glob("*.py"):
    rfile = open(filepath, encoding="UTF-8")
    text = rfile.read()
    rfile.close()
    for term in terms:
        cnt = text.count(term)
        terms[term] += cnt
print("これまでのプログラムに")
for _ in terms:
    print(" ", _, "は", terms[_], "回")
print("使われました。")
