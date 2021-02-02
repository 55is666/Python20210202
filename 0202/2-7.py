#2-7
import turtle                   # 匯入小烏龜模組

screen = turtle.Screen()        # 產生一個螢幕
screen.setup(500, 400)          # 設定螢幕寬高
screen.bgcolor('cyan')    # 設定螢幕背景

myTurtle = turtle.Turtle()      # 產生一個小烏龜物件
myTurtle.color('black')          # 設定小烏龜顏色
myTurtle.shape('turtle')        # 設定小烏龜形狀

myTurtle.penup()                # 提筆
for step in range(5, 60, 2):    # 迴圈：從 5 開始，每次跳 2 步，直到 60
    myTurtle.stamp()            # 蓋章
    myTurtle.forward(step)      # 向前 step 步
    myTurtle.right(24)          # 右轉 24 度

screen.exitonclick()            # 使用者點擊螢幕時結束程式