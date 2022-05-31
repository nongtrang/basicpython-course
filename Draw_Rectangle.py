import turtle
tao = turtle.Pen()  #ดึงความสามารถการใช้ปากกา
tao.shape('turtle')  #แปลงร่างเป็นปากกา

def Rectangle():
        '''funtion draw rectangle'''
	for i in range(4):
		tao.fd(100)
		tao.left(90)

def Go(x,y):
	tao.penup()
	tao.goto(x,y)
	tao.pendown()


Go(200,200)
Rectangle()
