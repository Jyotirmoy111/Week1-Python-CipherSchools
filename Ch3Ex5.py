n=input("Enter your name: ")
var=""
i=0
while i < len(n):
    if n[i] not in var:
        var+=n[i]
        print(f"{n[i]}:{n.count(n[i])}")
    i+=1