f=open("dataset_2_7.txt","r")
file_contents = f.read()
print("opened")
print(len(file_contents))
Flag = file_contents.count("GAGGCTGGA");
print(Flag-1)
f.close()
