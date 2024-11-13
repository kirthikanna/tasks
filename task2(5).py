#write a python program that takes a string and returns if it is palindrome, false otherwise
a="malayalam"
b=""
for i in a:
    b=i+b
if(a==b):
    print("string is palindrome")
else:
   print("string are not palindrome")