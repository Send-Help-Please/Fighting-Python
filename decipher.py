with open("ctf.txt", "r") as f:
    lines = f.readlines()
text=""
for line in lines[2:]:
    line = line.strip()
    codes=line.split()
    for asc in codes:
        asc=int(asc)
        if asc != " ":
            text += chr(asc)
        else:
            continue
print(text)

if "password" in text.lower():
    pass
print(text[80:]) 

