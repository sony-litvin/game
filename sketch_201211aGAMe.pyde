x=1000
y=600
x1=x/2
y1=y/2
y2=y1
y3=y1
y4=y1
y5=y1
y6=y1
x2=x1-490
x3=x1-450
x4=x1-480
x5=x1-455
x6=x1-475
x1=x1-460
a=949
b=300
speed=10
pct=speed
dim=80
dy=100
r=53
x0=a
y0=b
t=-1000
w='u win'
l='u lose'
r='retry'

def setup() :
    size(x,y)
    fill(12)
    distX1=a-x1
    distY1=b-y1

def keyReleased():
    global dy
    if key == ' ':
        dy=dy-19
        
def keyPressed():
    global a,b,x0,y0
    if key == 'w':
        b=b-speed
    if key == 's':
        b=b+speed
    if key == 'a':
        a=a-speed
    if key == 'd':
        a=a+speed
    if key == ' ' :
        x0=a-speed
        y0=b-speed

        
def draw():
    background(255)
    global x0,x1,x2,x3,x4,x5,x6,y0,y1,y2,y3,y4,y5,y6,a,b,dy
    
    x1=x1+0.8
    x2=x2+0.8
    x3=x3+0.8
    x4=x4+0.8
    x5=x5+0.8
    x6=x6+0.8
    
    noStroke()
    
    if x1<-dim/2:
        x1=width-dim/2
    if x1>width+dim/2:
        x1=dim/2
    if y1+dy > height-dim/2+1:
        dy=-0.5*dy
        y1=y1+dy
    ellipse(x1,y1-250,r,r)
    fill(200,100,150)
    
    if x2<-dim/2:
        x2=width-dim/2
    if x2>width+dim/2:
        x2=dim/2
    if y2+dy > height-dim/2+1:
        dy=-0.5*dy
        y2=y2+dy
        if y0==y2-160:
            y2=90
    ellipse(x2,y2-160,r,r)
    fill(200,120,200)
    
    if x3<-dim/2:
        x3=width-dim/2
    if x3>width+dim/2:
        x3=dim/2
    if y3+dy > height-dim/2+1:
        dy=-0.5*dy
        y3=y3+dy
    ellipse(x3,y3-70,r,r)
    fill(220,90,90)
    
    if x4<-dim/2:
        x4=width-dim/2
    if x4>width+dim/2:
        x4=dim/2
    if y4+dy > height-dim/2+1:
        dy=-0.5*dy
        y4=y4+dy
    ellipse(x4,y4+40,r,r)
    fill(190,25,120)
    
    if x5<-dim/2:
        x5=width-dim/2
    if x5>width+dim/2:
        x5=dim/2
    if y5+dy > height-dim/2+1:
        dy=-0.5*dy
        y5=y5+dy
    ellipse(x5,y5+150,r,r)
    fill(190,25,89)
    
    if x6<-dim/2:
        x6=width-dim/2
    if x6>width+dim/2:
        x6=dim/2
    if y6+dy > height-dim/2+1:
        dy=-0.5*dy
        y6=y6+dy
    ellipse(x6,y6+240,r,r)
    fill(125,225,225)
    
    if a>0 :
        rectMode(CENTER)
        rect(a,b,r,r,10)
        fill(190,25,90)
        rect(a,b,10,10,10)
        fill(225,0,0)

    x0=x0-50
    fill(225,0,0)
    ellipse(x0,y0,20,20) 
    
    if y0==y1-250 or x0==x1:
        y1=0
        x1=0
    if y0==y2-160 or x0==x2:
        y2=0
        x2=0
    if y0==y3-70 or x0==x3:
        y3=0
        x3=0
    if y0==y4+40 or x0==x4:
        y4=t
        x4=t
    if y0==y5+150 or x0==x5:
        y5=t
        x5=t
    if y0==y6+240 or x0==x6:
        y6=t
        x6=t
    
    fill(225,0,0)
    rect(900,300,10,-t)
    rect(995,300,10,-t)
    rect(949,5,90,10)
    rect(949,595,90,10)
    
    if a<920 or a > 970:
        a=t
        b=t
    if b>565 or b<35:
        a=t
        b=t
        
    if x1>870:
        x1=t
        y1=t
    if x2>870:
        x2=t
        y2=t
    if x3>870:
        x3=t
        y3=t
    if x4>870:
        x4=t
        y4=t
    if x5>870:
        x5=t
        y5=t
    if x6>870:
        x6=t
        y6=t
