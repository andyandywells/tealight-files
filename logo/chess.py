from tealight.logo import move, turn, color

colors = ["black", "red"]

for i in range (0,4):
   move(100)
   turn(90)
   move(100)
   for i in range(0,100):
    move(i)
    turn(90)
    color(colors[i%1])

