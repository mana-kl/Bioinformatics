f=open("dataset_2_10.txt","r")
file_contents = f.read()
k=13

def  FrequentWords(file_contents,k):
    count=[]
    nonD=[]
    length=len(file_contents)
    print(length)
    for i in range(0,length-k):
        matching=file_contents[i:i+k]
        flag=file_contents.count(matching)
        count.append(flag)
    maxVal=0
    for i in range(0,length-k):
        if count[i]>=maxVal:
                maxVal=count[i]
    print(maxVal)
    nonD=[]
    for i in range(0,length-k):
        if(count[i]==maxVal):
            nonD.append(file_contents[i:i+k])
    nonD = list(dict.fromkeys(nonD))
    print(nonD)
FrequentWords(file_contents,k)