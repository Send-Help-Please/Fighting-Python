import string

lowercase=list((string.ascii_lowercase[:]))
print(len(lowercase))
content=input("Input plain text: ")
key=int(input("Input key value: "))
enc_text=[]
enc=''   

for char in range(len(content)):
    #print(lowercase.index(content[char]))
    enc_value=lowercase.index(content[char]) + key
    print(enc_value)
    if enc_value >= 26:
        enc_value = enc_value -26
        enc_text.append(enc_value)
        print(enc_text)
    else:
        enc_text.append(enc_value)
for val in enc_text:
    #print(lowercase[val])
    enc += lowercase[val]
    
print(f"Encrypted text: {enc} ")