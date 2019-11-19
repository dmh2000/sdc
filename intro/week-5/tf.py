from scipy import signal
import matplotlib.pyplot as plt

num = [1]
den = [1, 10, 20]
dt = None

tf = signal.TransferFunction(num, den)
t, y = signal.step(tf)

plt.grid()
plt.plot(t, y)
plt.show()
