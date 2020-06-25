f=open("dataset_9_4.txt","r")
answer=open("appAnswer.txt","w")
pattern=f.readline().strip('\n')
text=f.readline().strip('\n')
d=int(f.readline().strip('\n'))
length=len(text)
pl=len(pattern)
def hamming(pattern,text,dist):
    count=0
    length=len(pattern)
    for i in range(0,length):
        if(pattern[i]!=text[i]):
            count+=1
    if(count<=dist):
        return 1
    else:
        return 0
for i in range(0,length-pl+1):
        index=hamming(pattern,text[i:i+pl],d)
        if(index>0):
            answer.write(str(i))
            answer.write(" ")