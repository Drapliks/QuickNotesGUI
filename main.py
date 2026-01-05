from Tkinter import *
import sys

root = Tk()
root.resizable(width=False, height=False)

def newnote():
    root.title('New note')
    root.geometry('295x190')

    def create():
        def notebook():
            root.geometry('365x110')
            root.title(newnotename)
            exitButt.destroy()
            notenameT.destroy()
            notename.destroy()
            createButt.destroy()

            def save():
                def ok():
                    savemessage.destroy()

                savetxt = inputfield.get()
                newnotefile.write(savetxt)

                savemessage = Tk()

                savemessage.title('')
                savemessage.geometry('190x110')
                savemessage.resizable(width=False, height=False)

                savesuccess = Label(savemessage, text='Successful save!')
                savesuccess.pack()

                okbutton = Button(savemessage, text='Ok', command=ok)
                okbutton.pack()

                savemessage.mainloop()

            def clear():
                inputfield.delete(0, END)

            inputfield = Entry(root)
            inputfield.pack(side='left')

            savebutt = Button(root, text='Save', command=save)
            savebutt.pack(side='left')

            clearbutt = Button(root, text='Clear', command=clear)
            clearbutt.pack(side='left')

            exitNotebookButt = Button(root, text='Exit', command=exitN)
            exitNotebookButt.pack(side='left')

        newnotename = notename.get() + '.txt'
        newnotefile = open(newnotename, "w+")
        notebook()


    notenameT = Label(root, text='Note name:')
    notenameT.pack()

    notename = Entry(root)
    notename.pack()

    createButt = Button(root, text='Create', command=create)
    createButt.pack()

    exitButt = Button(root, text='Exit', command=exitN)
    exitButt.pack()

def exitN():
    sys.exit()

newnote()

root.mainloop()
