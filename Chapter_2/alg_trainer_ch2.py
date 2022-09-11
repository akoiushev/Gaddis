# 5
total = 10 + 14
print(total)
print("-" * 10)

# 6
down_payment = 5
due = total - down_payment
print(f"К оплате: {due} р.")
print("-" * 10)

# 7
subtotal = 100
total = subtotal * 0.15
print(f"Нарастающий итог: {total} р.")
print("-" * 10)

# 10
sales = 100.123456789
print(round(sales, 2))
print("-" * 10)

# 11
number = 1234567.456
print(format(number, ',.1f'))
print("-" * 10)

# 12
print('Джордж', 'Джон', 'Пол', 'Ринго', sep='@')
print("-" * 10)

# 13 Круг диаметром 70
# import turtle
# turtle.circle(70)
# # turtle.done()
# print("-" * 10)
#
# # 14 Квадрат синего цвета со стороной 100
# import turtle
#
# turtle.fillcolor("blue")
# turtle.begin_fill()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.end_fill()
# # turtle.done()
#
# print("-" * 10)

# Квадрат со стороной 100, в центре квардрата красный круг диаметром 80
import turtle
turtle.penup()
turtle.forward(50)
turtle.left(90)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.done()

print("-" * 10)
