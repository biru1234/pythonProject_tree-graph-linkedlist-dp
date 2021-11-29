#jab recusrion se dynamic mai convet karao tab jab equal hoa i and j length wise joa change hoa rahe hai toa
#koi dikkat nahi hai but different hoa toa
#jab dp ka table creat kar rahe hoa toa joa row(1st) in list hoga woa looping timing mai column(2nd) hoa
#jayega

"""explanation : let i =4 and j= 10 toa table ban gya 4*10 ka mtlb 4 rows and 10 column
and generally base case mai 0 index wala ka value 0 set karte hai
toa jab loop chaleg tab dp[i][j]=0  set karn hoga and agar looping mai
i 1st hai and j second toa j 10 bar chalega since 4*10 hai and
case ayega dp[0][0] ,dp[0][1] ,dp[0][2] ,dp[0][3] ,dp[0][4] ,dp[0][5] ,dp[0][6] ,dp[0][7] ,.......
so on so error ayega since dp[0][4] exist hi nahi kart hai samjhe
isliye joa table banoge uska reverse way mai loping mai use hoga
"""

def max1(a,b):
    if a>b:
        return a
    else:
        return b

def knapsack(weight,value,n,w):
    if w==0 or n==0:
        return 0
    if w<weight[n-1]:
        return knapsack(weight,value,n-1,w)
    return max1((value[n-1]+knapsack(weight,value,n-1,w-weight[n-1])),knapsack(weight,value,n-1,w))

def knapsack_dynamic(weight,value,n,w):
    dp=[[-1 for y in range(w+1)] for z in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,w+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif weight[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max1(value[i-1]+dp[i-1][j-weight[i-1]],dp[i-1][j])
    return dp[-1][-1]

def knapsack_dynamic_1(weight,value,n,w):
    dp=[[-1 for y in range(n+1)] for z in range(w+1)]
    for i in range(0,w+1):
        for j in range(0,n+1):
            if i==0 or j==0:
                #print(i)
                #print(j)
                dp[i][j] = 0
                #print(dp)
            elif weight[j-1]>i:
                dp[i][j]=dp[i][j-1]
            else:
                dp[i][j]=max1(value[j-1]+dp[i-weight[j-1]][j-1],dp[i][j-1])
    return dp[-1][-1]

data = input("wight of items ")
data=data.split(",")
val=input("value or profit of item ")
val=val.split(",")
weight=[]
for x in data:
    weight.append(int(x))
value=[]
for x in val:
    value.append(int(x))

W=int(input("max weight we can take "))
print("by recursion")
print(knapsack(weight,value,len(weight),W))
print("by dynamic")
print(knapsack_dynamic(weight,value,len(weight),W))
print("another ")
print(knapsack_dynamic_1(weight,value,len(weight),W))
