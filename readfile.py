filepath = r"C:\Users\Bashko\Documents\simple.txt"

with open(filepath, "r", encoding="utf-8") as document:
    text = document.read()
print(text)
