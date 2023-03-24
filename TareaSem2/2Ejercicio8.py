list=range(0,100,1)

prime=[]

for a in list:
   c=0
   for j in range(1,a):
      if a%j==0:
         c+=1
   if c==1:
      prime.append(a)
print(prime)