num = int(input("Enter a nuber:"))
count=0
while num !=0:
   num //= 10
   count += 1
print("number of digits:" + str(count))
