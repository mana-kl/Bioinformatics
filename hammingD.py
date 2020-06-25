f=open("dataset_9_3.txt","r")
string1=f.readline()
string2=f.readline()
count=0
length=len(string1)
for i in range(length):
    if(string1[i]!=string2[i]):
        count+=1
print(count)
