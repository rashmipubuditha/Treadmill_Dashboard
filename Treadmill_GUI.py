from tkinter import *
from tkinter import messagebox
import calculation as clc
from PIL import Image,ImageTk
from datetime import date
import time
from tkcalendar import*

time_sec = 1
time_seconds = 1
time_min = 0
rpm = 0
speed = 0
radius_m = 0
height_m = 0
weight_kg = 0
height=0
weight=0
radius=0
gender = 0 #men
age = 0 

# Create time,date variables
today = date.today()
hour = time.strftime("%I")
minute = time.strftime("%M")
second = time.strftime("%S")
am_pm = time.strftime("%p")

Date = today.strftime("%A - %d %B %Y")
Date_ = today.strftime('%x')
Time = hour+":"+minute+":"+second+" "+am_pm

def operation_1():
    # Check that all inputs are in correct format
    if Entry.get(E0)=='' or Entry.get(E1)=='' or Entry.get(E2)=='' or Entry.get(E3)=='' or Entry.get(E5)=='':
        messagebox.showerror('ERROR FOUND', "You didn't complete input boxes")
    else:
        try:
            global rpm
            rpm = float(Entry.get(E0))
        except:
            messagebox.showerror('ERROR FOUND','Please check inputs for RPM')
        try:
            global radius
            radius = float(Entry.get(E1))
        except:
            messagebox.showerror('ERROR FOUND', 'Please check inputs for Shaft radius')
        try:
            global height
            height = float(Entry.get(E2))
        except:
            messagebox.showerror('ERROR FOUND', 'Please check inputs for Height')
        try:
            global weight
            weight = float(Entry.get(E3))
        except:
            messagebox.showerror('ERROR FOUND', 'Please check inputs for Weight')
        try:
            global age
            age = float(Entry.get(E5))
        except:
            messagebox.showerror('ERROR FOUND', 'Please check inputs for Age')

        # Get permission for further process
        if radius==0 or height==0 or weight==0 or rpm<0 or radius<0 or height<0 or weight<0 or age<=0 :
            messagebox.showerror('ERROR FOUND', 'Please check inputs')
        else:
            global button1,button2,button3,button4,button5
        
            # Enabale disabled buttons
            
            button1['state'] = 'normal'
            button2['state'] = 'normal'
            button3['state'] = 'normal'
            button5['state'] = 'normal'

            # Convert input units
            global radius_m
            global height_m
            global weight_kg
            global gender
            if clicked1.get()=='____meter (m)___':
                radius_m = radius
            elif clicked1.get()=='_centimeter (cm)':
                radius_m = radius/100
            else:
                radius_m = radius*0.0254
            if clicked2.get() == '____meter (m)___':  
                height_m = height
            elif clicked2.get() == '_centimeter (cm)':
                height_m = height / 100
            else:
                height_m = height * 0.0254
            if clicked3.get()=='kilogrammes (kg)':
                weight_kg = weight
            else:
                weight_kg = weight*0.453592

            if height_m>3:
                response = messagebox.askyesno('HEIGHT ERROR', 'Height is more than 3m. Are you sure you want to continue programme')
                if response == 1:
                    operation_2()
                else:
                    return
            else:
                operation_2()
            if clicked4.get() == 'Male':
                gender = 0
            else:
                gender = 1

# Loop operating happen hear
distance = 0
calories = 0
steps = 0

