a=open("following.txt","r")
b=open("followers.txt","r")
alist= []
for x in a:
    alist.append(x)
        
blist= []
for x in b:
    blist.append(x)

for y in alist:
    control=True
    for z in blist:
        if z==y:
            control=False 
    
    if control==True:
        print(y)