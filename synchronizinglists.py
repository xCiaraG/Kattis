mport sys
n = int(sys.stdin.readline().strip())
while n!= 0:
    list1 = []
    list2 = []
    for i in range(0,n):
        list1.append(int(sys.stdin.readline().strip()))
    for i in range(0,n):
        list2.append(int(sys.stdin.readline().strip()))
    sorted_list1 = sorted(list1[:])
    sorted_list2 = sorted(list2[:])
    new_list2 = []
    for i in range(0, len(list1)):
        new_list2.append(sorted_list2[sorted_list1.index(list1[i])])
        print(new_list2[i])
    print()
    n = int(sys.stdin.readline().strip())
