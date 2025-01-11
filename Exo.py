# nom =input("Entrez votre nom : ")
# prenom =input("Entrez votre prenom : ")
# print("Bonjour",prenom,nom)
# a="le chat"
# b= "chasse"
# c= "la souris"

# s=a+" "+b
# print(s)
# s+=" "+c
# print(s)

# s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(s[0],s[1],s[25])
# t=s[3:5]
# u=s[:5]
# r=s[16:]
# v=s[16:-2]
# # print(type(t), t,u,r,v)

# a=3
# b=4
# c="bob"

# print(f"nous avons {a} et {a+b} et aussi {c}")

# for i in range(2,10,2):
#     print(i)#multiple de 2 dans l'intervalle [2,10[

# for c in "blah":
#     print(c)
    
# a=2
# if a>3:
#     pass
# else:
#     print("a est plus petit ou egale  a 3")    

epsilon=1e-6
x=2
a=0
b=1+x

while b-a>=epsilon:
    c=(a+b)/2
    if (c*c>=x):
        b=c
    else:
        a=c
print(f"sqrt{x} est {c}")

for n in range(2,25):
    m=2
    while m<n and n%m>0 :
        m+=1
    if m==n:
        print(n)    