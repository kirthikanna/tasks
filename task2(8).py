#write a program that takes string and retruns true if it is anagram of another string
a="face"
b="cafe"
x=[a[i] for i in range(len(a))]
x.sort()
y=[b[j] for j in range(len(b))]
y.sort()
if(x == y):
 print("strings are anagram")
else:
 print("strings are not anagram")