import matplotlib.pyplot as plt


x = [1, 2, -1, -2, -2, 1.5]
y = [1, -2, -1.5, -1, 1, -0.5]
col = []

w0 = 0 
w1 = 1
w2 = 0.5

def equ(x, y):
    s = w0 + (w1*x) + (w2*y)
    print("S =", s)    
    return s


for i in range(len(x)):
    if(equ(x[i], y[i]) > 0):
        col.append('y')
    else:
        col.append('b')

for i in range(len(x)):
    plt.scatter(x[i], y[i], c=col[i])

plt.xlim(-6, 6)
plt.ylim(-6, 6)

plt.axhline(y=0, linestyle='-', c="black", linewidth=0.5)
plt.axvline(x=0, linestyle='-', c="black", linewidth=0.5)

plt.show()