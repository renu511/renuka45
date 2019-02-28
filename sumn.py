n,k=(int(x) for x in input().split())
l=[]
sum=0
for x in range(1,n+1):
  l.append(x)
print(*l) 
for x in range(1,k+1):
  sum=sum+x
print(sum)  


