from customtkinter import *
from tkinter import *
from tkinter import filedialog,messagebox
import subprocess as sp
import os
import re



# class TextLineNumbers(CTk.CTkCanvas):
#     def __init__(self, *args, **kwargs):
#         CTk.CTkCanvas.__init__(self, *args, **kwargs)
#         self.textwidget = None

#     def attach(self, text_widget):
#         self.textwidget = text_widget
        
#     def redraw(self, *args):
#         '''redraw line numbers'''
#         self.delete("all")

#         i = self.textwidget.index("@0,0")
#         while True :
#             dline= self.textwidget.dlineinfo(i)
#             if dline is None: break
#             y = dline[1]
#             linenum = str(i).split(".")[0]
#             self.create_text(2,y,anchor="nw", text=linenum)
#             i = self.textwidget.index("%s+1line" % i)

# class CustomText(CTk.CTkTextbox):
#     def __init__(self, *args, **kwargs):
#         CTk.CTkTextbox.__init__(self, *args, **kwargs)

#         # create a proxy for the underlying widget
#         self._orig = self._w + "_orig"
#         self.CTk.call("rename", self._w, self._orig)
#         self.CTk.createcommand(self._w, self._proxy)

#     def _proxy(self, *args):
#         # let the actual widget perform the requested action
#         cmd = (self._orig,) + args
#         result = self.tk.call(cmd)

#         # generate an event if something was added or deleted,
#         # or the cursor position changed
#         if (args[0] in ("insert", "replace", "delete") or 
#             args[0:3] == ("mark", "set", "insert") or
#             args[0:2] == ("xview", "moveto") or
#             args[0:2] == ("xview", "scroll") or
#             args[0:2] == ("yview", "moveto") or
#             args[0:2] == ("yview", "scroll")
#         ):
#             self.event_generate("<<Change>>", when="tail")
#             self.event_generate("<Configure>", when="tail")

#         # return what the actual widget returned
#         return result
    
# class Example(CTk.CTkFrame):
#     def __init__(self, *args, **kwargs):
#         CTk.CTkFrame.__init__(self, *args, **kwargs)
#         self.text = CustomText(self)
#         # self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
#         # self.text.configure(yscrollcommand=self.vsb.set)
#         # self.text.tag_config("bigfont", font=("Helvetica", "24", "bold"))
#         self.linenumbers = TextLineNumbers(self, width=30)
#         self.linenumbers.attach(self.text)

#         # self.vsb.pack(side="right", fill="y")
#         self.linenumbers.pack(side="left", fill="y")
#         self.text.pack(side="right", fill="both", expand=True)

#         self.text.bind("<<Change>>", self._on_change)
#         self.text.bind("<Configure>", self._on_change)


#     def _on_change(self, event=None):
#         self.linenumbers.redraw()







# class TextLineNumbers(tk.Canvas):
#     def __init__(self, *args, **kwargs):
#         tk.Canvas.__init__(self, *args, **kwargs)
#         self.textwidget = None

#     def attach(self, text_widget):
#         self.textwidget = text_widget
        
#     def redraw(self, *args):
#         '''redraw line numbers'''
#         self.delete("all")

#         i = self.textwidget.index("@0,0")
#         while True :
#             dline= self.textwidget.dlineinfo(i)
#             if dline is None: break
#             y = dline[1]
#             linenum = str(i).split(".")[0]
#             self.create_text(2,y,anchor="nw", text=linenum)
#             i = self.textwidget.index("%s+1line" % i)

# class CustomText(tk.Text):
#     def __init__(self, *args, **kwargs):
#         tk.Text.__init__(self, *args, **kwargs)

#         # create a proxy for the underlying widget
#         self._orig = self._w + "_orig"
#         self.tk.call("rename", self._w, self._orig)
#         self.tk.createcommand(self._w, self._proxy)

#     def _proxy(self, *args):
#         # let the actual widget perform the requested action
#         cmd = (self._orig,) + args
#         result = self.tk.call(cmd)

