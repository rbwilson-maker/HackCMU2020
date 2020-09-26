import tkinter as tk
def drawHangman(canvas, w, h):
    margin = 50
    poleLength = h - 2 * margin
    poleBaseWidth = w // 10
    poleTopWidth = w // 2
    poleX = margin + poleBaseWidth // 2
    poleBitLen = h // 10
    headRadius = h // 10
    bodyLength = 3 * headRadius
    armWidth = 4 * headRadius
    canvas.create_line(poleX, margin, poleX, margin + poleLength)
    canvas.create_line(margin, h - margin, margin + poleBaseWidth, h - margin)
    canvas.create_line(margin + poleTopWidth, margin, margin + poleTopWidth, margin + poleBitLen)
    canvas.create_line(margin + poleBaseWidth // 2, margin, margin + poleTopWidth, margin)
    canvas.create_oval(margin + poleTopWidth - headRadius, margin + poleBitLen, margin + poleTopWidth + headRadius, margin + poleBitLen + 2 * headRadius, fill = "white")
    canvas.create_line(margin + poleTopWidth, margin + poleBitLen + headRadius * 2, margin + poleTopWidth, margin + poleBitLen + headRadius * 2 + bodyLength)
    canvas.create_line(margin + poleTopWidth - armWidth // 2, margin + poleBitLen + headRadius * 2 + bodyLength // 3, margin + poleTopWidth + armWidth // 2, margin + poleBitLen + headRadius * 2 + bodyLength // 3)

def makeCanvas(w, h):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=w, height=h)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawHangman(canvas, w, h)
    root.mainloop()

makeCanvas(500, 500)
