life = 5
f_y = 500
iz_x = 5
iz_y = 7
y = 300
x = 300
def setup():
    size (666,666)
    
def draw():
    global x, iz_x,iz_y,y,f_y,life
    background(5,160,32)
    stroke(255,0,0)
    ellipseMode(CENTER)
    ellipse(x,y,50,50)
    ellipse(30,30,45,45)
    x = x + iz_x
    y = y + iz_y
    text (life ,81,50)
    text ("x" ,52,45)
    
    if life <= 0:
        push()
        stroke (0,0,0)
        strokeWeight(5)
        point (x-15,y)
        point (x+11,y)
        pop()
        push()
        stroke (0,0,255)
        fill (0,0,255)
        triangle (x-17,y+15,x-15,y+5,x-13,y+15)
        triangle (x+13,y+15,x+11,y+5,x+9,y+15)
        pop()
        
        text ("GAME OVER" ,250,200)
        textSize(50)
        
        noLoop()
    textSize(50)
    
    if y <= 0 or y >= 666:
        iz_y = -iz_y
    if x <= 0:
        iz_x = -iz_x
    if x >= 666:
        life = life - 1
        x = 300
        y = 300
    rectMode(CORNER)
    push()
    stroke(10,113,76)
    fill (10,113,76)
    rect (600,f_y,50,200)
    pop()
    if (600<x+35<650)and (f_y < y-25 < f_y + 200)and (f_y < y+25 < f_y + 200):
        iz_x = -iz_x
def keyPressed():
    global f_y
    if (key == "w" or key == "W") and f_y > 0 : 
        f_y = f_y - 20
        
    elif (key == "ц" or key == "Ц") and f_y > 0 :
        f_y = f_y - 20
    elif (key == "s" or key == "S" or key == "ы" or key == "Ы") and f_y + 200 <666:
        f_y = f_y + 20