def operation_2():
    global upordown,time_seconds,time_sec,time_min,runornot,button0,button1,button3,speed,new_speed,radius_m,height_m,weight_kg,reset,distance,calories,steps

    # Check that reset putton was pushed or not
    if reset == 'no':

        # Check that speed up or down button was pushed or not
        if upordown == 'normal':
            # Calculate nesscery outputs without increasing or decreasing speed
            distance += clc.distancecalc(rpm, radius_m, 1)
            speed = clc.speedcalc(rpm, radius_m) * 3.6
            new_speed = speed
            # Speed down button disable or enable
            if new_speed < 0.5:
                button3['state'] = 'disabled'
            else:
                button3['state'] = 'normal'

            calories += clc.caloriescalc(gender,weight_kg, height_m, rpm,radius_m, 1,age)
            steps += clc.stepscalc(height_m, rpm, radius_m, 1)

            # Show outputs on suitable labels
            label1.config(text='%.2f' % (distance / 1000))
            label2.config(text=str(time_min).zfill(2) + ' : ' + str(time_seconds).zfill(2))
            label3.config(text='%.2f' % speed)
            label4.config(text='%.2f' % calories)
            label5.config(text='%d' % steps)

            # Analys the time
            time_sec += 1
            time_seconds += 1
            if time_seconds == 60:
                time_min += 1
                time_seconds = 1

            # Check that pause button was pushed or not
            if runornot == 'run':
                label1.after(1000, operation_2)

                button0['state'] = 'disabled'
                button1['state'] = 'normal'
            # If pause button pushed
            else:
                runornot = 'run'
                button0['state'] = 'normal'
                button1['state'] = 'disabled'

        # If speed up or button pused
        else:

            global new_rpm
            if new_speed < 0.5:
                button3['state'] = 'disabled'
            else:
                button3['state'] = 'normal'

            # Calculate nesscery outputs when increasing or decreasing speed
            distance += clc.distancecalc(new_rpm, radius_m, 1)
            calories += clc.caloriescalc(gender,weight_kg, height_m, new_rpm,radius_m,1,age)
            steps += clc.stepscalc(height_m, new_rpm, radius_m, 1)

            # Show outputs on suitable labels
            label1.config(text='%.2f' % (distance / 1000))
            label2.config(text=str(time_min).zfill(2) + ' : ' + str(time_seconds).zfill(2))
            label3.config(text='%.2f' % new_speed)
            label4.config(text='%.2f' % calories)
            label5.config(text='%d' % steps)

            # Analys the time
            time_sec += 1
            time_seconds += 1
            if time_seconds == 60:
                time_min += 1
                time_seconds = 1

            # Check that pause button was pushed or not
            if runornot == 'run':
                label1.after(1000, operation_2)

                button0['state'] = 'disabled'
                button1['state'] = 'normal'
            # If pause button pushed
            else:
                runornot = 'run'
                button0['state'] = 'normal'
                button1['state'] = 'disabled'

    # If reset button pushed
    else:
        reset = 'no'
        E0.delete(0,END)
        E1.delete(0,END)
        E2.delete(0,END)
        E3.delete(0,END)
        label1.config(text=' ------ ')
        label2.config(text=' -- : --')
        label3.config(text=' ------ ')
        label4.config(text=' ------ ')
        label5.config(text=' ------ ')
        
        # Define buttons
        # Show buttons on the frame2
        button0['state'] = 'normal'
        button1['state'] = 'disabled'
        button2['state'] = 'disabled'
        button3['state'] = 'disabled'    
        button5['state'] = 'disabled'

# Function for pause button
runornot = 'run'
def paused(value):
    global runornot
    runornot = value

# Function for speed up and down buttons
upordown = 'normal'
new_speed = 0
new_rpm = 0
def speedv(value):
    global upordown
    global new_speed
    global speed
    if value=='inc':
        new_speed=new_speed+0.5
        upordown = 'inc'
    elif value=='dec':
        new_speed=new_speed-0.5
        upordown = 'dec'
    global new_rpm
    global radius_m
    new_rpm = clc.new_motor_variable(new_speed, radius_m)

