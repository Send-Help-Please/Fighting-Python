#1. Ededin boyukluk sirasi

"""eded1=int(input("Birinci ededi daxil edin: "))
eded2=int(input("Ikinci ededi daxil edin: "))

if eded1 >= eded2:
    print("Birinci eded ikinciden boyukdur", eded1, eded2, sep=", ")
else: 
    print("Ikinci eded birinciden boyukdur", eded2, eded1, sep=", ")
"""



#2. 3-e ve 5-e bolunmemesi

"""eded=int(input("ededi daxil edin: "))

if eded % 3 == 0 and eded % 5 == 0 : 
    print("Eded hem 3-e hem  5-e bolunur.")
elif eded % 3 ==0 and eded % 5 != 0 :
    print("Eded 3-e bolunur ancaq 5-e bolunmur.")
elif eded % 3 !=0 and eded % 5 == 0 :
    print("Eded 3-e bolunmur ancaq 5-e bolunur.")
else:
    print("Eded ne 3-e ne de 5-e bolunur.")"""



#3. Boyuk herfle yazilmis setir olmasini yoxlamaq

"""setir=input("Setiri daxil edin: ").strip()

if setir[0] == setir[0].upper():
    print("Ilk herf boyukdur.")
else:
    print("Ilk herf boyuk deyil.")"""


#4. Ededin kvadratini tapmaq

"""eded=int(input("Ededi daxil edin: "))
print("Ededin kvadrati: ", eded**2)"""

#5. 


"""calc=input("Hesablamani girin: ")
summ=0
if calc.find("+") != -1:
    calc=calc.split("+")
    #print(float(calc[0]) + float(calc[1]))
    for num in summ:
        num=int(num)
        sum +=0"""
"""elif calc.find("-") != -1:
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
    print(float(calc[0]) % float(calc[1]))"""
    
#------------------24 NOVEMBER -------------------

#practicing

"""var="nijat"
print(f"Hello, {var}")

var="Hello, {}"
print(var.format("nijat"))

name="nijat"
age=19
expression="Hello, my name is {}, i am {} years old"
print(expression.format(name, age))
print(expression.format("Amiray", age))"""

#-------- data types: list, tuple, dictionary, set ------
"""
lst =  [] 
lst.append(1)
lst2=[]
lst2.append(2)

lst += lst2
print(lst)

lst.remove(2)
print(lst)

#pop index ile silir
lst=["salam", "necesen", 1, 2]
removed_element=lst.pop()
print(lst) # defolt olaraq sonuncunu silir
print(removed_element) #pop-un return value su olur = Sildiyi element remove da bele sey yoxdu

#count listin icinde element sayi
print(lst.count("salam"))

#copy kopyalayir

lst3 = lst.copy()
print(lst3) # asili olmayan kopya yaradir
"""

"""
lst=["salam", "necesen", 1, 2]
lst.insert(3, 13) #append axira eleve edir bu ise index -e gore
print(lst)

array = [10, 1,4, 34, 5 ]
array.sort() 
print(array)

array = [10, 1,4, 34, 5 ]
array.sort(reverse=True) #Tersine sort edir 
print(array)

array = [10, 1,4, 34, 5 ]
print(sorted(array)) #array deyismeden siralayir.
print(array)
"""
#------------ BREAK -------------
"""
array = [10, 1,4, 34, 5 ]
del array[1] # return value-su yoxdur
print(array)

lst=[i for i in range(10)] #list comprehension 
print(lst)
"""

"""
soz="Azerbaycan"
print(list(soz))
print([i.upper() for i in soz]) # ['A', 'Z', 'E', 'R', 'B', 'A', 'Y', 'C', 'A', 'N']

lst=["a", "b", "c"]
print("".join(lst)) #listi stringe cevir
"""

"""
tup =(1,2) #immutable, deyismir 
print(tup, type(tup))
"""

"""dict={"key":"value", "key2":"value2"} # sira anlayisi yoxdur. Key-ler indexlenir.
print(dict["key2"])
dict["key3"]=2
print(dict)
"""

#--------------TASK: PORT TO SERVICE MAPPER -----------

"""ports={22:"SSH", 25: "SMTP", 443:"HTTPS", 80:"HTTP"}

while True:
    print("1. Search a port and corresponding service")
    print("2. Add a port and service")
    print("3. See all ports and services")
    print("4. Exit the program.")
    choice=int(input())
    if choice == 1:
        port=int(input("Enter a port number: "))
        if port in ports:
            print(f"Requested port is {port};", "the service is: ", ports[port])
        else:
            print("there's no such a port in database.")
            continue
    elif choice ==2:
        port=int(input("Enter a port number: "))
        if port in ports:
            print("This port already exists.")
        else:
            service_name=input("Enter a service name:")   
            ports[int(port)]=service_name
            print(f"You have added {port}:{service_name}")
            continue
    elif choice == 3:
        for i in ports:
            print(f"{i} - {ports[i]}")
    elif choice == 4: 
        print("Exiting...")
        break
    else:
        print("Invalid choice, please select a menu item!")
        continue"""
        
#-------------TASK ------------

"""ip=input("enter ip address: ").split(".")
ip_new=[]
print(ip)
if len(ip) != 4:
    print("this is not an IP address.")
else:
    for octet in ip:
        ip_new.append(int(octet))
        for i in ip_new: 
            if  i> 255 : 
                print("this is not an IP")
                print(f"Octet Number {i} is faulty.")
            else:
                print("you're good to go.")"""
                
