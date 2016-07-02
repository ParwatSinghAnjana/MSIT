s = input("Enter the String:")
subString = 'bob'
count =0
flag=True
start=0
while flag:
    a = s.find(subString,start)
    if a==-1:
        flag=False
    else:
        count=count+1        
        start=a+1
print("Number of time Bob occured is:")
print(count)