# Function for reset button
reset = 'no'
def resetpro():
    global calories, steps, distance,Date,Time
    response = messagebox.askyesno('RESET', 'Would you want to rest all?')
    if response == 1:
        global reset,radius_m,height_m,weight_kg,distance,calories,steps,speed,rpm,time_sec,time_min,time_seconds,height,weight,radius
        reset = 'yes'
        E0.delete(0, END)
        E1.delete(0, END)
        E2.delete(0, END)
        E3.delete(0, END)
        label1.config(text=' ------ ')
        label2.config(text=' -- : --')
        label3.config(text=' ------ ')
        label4.config(text=' ------ ')
        label5.config(text=' ------ ')

        # File handling part (saving part)
        file = open('data/history.txt','a')
        
        calories= str(round(calories))
        steps = str(round(steps))
        distance = str(round(distance/1000,2))
        time_min = str(time_min)
        time_seconds=str(time_seconds)
            
        file.write(Date_+','+
                        Date+','+
                        Time+','+
                        'Burnt Calories = '+ calories +','+
                        'Number of steps = '+ steps +','+
                        'Distance = '+ distance+' km'+','+
                        'Duration = '+ time_min +' min'+":"+ time_seconds +' sec'+','+
                        '*'*50+'\n')

        file.close()
        time_sec = 1
        time_seconds = 1
        time_min = 0
        rpm,speed,radius_m,height_m = 0,0,0,0
        height,weight,radius=0,0,0
        weight_kg = 0
        distance = 0
        calories = 0
        steps = 0
        
        # Define buttons
        # Show buttons on the frame2
        button0['state'] = 'normal'
        button1['state'] = 'disabled'
        button2['state'] = 'disabled'
        button3['state'] = 'disabled'
        
        button5['state'] = 'disabled'

        

# Create the interface
window = Tk()
window.title("Treadmill Dashboard")
window.iconbitmap('images/icon.ico')
window.configure(background='black')
load = Image.open('images\\w2.jpg')
render = ImageTk.PhotoImage(load)
img = Label(window,image = render)
img.place(x=0,y=0)
window.geometry('1000x670')

# Font types
font1 = ('Times',10,'bold')
font2 = ('Times',13,'bold')
font3 = ('Times',16,'bold')
font4 = ('Times',20,'bold')
font5 = ('Times',25,'bold')

## Create Menu bar
my_menu = Menu(window)
window.config(menu=my_menu)

# click command for menu bar
def history():
    global today
    #Create 2nd GUI window
    top = Toplevel()
    top.title("Treadmill Dashboard")
    top.iconbitmap('images/icon.ico')
    
    #create frames for top window
    fr1 =LabelFrame(top)
    fr2 =LabelFrame(top)
    #Show them
    fr1.grid(row=0,column=0,padx=10,pady=10)
    fr2.grid(row=1,column=0,padx=10,pady=10)
    
    def grab_date():
        count=0
        my_text.delete('1.0','end')
        string1 = 1
        string2 = 2
        selectdate = calendar.get_date()
        file= open('data/history.txt','r')
        for line in file:
            linelst = line.split(',')
            string = str(linelst[0])
            if string[0]=='0':
                string1 = string[1:]
                string2 = string
                if string1 == selectdate or string2 == selectdate:
                    for part in linelst[1:]:
                        my_text.insert(END,part+'\n')
                        count+=1
        if count==0:
                    my_text.insert(END,'No data'+'\n')

        file.close()
        
    but1 = Button(fr1,text='Select',command=grab_date)
    but1.grid(row=1,column=1)

    lab1 = Label(fr1,text='Select the date')
    lab1.grid(row=1,column=0)
    # Create calendar
    calendar = Calendar(fr1,selectmode="day",year=2021,month=3,day=int(today.strftime('%d')))
    calendar.grid(row=0,padx=10,pady=5)
    
    # Create text box
    my_text = Text(fr2,width=40,height=10,font=('Times',13))
    my_text.grid(row=0)
    
       
def clear():
    open('data/history.txt','w')
    
    
# Create a menu item
file_menu = Menu(my_menu,bg='#ECF0F1')
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='Open History',command=history)
file_menu.add_command(label='Clear History',command=clear)
file_menu.add_command(label='Close',command=exit)

