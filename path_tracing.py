import sys
def go_down():
   global y, m
   y += 1
   if y == len(m):
      m.append(" "*len(m[0]))
   
def go_up():
   global y, m
   y -= 1
   if y == -1:
      y = 0
      m = [" "*len(m[0])] + m

def go_left():
   global x, m
   x -= 1
   if x == -1:
      x = 0
      m = [" " + s for s in m]

def go_right():
   global x, m
   x += 1
   if x == len(m[0]):
      m = [s + " " for s in m] 

m, x, y = ["S"], 0, 0
directions = sys.stdin.readlines()
for direction in directions:
   direction = direction.strip()
   if direction == "down":
      go_down()
   elif direction == "up":
      go_up()
   elif direction == "left":
      go_left()
   elif direction == "right":
      go_right()
   if m[y][x] != "S":
      m[y] = m[y][:x] + "*" + m[y][x+1:]

m[y] = m[y][:x] + "E" + m[y][x+1:]
print("#"*(len(m[0])+2))
for l in m:
   print("#" + l + "#")
print("#"*(len(m[0])+2))