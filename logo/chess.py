from tealight.logo import move, turn, color

colors = ["black", "red"]

for i in range (0,4):
   move(200)
   turn(45)
   for i in range(0,50):
    move(i)
    turn(90)
    color(colors[i%1])

