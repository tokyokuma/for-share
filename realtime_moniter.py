import numpy as np
import matplotlib.pyplot as plt
import psutil
import time

ut = list()

temp = list()
fig = plt.figure()
ax_temp = fig.add_subplot(211)

cpu = list()
ax_cpu = fig.add_subplot(212)

base_time = time.time()

while True:
    ut.append(time.time() - base_time)

    cpu_temp = psutil.sensors_temperatures()['coretemp']
    average_cpu_temp = sum(i[1] for i in cpu_temp) / len(cpu_temp[0])
    temp.append(average_cpu_temp)

    cpu_use_rate = psutil.cpu_percent(interval=1, percpu=True)
    cpu.append(cpu_use_rate)

    line_temp = ax_temp.plot(ut, temp, color="blue")
    line_cpu = ax_cpu.plot(ut, cpu, color="blue")
    plt.pause(0.0001)
    #line.remove()
