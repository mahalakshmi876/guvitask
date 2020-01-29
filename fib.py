p=int(input("enter the value"))
f=0
s=1
if(p<=0):
 print("the series has no meaning",f)
else:
 print(f,s,end="")
 for i in range(2,p):
  next=f+s
  print(next,end="")
  f=s
  s=next
