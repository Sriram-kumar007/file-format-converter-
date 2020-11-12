#importing required modules

from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd 
from fpdf import FPDF


# functions 

def jpgtopng():
    root.config(bg='#badc57')# change bg
    def getjpgfile():#convert jpg to png
        
        file_path = fd.askopenfilename()
        pic=Image.open(file_path) 
        
   
        export_file_path = fd.asksaveasfilename(defaultextension='.png',filetypes= [('Image (.png file)','.png')] )
        pic.save(export_file_path)   
        
    global Head #destroy old configuration
    imagelabel.destroy()
    f1.destroy()
    Head.destroy()
    Head=Label(text='JPG To PNG Converter',font='Lucida 20 bold',bg='black',fg='#F4C724',padx=5,pady=5)
    Head.pack(pady=10)
   
    
    jpg=Button(text='  Convert JPG To PNG  ', bg='#BB2CD9', fg='white', font=('helvetica', 15, 'bold'),command=getjpgfile)
    jpg.pack(pady=100)#save button
    

    bottom_pic=Image.open('jpg to png.png') # bottom pic
    bottom_pic=bottom_pic.resize((400,250),Image.ANTIALIAS)
    bg_pic=ImageTk.PhotoImage(bottom_pic)
    img_label=Label(root,image=bg_pic)
    img_label.image=bg_pic  
    img_label.pack(side=BOTTOM,pady=40)

    close=Button(text='Close',command=root.destroy,bg='black',fg='white',font='11')
    close.place(x=105,y=600) #close button


def pngtojpg():
    root.config(bg='#67E6DC')# change bg
    def getpngfile():
        
        file_location=fd.askopenfilename()
        pic=Image.open(file_location)      
        pic=pic.convert('RGB') 
        
    
        export_file_location = fd.asksaveasfilename(defaultextension='.jpg',filetypes= [('Image ( file)','*.jpg')] )
        pic.save(export_file_location)  
        
    global Head#destroy old configuration
    imagelabel.destroy()
    f1.destroy()
    Head.destroy()
    Head=Label(text='PNG To JPG Converter',font='Lucida 20 bold',bg='black',fg='#F4C724',padx=5,pady=5)
    Head.pack(pady=10)
    #To get jpg file
   
    #To save jpg file
    png=Button(text='  Convert PNG To JPG  ', bg='#2B2B52', fg='white', font=('helvetica', 15, 'bold'),command=getpngfile)
    png.pack(pady=100)

    #Image in bottom
    bottom_pic=Image.open('png to jpg.png')# bottom pic
    bottom_pic=bottom_pic.resize((400,250),Image.ANTIALIAS)
    bg_pic=ImageTk.PhotoImage(bottom_pic)
    img_label=Label(root,image=bg_pic)
    img_label.image=bg_pic  
    img_label.pack(side=BOTTOM,pady=40)

    #Close Button
    close=Button(text='Close',command=root.destroy,bg='black',fg='white',font='11')
    close.place(x=105,y=600)



def jpgtopdf():
    root.config(bg='#FF54A7')# change bg
    def getjpgfile():
        
        file_path = fd.askopenfilename()
        img=Image.open(file_path)
    
        img.save(fd.asksaveasfilename(defaultextension='.pdf',filetypes= [("pdf files" ,'*.pdf')] ))
    global Head#destroy old configuration
    imagelabel.destroy()
    f1.destroy()
    Head.destroy()
    Head=Label(text='JPG to PDF Converter',font='Lucida 20 bold',bg='black',fg='#F4C724',padx=5,pady=5)

    Head.pack(pady=30)
    
    jpgtopdf=Button(text='  Convert JPG to PDF ', bg='#2B2B52', fg='white', font=('helvetica', 15, 'bold'),command=getjpgfile)
    jpgtopdf.pack(pady=100)

    bottom_pic=Image.open('jpg to pdf.png')
    bottom_pic=bottom_pic.resize((400,250),Image.ANTIALIAS)# bottom pic
    bg_pic=ImageTk.PhotoImage(bottom_pic)
    img_label=Label(root,image=bg_pic)
    img_label.image=bg_pic  
    img_label.pack(side=BOTTOM,pady=40)

    close=Button(text='Close',command=root.destroy,bg='black',fg='white',font='11')
    close.place(x=105,y=600)


def pngtopdf():
    root.config(bg='#8875F0')# change bg
    def getpngfile():

        img=Image.open(fd.askopenfilename())
        Img=img.convert('RGB')
        Img.save(fd.asksaveasfilename(defaultextension='.pdf',filetypes= [("pdf files" ,'*.pdf')] ))

    global Head#destroy old configuration
    imagelabel.destroy()
    f1.destroy()
    Head.destroy()
    Head=Label(text='PNG to PDF Converter',font='Lucida 20 bold',bg='black',fg='#F4C724',padx=5,pady=5)

    Head.pack(pady=10)
    
    pngtopdf=Button(text='  Convert PNG to PDF ', bg='#2B2B52', fg='white', font=('helvetica', 15, 'bold'),command=getpngfile)
    pngtopdf.pack(pady=100)

    bottom_pic=Image.open('png to pdf.png')
    bottom_pic=bottom_pic.resize((400,250),Image.ANTIALIAS)

    bg_pic=ImageTk.PhotoImage(bottom_pic)# bottom pic
    img_label=Label(root,image=bg_pic)
    img_label.image=bg_pic  
    img_label.pack(side=BOTTOM,pady=40)

    close=Button(text='Close',command=root.destroy,bg='black',fg='white',font='11')
    close.place(x=105,y=600)


