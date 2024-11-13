a="apple"
count=0
unique_character=""
for i in range(len(a)):
    if a[i] not in unique_character:
      unique_character=unique_character+a[i]
      count+=1
print("no of unique character", unique_character)
print("no of unique character", count)