2. Harshad Numbers

n = int(input())
s = 0
t = n
while t > 0:
    s += t % 10
    t //= 10
if n % s == 0:
    print("Yes")
else:
    print("No")
