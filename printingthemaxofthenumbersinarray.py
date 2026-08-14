arr= [1,1,0,0,0,1,0,0,1,1,1,1,0,1,1,1,1,1]
max_count =0
count =0
for i in range (0,len(arr)):
    if arr[i]==1:
        count+=1
    else:
        count=0
    if (count>max_count):
      max_count=count

print(max_count)