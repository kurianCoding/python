class user:
    def __init__(self,name):
        self.friends=[]
        self.name=name
    def __str__(self):
        return self.name+":"+','.join(self.friends)
userCount=raw_input("enter the number of users\n")
count=int(userCount)
users=[]
## a function which will input a graph with nodes and edges
def intput():
    for i in range(count):
        name=raw_input("enter name of the user\n")
        print(name)
        protoUser=user(name)
        users.append(protoUser)
    for j in users:
        friendList=raw_input("enter the names of friends of "+j.name+"\n").split(" ")
        j.friends=friendList
    for k in users:
        print k
