

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Pineapple",
    "Strawberry",
    "Blueberry",
    "Grapes",
    "Watermelon",
    "Kiwi",
    "Papaya",
    "Peach",
    "Pear",
    "Cherry",
    "Pomegranate",
    "Plum",
    "Lemon",
    "Lime",
    "Coconut"
]

print(fruits)


L=['q','w','e','t','y']
length=len(L)
for a in range(length):
    print("At indexes",a,"and",(a-length),"element:",L[a])


lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
slc1=lst[5:15:2]
slc2=lst[::4]
sum=avg=0
print("Slice1")
for a in slc1:
    sum+=a
    print(a,end='')
print()
print("Sum of elements of slice 1:",sum)
print("Slice 2")
sum=0
for a in slc2:
    sum+=a
    print(a,end='')
print()
avg=sum/len(slc2)
print("Average of elements of slice2:",avg)


L1=[17,24,15,30,34,27]
L2=L1.copy()
print("Original list:",L1)
print("Created copy of the list:",L2)
L2[0]+=10  #first element changed in the list copy
L2[-1]+=10 #last element changed in the list copy
print("Copy of the list after changes:",L2)
print("Original list:",L1)


my1=[2,4,6]
print("Exsisting list is :",my1)
n=eval(input("Enter a number or a list to be appended:")
if type(n)== type([]): #if a list is input
    my1.extend(n)
elif type(n)==type(1): #if an integer is input
    my1.append(n)
else:
    print("Please enter either an integer or a list.")
print("Appended list is:",my1)
