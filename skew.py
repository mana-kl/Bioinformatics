file_pointer= open("dataset_7_6.txt","r")
file_contents=file_pointer.read()
answer=[]
answer.append(0)
value=0
length=len(file_contents)
for i in range(length):
    if(file_contents[i]=="A"):
        answer.append(value)
    elif(file_contents[i]=="T"):
        answer.append(value)
    elif(file_contents[i]=="G"):
        value+=1
        answer.append(value)
    elif(file_contents[i]=="C"):       
        value-=1     
        answer.append(value)
minimum=min(answer)
for i in range(len(answer)):
    if(answer[i]==minimum):
        print(i)