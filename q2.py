num = int(input("enter a number :"))
a = []
while(num>0):
    d = num%2
    a.append(d)
    num = num//2
a.reverse()
print("the binary format is:")
for i in a:
    print(i , end="")