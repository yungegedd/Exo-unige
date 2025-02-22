# syntaxe generale python

# for k in range(10):
#     print(k)

# s=0
# t=0

# for k in range(5):
#     print("k=",k)

#     if k%3==0:
#         print("k est multiple de 3")
#         t= t+k
    
#     s=s+k

#     print("s=",s , "t=",t)



# s=3

# for k in range(10):
#     s=s+k
#     print("s=",s)

# nom=input("Entrez votre nom : ")
# print("Bonjour chère/cher",nom)

# a=3
# print(a,type(a))

# a="toto"
# print(a,type(a))

# a,b=3,4
# print(a,b,type(a),type(b))

# a= 3
# b= 4.2
# print(a,type(a))
# print(b,type(b))

# print(a+b,type(a+b))

# #conversion de type
# x=3
# print(x,type(x))

# x=float(x)
# print(x,type(x))

# x=str(x)
# print(x,type(x))

# x=float(x)
# print(x,type(x))
 #operateurs arithmetiques

# a=14
# b=5

# print(a/b , a//b , a%b , a**b)

# a = True
# b=4<5
# print(not(a) or b)

# a="le chat"
# b="chasse"
# c="la souris"

# s= a + "" + b
# print(s)

# s += " " + c

# s="ABCDEFGHIJKLBNOPQRSTUVWXYZ"
# print(s[0] ,s[10],s[20],s[25])
# t=s[0:10]
# print(t)
# u=s[3:5]
# print(u)
# r=s[:5]
# print(r)
# v=s[16:]
# print(v)
# w=s[16:-2]
# print(w)
# print(type(t), t ,u , r , v)
# a=3
# b=4.5
# c="toto"
# print(f"Vous avez {a} et {a+b} et aussi {c}")
# print("Vous avez",a,"et",a+b,"et aussi",c)

# for i in range(0,50,5):
    # print(i)
# for i in range(50,0,-5):
#     print(i)  
# for i in range(0,50,5):les nombres de 0 à 50 par pas de 5
# borne n'est pas incluse  

# for c in "blah":
#     print(c)

# for a in range(10):
#     if a > 3:
#         pass    
#     else:
#         print(a)
#         print("a est inferieur à 3")

# //version python de calcul de la racine carrée
# epsilon = 1e-6
# x = int(input("Entrez un nombre : "))
# a = 0
# b = 1+x

# while b-a >= epsilon:
#     c =(a+b)/2
#     if c**2 > x:
#         b = c
#     else:
#         a = c
# print(f"sqrt{x}~{c}")   

# version pour estimer pi

# N = 0
# M = 0
# delta = 5e-4

# x = 0
# while x < 1:
#     y = 0
#     while y <= 1:
#         N += 1
#         if x**2 + y**2 <= 1:
#             M += 1
#             y += delta

#     x += delta

# print(f"pi~{4*M/N}")            

for n in range (100):
    m=2
    while m<n and n%m>0:
        m+=1
    if m==n:print (n)    


