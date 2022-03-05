import turtle, math
graphSize = 300


t = turtle.Turtle()
t.speed(0)
clear = "\n" * 100## define a way to clear the screen

def drawGraph(x,y): ## function to draw a graph based on upper left corner coord
  t.pensize(.5)
  """
   push the coordinates of the grids N,P corner.
  the grid will be build off of the graphSize variable
  """
  t.penup()
  t.goto(x,y)
  t.pendown()
  for i in range(graphSpaces/2):
    t.forward(graphSize)
    t.right(90)
    t.forward(interval)
    t.right(90)
    t.forward(graphSize)
    t.left(90)
    t.forward(interval)
    t.left(90)
  t.left(90)
  for i in range(graphSpaces/2):
    t.forward(graphSize)
    t.right(90)
    t.forward(interval)
    t.right(90)
    t.forward(graphSize)
    t.left(90)
    t.forward(interval)
    t.left(90)

  t.forward(graphSize)
  t.penup()
  t.goto(x,y-graphSize)
  t.pendown()
  t.goto(x + graphSize,y - graphSize)
  t.penup()

  t.goto(0,0)
  t.right(90)
def createOutlines(mode):
  if mode == "center_cross":
    t.penup()
    t.color("black")
    t.pensize(3)
    t.goto(-graphSize,0)
    t.pendown()
    t.goto(graphSize,0)
    t.penup()
    t.goto(0,graphSize)
    t.pendown()
    t.goto(0,-graphSize)
    t.color("black")
    t.penup()
    t.pensize(1)
#=========================draw through lines
def drawThroughLines():
  t.goto(dx * interval,dy * interval)
  t.pencolor("green")
  t.pendown()
  t.goto(axp * interval,ayp * interval)
  t.penup()
  t.goto(dx * interval,dy * interval)
  t.pendown()
  t.goto(bxp * interval,byp * interval)
  t.penup()
  t.goto(dx * interval,dy * interval)
  t.pendown()
  t.goto(cxp * interval,cyp * interval)
  t.goto(dx * interval,dy * interval)
  t.goto(ax * interval,ay * interval)
  t.goto(dx * interval,dy * interval)
  t.goto(bx * interval,by * interval)
  t.goto(dx * interval,dy * interval)
  t.goto(cx * interval,cy * interval)
###=============================================MAIN code
##==========================================gather data about triangle ABC
print clear
print("Please enter the following points for point A")
ax = float(input('x: '))
ay = float(input('y: '))
print clear
print("Please enter the following points for point B")
bx = float(input('x: '))
by = float(input('y: '))
print clear
print("Please enter the following points for point C")
cx = float(input('x: '))
cy = float(input('y: '))
print clear
print("Please enter the following for the point of dialation")
dx = float(input('x: ')) ### dialation point x
dy = float(input('y: ')) ### dialation point y
print clear
k = float(input('dialate by: '))
print clear
#===================================dialation formula
axp = (k * (ax - dx)) + dx 
ayp = (k * (ay - dy)) + dy
bxp = (k * (bx - dx)) + dx ### key: first letter is the point, second is x or y and p if it is prime(second triangle)
byp = (k * (by - dy)) + dy
cxp = (k * (cx - dx)) + dx
cyp = (k * (cy - dy)) + dy
#===================================
points = [ax,ay,bx,by,cx,cy,axp,ayp,bxp,byp,cxp,cyp]
largestPoint = 0 # largest
for item in points:
  if item > largestPoint:
    largestPoint = item
#######====================== calculate how large the graph should be
graphSpaces = int(largestPoint)
while graphSpaces%10 != 0:
  graphSpaces += 1
if graphSpaces == 0:
  graphSpaces += 10
