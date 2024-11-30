a = """Passwd12!
letmein2@
!!pwd12!!
@B4kili@
Salamm23@
gedebey2!
abcdefg5@
Strong23^
##qwerty33""".split("\n")
for char in range(len(a)):
    pattern=''
    for letter in range(len(a[char])):
        #print(a[char][letter])
        if a[char][letter].isupper():
            pattern += "?u"
        if a[char][letter].islower():
            pattern += "?l"
        if a[char][letter].isnumeric():
            pattern += "?d"
        else:
            pattern += "?s"
    print(f"{a[char]} : {pattern}")
    
    
       