from math import radians
from math import tan
from math import sin
from math import cos

ag = float(input('Qual Angulo Deseja Informar (Graus) : '))
ar = radians(ag)
t = tan(ar)
s = sin(ar)
c = cos(ar)

print('Voce Digitou o Angulo de ({:.3f}), Suas Funções Trigonometricas Valem : '.format(ag))
print('Tangente de ({}) Vale : {:.3f}'.format(ag, t))
print('Seno de ({}) Vale : {:.3f}'.format(ag, s))
print('Cosseno de ({}) Vale : {:.3f}'.format(ag, c))
