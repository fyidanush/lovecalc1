name1 = input("Enter your name: \n ")
name2 = input("Enter their name: \n ")
full_name = name1 + name2
a = full_name.lower()
t1 = a.count("t")
r1 = a.count("r")
u1 = a.count("u")
e1 = a.count("e")
true = t1 + r1 + u1 + e1
l = a.count("l")
o = a.count("o")
v = a.count("v")
e = a.count("e")
love = l + o + v + e
calc = str(true)+ str(love)
calc1 = int(calc)

#Result
if calc1 < 10 or calc1 > 90:
    print("your score is",calc,"% you go together like coke n mentos")
elif calc1 >= 40 or calc1 <= 50:
    print("your score is",calc,"% you are alright together")
else:
    print("Your love score is",calc,"%")