# Function to set up the window with the background image
def setup_window_with_background(window, image_path):
    # Load the image
    bg_image = Image.open(image_path)
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Create a label with the background image
    bg_label = Label(window, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set up the background image
setup_window_with_background(window, "images/bck.jpg")

# Create frames
frame0 = LabelFrame(window,text='------TREADMILL DASHBOARD------',fg='navy',font=font5,padx=10,pady=10) # frame for inputs
frame1 = LabelFrame(frame0 ,text='INPUT DATA',fg='darkblue',bg ="lightgray",font=font3,padx=10,pady=10) # frame for inputs
frame2 = LabelFrame(frame0 ,text='OUTPUT',fg='darkblue',bg='lightgray',font=font3,padx=10,pady=10) # frame for outputs
frame3 = LabelFrame(frame0 ,font = font3, text='CHOOSE YOUR INPUT UNIT FORMAT',bg='lightgray',fg='darkblue',padx=10,pady=10) # frame for units
frame4 = LabelFrame(frame0,padx=10,pady=10) # frame for speed up and down button


# Show frames onthe screen
frame0.grid(row=1,padx=10,pady=10)
frame1.grid(row=2,padx=10,pady=10)
frame2.grid(row=3,padx=10,pady=10)
frame3.grid(row=0,padx=10,pady=10)
frame4.grid(row=4,padx=10,pady=10)

# Lables for input boxes
L0 = Label(frame1,text="Motor Speed (RPM)",font=font2,padx=30,pady=10)
L1 = Label(frame1,text="Radius of the shaft",font=font2,padx=30,pady=10)
L2 = Label(frame1,text="Your Height",font=font2,padx=30,pady=10)
L3 = Label(frame1,text="Your Weight",font=font2,padx=50,pady=10)
L5 = Label(frame1,text="Your Age",font=font2,padx=40,pady=10)


# Show input label on the frame1
L0.grid(row=1,column=0)
L1.grid(row=1,column=1)
L2.grid(row=1,column=2)
L3.grid(row=1,column=3)
L5.grid(row=1,column=5)

# Drop boxes labels
drop1L = Label(frame3,text="RADIUS",font=font2,padx=10,pady=10)
drop2L = Label(frame3,text="HEIGHT",font=font2,padx=10,pady=10)
drop3L = Label(frame3,text="WEIGHT",font=font2,padx=10,pady=10)
drop4L = Label(frame3,text="GENDER",font=font2,padx=10,pady=10)

#Show Drop boxes labels on the frame 3
drop1L.grid(row=1,column=0)
drop2L.grid(row=1,column=1)
drop3L.grid(row=1,column=2)
drop4L.grid(row=1,column=3)

# Drop boxes
clicked1 = StringVar()
clicked1.set('Meter (m)')
clicked2 = StringVar()
clicked2.set('Meter (m)')
clicked3 = StringVar()
clicked3.set('Kilo grammes (kg)')
clicked4 = StringVar()
clicked4.set('Male')

drop1 = OptionMenu(frame3,clicked1,'Meter (m)','Centimeter (cm)',' Inches (in)')
drop2 = OptionMenu(frame3,clicked2,'Meter (m)','Centimeter (cm)','Inches (in)')
drop3 = OptionMenu(frame3,clicked3,'Kilo grammes (kg)','Pounds (lb)')
drop4 = OptionMenu(frame3,clicked4,'Male','Female')

drop1.config(font=font1,padx=10,pady=10, bg='purple',fg = 'white')
drop2.config(font=font1,padx=10,pady=10, bg='purple',fg = 'white')
drop3.config(font=font1,padx=10,pady=10, bg='purple',fg = 'white')
drop4.config(font=font1,padx=10,pady=10, bg='purple',fg = 'white')

# Show drop boxes on the frame3
drop1.grid(row=2,column=0)
drop2.grid(row=2,column=1)
drop3.grid(row=2,column=2)
drop4.grid(row=2,column=3)

# Define input boxes
E0 = Entry(frame1,bd=5) # box to take the RPM value
E1 = Entry(frame1,bd=5) # box to take the radius
E2 = Entry(frame1,bd=5) # box to take the height
E3 = Entry(frame1,bd=5) # box to take the weight
E5 = Entry(frame1,bd=5) # box to take the age

# Show input boxes on the frame1
E0.grid(row=2,column=0,padx=5,pady=5)
E1.grid(row=2,column=1,padx=5,pady=5)
E2.grid(row=2,column=2,padx=5,pady=5)
E3.grid(row=2,column=3,padx=5,pady=5)
E5.grid(row=2,column=5,padx=5,pady=5)

# Lables for outputs
L4 = Label(frame2,text="DISTANCE (km)",font=font3,padx=20)
L5 = Label(frame2,text="TIME (min:sec)",font=font3,padx=20)
L6 = Label(frame2,text="SPEED (km/h)",font=font3,padx=20)
L7 = Label(frame2,text="CALORIES",font=font3,padx=30)
L8 = Label(frame2,text="STEPS",font=font3,padx=20)

# Show output label on the frame2
L4.grid(row=0,column=0)
L5.grid(row=0,column=1)
L6.grid(row=0,column=2)
L7.grid(row=0,column=3)
L8.grid(row=0,column=4)

# Define output lables
label1 = Label(frame2,text='  ',font=font3,padx=20) # box for distance
label2 = Label(frame2,text='  ',font=font3,padx=20) # box for time
label3 = Label(frame2,text='  ',font=font3,padx=20) # box for speed
label4 = Label(frame2,text='  ',font=font3,padx=20) # box for calories
label5 = Label(frame2,text='  ',font=font3,padx=20) # box for steps

# Show output boxes on the frame2
label1.grid(row=1,column=0,padx=10,pady=10)
label2.grid(row=1,column=1,padx=10,pady=10)
label3.grid(row=1,column=2,padx=10,pady=10)
label4.grid(row=1,column=3,padx=10,pady=10)
label5.grid(row=1,column=4,padx=10,pady=10)

# Define buttons
stimg = PhotoImage(file = 'images\\start.png')
button0 = Button(frame4,image = stimg,bd=0,font=font5,command = operation_1)
psimg = PhotoImage(file = 'images\\pause.png')
button1 = Button(frame4,image =psimg ,bd =0,font=font5,state='disabled',command=lambda: paused('paused'))
upimg = PhotoImage(file = 'images\\up.png')
button2 = Button(frame4,image = upimg,bd =0,font=font5,state='disabled',command=lambda: speedv('inc'))
dwimg = PhotoImage(file = 'images\\down.png')
button3 = Button(frame4,image = dwimg,bd =0,font=font5,state='disabled',command=lambda: speedv('dec'))
rtimg = PhotoImage(file = 'images\\reset.png')
button5 = Button(frame4,image = rtimg,bd=0,font=font5,state='disabled',command=resetpro)

# Show buttons on the frame2
button0.grid(row=4,column=0,padx=10)
button1.grid(row=4,column=1,padx=10)
button2.grid(row=4,column=2,padx=10)
button3.grid(row=4,column=3,padx=10)
button5.grid(row=4,column=4,padx=10)

def datetime():
    today = date.today()
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    Date = today.strftime("%A - %d %B, %Y")
    Time = hour+":"+minute+":"+second+" "+am_pm
    status.config(text=Date+' - '+Time)
    status.after(1000,datetime)
    
# Status bar
status = Label(window,text='',bg='lightgray',bd=2,relief=SUNKEN,anchor=CENTER,padx=10)
# status.grid(row=3,sticky=W+E)

datetime()

window.mainloop()
