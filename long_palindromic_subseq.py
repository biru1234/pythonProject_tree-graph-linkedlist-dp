
def max1(a,b):
    return a if a>b else b

def lps_recursion(list1,start,end):
    if start==(end-1):
        return 1
    if list1[start]==list1[end-1] and (start+1)==(end-1):
        return 2
    if list1[start]==list1[end-1]:
        return 2+lps_recursion(list1,start+1,end-1)
    return max1(lps_recursion(list1,start+1,end),lps_recursion(list1,start,end-1))


#for each subset lea jaisa ki 2 ka element then 3 ka element and 4 soon
#and table mai store karte jaa rahe hai toa iss subset ka direct an mila toa thik warna recusrsion walea
#se dekh best choice kya hai ek elemnt remove ya sarae remove karna
#yaha direct recusrion can't convert to dynamic since yaha ek hi array mai move karn hai
#recusrion mai ek hi movement tha ek from start and ek from end so logic chnage

def lps(list1,start,end):
    dp=[[0 for x in range(end+1)] for y in range(end+1)]
    max2 = -1
    for i in range(end):
        for j in range(end):
            if i==j:
                dp[i][j]=1
                if max2<dp[i][j]:
                    max2=dp[i][j]
            elif list1[i]==list1[j] and i+1==j :
                dp[i][j]=2
                if max2<dp[i][j]:
                    max2=dp[i][j]
            elif list1[i]==list1[j]:
                if i+1>=end or j-1<0:
                    dp[i + 1][j - 1]=0
                dp[i][j]=2+dp[i+1][j-1]
                if max2<dp[i][j]:
                    max2=dp[i][j]
            else:
                if i+1>=end :
                    dp[i+1][j]=0
                if j-1<0:
                    dp[i][j-1]=0
                dp[i][j]=max1(dp[i][j-1],dp[i+1][j])
                if max2<dp[i][j]:
                    max2=dp[i][j]
    return max2


list1=input()

print(lps(list1,0,len(list1)))
#print(lps_recursion(list1,0,len(list1)))
