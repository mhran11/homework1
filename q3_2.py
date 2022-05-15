import json
x1 = 0
x2 = {}
x3 = []
name = input(" name :")
with open("bb.json","r") as f:
    bb = json.loads(f.read())
    for i in bb :
        print(i)
        a1 = input("enter  a or b :")
        x3.append(a1)
        if a1 == bb[i]:
           x1 = x1+1
        else:
            x1 = x1-1

    x2 ={name:x3}
    print(x2)

    print("The result :",x1)