from ctypes import windll
import Tkinter as tk

parport = windll.inpout32

forw = 0b0001
back = 0b0010
left = 0b0100
righ = 0b1000

def drive(b):
    if b==forw+back: return 'Car can\'t go forwards and backwards simultaneously'
    elif b==left+righ: return 'Car can\'t go left and right simultaneously'
    else:
        parport.Out32(0x378,b)
        return 'Sent signal %d' % b

def key(press):
    if   press.keysym=='Escape': root.destroy()
    if   press.char=='1': drive(back+left)
    elif press.char=='2': drive(back)
    elif press.char=='3': drive(back+righ)
    elif press.char=='4': drive(left)
    elif press.char=='5': drive(0)
    elif press.char=='6': drive(righ)
    elif press.char=='7': drive(forw+left)
    elif press.char=='8': drive(forw)
    elif press.char=='9': drive(forw+righ)
    
        
root = tk.Tk()
print 'Numpad to control the car. ESC to exit.'
root.bind_all('<Key>', key)
root.wm_title('Parport RC')
root.mainloop()
