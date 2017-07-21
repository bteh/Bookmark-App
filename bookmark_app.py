import tkinter as tk
import webbrowser

#assign web links variables
def click_facebook(event):
    webbrowser.open_new_tab("https://facebook.com")
def click_amazon(event):
    webbrowser.open_new_tab("https://amazon.com")
def click_instagram(event):
    webbrowser.open_new_tab("https://instagram.com")


window = tk.Tk()
#create a window
window.geometry("400x200")
#create a button 
button = tk.Button(window, text="Facebook")
button1 = tk.Button(window, text="Amazon")
button2 = tk.Button(window, text="Instagram")

alabel = tk.Label(text= "News Feed")
#putting the button in which column/row
alabel.grid(column=0, row=0)
#bind button to Facebook
button.bind("<Button-1>",click_facebook)
button.grid(column=0)

blabel = tk.Label(text= "Shopping Page")
blabel.grid(column=1, row=0)
button1.bind("<Button-1>",click_amazon)
button1.grid(column=1, row=1)

clabel = tk.Label(text= "Front Page")
clabel.grid(column=2, row=0)
button2.bind("<Button-1>",click_instagram)
button2.grid(column=2, row=1)
window.mainloop()

