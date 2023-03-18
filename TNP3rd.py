#matrix
'''mat=[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
for i in range(len(mat)):
    for j in  range(len(mat)):
         if mat[i][j]%2==0:
             mat[i][j]=mat[i][j]**2
         else:
             mat[i][j]=mat[i][j]**3
print(mat)
#list comprehension
mat=[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
mat=[[mat[i][j]**2 if mat[i][j]%2==0 else mat[i][j]**3 for j in range(len(mat))] for i in  range(len(mat))]
print(mat)'''
#paired output

'''mylist=list(map(int,input().split()))
list_b=list(map(int,input().split()))
result=[]
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)

print({i:mylist.index(i)}for i in list_b)'''

#stop words
'''sentences=["C"
           "in the holy city of ayodhya",
           "on the eve of diwali on teusday",
           "with over three lakhs diya or earthen lamps",
           "lit up simultaneously on the bank of river sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with"]
result=[]
for sentence in sentences:#in the holy city of ayodhya
    row_data=[]#empty list
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)# holy city ayodhya
    result.append(row_data)
print(result)
#list comprehension
print([[word for word in sentence,split()if word not in stopwords]for sentence in sentences])'''
#string
'''lst = [3,2,6,5,1,4,8,9]
for i in lst:
    if lst.index(i)<lst.index(5) or lst.index(i)>lst.index(8):
        print(i)
num1=sum(lst[0:lst.index(5)])+sum(lst[lst.index(8)+1:])
print(num1)
temp=list(map(str,lst[lst.index(5):lst.index(8)+1]))
num2="".join(temp)
op=int(num2)+num1
print(op)

print(sum(lst[0:lst.index(5)])+sum(lst[lst.index(8)+1:])+int("".join(list(map(str,lst[lst.index(5):lst.index(8)+1]))))) '''

#string rotation
'''s=input().split(",")
stt=[]
for i in s:
   s1,n=i.split(":")
   stt.append(s1)#stt=[rhdt,ghftd]
   numm.append(n)#numm=[246,1246]
def rotate (ss,n):#ss=rhdt,n=246
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]  # rhdt t   +rhd
    else:
        return ss[2:]+ss[:2] # ghftd  ftdgh
for i in range(len(numm)):
    print(rotate(strr[i],numm[i]))'''
#prime addition
n=int(input())
for i in range(n,n+9):
    if (n%i)==0:
        print(n)
        print(i,n//i,n)
        break
    else:
        print(n)
    
    
            
        





        
   

