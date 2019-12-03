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
#    ynew=f(xnew)
#    ynew1=f1(xnew)
    ynew2=f2(xnew)

    fig = Figure(figsize=(5, 4), dpi=100)
#    fig.add_subplot(111).plot(xnew, ynew,"ro")
#    fig.add_subplot(111).plot(xnew, ynew1,"b--")
    fig.add_subplot(111).plot(xnew, ynew2,"g^")

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.mpl_connect("key_press_event", on_key_press)
    
#importacao do arquivo com as temperaturas
data = open('201910292240measures107.txt','r')

#criacao do array de temperaturas tirando o nextLine
array=data.read().splitlines()

#criacao da lista para inserir os segundos e as temperaturas
pointVec=[]

#inicio dos segundos em float, devido a classe Point
sec=0.0

#insercao das instancias de Point (segundo,temperatura) a partir do vetor de temperaturas
#e do contador sec 
for i in range(0,len(array)):
   
   temp = point.Point(float(sec),float(array[i]))
   pointVec.append(temp)
   sec+=1

#fechamento do arquivo
data.close()

#passo para criar os pontos
step=5.0

root = tkinter.Tk()
root.wm_title("Embedding in Tk")
#criacao dos arrays de numpy para x e y
temp3X=[]
temp3Y=[]

for i in pointVec:
  temp3X.append(i.getX())
  temp3Y.append(i.getY())
arrayX=np.array(temp3X)
arrayY=np.array(temp3Y)
#print("Array Y:",len(arrayY))

f=interpolate.interp1d(arrayX,arrayY,kind='linear')
"""Este metodo gera uma funcao para a interpolacao linear"""

#interpolacao polinomial por lagrange - f1
#f1=interpolate.lagrange(arrayX,arrayY)
"""Este metodo gera polinomios para a interpolacao baseados nos pontos dados"""

#interpolacao de spline Cubico - f2
#f2=interpolate.CubicSpline(arrayX,arrayY)
"""Este metodo gera polinomios para a interpolacao baseados nos pontos dados"""

#xnew=np.arange(p1.getX(),p3.getX(),step)
xnew=np.arange(pointVec[0].getX(),pointVec[len(pointVec)-1].getX(),step)

ynewSpline=[]
for k in range(0,len(pointVec),int(step)):
    ynewSpline.append(pointVec[k].getY())

#ynewSpline=np.arange(pointVec[0].getY(),pointVec[len(pointVec)-1].getY(),step)
print(len(xnew)," ",len(ynewSpline))
#array de step segundos, interpolacao linear 
ynew=f(xnew)

#ynew1=f1(xnew)

#Spline para cada step segundos
f2=interpolate.CubicSpline(xnew,ynewSpline)
ynew2=f2(arrayX)
print("Y spline cubico: ",len(ynew2))
#diffs = arrayY - ynew2

#print(numpy.amax(diffs))
#print(numpy.amin(diffs))

fig = Figure(figsize=(5, 4), dpi=100)
fig.add_subplot(111).plot(arrayX,arrayY,"ro")
fig.add_subplot(111).plot(xnew, ynew,"b^")
#fig.add_subplot(111).plot(xnew, ynew1,"b--")
fig.add_subplot(111).plot(arrayX, ynew2,"g--")

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

