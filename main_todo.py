# om ganganpatay namah
# jai shri ram
# har har mahadev
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

def save():
  file_name=filedialog.asksaveasfilename(
    title="save file",
    filetypes=(("Dat files","*.dat"),("All","*.*"))
  )#we can set initialdir="path of folder" also
  if file_name:
    if file_name.endswith(".dat"):
      pass
    else:
      file_name=f"{file_name}.dat"
    # deleting cross_offed item before saving
    count=0
    while count<my_list.size():
      if my_list.itemcget(count,"fg")=="#dedede":
        #itemcget to get some properties of some item
        my_list.delete(my_list.index(count))
      else:
        count+=1
    stuff=my_list.get(0,END)
    with open(f"{file_name}","wb") as output:
      pickle.dump(stuff,output)
  
def open_():
  file_name=filedialog.askopenfilename(
    title="save file",
    filetypes=(("Dat files","*.dat"),("All","*.*"))
  )
  print(file_name)
  if file_name:
    my_list.delete(0,END)
    with open(file_name,"rb") as input:
      stuff=pickle.load(input)
      # The error "_pickle. UnpicklingError: invalid load key, '\xef'" typically occurs when trying to unpickle data that has been corrupted or improperly formatted 1.
    for i in stuff:
      my_list.insert(END,i)#END means inserting at the end of the list
def clear():
  my_list.delete(0,END)

def delete():
  my_list.delete(ANCHOR)# Any item that is selected can be referred to as 'ANCHOR'.

def add():
  my_list.insert(0,my_entry.get())# to fix at starting else END
  my_entry.delete(0,END)

def crossoff():
  my_list.itemconfig(
    my_list.curselection(),
    fg="#dedede"
  )
  my_list.select_clear(0,END)

def uncrossoff():
  my_list.itemconfig(
    my_list.curselection(),
    fg="#464646"
  )
  my_list.select_clear(0,END)
def delete_crossedoff():
  count=0
  while count<my_list.size():
    if my_list.itemcget(count,"fg")=="#dedede":
      #itemcget to get some properties of some item
      my_list.delete(my_list.index(count))
    else:
      count+=1

root=Tk()
root.title("Todo app")
root.geometry("500x500")
# defining the  font
font=Font(
  family="MorganChalk-L3aJy.ttf",
  size=30,
  weight="bold"
)
my_frame=Frame(root)
my_frame.pack()

#creating the menu
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="save",command=save)
file_menu.add_separator()
file_menu.add_command(label="open_",command=open_)
file_menu.add_separator()
file_menu.add_command(label="clear",command=clear)

# creating the list box

my_list=Listbox(
  my_frame,
  font=font,
  height=5,
  width=25,
  bg="white",
  bd=0,
  fg="#464646",
  highlightthickness=0,
  selectbackground="blue",
  activestyle="none",
)
my_list.pack(side=LEFT,fill=BOTH)

Scrollbar=Scrollbar(my_frame)
Scrollbar.pack(side=RIGHT,fill=BOTH)
my_list.config(yscrollcommand=Scrollbar.set)
Scrollbar.config(command=my_list.yview)

my_entry=Entry(root)
my_entry.pack(pady=20)

button_frame=Frame(root)
button_frame.pack(pady=20)

delete_button=Button(button_frame,text="delete",command=delete)
delete_button.grid(row=0,column=0)
add_button=Button(button_frame,text="add",command=add)
add_button.grid(row=0,column=1)
cross_off_button=Button(button_frame,text="cross_off",command=crossoff)
cross_off_button.grid(row=0,column=2)
uncross_button=Button(button_frame,text="uncross",command=uncrossoff)
uncross_button.grid(row=0,column=3)
delete_crossed_button=Button(button_frame,text="delete_crossed",command=delete_crossedoff)
delete_crossed_button.grid(row=0,column=4)


root.mainloop()