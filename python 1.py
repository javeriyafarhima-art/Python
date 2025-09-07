M={}
n=int(input("How many students?"))
for i in range(n):
    r,m=eval(input("Enter Roll No.,Marks:"))
    M[r]=m
print("Created dictionary")
print(M)





print("Created dictionary")
print(M)
print("To modify marks")
r=int(input("Enter roll number:"))
if r in M:
      M[r]=float(input("Enter new marks:"))
else:
    print("No such roll number found")
print("Modified dictionary is")
print(M)
