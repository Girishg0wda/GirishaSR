a = int(input("Enter a number: "))

series = []
for i in range(1, a+1):
    series.append(2*i - 1)

print(", ".join(map(str, series)))
