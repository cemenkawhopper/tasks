#task 2
a = int(input())
b = int(input())
if a < b:
 while a <= b-1:
    a+=1
    print(a)
else:
    while a >= b + 1:
        a -= 1
        print(a)