######=======================
print( "(" + str(ax)+ "," +str(ay)+ ")" + ">" + "(" + str(axp)+ "," +str(ayp)+ ")" +">" + "(" + str(bx)+ "," +str(by)+ ")" +">" + "(" + str(bxp)+ "," +str(byp)+ ")" +">" + "(" + str(cx)+ "," +str(cy)+ ")" +">" + "(" + str(cxp)+ "," +str(cyp) + ")")
print(" ")
print("red = preimage, blue = image")
print(" ")
interval = graphSize / graphSpaces
#==================================draw triangle ABC 
t.pencolor("red")
t.penup()
t.pensize(3)
t.goto(ax*interval,ay*interval)
t.pendown()
t.goto(bx*interval,by*interval)
t.goto(cx*interval,cy*interval)
t.goto(ax*interval,ay*interval)
t.penup()
t.pencolor("black")
t.pensize(1)
##================================draw graph with defined func
drawGraph(0,graphSize)          ##TR
drawGraph(-graphSize,graphSize) ##TL
drawGraph(-graphSize,0)          ##BR
drawGraph(0,0)                   ##BL 
createOutlines("center_cross")
##===============================draw primed shapes
t.goto(axp * interval,ayp * interval)## a prime
t.pendown()
t.pensize(3)
t.pencolor("blue")
t.goto(bxp * interval,byp * interval)## b prime
t.goto(cxp * interval,cyp * interval)## c prime
t.goto(axp * interval,ayp * interval) ## a prime to complete triangle
t.penup()
if input('Draw through lines? y/n (it can get messy)').lower() == "y":
  drawThroughLines()
  t.penup()
if input('show lengths? y/n').lower() == "y": ##====================================draw lengths on each side
  abDist = math.sqrt((ay - by)**2 +(ax - bx)**2) ## revised distance method
  bcDist = math.sqrt((by - cy)**2 +(bx - cx)**2)
  caDist = math.sqrt((cy - ay)**2 +(cx - ax)**2)
  t.goto(((ax+bx) / 2 ) * interval , ((ay + by) / 2) * interval)
  t.write(abDist)
  t.goto(((bx+cx) / 2 ) * interval , ((by + cy) / 2) * interval)
  t.write(bcDist)
  t.goto(((cx+ax) / 2 ) * interval , ((cy + ay) / 2) * interval)
  t.write(caDist)
  t.goto(((axp+bxp) / 2 ) * interval , ((ayp + byp) / 2) * interval)
  t.write(abDist * k)
  t.goto(((bxp+cxp) / 2 ) * interval , ((byp + cyp) / 2) * interval)
  t.write(bcDist * k)
  t.goto(((cxp+axp) / 2 ) * interval , ((cyp + ayp) / 2) * interval)
  t.write(caDist * k)
  
  











  

  if False: ## old distance method
  #===========================preimage triangle
    t.goto(((ax+bx) / 2 ) * interval , ((ay + by) / 2) * interval)
    t.write(str(int((math.sqrt((by - ay) **2) + ((bx - ax) **2)))), font=("Arial", 16, "normal"))
    t.penup()
    t.goto(((cx+ax) / 2 ) * interval , ((cy + ay) / 2) * interval)
    t.write(str(int(math.sqrt((( cx - ax ) ** 2 ) + (( cy - ay ) ** 2 )))), font=("Arial", 16, "normal"))
    t.goto(((cx+bx) / 2 ) * interval , ((cy + by) / 2) * interval)
    t.write(str(int(math.sqrt((( cx - bx ) ** 2 ) + (( cy - by ) ** 2 )))), font=("Arial", 16, "normal"))
  #==========================image triangle
    t.goto(((axp+bxp) / 2 ) * interval , ((ayp + byp) / 2) * interval)
    t.write(str(int((math.sqrt((byp - ayp) **2) + ((bxp - axp) **2)))), font=("Arial", 16, "normal"))
    t.penup()
    t.goto(((cxp+axp) / 2 ) * interval , ((cyp + ayp) / 2) * interval)
    t.write(str(int(math.sqrt((( cxp - axp ) ** 2 ) + (( cyp - ayp ) ** 2 )))), font=("Arial", 16, "normal"))
    t.goto(((cxp+bxp) / 2 ) * interval , ((cyp + byp) / 2) * interval)
    t.write(str(int(math.sqrt((( cxp - bxp ) ** 2 ) + (( cyp - byp ) ** 2 )))), font=("Arial", 16, "normal"))
