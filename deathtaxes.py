from sys import stdin

def buy(stocks, average_cost, amount):
	amount, cost = [int(x) for x in amount]
	average_cost = ((stocks * average_cost) + (amount * cost)) / (amount + stocks)
	return stocks + amount, average_cost

def sell(stocks, average_cost, amount):
	amount, cost = [int(x) for x in amount]
	return stocks - amount, average_cost

def split(stocks, average_cost, amount):
	amount = int(amount[0])
	return stocks * amount, average_cost / amount

def merge(stocks, average_cost, amount):
	amount = int(amount[0])
	return stocks // amount, average_cost * amount

def die(stocks, average_cost, amount):
	amount = int(amount[0])
	print(stocks * (amount - max(0, amount - average_cost) * 0.3))
	return 0, 0

lines = stdin.readlines()
stocks = 0
average_cost = 0

actions = {"buy" : buy, "sell" : sell, "split" : split, "merge" : merge, "die" : die}

for line in lines:
	action, *amount = line.split()
	stocks, average_cost = actions[action](stocks, average_cost, amount)