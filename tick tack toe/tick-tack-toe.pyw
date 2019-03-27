from tkinter import *
import tkinter.messagebox

def start_gui():
    global root
    #finds element index and stores it in a list
    def eLoc(array,element):
        new=[i for i,x in enumerate(array) if x==element]
        return new

    #function that does the actual game and process
    def onClick(event):
        #geting button id and location of click
        loc=event.widget.find_closest(event.x, event.y)
        xLocation=event.x 
        yLocation=event.y
        location=loc[0]
        location-=5
        #generation variables
        X='X'
        O='O'
        x=40
        y=40
        global turn
        global newPos
        global board
        global draw
        
        #deletes 'blank' text and replace with an 'x' or 'o' depending on the turn
        canvas.delete(positions[location])       
        if turn%2==0:
            new=canvas.create_text(xLocation,yLocation,text=X)
            newPos.append(new)
            board[location]=1
            
        if turn%2==1:
            new=canvas.create_text(xLocation,yLocation,text=O)
            newPos.append(new)
            board[location]=2  
        turn+=1
        # more game parameters
        del row[:]
        del column[:]
        del slope[:]
        c=0
        for i in range(0,3):
            row.append(board[c:c+3])
            column.append([board[i] for i in range(i,9,3)])
            c+=3
        slope.insert(0,[board[4*i-4] for i in range(1,4)])
        slope.insert(1,[board[2*i] for i in range(1,4)])
        #cheking for win
        if len(eLoc(row[0],1))==3 or len(eLoc(row[1],1))==3 or len(eLoc(row[2],1))==3:
            places=[]
            for i in range(0,3):
                if len(eLoc(row[i],1))==3:
                    places.append(i)
            place=places[0]+1    
            canvas.create_line(0,80*place-40,240,80*place-40,width=10)
            tkinter.messagebox.showinfo('Game over','"X" player won')        

        
        if sum(row[0])==6 or sum(row[1])==6 or sum(row[2])==6:
            places=[]
            for i in range(0,3):
                if sum(row[i])==6:
                    places.append(i)
            place=places[0]+1    
            canvas.create_line(0,80*place-40,240,80*place-40,width=10)
            tkinter.messagebox.showinfo('Game over','"0" player won')

        if len(eLoc(column[0],1))==3 or len(eLoc(column[1],1))==3 or len(eLoc(column[2],1))==3:
            places=[]
            for i in range(0,3):
                if len(eLoc(column[i],1))==3:
                    places.append(i)
            place=places[0]+1    
                
            canvas.create_line(80*place-40,0,80*place-40,240,width=10)
            tkinter.messagebox.showinfo('Game over','"X" player won')

        if sum(column[0])==6 or sum(column[1])==6 or sum(column[2])==6:
            places=[]
            for i in range(0,3):
                if sum(column[i])==6:
                    places.append(i)
            place=places[0]+1
                
            canvas.create_line(80*place-40,0,80*place-40,240,width=10)
            tkinter.messagebox.showinfo('Game over','"0" player won')

        if len(eLoc(slope[0],1))==3 or len(eLoc(slope[1],1))==3:           
            if len(eLoc(slope[0],1))==3:
                canvas.create_line(0,0,240,240,width=10)
            if len(eLoc(slope[1],1))==3:
                canvas.create_line(240,0,0,240,width=10)
            tkinter.messagebox.showinfo('Game over','"X" player won')

        if sum(slope[0])==6 or sum(slope[1])==6:
            if sum(slope[0])==6:
                canvas.create_line(0,0,240,240,width=10)
            if sum(slope[1])==6:
                canvas.create_line(240,0,0,240,width=10)
            tkinter.messagebox.showinfo('Game over','"0" player won')
        #cheking if the game is a draw
        if turn==9:
            for i in range(0,3):
                if sum(row[i])!=6 and sum(column[i])!=6:
                    draw+=1
                    print(draw)
                if len(eLoc(row[i],1))!=3 and len(eLoc(column[i],1))!=3:
                    draw+=1
                    print(draw)
            for i in range(0,2):
                if sum(slope[i])!=6 and len(eLoc(slope[i],1))!=3:
                    draw+=1
                    print(draw)
        if draw==8:
            tkinter.messagebox.showinfo('DRAW','game ended in a draw!!')

    #configuring window
    root=Tk()    
    root.iconbitmap('Iconsmind-Outline-Chess-Board.ico')
    root.title('tick-tack-toe')
    root.geometry('480x480+0+0')
    root.configure(bg='silver')

    #generating grid
    canvas = Canvas(root,width=240,height=240)
    vertical_Line1 = canvas.create_line(80,0,80,240)
    vertical_Line2 = canvas.create_line(160,0,160,240)
    horizontal_line1 = canvas.create_line(0,80,240,80)
    horizontal_line2 = canvas.create_line(0,160,240,160)
    canvas.pack()

    x=40
    y=40
    positions=[]

    for i in range(0,9):
        loc=canvas.create_text(x,y,text='blank', tags='spot'+str(i))
        positions.append(loc)
        canvas.tag_bind('spot'+str(i),'<ButtonPress-1>', onClick)
        x+=80
        if x==280:
            x=40
            y+=80

    global turn
    global newPos
    global draw
    turn=0
    newPos=[]
    draw=0

    exitButton= Button(root,text='exit',command=root.destroy).pack()
    resetButton = Button(root,text='reset',command=refresh).pack()

    #game parameters aka rules
    x=0
    global board
    board=[x for i in range(0,9)]
    global row 
    global column
    global slope
    row=[]
    column=[]
    slope=[]
    root.mainloop()

def refresh():
    root.destroy()
    start_gui()

start_gui()