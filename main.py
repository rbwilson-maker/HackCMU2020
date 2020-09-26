import tkinter as tk
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
    
    #to make post/pole#
    #vertical pole#
    canvas.create_line(poleX, margin, poleX, margin + poleLength)
    #pole base#
    canvas.create_line(margin, h - margin, margin + poleBaseWidth, h - margin)
    #top of pole#
    canvas.create_line(margin + poleTopWidth, margin, margin + poleTopWidth, margin + poleBitLen)
    #extra pole bit on top
    canvas.create_line(margin + poleBaseWidth // 2, margin, margin + poleTopWidth, margin)
    
    #gets cases#
    population = 3000
    cases = int(input("How many COVID cases? "))
    caseRatio = cases/population
    increment = 0.02

    #makes body based on cases#
    if (caseRatio > increment):
        #head#
        canvas.create_oval(margin + poleTopWidth - headRadius, margin + poleBitLen, margin + poleTopWidth + headRadius, margin + poleBitLen + 2 * headRadius)
        if (caseRatio > 2*increment):
            #body#
            canvas.create_line(margin + poleTopWidth, margin + poleBitLen + headRadius * 2, margin + poleTopWidth, margin + poleBitLen + headRadius * 2 + bodyLength)
            if (caseRatio > 3*increment):
                #arms#
                canvas.create_line(margin + poleTopWidth - armWidth // 2, margin + poleBitLen + headRadius * 2 + bodyLength // 3, margin + poleTopWidth + armWidth // 2, margin + poleBitLen + headRadius * 2 + bodyLength // 3)
                if (caseRatio > 4*increment):
                    #left leg#
                    canvas.create_line(margin + poleTopWidth, margin + poleBitLen + headRadius * 2 + bodyLength, margin + poleTopWidth - armWidth // 2, h - margin * 2)
                    if(caseRatio> 5*increment):
                        #right leg#
                        canvas.create_line(margin + poleTopWidth, margin + poleBitLen + headRadius * 2 + bodyLength, margin + poleTopWidth + armWidth // 2, h - margin * 2)
                        canvas.create_text(w/2, h/2, text="!!!GO HOME!!!", font = "Nunito 38 bold", color = "red")

def makeCanvas(w, h):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=w, height=h)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawHangman(canvas, w, h)
    root.mainloop()

makeCanvas(500, 500)
