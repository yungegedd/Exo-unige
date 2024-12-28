#x, y = 3, 5
#print("x=%s" % x)
#print("y=%s" % y)
 #print("la somme de %s et %s est %s" % (x, y, (x+y)))

#fonction et methode
# x="123"
# int("123")
# print(type("x"))



# --------exercice 1------------
x=str(input("entrer votre nom: "))
print("Bonjour %s comment allez vous?" %x)
y=int(input("entrer votre age: "))
print("vous avez %s ans. plus que %s pour etre centenaire." % (y, str(100-y)))

# --------exercice 2------------
ch="salut"
print('*'+ch[0]+'*'+ch[1]+'*'+ch[2]+'*'+ch[3]+'*'+ch[4])

# --------exercice 3------------
u=1
print("u0=",u)
u=2*u-7
print("u1=",u)
u=2*u-7
print("u2=",u)

# --------exercice 4------------
x,y,z=3,5,7
v=x*y*z
print("volume du parallépipede v=", v)

# --------exercice 5------------
ts=189956 #temps en seconde
h=ts//3600
m=(ts%3600)//60
s=(ts%3600)%60
j=ts//86400
week=j//7
print("durée=",ts, h, "h", m, "m", s, "s", j, "j", week, "semaine")

# --------exercice 6------------
x="fotes"
x.replace("o", "au")
print(x.replace("o", "au"))