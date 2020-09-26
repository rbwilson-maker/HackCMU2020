import tkinter as tk
#from https://www.cs.cmu.edu/~112/notes/notes-graphics.html#customColors
def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'

def drawHangman(canvas, w, h):
    #variables#
    margin = 50
    poleLength = h - 2 * margin
    poleBaseWidth = w // 10
    poleTopWidth = w // 2
    poleX = margin + poleBaseWidth // 2
    poleBitLen = h // 10
    headRadius = h // 10
    bodyLength = 2.5 * headRadius
    armWidth = 3.5 * headRadius
    darkRed = rgbString(200, 10, 75)

    canvas.create_text(w/2, h/2, text="CMU", font="Roboto 215 bold", fill = darkRed)

    #to make post/pole#
    #vertical pole#
    canvas.create_line(poleX, margin, poleX, margin + poleLength, width=10)
    #pole base#
    canvas.create_line(margin, h - margin, margin + poleBaseWidth, h - margin, width = 10)
    #top of pole#
    canvas.create_line(margin + poleTopWidth, margin, margin + poleTopWidth, margin + poleBitLen, width =10)
    #extra pole bit on top
    canvas.create_line(margin + poleBaseWidth // 2, margin, margin + poleTopWidth, margin, width = 10)
    
    #gets cases#
    population = 3000
    cases = int(input("How many COVID cases? "))
    caseRatio = cases/population
    increment = 0.02

    #makes body based on cases#
    if (caseRatio > increment):
        #head#
        canvas.create_oval(margin + poleTopWidth - headRadius, margin + poleBitLen, margin + poleTopWidth + headRadius, margin + poleBitLen + 2 * headRadius, width = 10)
        if (caseRatio > 2*increment):
            #body#
            canvas.create_line(margin + poleTopWidth, margin + poleBitLen + headRadius * 2, margin + poleTopWidth, margin + poleBitLen + headRadius * 2 + bodyLength, width = 10)
            if (caseRatio > 3*increment):
                #arms#
                canvas.create_line(margin + poleTopWidth - armWidth // 2, margin + poleBitLen + headRadius * 2 + bodyLength // 3, margin + poleTopWidth + armWidth // 2, margin + poleBitLen + headRadius * 2 + bodyLength // 3, width = 10)
                if (caseRatio > 4*increment):
                    #left leg#
                    canvas.create_line(margin + poleTopWidth, margin + poleBitLen + headRadius * 2 + bodyLength, margin + poleTopWidth - armWidth // 2, h - margin * 2, width = 10)
                    if(caseRatio> 5*increment):
                        #right leg#
                        canvas.create_line(margin + poleTopWidth, margin + poleBitLen + headRadius * 2 + bodyLength, margin + poleTopWidth + armWidth // 2, h - margin * 2, width = 10)
                        canvas.create_text(w/2, h/2, text="!!!GO HOME!!!", font = "Nunito 58 bold", fill = rgbString(240,240,50))

def drawMask(canvas, margin, poleTopWidth, headRadius, poleBitLen):
    maskRatio = 0.75
    canvas.create_line(margin + poleTopWidth - headRadius, margin + poleBitLen + headRadius, margin + poleTopWidth + headRadius, margin + poleBitLen + headRadius)
    canvas.create_line(margin + poleTopWidth - headRadius, margin + poleBitLen + headRadius + headRadius * maskRatio, margin + poleTopWidth + headRadius, margin + poleBitLen + headRadius + headRadius * maskRatio)
    canvas.create_line(margin + poleTopWidth - headRadius * maskRatio, margin + poleBitLen + headRadius, margin + poleTopWidth - headRadius * maskRatio, margin + poleBitLen + headRadius + headRadius * maskRatio)
    canvas.create_line(margin + poleTopWidth + headRadius * maskRatio, margin + poleBitLen + headRadius, margin + poleTopWidth + headRadius * maskRatio, margin + poleBitLen + headRadius + headRadius * maskRatio)


    
                        
def makeCanvas(w, h):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=w, height=h)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawHangman(canvas, w, h)
    root.mainloop()

makeCanvas(500, 500)
