calc=input("Hesablamani girin: ")

if calc.find("+") != -1:
    calc=calc.split("+")
    print(float(calc[0]) + float(calc[1]))
elif calc.find("-") != -1:
    calc=calc.split("-")
    print(float(calc[0]) - float(calc[1]))
elif calc.find("*") != -1:
    calc=calc.split("*")
    print(float(calc[0]) * float(calc[1]))
elif calc.find("/") != -1:
    calc=calc.split("/")
    print(float(calc[0]) / float(calc[1]))
elif calc.find(":") != -1 :
    calc=calc.split(":")
    print(float(calc[0]) % float(calc[1]))