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
s= 'Une Grande Maison'
str.lower(s)    
print(str.lower(s))   
s.lower()
print(s.lower())
#liste tuple ensemble dictionnaire
a=['un',2,3,'quatre',5,6,7,'sept']
print(a)
print(a[0])
print(a[1:])
print(a[2:-1])

a='toto'
b=a
a+= ' et titi'
print(a)
print(b)

a=[1,2,3]
b=a
a+=[4,5,6]
print(a)
print(b)

a+='blah'
print(a)

a=['truc']
b=a
c=a.copy()
a+=['machin']
print(a)
print(b)
print(c)

l=[[1,2],[3]]
print(l)
m=l.copy()
print(m)
l[0]='truc'
print(l)
print(m)
l[1]+=['un']
print(l)
print(m)

l=[0,1,2,3,4,5,6,7,8,9]
print(len(l))
l.append(10)
print(l)
l.insert(4,40)
print(l)
l.remove(40)
print(l)
l.reverse()
print(l)
l[5]=111
print(l)
l[1:4]=['a','b']
print(l)

a=[0,1,2,3,4,5]
print(a)
del a[2]
print(a)
del a[1:3]
print(a)

for m in ['premier','deuxieme','troisieme']:
    print(m)
a=[1,2,3,4,5]
2 in a    
print(2 in a)
1 in a
print(1 in a)
10 in a
print(10 in a)
p =[]
p.append('paris')
print(p)
p.append('london')
print(p)
p.append("tokyo")
print(p)
p.pop()
print(p)
p.append('berlin')
print(p)
print(p.pop())
print(p)

#tuples
a=("un",2,3.0)
print(a)
print(len(a))

b="un",2,3.0
print(b)

s=150,
print(s)
print(a[0])
print(b[1:3])
l=[1,2,3]
l[2]=4
print(l)
t='un',2,3
print(t)
#t[2]=4
#t[2]=4(impossible)

a,b=(1,2)
print(a)
print(b)
x=['bob',35,'berlin']
name,age,city=x
print(name)
print(age)
print(city)

#a,b,c=(1,2,3,4,5)
#print(a)

for a,b in [(1,-1),[3,4],["pim","pam"]]:
    print(a+b)
a='123' 
print(list(a))  
print(tuple(a)) 
l=tuple(a)
print(l)
l=['un','deux','trois']
print(tuple(l))

#ensembles
print({1,2,3,5,3,2})
print(set('abracadabra'))
a=set([12,56,78,12,34,56,12,17])
print(a)
print(35 in a)

f={'geneve','zurich','berne','neuchatel','lausanne'}
g={'berne','zurich','berne','bale','fribourg'}
print(f-g)
print(f|g)
print(f&g)
print('berne' in f)

#dictionnaires
prix={'pomme':1.5,'poire':2.0,'banane':1.0}
print(prix['pomme'])
prix['pomme']=1.6
print(prix['pomme'])
prix['orange']=1.8
print(prix)
del prix['banane']
print(prix)
prix['orange']=1.9
print(prix)
d=dict([(1,'un'),(2,'deux'),(3,'trois')])
print(d)
for k,v in d.items():
    print(k,v)
prix={'pomme':1.5,'poire':2.0,'banane':1.0}
print(list(prix.keys()))
print(list(prix.values())) 
#fonctions

def le_plus_grand(a,b):
    if a>b:
        return a
    else:
        return b
print(le_plus_grand(3,5))  
print(le_plus_grand(5,3))   
print(le_plus_grand('toto','titi')) 

def bonjour(nom):
    print('Bonjour',nom)
bonjour('toto')
bonjour(456)    
