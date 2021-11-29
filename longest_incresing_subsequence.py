#sara element ans hoa sakta hai and pta nahi kon sa ans mai ayega jb tak pura na dekhlea
#toa dynamic ka problem hai

#simple dynamic approach

data=input()
data=data.split(",")
list=[]
for i in data:
    list.append(int(i))
n = len(list)
lis_len = [1]*n  # to create an list of n size with value 1
max = 1
#for i in list:   we will not use this since we need index
for i in range(1,n):
    for j in range(0,i):
        if list[i]>list[j]:
            temp = lis_len[j]+1
            if temp>lis_len[i]:
                lis_len[i]=temp
                if temp>max:
                    max = temp
print("longest increasing subsequence is = "+str(max))


#also by sort your list now find longest commmon subsequence in sorted vs unsorted list

#by recursion
def max1(a,b,c):
    if (a>b and a>c):
        return a
    if (b>c):
        return b
    else:
        return c
def lcs(list1,list2,l1,l2):
    if ((l1==0) or (l2==0)):
        return 0
    if list1[l1-1]==list2[l2-1]:
        return 1+lcs(list1,list2,l1-1,l2-1)
    return max1(lcs(list1,list2,l1-1,l2-1),lcs(list1,list2,l1,l2-1),lcs(list1,list2,l1-1,l2))

def lcs_dynamic(list1,list2,l1,l2):
    ans=[[-1 for i in range(l1+1) ] for j in range(l2+1)]
    for i in range(0,l1+1):
        for j in range(0,l2+1):
            if i==0 or j==0:
                ans[i][j]=0
            elif list1[i-1]==list2[j-1]:
                ans[i][j]=1+ans[i-1][j-1]
            else:
                ans[i][j]=max1(ans[i-1][j-1],ans[i][j-1],ans[i-1][j])
    return ans[-1][-1]


data=input()
data=data.split(",")
list1=[]
for i in data:
    list1.append(int(i))
l1 = len(list)
l2 = l1
list2= sorted(list1)
print(lcs_dynamic(list1,list2,l1,l2))
