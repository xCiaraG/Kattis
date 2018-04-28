from sys import stdin

def main():
   lines = stdin.readlines()
   for line in lines:
      n = int(line.strip())
      count = 1
      ans = 1
      while ans != 0:
         ans = ((ans * 10) + 1) % n
         count += 1
      if n == 1:
         count = 1
      print(count)

if __name__ == '__main__':
   main()
