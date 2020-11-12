READ ME

WHAT IS IT ?

 	This is a project to convert file formats with tkinter. Png(.png),jpg(.jpg),pdf(.pdf),text(.txt) files can be converted.

HOW TO USE IT ?
	
	After running the project you can see 5 buttons, by clicking that you can go into it and click to open the file after openning the file, next dialog box opens you can save the converted file in the machine and use it.


INSTALLING REQUIRED MODULES IN CMD:

tkinter:
        tkinter is a default module with python

pillow:
       pip install PIL

fpdf:
     pip install fpdf       



CODE EXPLANATION:

 #importing required modules

from tkinter import * - importing tkinter for the window

from PIL import Image, ImageTk - importing pillow for opening
                                 images  

from tkinter import filedialog as fd - for browsing the file in 
                                       machine

from fpdf import FPDF -importing fpdf for opening
                       pdf


def jpgtopng(): - defineing function

    root.config(bg='#badc57') - change bg colour
    def getjpgfile():- drfing function convert jpg to png
        
        file_path = fd.askopenfilename() - dialogbox to find the 
                                           path

        pic=Image.open(file_path) - opening the image
        
   
        export_file_path = fd.asksaveasfilename(defaultextension='.png',filetypes= [('Image (.png 
        file)','.png')] ) - path to save image

        pic.save(export_file_path) - saving converted image  
        
    global Head - destroy  all old configuration

    imagelabel.destroy()- destroy  all old configuration

    f1.destroy()- destroy  all old configuration

    Head.destroy()- destroy  all old configuration

    Head=Label(text='JPG To PNG Converter',font='Lucida 20 bold',bg='black',fg='#F4C724',padx=5,pady=5)- destroy  all 
                                                  old configuration

    Head.pack(pady=10)- destroy  all old configuration
   
    
    jpg=Button(text='  Convert JPG To PNG  ', bg='#BB2CD9', fg='white', font=('helvetica', 15, 'bold'),command=getjpgfile) - button to convert 

    jpg.pack(pady=100)#save button - packing the button
    

    bottom_pic=Image.open('E:\\images\\jpg to png.png') - image

    bottom_pic=bottom_pic.resize((400,250),Image.ANTIALIAS)

    bg_pic=ImageTk.PhotoImage(bottom_pic)

    img_label=Label(root,image=bg_pic)

    img_label.image=bg_pic  

    img_label.pack(side=BOTTOM,pady=40)

    close=Button(text='Close',command=root.destroy,bg='black',fg='white',font='11') - button to close

    close.place(x=105,y=600) #close button - packing close button

FOR ALL THE NEXT FUNCTIONS THE CORDINATES OF CONFIGURATION ONLY CHANGES SO IT IS NOT EXPLAINED AGAIN, THE INER FUCTIO IS EXPLAINED BELOW:

def pngtojpg(): - defining function

    root.config(bg='#67E6DC') - change bg color

    def getpngfile():- defining function to convert
        
        file_location=fd.askopenfilename() - dialog box to find 
                                             the path
        pic=Image.open(file_location) 

        pic=pic.convert('RGB') - converting to rgb form 
        
    
        export_file_location = fd.asksaveasfilename(defaultextension='.jpg',filetypes= [('Image ( file)','*.jpg')] ) - saving converted 
                             image 

        pic.save(export_file_location)  

def jpgtopdf(): - defineing function
    
    def getjpgfile(): - defineing function to convert
        
        file_path = fd.askopenfilename()- dialog box to find 
                                          the path
        img=Image.open(file_path)
    
        img.save(fd.asksaveasfilename(defaultextension='.pdf',filetypes= [("pdf files" ,'*.pdf')] )) - saving converted 
                             image 

def pngtopdf(): - defining function
   
    def getpngfile(): - defing function to convert

        img=Image.open(fd.askopenfilename()) - dialog box to 
                                               find the path

        Img=img.convert('RGB') - converting to rgb form 

        Img.save(fd.asksaveasfilename(defaultextension='.pdf',filetypes= [("pdf files" ,'*.pdf')] )) - saving converted 
                             image 


def texttopdf(): - defining functon

    
    def txttopdf(): - defing function to convert

        a=open(fd.askopenfilename()) - dialog box to find 
                                          the path
        

        pdf=FPDF() - asigning fpdf to a variable

        pdf.add_page() - adding pages

        pdf.set_font("Arial",size=12) - seting default font

        for i in a:
            pdf.cell(200,10,txt=i,ln=1,align='L') - looping function to 
                                                    convert every line in text file to pdf

        b=fd.asksaveasfilename(defaultextension='.pdf',filetypes= [("pdf files" ,'*.pdf')] ) - saving pdf 

        pdf.output(b)

THIS FUNCTION REMAINS SAME FOR ALL BUTTON EXCEPT THE PUTTON NAME


def jtopenter(event): - defing fuction to convert bg and fg of the 
                        button when mouse point enters

    jtop.config(bg='black',fg='white') - configuring 

def jtopleave(event): - defing fuction to convert bg and fg of the 
                        button when mouse point enters
    
    jtop.config(bg='white',fg='black') - configuring 


Adding details to the window

root=Tk()
root.title('File Format Converter')
root.config(bg='white')

root.state('zoomed')

ADDING BUTTONS FRAMES AND HEADING TO TKINTER WINDOW

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

sbar=Label(text='By Sriram k.v',font='Helvetica 10 bold',relief=SUNKEN,anchor='w',padx=10) - Status Bar

sbar.pack(side=BOTTOM,fill=X)

root.mainloop() - loop to run it continuously


DEVELOPER CONTACT: sriramvkumar007@gmail.com
for any comments and sugesstion please contact me
