file_pointer= open("dataset_3_2 (7).txt","r")
output_file=open("assignment3answer.txt","w")
file_contents=file_pointer.read()
file_reverse=file_contents[::-1]
answer=[]
length=len(file_reverse)
for i in range(length):
    if(file_reverse[i]=="A"):
        answer.append("T")
    elif(file_reverse[i]=="T"):
        answer.append("A")
    elif(file_reverse[i]=="G"):
        answer.append("C")
    elif(file_reverse[i]=="C"):            
        answer.append("G")
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1 
output_file.writelines(listToString(answer))