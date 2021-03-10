import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
# Main application begin's

application=tk.Tk()
application.geometry('1200x800')
application.title('MyPersonal Text Editor')
#......................................Main Menu ...........................
main_menu=tk.Menu(application)
#file
new_icon=tk.PhotoImage(file='icons/new_1.png')
open_icon=tk.PhotoImage(file='icons/open_1.png')
save_icon=tk.PhotoImage(file='icons/save_1.png')
saveas_icon=tk.PhotoImage(file='icons/saveas_1.png')
exit_icon=tk.PhotoImage(file='icons/exit_1.png')
file=tk.Menu(main_menu,tearoff=0)

#edit-copy,paste,cut,clearall,paste
cut_icon=tk.PhotoImage(file='icons/scissors_1.png')
copy_icon=tk.PhotoImage(file='icons/copy_1.png')
paste_icon=tk.PhotoImage(file='icons/paste_1.png')
clear_icon=tk.PhotoImage(file='icons/rubber_1.png')
find_icon=tk.PhotoImage(file='icons/search_1.png')
edit=tk.Menu(main_menu,tearoff=0)

#View-Toolbar,StatusBAr
toolbar_icon=tk.PhotoImage(file='icons/toolbar.png')
statusbar_icon=tk.PhotoImage(file='icons/setting.png')
view=tk.Menu(main_menu,tearoff=0)

#Colour Theme
light_default=tk.PhotoImage(file='icons/theme.png')
dark=tk.PhotoImage(file='icons/theme.png')
red=tk.PhotoImage(file='icons/theme.png')
color_theme=tk.Menu(main_menu,tearoff=0)
theme_choice=tk.StringVar()
color_icons=(light_default,dark,red)
color_dict={
    'Light_default':{'#000000','#ffffff'},
    'Dark':{'#c4c4c4','#2d2d2d'},
    'Red':{'#2d2d2d','#ffe848'}
}
count=0
#cascading submenues in main_menu
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Theme",menu=color_theme)

#.......................................End of main Menu....................



#......................................Toolbar..............................
tool_bar=ttk.Label(application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
#Font Box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)
#Size Box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

# button
bold_icon=tk.PhotoImage(file='icons/bold-button.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

italic_icon=tk.PhotoImage(file='icons/italic-button.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

underline_icon=tk.PhotoImage(file='icons/underline-button.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

font_icon=tk.PhotoImage(file='icons/font.png')
font_btn=ttk.Button(tool_bar,image=font_icon)
font_btn.grid(row=0,column=5,padx=5)

left_icon=tk.PhotoImage(file="icons/left-align.png")
right_icon=tk.PhotoImage(file="icons/right1.png")
centre_icon=tk.PhotoImage(file="icons/centre.png")
left_bttn=ttk.Button(tool_bar,image=left_icon)
left_bttn.grid(row=0,column=6,padx=5)
right_bttn=ttk.Button(tool_bar,image=right_icon)
right_bttn.grid(row=0,column=7,padx=5)
centre_bttn=ttk.Button(tool_bar,image=centre_icon)
centre_bttn.grid(row=0,column=8,padx=5)
#......................................End of toolbar........................

#.......................................Text Editor............................
text_editor=tk.Text(application)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

                                                       #font family and font size functionality
current_font_family='Arial'
current_font_size=12
#current_font_weight='normal'
def change_font(application):   #we r passing application as an argument just because of bind function
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_size(application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)

                                                           #buttons functionality

# print(tk.font.Font(font=text_editor['font']).actual()) This command gives an object of deatils of text_editor
#Bold button functionality
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_btn.configure(command=change_bold)
#Itallic button functionality
def change_slant():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

italic_btn.configure(command=change_slant)

#Underline button functionality

def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_btn.configure(command=change_underline)

#font colour functionality

def change_font_color():
    color_var=tk.colorchooser.askcolor()
    # print(color_var)#returns tuble of colour details
    text_editor.configure(fg=color_var[1])
font_btn.configure(command=change_font_color)

#Align functionality
def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
left_bttn.configure(command=align_left)

def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
right_bttn.configure(command=align_right)

def align_centre():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('centre',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'centre')
centre_bttn.configure(command=align_centre)


text_editor.configure(font=('Arial',12))


# print(tk.font.Font(font=text_editor['font']).actual())
#.......................................End of Text Editor.....................

#......................................Main Status BAr.........................
status_bar=tk.Label(application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)


def changed(event=None):
    if text_editor.edit_modified():
        words=len(text_editor.get(1.0,'end-1c').split())
        ch=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f"Characters : {ch}          Words: {words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",changed)

#.......................................End of Status Bar.......................


#..........................................Main Menu Functionality..................
#file menu commands
file.add_command(label="New",image=new_icon,compound=tk.LEFT)
file.add_command(label="Open",image=open_icon,compound=tk.LEFT)
file.add_command(label="Save",image=save_icon,compound=tk.LEFT)
file.add_command(label="Save As",image=saveas_icon,compound=tk.LEFT)
file.add_command(label="Exit",image=exit_icon,compound=tk.LEFT)

#edit menu commands
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT)
edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT)
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT)
edit.add_command(label="Clear All",image=clear_icon,compound=tk.LEFT)
edit.add_command(label="Find",image=find_icon,compound=tk.LEFT)

#view menu commands
view.add_checkbutton(label="Toolbar",image=toolbar_icon,compound=tk.LEFT)
view.add_checkbutton(label="Status Bar",image=statusbar_icon,compound=tk.LEFT)

#theme commands
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT)
    count=count+1





#..........................................End Main Menu ...........................



application.config(menu=main_menu)
application.mainloop()

