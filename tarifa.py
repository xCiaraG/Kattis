per_month = int(input())
n = int(input())
to_spend = (n+1)*per_month
for i in range(0, n):
    m = int(input())
    to_spend -= m
print(to_spend)
