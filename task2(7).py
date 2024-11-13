a="geeks network"
print(a)
most_frequent={}
for i in a:
    if i in most_frequent:
        most_frequent[i]=most_frequent[i]+1
    else:
        most_frequent[i]=1
    result=max(most_frequent , key = most_frequent.get)
    print("most frequent character", result)