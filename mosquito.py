import sys
lines = sys.stdin.readlines()
for line in lines:
    line = list(map(int, line.strip().split()))
    mosquito = line[0]
    pupae = line[1]
    larvae = line[2]
    eggs = line[3]
    larva_survive = line[4]
    pupae_survive = line[5]
    weeks = line[6]
    for i in range(0, weeks):
        tmp = mosquito * eggs
        mosquito = pupae//pupae_survive
        pupae = larvae//larva_survive
        larvae = tmp
    print(mosquito)
