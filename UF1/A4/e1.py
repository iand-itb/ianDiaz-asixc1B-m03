num = int(input("Give me a number: "))
m = 1

for i in range(1, num):
    m = m * (i + 1)
print(f"{num}! = {m}")