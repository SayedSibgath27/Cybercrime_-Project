import pandas as pd
import random
from tkinter import*
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.filedialog import askopenfilename
def uploadfile():
    
    path=askopenfilename(initialdir="",
                         filetypes=(("txtfile","*.txt"),("allfile","*.*")),
                         title="Choose a file")
    print(path)
    name=path.split('/')
    #print(name)
    filename1=name[-1]
    print(filename1)
    filename.configure(text=filename1)
    #Find put the suspicios and nonsuspicious word
    #import cybercrimedatabase
    import pandas as pd
    cybercrimedata=pd.read_excel('C:\\Users\\HP Elitebook G6\\Desktop\\Python\\cybercrimeproject\\cybercrimedatabase.xlsx')
    print(cybercrimedata)
    cyberword=cybercrimedata['Mword']
    print(cyberword)
    cybercrimeword_list=list(cyberword)
    print(cybercrimeword_list)
    #Create a list of all the useres word 
    file=open(path)
    userdata=file.read()
    userdata_list=userdata.split()
    print(userdata_list)
    
    
    ns=0
    s=0
    tw=len(userdata_list)
    #Compair both data
    for i in cybercrimeword_list:
        for j in userdata_list:
         if i.lower()==j.lower():
            s=s+1
            ns=tw-s
            print(s)
            print(ns)
            slable.configure(text="Suspicous word found="+str(s),fg='red')
            nlable.configure(text="Non Suspicous word found="+str(ns),fg='Green')
            
            #draw the Scatter Plot Graph
            figure=plt.Figure(figsize=(6,5),dpi=100)
            ax=figure.add_subplot()
            bargraph=FigureCanvasTkAgg(figure,w)
            Graph=bargraph.get_tk_widget()
            Graph.place(x=700, y=160)
            nx=[]
            ny=[]
            for i in range(ns):
                nx.append(random.randint(1, 10))
                ny.append(random.randint(1, 10))
            df=pd.DataFrame({'nx':nx,'ny':ny})
            df.plot.scatter(x='nx', y='ny', color="blue",legend=True,ax=ax)

            sx=[]
            sy=[]
            for i in range(s):
                sx.append(random.randint(1, 10))
                sy.append(random.randint(1, 10))
            df=pd.DataFrame({'sx':sx,'sy':sy})
            df.plot.scatter(x='sx', y='sy', color="red",legend=True,ax=ax)
w=Tk()

w.geometry('1550x1550')
heading=Label(w,text="Cyber Crime Application", font=300, fg="red")
heading.place(x=700,y=40)
upload_BTW=Button(w,text='Upload Userfile', font=200,bg='grey',fg='Dark blue',command=uploadfile)
upload_BTW.place(x=750,y=80)


filename=Label(w,text='Upload Userfile', font=200,fg='Dark blue')
filename.place(x=800,y=140)

slable=Label(w,text="Suspiciousword:- No data found", font=300, fg="black")
slable.place(x=200,y=250)

nlable=Label(w,text="NONSuspiciousword:- No data found", font=300, fg="black")
nlable.place(x=200,y=300)



w.mainloop()

