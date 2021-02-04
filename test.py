from PyQt5.QtWidgets import QWidget,QHBoxLayout, QVBoxLayout, QApplication
from PyQt5 import QtCore
from numpy.lib.function_base import select
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
import psutil
import time
import numpy as np
from scipy import interpolate
from random import randint


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        
        self.initUI()

    def initUI(self):
        
        # Define a top-level widget to hold everything
        self.graphWidgetCpuTemp = pg.PlotWidget()
        self.graphWidgetCpuRate = pg.PlotWidget()
  
        ## Create a grid layout to manage the widgets size and position
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.graphWidgetCpuTemp)
        self.vbox.addWidget(self.graphWidgetCpuRate)
        self.setLayout(self.vbox) 
        
        self.x_time = []
        self.y_cpu_temp = []
        self.y_cpu_rate1 = []
        self.y_cpu_rate2 = []
        self.y_cpu_rate3 = []
        self.y_cpu_rate4 = []


        self.graphWidgetCpuTemp.setBackground('w')
        self.graphWidgetCpuTemp.setYRange(0, 100, padding=0)
        self.graphWidgetCpuTemp.setXRange(60, 0, padding=0)
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_cpu_temp =  self.graphWidgetCpuTemp.plot(self.x_time, self.y_cpu_temp, pen=pen)

        self.graphWidgetCpuRate.setBackground('w')
        self.graphWidgetCpuRate.setYRange(0, 100, padding=0)
        self.graphWidgetCpuRate.setXRange(60, 0, padding=0)
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_cpu_rate1 =  self.graphWidgetCpuRate.plot(self.x_time, self.y_cpu_rate1, pen=pen)
        self.data_line_cpu_rate2 =  self.graphWidgetCpuRate.plot(self.x_time, self.y_cpu_rate2, pen=pen)
        self.data_line_cpu_rate3 =  self.graphWidgetCpuRate.plot(self.x_time, self.y_cpu_rate3, pen=pen)
        self.data_line_cpu_rate4 =  self.graphWidgetCpuRate.plot(self.x_time, self.y_cpu_rate4, pen=pen)


        # ... init continued ...
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        self.start_time = time.time()
        

        
    def update_plot_data(self):
        x_time_cp = []
        y_cpu_temp_cp = []
        y_cpu_rate1_cp = []
        y_cpu_rate2_cp = []
        y_cpu_rate3_cp = []
        y_cpu_rate4_cp = []
        elapsed_time = time.time() - self.start_time    

        cpu_temp = psutil.sensors_temperatures()['coretemp']
        average_cpu_temp = sum(i[1] for i in cpu_temp) / len(cpu_temp[0])
        cpu_use_rate = psutil.cpu_percent(interval=0.1 ,percpu=True)
       
           
        #if len(self.x) == 100:
        if False:
            self.x = self.x[1:]  # Remove the first 
            self.y = self.y[1:]  # Remove the first 
            self.y.append(average_cpu_temp)  # Add a new random value.
        
        else:
            self.x_time.append(elapsed_time)
            self.y_cpu_temp.append(average_cpu_temp)
            self.y_cpu_rate1.append(cpu_use_rate[0])
            self.y_cpu_rate2.append(cpu_use_rate[1])
            self.y_cpu_rate3.append(cpu_use_rate[2])
            self.y_cpu_rate4.append(cpu_use_rate[3])
        
        # x_time_cp, y_cpu_temp_cp = self.spline1(self.x_time,self.y_cpu_temp,200)            
        # x_time_cp, y_cpu_rate_cp = self.spline1(self.x_time,self.y_cpu_rate,200)            
        # self.data_line_cpu_temp.setData(x_time_cp, y_cpu_temp_cp)  # Update the data.
        # self.data_line_cpu_rate.setData(x_time_cp, y_cpu_rate_cp)  # Update the data.
        
        self.data_line_cpu_temp.setData(self.x_time, self.y_cpu_temp)  # Update the data.
        #self.data_line_cpu_rate1.setData(self.x_time, self.y_cpu_rate1)  # Update the data.
        #self.data_line_cpu_rate2.setData(self.x_time, self.y_cpu_rate2)  # Update the data.
        #self.data_line_cpu_rate3.setData(self.x_time, self.y_cpu_rate3)  # Update the data.
        self.data_line_cpu_rate4.setData(self.x_time, self.y_cpu_rate4)  # Update the data.
#
    def spline1(self,x,y,point):
        f = interpolate.interp1d(x, y,kind="cubic") 
        X = np.linspace(x[0],x[-1],num=point,endpoint=True)
        Y = f(X)
        return X,Y
        
def main():
    # initializing Qt
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()