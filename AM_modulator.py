# AM modulator

# The software takes m(t) signal, carrier frequency and "A" value as an input
# and shows the m(t) wave, modulated wave “s(t)” and its power efficiency on the same graph. 

import matplotlib

signal = input("m(t) = ")
A = float(input("A = "))
fc = float(input("Frequency of Carrier = "))

if "sin" in signal:
    mp = signal[:signal.find("s")]
    if mp.isdecimal():
        mp=int(mp)
    else:
        mp=1

    value = signal.split("(")[1]
    for i in ["pi",".","*","t",")"]:
        value = value.replace(i,"")

    value = int(value)
    mts=[]
    out=[]
    time=[]
    for t in range(10000):
        t = t / 1000000
        mt= mp*np.sin(value*math.pi*t)
        st= (A + mt) * np.cos(2*fc*math.pi*t)
        mts.append(mt)
        out.append(st)
        time.append(t)

if "cos" in signal:
    mp = signal[:signal.find("c")]
    if mp.isdecimal():
        mp=int(mp)
    else:
        mp=1

    value = signal.split("(")[1]
    for i in ["pi",".","*","t",")"]:
        value = value.replace(i,"")

    value = int(value)
    mts=[]
    out=[]
    time=[]
    for t in range(10000):
        t = t / 1000000
        mt= mp*np.cos(value*math.pi*t)
        st= (A + mt) * np.cos(2*fc*math.pi*t)
        mts.append(mt)
        out.append(st)
        time.append(t)

u = mp/A
PowerE = str((u*u) / ( (u*u) + 2 ) * 100)
PowerE = "Power Efficiency = %" + PowerE[:4]
upper = np.max(out)-0.5

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(time, mts, label="s(t)")
ax1.plot(time, out, label="m(t)")
ax1.text(0.006, upper, PowerE, style='italic',
         bbox={'facecolor': 'green', 'alpha': 0.8, 'pad': 6})
ax1.legend(loc=4)
ax1.set(xlabel="t")
plt.show()
