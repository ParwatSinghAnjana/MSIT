s = input("Enter the String:")
subString = 'bob'
count =0
flag=True
start=0
while flag:
    a = s.find(subString,start)  # find() returns -1 if the word is not found, 
                            #start i the starting index from the search starts(default value is 0)
    if a==-1:          #if pattern not found set flag to False
        flag=False
    else:               # if word is found increase count and set starting index to a+1
        count=count+1        
        start=a+1
print(count)
