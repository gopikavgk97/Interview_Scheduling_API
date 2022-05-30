
from gevent import get_hub


def checkarmstrong(a):
    temp=0
    dig=0
    new=a
    l=len(str(a))
    while(new!=0):
        dig=new%10
        temp=temp+(dig**l)
        new=new//10
    if(temp==a):
        print(temp)
# for i in range(10,400):
#     checkarmstrong(i)
def checkprime(a):
    for i in range(2,a):
        if(a%i==0):
            break
    else:
        return True
b=[2,]
for i in range(3,40):        
    if(checkprime(i)):
        #print(i) 
        b.append(i)  
print(b)         

def checkpalindrome(a):
        temp=0
        dig=0
        new=a
        while(new!=0):
            dig=new%10
            temp=temp*10+dig
            new=new//10
        if(temp==a):
            return temp
        

# a=222        
# checkpalindrome(a)  



# c=[112,212,111]
# b=[]
# b.append([checkpalindrome(i) for i in c])
# print(b)

# c={"1":2,"3":4,"5":6}
# b=[]
# d=[]
# b=list(c.items())
# d.append(c.items())
# print(b)
# print(d)
# e=[1,2,3,4,5,6]
# c='gopika'
# # d=list(c.split(" "))
# print(e[:0])
# def Convert(string):
#     list1=[]
#     list1[:0]=string
#     return list1
# # Driver code
# str1="ABCD"
# print(Convert(str1))
# get_hub
# jkjIp
# jo
test_str='gopikaaaaaa'
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get) 
print(all_freq)