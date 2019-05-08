import dataRetrieval

dataRetrieval.getData()

followingFolder=open("following.txt","r")
followingList= []
for following in followingFolder:
    followingList.append(following)

followersFolder=open("followers.txt","r") 
followersFist= []
for follower in followersFolder:
    followersFist.append(follower)

for followingUser in followingList:
    control=True
    for followerUser in followersFist:
        if followerUser==followingUser:
            control=False 
    
    if control==True:
        print(followingUser)