def texttopdf():
    root.config(bg='#FFA4A4')# change bg
    def txttopdf():
        a=open(fd.askopenfilename())
        

        pdf=FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size=12)
        for i in a:
            pdf.cell(200,10,txt=i,ln=1,align='L')
        b=fd.asksaveasfilename(defaultextension='.pdf',filetypes= [("pdf files" ,'*.pdf')] )
        pdf.output(b)


          
    global Head#destroy old configuration
    imagelabel.destroy()
    f1.destroy()
    Head.destroy()
    Head=Label(text='TEXT to PDF Converter',font='Lucida 20 bold',bg='black',fg='#F4C724',padx=5,pady=5)

    Head.pack(pady=10)
    
    texttopdf=Button(text='  Convert Text file ', bg='#2B2B52', fg='white', font=('helvetica', 15, 'bold'),command=txttopdf)
    texttopdf.pack(pady=100)

    
    
    bottom_pic=Image.open('txt to pdf.png')
    bottom_pic=bottom_pic.resize((500,300),Image.ANTIALIAS)# bottom pic
    bg_pic=ImageTk.PhotoImage(bottom_pic)
    img_label=Label(root,image=bg_pic)
    img_label.image=bg_pic  
    img_label.pack(side=BOTTOM,pady=20)

    close=Button(text='Close',command=root.destroy,bg='black',fg='white',font='11')
    close.place(x=105,y=600)











def jtopenter(event):
    jtop.config(bg='black',fg='white')
def jtopleave(event):
    jtop.config(bg='white',fg='black')

def ptojenter(event):
    ptoj.config(bg='black',fg='white')
def ptojleave(event):
    ptoj.config(bg='white',fg='black')

def statuse(event):
    jpga.config(bg='black',fg='white')
def statusl(event):
    jpga.config(bg='white',fg='black')

def status1e(event):
    pnga.config(bg='black',fg='white')
def status1l(event):
    pnga.config(bg='white',fg='black')

def status2e(event):
    texta.config(bg='black',fg='white')
def status2l(event):
    texta.config(bg='white',fg='black')

def status3e(event):
    worda.config(bg='black',fg='white')
def status3l(event):
    worda.config(bg='white',fg='black')


root=Tk()
root.title('File Format Converter')
root.config(bg='white')

root.state('zoomed')


'''Creating Main Window :'''

#Heading of GUI
Head=Label(text='File Format Converter',font='Lucida 20 bold',bg='black',fg='#F4C724',padx=5,pady=5)
Head.pack(pady=10)

#Buttons
f1=Frame(root)
jtop=Button(f1,text='JPG To PNG',font='arial 15 bold',command=jpgtopng)
jtop.pack(side=RIGHT)
jtop.config(bg='white',width=15)
jtop.bind('<Enter>',jtopenter)
jtop.bind('<Leave>',jtopleave)

ptoj=Button(f1,text='PNG To JPG',font='arial 15 bold',command=pngtojpg)
ptoj.pack(side=RIGHT)
ptoj.config(bg='white',width=15)
ptoj.bind('<Enter>',ptojenter)
ptoj.bind('<Leave>',ptojleave)

jpga=Button(f1,text='JPG To PDF',font='arial 15 bold',command=jpgtopdf)
jpga.pack(side=RIGHT)
jpga.config(bg='white',width=15)
jpga.bind('<Enter>',statuse)
jpga.bind('<Leave>',statusl)


pnga=Button(f1,text='PNG To PDF',font='arial 15 bold',command=pngtopdf)
pnga.pack(side=RIGHT)
pnga.bind('<Enter>',status1e)
pnga.config(bg='white',width=15)
pnga.bind('<Leave>',status1l)



texta=Button(f1,text='Txt To PDF',font='arial 15 bold',command=texttopdf)
texta.pack(side=RIGHT)
texta.config(bg='white',width=15)
texta.bind('<Enter>',status2e)
texta.bind('<Leave>',status2l)
f1.pack(pady=20)

img=Image.open('imgconv.png')
img=img.resize((400,375),Image.ANTIALIAS)
bgpic=ImageTk.PhotoImage(img)
imagelabel=Label(image=bgpic)
imagelabel.place(x=300,y=200)



#Status Bar
sbar=Label(text='By Sriram k.v',font='Helvetica 10 bold',relief=SUNKEN,anchor='w',padx=10)
sbar.pack(side=BOTTOM,fill=X)

root.mainloop()


# read README for detail explanation
#for any comments and sugesstion please contact me
#Developer contact: sriramvkumar007@gmail.com