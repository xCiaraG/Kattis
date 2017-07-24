n = input().strip().split()
number_lines = int(n[1])
capactity = int(n[0])
passengers_aboard = 0
a = True
for i in range(0, number_lines):
    n = list(map(int, input().strip().split()))
    passengers_aboard -= n[0]
    if passengers_aboard < 0:
        a = False
    passengers_aboard += n[1]
    if passengers_aboard > capactity or passengers_aboard < capactity and n[2] > 0:
        a = False

if passengers_aboard > 0:
    a = False

if a:
    print("possible")
else:
    print("impossible")
