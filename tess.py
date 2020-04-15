"""Case-study #5 Тесселяция
Разработчики:
Шарков К.(70), Кеда С., Ермоленко В (20%):
"""
import math
import turtle
import time


def get_color_choice():
    while True:
        colors = ['зеленый', 'красный', 'оранжевый', 'синий', 'бирюзовый', 'малиновый', 'индиго']
        color = input("Допустимые цвета заливки(введите 1-7)\n"
                      "1. Зеленый \n"
                      "2. Красный \n"
                      "3. Оранжевый \n"
                      "4. Синий \n"
                      "5. Бирюзовый \n"
                      "6. Малиновый \n"
                      "7. Индиго \n"
                      "Пожалуйста, введите цвет: \n")
        if color.lower() in colors:
            if color == 'зеленый':
                return 'green'
            if color == 'красный':
                return 'red'
            if color == 'оранжевый':
                return 'orange'
            if color == 'синий':
                return 'midnightblue'
            if color == 'бирюзовый':
                return 'turquoise'
            if color == 'малиновый':
                return 'crimson'
            if color == 'индиго':
                return 'indigo'
            break
        print('%s не является верным значением. Пожалуйста повторите попытку.' % color)


def get_num_hexagons():
    while True:
        amount = ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                  '18', '19', '20']
        amount_of_hex = input("Допустимое количество шестиугольников (4 - 20)\n"
                              "Пожалуйста, выберите количество шестиугольников: \n")
        if amount_of_hex in amount:
            if amount_of_hex == "4":
                return "4"
            if amount_of_hex == "5":
                return "5"
            if amount_of_hex == "6":
                return "6"
            if amount_of_hex == "7":
                return "7"
            if amount_of_hex == "8":
                return "8"
            if amount_of_hex == "9":
                return "9"
            if amount_of_hex == "10":
                return "10"
            if amount_of_hex == "11":
                return "11"
            if amount_of_hex == "12":
                return "12"
            if amount_of_hex == "13":
                return "13"
            if amount_of_hex == "14":
                return "14"
            if amount_of_hex == "15":
                return "15"
            if amount_of_hex == "16":
                return "16"
            if amount_of_hex == "17":
                return "17"
            if amount_of_hex == "18":
                return "18"
            if amount_of_hex == "19":
                return "19"
            if amount_of_hex == "20":
                return "20"
            break
        print('%s не является верным значением. Пожалуйста повторите попытку.' % amount_of_hex)

    pass                        #4-20  return n


def draw_hexagon(x, y, side_len, color):
    turtle.goto(x, y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(30)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.end_fill()
    turtle.right(30)
    turtle.penup()


def findparametrs(side_len, n):
    parametrs = []
    for vertik in range(1, n + 1):
        if vertik == 1:
            x0 = math.sqrt(3) * side_len/2
            y0 = 0
            parametrs.append([x0, y0])
        for gorizont in range(2, n + 1):
            x0 += math.sqrt(3) * side_len
            parametrs.append([x0, y0])
            if gorizont == n and vertik != n:       #[x0,y0] в parametrs - координаты верхних углов всех шестиугольников
                if vertik % 2 == 1:
                    y0 += 1.5 * side_len
                    #x0 = 0
                    x0 = math.sqrt(3) * side_len
                    parametrs.append([x0, y0])
                elif vertik % 2 == 0:
                    #x0 = math.sqrt(3) * side_len
                    x0 = math.sqrt(3) * side_len/2
                    y0 += 1.5 * side_len
                    parametrs.append([x0, y0])
    return parametrs

def find_colors(color1, color2,n):
    colors = []
    for i in range(1, (n*n)+1):
        if (i // (n*2)) % 2 == 0:
            if i % 2 == 1:
                colors.append(color1)
            else:
                colors.append(color2)
        else:
            if i % 2 == 1:
                colors.append(color2)
            else:
                colors.append(color1)
    return colors

def main():
    color1 = get_color_choice()
    color2 = get_color_choice()
    color1 = 'green'
    color2 = 'red'
    n = int(get_num_hexagons())
    turtle.speed(100)
    side_len = 500 // ((n + 0.5) * math.sqrt(3))
    params = findparametrs(side_len, n)
    streamlined_colors = find_colors(color1, color2,n)

    for quantity in range(0, (n * n) ):
       draw_hexagon(params[quantity][0], params[quantity][1], side_len, streamlined_colors[quantity])
    time.sleep(5)

main()
