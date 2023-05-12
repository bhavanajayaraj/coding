"""an automobile company manufactures both a 2 wheeler(tw) and a 4 wheeler(fw).a company manager wants to 
make the production of both types of vehicle acc to the given data below:
    d1=total vehicles(v)=tw+fw
    d2=total wheels=w
    task is to find how many tw as well as fw need to manufacture as per the given data
    i/p:v=200
        w=540  #same ip op format
    o/p:tw=130 fw=70
    explanation:
        (70*4)+(130*2)=540
        (x*4)+(w-x*2)=w
        
        v<w print invalid ip
        """
        
    
t=int(input("enter :"))
for i in range(t):
    v=int(input("v:"))
    w=int(input("w:"))
    if (w&1)==1 or w<2 or w<=v:
        print("invalid")
    else:
        x=((4*v)-w)//2
        print("tw={0}fw={1}".format(x,v-x))
    