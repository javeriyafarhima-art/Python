r=int(input("Please Enter the Total Number of Rows :"))
print("Mirrored Right Traingle Star Pattern")
for i in range(1, r+1):
    if(j <= r - i):
        print(' ', end =' ')
    else:
        print('*',end=' ')
print()
