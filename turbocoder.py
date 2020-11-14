from tkinter import *
from winsound import Beep

def main():
	root = Tk()
	root.title("TurboCoder")
	root.geometry("1200x850")
	root.configure(bg="#171717")

	main_code_pad = Text(root)
	current_file_widget = Entry(root)
	file_label = Label(root, text="Current file:")

	def attach(event=None):
		try:
			file = current_file_widget.get()

			main_code_pad.delete("1.0", END)

			current_file = open(file, "r+")
			main_code_pad.insert("1.0", current_file.read())

			Beep(1000, 40)
		except:
			pass

	def get_file():
		return current_file_widget.get()

	def save(event=None):
		try:
			current_file = open(get_file(), "r+")

			current_file.write(main_code_pad.get("1.0", END))

			Beep(500, 40)
		except:
			pass

	save_button = Button(root, text="SAVE", command=save)
	attach_button = Button(root, text="ATTACH", command=attach)

	root.bind("<Control-s>", save)
	root.bind("<Control-f>", attach)

	main_code_pad.configure(bg="black", fg="green", insertbackground="green")
	current_file_widget.configure(bg="black", fg="green")
	file_label.configure(bg="#171717", fg="green")
	save_button.configure(bg="black", fg="green", border=0)
	attach_button.configure(bg="black", fg="green", border=0)

	main_code_pad.place(x=0, y=40, width=1200, height=830)
	current_file_widget.place(x=100, y=9, width=150, height=20)
	file_label.place(x=0, y=5, width=80, height=30)
	save_button.place(x=1120, y=7, width=50, height=25)
	attach_button.place(x=270, y=7, width=60, height=25)

	root.mainloop()

main()