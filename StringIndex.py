f=open("Vibrio_cholerae.txt","r")
file_contents = f.read()
matching="CTTGATCAT"
length=len(file_contents)
for i in range(0,length-9):
        index=file_contents.find(matching,i,i+9)
        if(index>0):
            print(index)