

p0, p1 = 1 + 2j, 3+4j

x0 = p0.real
y0 = p0.imag

x1 = p1.real
y1 = p1.imag

xm = 0.5*(x1+x0)
ym = 0.5*(y1+y0)
print(y1,y0)
print("The midpoint is (%s,%s)"%(xm,ym))

