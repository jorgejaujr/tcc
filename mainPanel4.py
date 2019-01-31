import numpy as np
import point
from scipy import interpolate
import matplotlib.pyplot as ptl
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import tkinter


step=0.1
"""

p3 = point.Point(3.0,4.0)
p2 = point.Point(2.0,3.0)
p1 = point.Point(1.0,2.0)

arrayX = np.array([p1.getX(),p2.getX(),p3.getX()])
arrayY = np.array([p1.getY(),p2.getY(),p3.getY()])

f=interpolate.interp1d(arrayX,arrayY,kind='linear')
#Este metodo gera uma funcao para a interpolacao linear

#interpolacao polinomial por lagrange - f1
f1=interpolate.lagrange(arrayX,arrayY)
#Este metodo gera polinomios para a interpolacao baseados nos pontos dados

#interpolacao de spline Cubico - f2
f2=interpolate.CubicSpline(arrayX,arrayY)
#Este metodo gera polinomios para a interpolacao baseados nos pontos dados

xnew=np.arange(p1.getX(),p3.getX(),step)
ynew=f(xnew)
ynew1=f1(xnew)
ynew2=f2(xnew)

fig = Figure(figsize=(5, 4), dpi=100)

#grafico da interpolacao linear
fig.add_subplot(111).plot(xnew, ynew,"ro")

#grafico da interpolacao polinomial de Lagrange
fig.add_subplot(111).plot(xnew, ynew1,"b--")

#grafico da interpolacao com Spline Cubico
fig.add_subplot(111).plot(xnew, ynew2,"g^")

#adicionando os pontos originais
fig.add_subplot(111).plot(np.arange(p1.getX(),p3.getX(),1.0),np.arange(p1.getY(),p3.getY(),1.0),"r^")
"""
class Gui:
   def __init__(self, master):
       	self.master = master
        self.p3 = point.Point(3.0,4.0)
        self.p2 = point.Point(2.0,3.0)
        self.p1 = point.Point(1.0,2.0)

        self.arrayX = np.array([self.p1.getX(),self.p2.getX(),self.p3.getX()])
        self.arrayY = np.array([self.p1.getY(),self.p2.getY(),self.p3.getY()])

        self.f=interpolate.interp1d(self.arrayX,self.arrayY,kind='linear')
        """Este metodo gera uma funcao para a interpolacao linear"""

        #interpolacao polinomial por lagrange - f1
        self.f1=interpolate.lagrange(self.arrayX,self.arrayY)
        """Este metodo gera polinomios para a interpolacao baseados nos pontos dados"""

        #interpolacao de spline Cubico - f2
        self.f2=interpolate.CubicSpline(self.arrayX,self.arrayY)
        """Este metodo gera polinomios para a interpolacao baseados nos pontos dados"""

        self.xnew=np.arange(self.p1.getX(),self.p3.getX(),step)
        self.ynew=self.f(self.xnew)
        self.ynew1=self.f1(self.xnew)
        self.ynew2=self.f2(self.xnew)

        self.fig = Figure(figsize=(5, 4), dpi=100)

        #grafico da interpolacao linear
        self.fig.add_subplot(111).plot(self.xnew, self.ynew,"ro")

        #grafico da interpolacao polinomial de Lagrange
        self.fig.add_subplot(111).plot(self.xnew, self.ynew1,"b--")

        #grafico da interpolacao com Spline Cubico
        self.fig.add_subplot(111).plot(self.xnew, self.ynew2,"g^")

        #adicionando os pontos originais
        self.fig.add_subplot(111).plot(np.arange(self.p1.getX(),self.p3.getX(),1.0),np.arange(self.p1.getY(),self.p3.getY(),1.0),"r^")
  
       #parte da decoracao da tela
       	master.wm_title("Embedding in Tk")
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)# A tk.DrawingArea.
        self.canvas.draw()

        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, master)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.canvas.mpl_connect("key_press_event", self.on_key_press)

        self.var1=tkinter.IntVar()
        self.var2=tkinter.IntVar()
        self.var3=tkinter.IntVar()
        self.chkbox1 = tkinter.Checkbutton(master=master, text="Check 1",variable = self.var1)
        self.chkbox1.pack(side=tkinter.BOTTOM)
        self.chkbox2 = tkinter.Checkbutton(master=master, text="Check 2",variable = self.var2)
        self.chkbox2.pack(side=tkinter.BOTTOM)
        self.chkbox3 = tkinter.Checkbutton(master=master, text="Check 3",variable = self.var3)
        self.chkbox3.pack(side=tkinter.BOTTOM)


        self.button = tkinter.Button(master=master, text="Quit", command=master.quit)
        self.button.pack(side=tkinter.BOTTOM)
        self.button1 = tkinter.Button(master=master, text="Pega passo", command=self.redo)
        self.button1.pack(side=tkinter.BOTTOM)

        self.e1=tkinter.Entry(master)
        self.e1.pack(side=tkinter.BOTTOM)

        self.lb1=tkinter.Label(master,text="Passo de Spline")
        self.lb1.pack()
   
   def redo(self):
        self.destroy()
        step=float(self.e1.get())
        f=interpolate.interp1d(self.arrayX,self.arrayY,kind='linear')
        """Este metodo gera uma funcao para a interpolacao linear"""

        #interpolacao polinomial por lagrange - f1
        f1=interpolate.lagrange(self.arrayX,self.arrayY)
        """Este metodo gera polinomios para a interpolacao baseados nos pontos dados"""

        #interpolacao de spline Cubico - f2
        f2=interpolate.CubicSpline(self.arrayX,self.arrayY)
        """Este metodo gera polinomios para a interpolacao baseados nos pontos dados"""

        self.xnew=np.arange(self.p1.getX(),self.p3.getX(),step)
        self.ynew=f(self.xnew)
        self.ynew1=f1(self.xnew)
        self.ynew2=f2(self.xnew)

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.fig.add_subplot(111).plot(self.xnew, self.ynew,"ro")
        self.fig.add_subplot(111).plot(self.xnew, self.ynew1,"b--")
        self.fig.add_subplot(111).plot(self.xnew, self.ynew2,"g^")
        #adicionando os pontos originais
        self.fig.add_subplot(111).plot(np.arange(self.p1.getX(),self.p3.getX(),1.0),np.arange(self.p1.getY(),self.p3.getY(),1.0),"r^")

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, root)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
   
   def on_key_press(self,event):
        print("you pressed {}".format(event.key))
        self.key_press_handler(self.event, self.canvas, self.toolbar)

   def destroy(self):
        self.canvas.get_tk_widget().destroy()

        
root = tkinter.Tk()
gui=Gui(root)
root.mainloop()

