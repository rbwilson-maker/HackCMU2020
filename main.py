
import tkinter as tk
import requests

#from https://www.cs.cmu.edu/~112/notes/notes-graphics.html#customColors
def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'

def drawLabels(canvas, w, h, margin):
    canvas.create_oval(w - margin*2.75, margin*2, w - margin*2.25, margin*2.5)
    canvas.create_text(w - margin*2, margin*2, text = "> 2%", anchor = "nw")
    canvas.create_line(w - margin*2.5, margin*2.75, w - margin*2.5, margin*3)
    canvas.create_text(w - margin*2, margin*2.875, text = "> 4%", anchor = "nw")
    canvas.create_line(w - margin*2.75, margin*3.375, w - margin*2.25, margin*3.375)
    canvas.create_text(w - margin*2, margin*3.25, text = "> 6%", anchor = "nw")
    
def getCases(state, increment):
    if (len(state)!=2):
        validState = False
        return None, validState
    r = requests.get(' https://api.covidtracking.com/v1/states/' + state + '/current.json')
    d = r.json()
    positive = d['positiveIncrease']
    total = d['totalTestResultsIncrease']

    if total ==0 or (positive == None) or (total == None):
        validState = False
        return None, validState
    else:
        validState = True
        caseRatio = positive/total
        increment = increment
        return caseRatio, validState

def drawBackground(canvas, w, h, margin):
    red = rgbString(196, 18, 48)
    green = rgbString(0,150,71)
    yellow = rgbString(253, 181, 21)
    blue = rgbString(4, 54, 115)
    colors = [red, green, yellow, red, blue, green]
    colorCount = 0
    for col in range(0, w, w//20):
        fill = colors[colorCount% 6]
        canvas.create_rectangle(col, 0, col + w//10, margin//2, fill = fill)
        canvas.create_rectangle(col, h-margin//2, col + w//10, h, fill = fill)
        colorCount +=1
    for row in range(0, h, h//20):
        fill = colors[colorCount%6]
        canvas.create_rectangle(0, row, margin//2, row+h//10, fill = fill)
        canvas.create_rectangle(w-margin//2, row, w, row+h//10, fill = fill)
        colorCount +=1

    #canvas.create_text(w/2, h/2, text="CMU", font="Roboto 215 bold", fill = darkRed)

def drawPole(canvas, h, margin, poleLength, poleBaseWidth, poleTopWidth, poleX, poleBitLen):
    #to make post/pole#
    #vertical pole#
    canvas.create_line(poleX, margin, poleX, margin + poleLength, width=10)
    #pole base#
    canvas.create_line(margin, h - margin, margin + poleBaseWidth, h - margin, width = 10)
    #top of pole#
    canvas.create_line(margin + poleTopWidth, margin, margin + poleTopWidth, margin + poleBitLen, width =10)
    #extra pole bit on top
    canvas.create_line(margin + poleBaseWidth // 2, margin, margin + poleTopWidth, margin, width = 10)

def drawHead(canvas, margin, headRadius, poleBitLen, poleTopWidth):
    canvas.create_oval(margin + poleTopWidth - headRadius, margin + poleBitLen, margin + poleTopWidth + headRadius, margin + poleBitLen + 2 * headRadius, width = 10, fill = "white")

def drawMask(canvas, margin, poleTopWidth, headRadius, poleBitLen):
    maskRatio = 0.75
    fill = 'black'
    canvas.create_rectangle(margin + poleTopWidth - headRadius, margin + poleBitLen + headRadius, margin + poleTopWidth + headRadius, margin + poleBitLen + headRadius + 5, fill = fill)
    canvas.create_rectangle(15 + margin + poleTopWidth - headRadius, margin + poleBitLen + headRadius, margin + poleTopWidth + headRadius - 15, margin + poleBitLen + headRadius + headRadius * maskRatio, fill = fill)

def drawBody(canvas, margin, poleTopWidth, poleBitLen, headRadius, bodyLength):
    canvas.create_line(margin + poleTopWidth, margin + poleBitLen + headRadius * 2, margin + poleTopWidth, margin + poleBitLen + headRadius * 2 + bodyLength, width = 10)

def drawArms(canvas, margin, poleTopWidth, armWidth, poleBitLen, bodyLength, headRadius):
    canvas.create_line(margin + poleTopWidth - armWidth // 2, margin + poleBitLen + headRadius * 2 + bodyLength // 3, margin + poleTopWidth + armWidth // 2, margin + poleBitLen + headRadius * 2 + bodyLength // 3, width = 10)

def drawLegs(canvas, h, margin, poleTopWidth, poleBitLen, headRadius, bodyLength, armWidth):
    canvas.create_line(margin + poleTopWidth, margin + poleBitLen + headRadius * 2 + bodyLength, margin + poleTopWidth - armWidth // 2, h - margin * 2, width = 10)
    canvas.create_line(margin + poleTopWidth, margin + poleBitLen + headRadius * 2 + bodyLength, margin + poleTopWidth + armWidth // 2, h - margin * 2, width = 10)

def drawHangman(canvas, w, h, state):
    #variables#
    margin = 50
    poleLength = h - 2 * margin
    poleBaseWidth = w // 10
    poleTopWidth = w // 5 *2
    poleX = margin + poleBaseWidth // 2
    poleBitLen = h // 10
    headRadius = h // 10
    bodyLength = 2.5 * headRadius
    armWidth = 3.5 * headRadius
    increment = 0.015
    
    state = state
    caseRatio, validState = getCases(state, increment)
    while(not validState):
        state = input("Not enough data for that state. Please choose another:")
        state = state.strip().lower()
        caseRatio, validState = getCases(state, increment)

    drawBackground(canvas,w,h, margin)
    drawLabels(canvas, w, h, margin)
    drawPole(canvas, h, margin, poleLength, poleBaseWidth, poleTopWidth, poleX, poleBitLen)

    
    
    #displays data
    canvas.create_text(w-margin, margin, text = f"State: {state.upper()}", anchor = 'ne', font = "Nunito 20 bold")
    canvas.create_text(w-margin, margin+20, text = "Positivity rate: %0.2f" % (caseRatio*100) + "%", anchor = 'ne', font = "Nunito 15 bold")
    

    #makes body based on cases#
    if (caseRatio > increment):
        drawHead(canvas, margin, headRadius, poleBitLen, poleTopWidth)
        drawMask(canvas, margin, poleTopWidth, headRadius, poleBitLen)
        if (caseRatio > 2*increment):
            drawBody(canvas, margin, poleTopWidth, poleBitLen, headRadius, bodyLength)
            if (caseRatio > 3*increment):
                drawArms(canvas, margin, poleTopWidth, armWidth, poleBitLen, bodyLength, headRadius)
                if (caseRatio > 4*increment):
                    drawLegs(canvas, h, margin, poleTopWidth, poleBitLen, headRadius, bodyLength, armWidth)
                    #if(caseRatio> 5*increment):
                        #canvas.create_text(w/2, h/2, text="!!!GO HOME!!!", font = "Nunito 58 bold", fill = rgbString(240,240,50))
    makeCanvas(w,h)

def makeCanvas(w, h):
    state = input("Which state (use abbreviation)?").strip().lower()
    root = tk.Tk()
    canvas = tk.Canvas(root, width=w, height=h)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawHangman(canvas, w, h, state)
    root.mainloop()
    
makeCanvas(500, 500)
