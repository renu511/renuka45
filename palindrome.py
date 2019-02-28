a=int( input())
temp=a
reve=0
while(a>0):
  var=a%10
  reve=reve*10+var
  a=a//10
if reve==temp:
  print("yes")
else:
  print("no")
