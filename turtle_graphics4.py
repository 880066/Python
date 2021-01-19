import turtle,time,sys,random

ok=turtle.Turtle()
wn=turtle.Screen()
width=800
height=600
wn.setup(width,height)

ok.speed(0)
rainbow=["red","orange","yellow","green","blue","indigo","violet"]
kenar=100
ok.width(1)

ok.penup()
ok.goto(0,200)
ok.pendown()
wn.bgcolor("black")

def sekiz(k):
    for i in range (8):
        color = random.choice(rainbow)
        ok.pencolor("green")
        ok.forward(k)
        ok.right(45)
    ok.penup()
    ok.right(5)
    ok.forward(10)
    ok.pendown()
    global kenar
    kenar +=3


for i in range (130):
    sekiz(kenar)


time.sleep(2)

sys.exit()
