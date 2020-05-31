import math
import numpy as np

f = open('values.txt', 'r')
f.readline()
radius = []
Mc = []

for line in f:
  radius.append(float(line.split('\t')[0]))

a1 = 1.3876*(10**9)

for i in radius:
  atan = math.atan(i/(1.87))
  equationb = i-((1.87)*(atan))
  equation = (a1)*(equationb)
  Mc.append(equation)

print(Mc)