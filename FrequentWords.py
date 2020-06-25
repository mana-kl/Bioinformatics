f=open("dataset_2_10 (18).txt","r")
count=[]
string_pattern=[]
nonD=[]
file_contents = f.read()
length=len(file_contents)
print(length)
for i in range(0,length-13):
        matching=file_contents[i:i+13]
        flag=file_contents.count(matching)
        count.append(flag)
        string_pattern.append(matching)
maxVal=0
for i in range(len(count)):
        if count[i]>=maxVal:
                maxVal=count[i]
print(maxVal)
nonD=[]
for i in range(len(count)):
    if(count[i]==maxVal):
        nonD.append(string_pattern[i])
nonD = list(dict.fromkeys(nonD))
print(nonD)