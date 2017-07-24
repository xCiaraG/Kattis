n =   int(input())
while n != 0:
    small = []
    medium = []
    large = []
    for i in range(0, n):
        line = input().strip().split()
        if line[-1] == "small":
            small.append([float(line[0]), float(line[1]),   float(line[2]),   float(line[3])])
        elif line[-1] == "medium":
            medium.append([float(line[0]), float(line[1]),   float(line[2]),   float(line[3])])
        else:
            large.append([float(line[0]), float(line[1]),   float(line[2]),   float(line[3])])
    m = int(input())
    for i in range(0, m):
        line = input().strip().split()
        x = float(line[0])
        y = float(line[1])
        a = True
        for coordinates in small:
            if (coordinates[0] <= x <= coordinates[2]) and (coordinates[1] <= y <= coordinates[3]):
                if line[2] == "small":
                    print("small correct")
                    a = False
                else:
                    print("{} small".format(line[2]))
                    a = False
        for coordinates in medium:
            if (coordinates[0] <= x <= coordinates[2]) and (coordinates[1] <= y <= coordinates[3]):
                if line[2] == "medium":
                    print("medium correct")
                    a = False
                else:
                    print("{} medium".format(line[2]))
                    a = False
        for coordinates in large:
            if (coordinates[0] <= x <= coordinates[2]) and (coordinates[1] <= y <= coordinates[3]):
                if line[2] == "large":
                    print("large correct")
                    a = False
                else:
                    print("{} large".format(line[2]))
                    a = False
        if a:
            print("{} floor".format(line[2]))
    n = int(input())
    if n != 0:
        print()
