rfile = open("natsume.txt", encoding="UTF-8")
text = rfile.read()
rfile.close()
text = text.replace("。", "〜♪")
print(text)

wfile = open("natsume_kai.txt", encoding="UTF-8", mode="w")
wfile.write(text)
wfile.close
