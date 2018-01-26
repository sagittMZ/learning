# coding: utf-8
# import tkSimpleDialog #2.x Python
import turtle, random, math
import mr_robot # подключение модуля mr_robot (соседний скрипт)

PHI = 360/7 # разбиваем барабан (окружность) на количество зарядов
R = 50 # вершины окружностей для обозначения мест для патронов

def gotoxy(x,y):  # Функция для упрощения рисования кругов
    turtle.penup()
    turtle.goto(x,y)  # x y - координаты
    turtle.pendown()

def draw_circle(r,color):
    turtle.fillcolor(color) # Выбирает цвет
    turtle.begin_fill() # заполнение цветом
    turtle.circle(r)   # Рисует окружность (радиус)
    turtle.end_fill()  # Окончание заполнения

turtle.speed(0) # Отвечает за скорость рисования кругов

def draw_pistol(base_x, base_y):
    # отрисовка основного круга для барабана
    gotoxy(base_x, base_y)
    turtle.circle(80)
    # отрисовка мушки
    gotoxy(base_x, base_y+160)
    draw_circle(5, "red")
    # отрисовка барабана
    for i in range(0, 7):  # переменные берутся от 0 до 6, 7ка не берется
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x+math.sin(phi_rad) * R, base_y+math.cos(phi_rad) * R + 55)
        draw_circle(22, "white")

def rotate_pistol(base_x, base_y, start):
    for i in range(start, random.randrange(7, 18)):  # переменные берутся от 0 до 6, 7ка не берется
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x+math.sin(phi_rad) * R, base_y+math.cos(phi_rad) * R + 55)
        draw_circle(22, "brown")
        draw_circle(22, "white")

    gotoxy(base_x+math.sin(phi_rad * i) * R, base_y+math.cos(phi_rad * i) * R + 55)
    draw_circle(23, "brown")
    return i%7

def main():
    draw_pistol(100,100)

    answer = ''
    start = 0
    while answer != 'N':
        answer = turtle.textinput("Let's play?", "Y/N")
        # tkSimpleDialog.askstring("Нарисовать окружность", "Y/N")  # 2.x Python
        if answer == 'Y':
            start = rotate_pistol(100, 100, start)
            start =0
            if start == 0:  # условие выстрела - патрон у мушки. т.е. т.к. патронов 7 штук, то каждый 7 патрон.
                gotoxy(-150, 250)
                turtle.write("u'r loser", font=("Currier New", 20, "bold"))
                mr_robot.double_files('.') # использование функции из подключенного модуля
            else:
                gotoxy(-150, 250)
                turtle.write("u'r winner", font=("Currier New", 20, "bold"))

            # turtle.penup() # penup() / pendown() "приподнимает" перо, убирая соединяющие линии между элементами графики
            # turtle.goto(random.randrange(-200,100), random.randrange(40,100)) # задание координаты точки старта выполнения рисования круга
            # turtle.pendown()
            # turtle.fillcolor(random.random(), random.random(), random.random()) # произвольный цвет для закрашивания в rgb
            # turtle.begin_fill()
            # turtle.circle(random.randrange(1,100))
            # turtle.end_fill()
        else:
            pass


if __name__ == "__main__":
    main()