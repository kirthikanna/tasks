#write program that takes a string and retruns a new string with all the vowels are removed
a="guvi geeks network private limited"
b=""
vowels=["a","e","i","o","u"]
for i in range(len(a)):
    if a[i] not in vowels:
        b=b+a[i]
print("After removing vowels", b)