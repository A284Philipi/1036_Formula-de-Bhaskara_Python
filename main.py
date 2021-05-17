import math
a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
delta = float(((b * b) - (4 * a * c)))
if (a == 0) or (delta < 0):
    print("Impossivel calcular")
else:
    r1 = float(((b * -1) + math.sqrt(delta)) / (2 * a))
    r2 = float(((b * -1) - math.sqrt(delta)) / (2 * a))
    print("R1 = %.5f\nR2 = %.5f"%(r1, r2))