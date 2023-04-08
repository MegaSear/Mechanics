import matplotlib.pyplot as plt
from math import sin, cos, pi, sqrt
def sign(x):
    return (x >= 0) - (x < 0)

C_x = 0.47
g = 9.8
q = 0.45
R = 0.015/2
density_air = 1.225
alpha_degree = 45
density_ball = 7860
dx = 0.012
k = 1461
V_ball = (4/3) * pi * pow(R, 3)
S = pi * pow(R, 2)
m_ball = density_ball * V_ball
print("Доброго времени суток! Вас приветствует помощник по обработке баллистического "
      "движения при запуске из механической модели. Введите входные данные:")
print("Масса снаряда в килограммах:")
m_ball = float(input())
print("Угол под котором был запущен снаряд в градусах")
alpha_degree = int(input())
print("\n")

t = (pi/2)*sqrt(m_ball/k)

eps = 0.000001
x0 = 0.0
alpha = (alpha_degree) * pi / 180
y0 = (0.207 + (0.053- dx))*sin(alpha)
w = (0.5 * C_x * S * density_air) / m_ball

Arr_x = []
Arr_x.append(x0)
Arr_y = []
Arr_y.append(y0)

A = (m_ball*g/k)*((q/R)*cos(alpha) + sin(alpha))
v0 = sin(sqrt(k/m_ball) * t) * (dx - A) * sqrt(k/m_ball)
print("Скорость снаярда при вылете из трубки v = ", v0)
vy0 = v0 * sin(alpha)
vx0 = v0 * cos(alpha)

Arr_vy = []
Arr_vy.append(vy0)
Arr_vx = []
Arr_vx.append(vx0)

i = 0
while(True):
    vx = Arr_vx[i - 1]
    vy = Arr_vy[i - 1]
    d = abs(pow(pow(vy, 2) + pow(vx, 2), 0.5))
    Arr_vy.append(vy - eps * (g + vy * w * d))
    Arr_vx.append(vx - eps * (0 + vx * w * d))
    if(sign(Arr_vx[i]) == -1):
        print("Снаряд такой массы не полетит. В проекте подразумевалась масса не больше 40 грамм. "
              "Кстати, оптимальный угол равен 57 градусам")
        break
    Arr_y.append(Arr_y[i - 1] + eps * vy)
    Arr_x.append(Arr_x[i - 1] + eps * vx)
    if( abs(Arr_y[i]) <= (eps/2) or Arr_y[i] <= -eps/2):
        print("Дальность полёта L =", round(Arr_x[i], 3), "метров")
        print("Время полёта t =", i*eps, "секунд" )
        break
    i += 1
print(Arr_x[i], Arr_y[i])
plt.plot(Arr_x, Arr_y)
plt.show()

