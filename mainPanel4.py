import numpy as np
import point
from scipy import interpolate
import matplotlib.pyplot as ptl
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import tkinter

def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
def destroy():
    canvas.get_tk_widget().destroy()

def redo():
    destroy()
    step=float(e1.get())
    f=interpolate.interp1d(arrayX,arrayY,kind='linear')
    """Este metodo gera uma funcao para a interpolacao linear"""

    #interpolacao polinomial por lagrange - f1
    f1=interpolate.lagrange(arrayX,arrayY)
    """Este metodo gera polinomios para a interpolacao baseados nos pontos dados"""

    #interpolacao de spline Cubico - f2
    f2=interpolate.CubicSpline(arrayX,arrayY)
    """Este metodo gera polinomios para a interpolacao baseados nos pontos dados"""

    xnew=np.arange(p1.getX(),p3.getX(),step)
    ynew=f(xnew)
    ynew1=f1(xnew)
    ynew2=f2(xnew)

    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).plot(xnew, ynew,"ro")
    fig.add_subplot(111).plot(xnew, ynew1,"b--")
    fig.add_subplot(111).plot(xnew, ynew2,"g^")

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.mpl_connect("key_press_event", on_key_press)
    
step=0.1

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

p3 = point.Point(3.0,4.0)
p2 = point.Point(2.0,3.0)
p1 = point.Point(1.0,2.0)

arrayX = np.array([p1.getX(),p2.getX(),p3.getX()])
arrayY = np.array([p1.getY(),p2.getY(),p3.getY()])

f=interpolate.interp1d(arrayX,arrayY,kind='linear')
"""Este metodo gera uma funcao para a interpolacao linear"""

#interpolacao polinomial por lagrange - f1
f1=interpolate.lagrange(arrayX,arrayY)
"""Este metodo gera polinomios para a interpolacao baseados nos pontos dados"""

#interpolacao de spline Cubico - f2
f2=interpolate.CubicSpline(arrayX,arrayY)
"""Este metodo gera polinomios para a interpolacao baseados nos pontos dados"""

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

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
canvas.mpl_connect("key_press_event", on_key_press)

var1=tkinter.IntVar()
var2=tkinter.IntVar()
var3=tkinter.IntVar()
chkbox1 = tkinter.Checkbutton(master=root, text="Check 1",variable = var1)
chkbox1.pack(side=tkinter.BOTTOM)
chkbox2 = tkinter.Checkbutton(master=root, text="Check 2",variable = var2)
chkbox2.pack(side=tkinter.BOTTOM)
chkbox3 = tkinter.Checkbutton(master=root, text="Check 3",variable = var3)
chkbox3.pack(side=tkinter.BOTTOM)

button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)
button = tkinter.Button(master=root, text="Pega passo", command=redo)
button.pack(side=tkinter.BOTTOM)

e1=tkinter.Entry(root)
e1.pack(side=tkinter.BOTTOM)

lb1=tkinter.Label(root,text="Passo de Spline")
lb1.pack()

tkinter.mainloop()
# aqui terminam as alteracores
# basta descomentar esta parte do codigo que volta ao normal.
"""
ptl.plot(arrayX,arrayY,"ro",xnew,ynew,"b--",xnew,f2(xnew),"g^",xnew,f2(xnew,1),"r--",xnew,f1(xnew),"go")
ptl.show()
"""