#         # generate an event if something was added or deleted,
#         # or the cursor position changed
#         if (args[0] in ("insert", "replace", "delete") or 
#             args[0:3] == ("mark", "set", "insert") or
#             args[0:2] == ("xview", "moveto") or
#             args[0:2] == ("xview", "scroll") or
#             args[0:2] == ("yview", "moveto") or
#             args[0:2] == ("yview", "scroll")
#         ):
#             self.event_generate("<<Change>>", when="tail")

#         # return what the actual widget returned
#         return result
    
# class Example(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         self.text = CustomText(self)
#         self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
#         self.text.configure(yscrollcommand=self.vsb.set)
#         self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
#         self.linenumbers = TextLineNumbers(self, width=30)
#         self.linenumbers.attach(self.text)

#         self.vsb.pack(side="right", fill="y")
#         self.linenumbers.pack(side="left", fill="y")
#         self.text.pack(side="right", fill="both", expand=True)

#         self.text.bind("<<Change>>", self._on_change)
#         self.text.bind("<Configure>", self._on_change)

#         self.text.insert("end", "one\ntwo\nthree\n")
#         self.text.insert("end", "four\n",("bigfont",))
#         self.text.insert("end", "five\n")

#     def _on_change(self, event):
#         self.linenumbers.redraw()





# class MyTabView(customtkinter.CTkTabview):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         # create tabs
#         name = " "*10 + "tab 1"+" "*10
#         name2 = " "*10 + "tab 2"+" "*10
#         self.add(name)
#         self.add(name2)
#         name3 = " "*10 + "tab 3"+" "*10
#         name4 = " "*10 + "tab 4"+" "*10
#         self.add(name3)
#         self.add(name4)
#         name5 = " "*10 + "tab 5"+" "*10
#         name6 = " "*10 + "tab 6"+" "*10
#         self.add(name5)
#         self.add(name6)

#         # add widgets on tabs
#         self.label = customtkinter.CTkLabel(master=self.tab(name))
#         self.label.grid(row=0, column=0, padx=20, pady=10)




