import sys
lines = sys.stdin.readlines()
i = 0
while i < len(lines):
	n = int(lines[i].strip())
	j = 0
	queue = []
	queue_output = []
	priority_queue = []
	priority_queue_output = []
	stack = []
	stack_output = []
	output = []
	while j < n:
		i += 1
		tmp = list(map(int, lines[i].strip().split()))
		if tmp[0] == 1:
			queue.append(tmp[1])
			priority_queue.append(tmp[1])
			stack.append(tmp[1])
		elif tmp[0] == 2:
			if queue:
				queue_output.append(queue[0])
				queue.remove(queue[0])
				stack_output.append(stack.pop())
				priority_queue_output.append(max(priority_queue))
				priority_queue.remove(max(priority_queue))
			output.append(tmp[1])
		j += 1
	c = 0
	if output == priority_queue_output:
		c += 1
	if output == queue_output:
		c += 1
	if output == stack_output:
		c += 1
	if c > 1:
		print("not sure")
	elif c == 0:
		print("impossible")
	elif output == queue_output:
		print("queue")
	elif output == stack_output:
		print("stack")
	else:
		print("priority queue")
	i += 1

		