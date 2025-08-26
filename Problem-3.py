a = int(input("Enter a number: "))

limit = a if a % 2 != 0 else a - 1

series = []
for i in range(1, limit + 1):
    series.append(2 * i - 1)

print(", ".join(map(str, series)))
