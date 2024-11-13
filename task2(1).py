a="Guvi Geeks Network private limited"
b=a.count("a")
c=a.count("e")
d=a.count("i")
e=a.count("o")
f=a.count("u")
print(b)
print(c)
print(d)
print(e)
print(f)
count=0
vowels=["a","e","i","o","u"]
for i in range(len(a)):
    if a[i] in vowels:
      count=  count+1
print("no of vowels in a",count)