class PythonEditor:
    def __init__(self):
        self.app = CTk()
        self.width = 1380
        self.height = 670
        self.fontSize = 14
        self.undo_stack = []
        self.redo_stack = []
        self.path = ""
        self.folder_path = "" 
        self.fontName = "Consolas"  
        # self.MenuFrame = Frame()
        self.textframe = Frame(self.app)
        self.MenuFrame = Frame(self.app,background="#333")
        self.MenuFrame.place(x=0,y=0,width=self.width,height=35)
        self.terminalframe = LabelFrame(self.app,text="TERMINAL",foreground="#fff",background="#222")
        self.textArea = CTkTextbox(self.textframe,text_color="#59d3ff",height=500,font=(self.fontName,self.fontSize,'bold'))
        self.terminAlarea = CTkTextbox(self.terminalframe,font=(self.fontName,self.fontSize,'bold'))

        self.textScroll = CTkScrollbar(self.textframe,height=500,command=self.textArea.yview,bg_color="#222")
        self.termScroll = CTkScrollbar(self.terminalframe,command=self.terminAlarea.yview)
        self.check = StringVar()
        

        self.ScrollableFrame = CTkScrollableFrame(self.app, width=138,height=700)
        self.ScrollableFrame.place(y=30)
        self.listbox = Listbox(self.ScrollableFrame, width=25,height=50,background="#222",fg="#eee")
        self.listbox.place(y=160)
        
    def colorize_keywords(self,event=None):
        keyword_color = "#007acc"
        keyword_color_p = "#ba417f"
        keywords = {"and":keyword_color, "as":keyword_color,
                    "assert":keyword_color, "async":keyword_color,
                    "await":keyword_color, "break":keyword_color, "class":keyword_color, "continue":keyword_color, 
                    "def":keyword_color, "del":keyword_color, "elif":keyword_color_p, "else":keyword_color_p, "except":keyword_color, "False":keyword_color,
                    "finally":keyword_color, "for":keyword_color_p,"from":keyword_color_p, "global":keyword_color, "if":keyword_color_p,
                    "import":keyword_color_p, "in":keyword_color, "is":keyword_color, "lambda":keyword_color, "None":keyword_color, 
                    "nonlocal":keyword_color, "not":keyword_color, "or":keyword_color, "pass":keyword_color_p, "raise":keyword_color, "return":keyword_color,
                    "True":keyword_color, "try":keyword_color,"while":keyword_color, "with":keyword_color,"self":keyword_color, "yield":keyword_color}
        text_content = self.textArea.get("1.0", "end")
        purple_keywords = ["if", "elif", "while","for","else","import","from","try","except","pass","with","retrun"]

        keyword_pattern = r"\b(" + "|".join(keywords) + r")\b"
        purple_pattern = r"\b(" + "|".join(purple_keywords) + r")\b"
        matches = re.finditer(keyword_pattern, text_content)
        purple_matches = re.finditer(purple_pattern, text_content)
        class_pattern = r"(?<=\bclass\s)(\w+)(?=\s)|(?<=\bimport\s)(\w+)(?=\s)|(?<=\bfrom\s)(\w+)(?=\s)"
        class_matches = re.finditer(class_pattern, text_content)

        for match in matches:
            start_index = match.start()
            end_index = match.end()
            self.textArea.tag_add("keyword", f"1.0+{start_index}c", f"1.0+{end_index}c")
            self.textArea.tag_config("keyword", foreground=keyword_color)

    
        for match in purple_matches:
            start_index = match.start()
            end_index = match.end()
            self.textArea.tag_add("purple_keyword", f"1.0+{start_index}c", f"1.0+{end_index}c")
            self.textArea.tag_config("purple_keyword", foreground=keyword_color_p)

        for match in class_matches:
            start_index = match.start()
            end_index = match.end()
            self.textArea.tag_add("class_name", f"1.0+{start_index}c", f"1.0+{end_index}c")
            self.textArea.tag_config("class_name", foreground="#00aa7f")


    def save_as(self,event=None):
        
        self.path = filedialog.asksaveasfilename(filetypes=[("python file","*py")],defaultextension=(".py"))
        if self.path != "":
            file = open(self.path,"w")
            file.write(self.textArea.get(1.0,END))
            file.close()

    


        
    def open_file(self,event=None):
        self.path = filedialog.askopenfilename(filetypes=[("python file","*.py")],defaultextension=(".py"))
        if self.path != "":
            file = open(self.path,"r")
            # self.tab_view = MyTabView(master=self.app,border_width=2,width=1165,height=500)
            # self.tab_view.place(x=160,y=37)
            data = file.read()
            self.textArea.delete(1.0,END)
            self.textArea.insert(1.0,data)
            file.close()



    def save_file(self,event=None):
        if self.path == "":
            self.save_as()
        else:
            file = open(self.path,"w")
            file.write(self.textArea.get(1.0,END))
            file.close()
            


    def New_file(self,event=None):
        
        self.path = ""
        # self.tab_view = MyTabView(master=self.app,border_width=2,width=1065)
        # self.tab_view.place(x=300,y=50)
        self.textArea.delete(1.0,END)
        self.terminAlarea.delete(1.0,END)



    def close_win(self,event=None):
        ret = messagebox.askyesno("confirm","do you want to exit ?")
        if ret:
            self.app.destroy()
        else:
            pass


    def change_theme(self,choise):
        set_appearance_mode(choise)
        if choise == "light":
            self.listbox.config(background="white",fg="black")
            self.MenuFrame.config(background="white")
            self.terminalframe.config(background="white",fg="black")

        elif choise == "dark":
            self.listbox.config(background="#222",fg="white")
            self.MenuFrame.config(background="#222")
            self.terminalframe.config(background="#222",fg="white")

         

    def run_code(self):
        
        if self.path =="":
            messagebox.showerror("Error","save the file !!")
        else:
            # print(self.path)
            commands = f"python {self.path}"
            print(commands)
            runFile = sp.Popen(commands,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE,shell=True)
            output,error = runFile.communicate()
            self.terminAlarea.delete(1.0,END)
            self.terminAlarea.insert(1.0,output)
            self.terminAlarea.insert(1.0,error)
            


 
    def incFont(self,event=None):
        self.fontSize
        self.fontSize +=1
        self.textArea.configure(font=(self.fontName,self.fontSize,'bold'))
        # self.terminAlarea.configure(font=(self.fontName,self.fontSize,'bold'))

    def decFont(self,event=None):
        self.fontSize
        self.fontSize -=1
        self.textArea.configure(font=(self.fontName,self.fontSize,'bold'))
        # self.terminAlarea.configure(font=(self.fontName,self.fontSize,'bold'))
        
    def insert_spaces(self,event=None):
        self.textArea.insert(INSERT, " " * 4)
        return "break"
        
    def update_listbox(self,event=None):
        self.folder_path = filedialog.askdirectory()
        print(self.folder_path)
        files = os.listdir(self.folder_path)
        self.listbox.delete(0, END)
        for file in files:
            self.listbox.insert(END, file)

    


    def checkingFun(self,choise):
       
        if choise == "new file":
            self.New_file()
        elif choise == "open file...":
            self.open_file()
        elif choise == "open folder...":
            self.update_listbox()
        elif choise == "save as...":
            self.save_as()
        elif choise == "save": 
            self.save_file()
        elif choise == "close editor":
            self.close_win()
        elif choise == "Undo":
            self.undo()
        elif choise == "Redo":
            self.redo()

        elif choise == "Cut":
            self.cut()

        elif choise == "Copy":
            self.copy()
        elif choise == "Paste":
            self.paste()


    def cut(self,event=None):
        self.copy()
        self.textArea.delete("sel.first", "sel.last")

    def copy(self,event=None):
        self.app.clipboard_clear()
        text = self.textArea.get("sel.first", "sel.last")
        self.app.clipboard_append(text)

    def paste(self,event=None):
        text = self.app.clipboard_get()
        self.textArea.insert("insert", text)

    def undo(self, event=None):
        self.redo_stack.append(self.textArea.get('1.0', 'end'))
        self.textArea.delete('1.0', 'end')
        self.textArea.insert('1.0', self.undo_stack.pop())

        
    def redo(self, event=None):
        self.undo_stack.append(self.textArea.get('1.0', 'end'))
        self.textArea.delete('1.0', 'end')
        self.textArea.insert('1.0', self.redo_stack.pop())


        

    def save_to_undo_stack(self):
        self.undo_stack.append(self.textArea.get('1.0', 'end'))


    def display_file_contents(self,event=None):
        file_path = self.folder_path+"/"+self.listbox.get(self.listbox.curselection())
        self.path = file_path
        file = open(file_path, 'r') 
        data = file.read()
        self.textArea.delete(1.0, END)
        self.terminAlarea.delete(1.0, END)
        self.textArea.insert(1.0, data)
        file.close()


    def colorize_functions(self,event=None):
        text_content = self.textArea.get("1.0", "end")
        function_pattern = r"\b([a-zA-Z_][a-zA-Z0-9_]*)\("
        matches = re.finditer(function_pattern, text_content)
        for match in matches:
            start_index = match.start()
            end_index = match.end()-1
            self.textArea.tag_add("function", f"1.0+{start_index}c", f"1.0+{end_index}c")
            self.textArea.tag_config("function", foreground="#dcdcaa")

    def colorize_comments(self,event=None):
        text_content = self.textArea.get("1.0", "end")
        comment_pattern = r"#.*"
        matches = re.finditer(comment_pattern, text_content)
        for match in matches:
            start_index = match.start()
            end_index = match.end()
            self.textArea.tag_add("comment", f"1.0+{start_index}c", f"1.0+{end_index}c")
            self.textArea.tag_config("comment", foreground="#508d31")

    def colorize_string(self,event=None): 
        text_content = self.textArea.get("1.0", "end")
        string_pattern = r'"[^"\\]*(?:\\.[^"\\]*)*"'
        matches = re.finditer(string_pattern, text_content)
        for match in matches:
            start_index = match.start()
            end_index = match.end()
            self.textArea.tag_add("string", f"1.0+{start_index}c", f"1.0+{end_index}c")
            self.textArea.tag_config("string", foreground="#CD853F")

    def colorize_brackets(self,event=None):
        text_content = self.textArea.get("1.0", "end")

        # Define the regular expression to match brackets
        bracket_pattern = r"[\(\{\[]|[\)\}\]]"

        # Find all matches in the text content
        matches = re.finditer(bracket_pattern, text_content)

        # Apply a tag with purple color to each match
        for match in matches:
            start_index = match.start()
            end_index = match.end()
            self.textArea.tag_add("bracket", f"1.0+{start_index}c", f"1.0+{end_index}c")
            self.textArea.tag_config("bracket", foreground="yellow")


    


    def mainConfig(self):
        self.app.bind("<Control-n>",self.New_file)
        self.app.bind("<Control-o>",self.open_file)
        self.app.bind("<Control-s>",self.save_file)
        self.app.bind("<Control-a>",self.save_as)
        self.app.bind("<Control-q>",self.close_win)
        self.app.bind("<Control-p>",self.incFont)
        self.app.bind("<Control-m>",self.decFont)
        self.app.bind("<Control-z>",self.undo)
        self.app.bind("<Control-y>",self.redo)
        self.app.bind("<Control-x>",self.cut)
        self.app.bind("<Control-c>",self.copy)
        self.app.bind("<Control-v>",self.paste)

        self.textArea.bind("<KeyRelease>",self.colorize_keywords)
        self.textArea.bind("<KeyRelease>",self.colorize_functions)
        self.textArea.bind("<KeyRelease>",self.colorize_comments)
        self.textArea.bind("<KeyRelease>",self.colorize_brackets)
        self.textArea.bind("<KeyRelease>",self.colorize_string)
        
        
        self.textArea.bind("<Tab>", self.insert_spaces)
        self.listbox.bind("<<ListboxSelect>>",self.display_file_contents)
        # self.display_line_numbers()
        self.app.title("PyAmmar") # the old version was the PyCharm the new one is PyAmmar 😂😂😂😂
        self.app.geometry("1227x670+0+0")
        self.listbox.pack(side=LEFT, padx=0, pady=0)
        filemenu = CTkComboBox(self.app,button_color="#144870",button_hover_color="#0b2b43",width=95,values=["new file","open file...","open folder...","save","save as...","close editor"],command=self.checkingFun)
        filemenu.place(x=1,y=3)
        filemenu.set("File")
        editmenu =  CTkComboBox(self.app,button_color="#144870",button_hover_color="#0b2b43",width=95,values=["Undo","Redo","Cut","Copy","Paste"],command=self.checkingFun)
        editmenu.place(x=98,y=3)
        editmenu.set("Edit")
        setting = CTkComboBox(self.app,button_color="#144870",button_hover_color="#0b2b43",width=95,values=["dark","light","sytem","blue"],command=self.change_theme)
        setting.place(x=196,y=3)
        setting.set("theme")
       
        help =  CTkComboBox(self.app,button_color="#144870",button_hover_color="#0b2b43",width=95,values=["welcome","about","join us"])
        help.place(x=294,y=3)
        help.set("Help")
        Run = CTkButton(self.app,width=65,text="Run",command=self.run_code)
        Run.place(x=395,y=3)
        
        self.textframe.place(x=160,y=32,height=500,width=self.width-120)
        self.textScroll.place(x=1190)
       
        self.textArea.pack(fill=BOTH)
        self.textArea.configure(yscrollcommand=self.textScroll.set)
        # self.display_line_numbers()
        self.terminalframe.place(x=160,y=530,height=470,width=self.width-20)
        self.termScroll.place(x=1190)
        self.terminAlarea.pack(fill=BOTH)
        self.terminAlarea.configure(yscrollcommand=self.termScroll.set)
        self.app.mainloop()




if __name__=="__main__":
    PythonEditor().mainConfig()
