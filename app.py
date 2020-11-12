from tkinter import *
import rotatescreen



class Rotate_Screen:
    def __init__(self,root):
        self.root=root
        self.root.title("Screen Rotation")
        self.root.geometry("400x200")
        self.root.iconbitmap("logo804.ico")
        self.root.resizable(0,0)



        def on_enter1(e):
            but_top['background']="black"
            but_top['foreground']="cyan"  
        def on_leave1(e):
            but_top['background']="SystemButtonFace"
            but_top['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_left['background']="black"
            but_left['foreground']="cyan"  
        def on_leave2(e):
            but_left['background']="SystemButtonFace"
            but_left['foreground']="SystemButtonText"


        def on_enter3(e):
            but_right['background']="black"
            but_right['foreground']="cyan"  
        def on_leave3(e):
            but_right['background']="SystemButtonFace"
            but_right['foreground']="SystemButtonText"

            

        def on_enter4(e):
            but_bottom['background']="black"
            but_bottom['foreground']="cyan"  
        def on_leave4(e):
            but_bottom['background']="SystemButtonFace"
            but_bottom['foreground']="SystemButtonText"
        

        screen=rotatescreen.get_primary_display()


        def top():
            screen.set_landscape()

        def bottom():        
            screen.set_portrait()

        def right():
            screen.set_portrait_flipped()

        def left():
            screen.set_landscape_flipped()





#=====================mainframe========================#
        
        mainframe=Frame(self.root,width=400,height=200,relief="ridge",bd=3,bg="gray80")
        mainframe.place(x=0,y=0)

#======================button==========================
        
        but_top=Button(mainframe,text="Top",width=18,font=('times new roman',12),cursor="hand2",command=top)
        but_top.place(x=110,y=20)
        but_top.bind("<Enter>",on_enter1)
        but_top.bind("<Leave>",on_leave1)

        but_left=Button(mainframe,text="Left",width=18,font=('times new roman',12),cursor="hand2",command=left)
        but_left.place(x=20,y=80)
        but_left.bind("<Enter>",on_enter2)
        but_left.bind("<Leave>",on_leave2)

        but_right=Button(mainframe,text="Right",width=18,font=('times new roman',12),cursor="hand2",command=right)
        but_right.place(x=200,y=80)
        but_right.bind("<Enter>",on_enter3)
        but_right.bind("<Leave>",on_leave3)

        but_bottom=Button(mainframe,text="Bottom",width=18,font=('times new roman',12),cursor="hand2",command=bottom)
        but_bottom.place(x=110,y=140)
        but_bottom.bind("<Enter>",on_enter4)
        but_bottom.bind("<Leave>",on_leave4)

        
             




if __name__ == "__main__":
    root=Tk()
    app=Rotate_Screen(root)
    root.mainloop()
