n = int(input())
prices = [0]*n
for i in range(0, n):
    prices[i] = int(input().strip())
balance = 100
prev_balance = 100
number_stocks = 0
j = 0
while j + 1 < n:
    if prices[j+1] < prices[j] and number_stocks > 0:
        balance += number_stocks * prices[j]
        number_stocks = 0
        prev_balance = balance
    elif prices[j+1] > prices[j] and number_stocks == 0:
        if balance//prices[j] > 100000:
            number_stocks = 100000
            balance -= (prices[j]*100000)
        else:
            number_stocks = balance//prices[j]
            balance = balance % prices[j]
    j += 1
balance += (number_stocks*prices[-1])
if prev_balance > balance:
    print(prev_balance)
else:
    print(balance)
