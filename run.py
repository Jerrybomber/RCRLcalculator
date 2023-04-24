""""
File:		run.py
Author:		Jerry Karkainen
Description:Graphigal user interface for calculator using c.
""""

from tkinter import *
from tkinter import messagebox
import ctypes

root = Tk()
root.title("Calculator")
root.geometry("900x500")

#connect c file to python file
cfile = ctypes.CDLL('./calculator.so')

# define function to create new window
def open_rc_circuit():
    rc_window = Toplevel(root)
    rc_window.title("RC-Circuit")
    rc_window.geometry("600x550")

    # add text boxes and entrys for user input
    voltage_label = Label(rc_window, text="Voltage(V):")
    voltage_label.pack(pady=10)
    voltage_entry = Entry(rc_window, width=10)
    voltage_entry.pack(pady=5)
    resistance_label = Label(rc_window, text="Resistance:")
    resistance_label.pack(pady=10)
    resistance_entry = Entry(rc_window, width=10)
    resistance_entry.pack(pady=5)
    capacitance_label = Label(rc_window, text="Capacitance:")
    capacitance_label.pack(pady=10)
    capacitance_entry = Entry(rc_window, width=10)
    capacitance_entry.pack(pady=5)
    start_hz_label = Label(rc_window, text="Start frequency(hz):")
    start_hz_label.pack(pady=10)
    start_hz_entry = Entry(rc_window, width=10)
    start_hz_entry.pack(pady=5)
    step_hz_label = Label(rc_window, text="How big steps in hz:")
    step_hz_label.pack(pady=10)
    step_hz_entry = Entry(rc_window, width=10)
    step_hz_entry.pack(pady=5)
    max_hz_label = Label(rc_window, text="Max frequency(hz):")
    max_hz_label.pack(pady=10)
    max_hz_entry = Entry(rc_window, width=10)
    max_hz_entry.pack(pady=5)
    calculate_button = Button(rc_window, text="Calculate", command=lambda: run_rc(voltage_entry.get(), resistance_entry.get(), capacitance_entry.get(), start_hz_entry.get(), step_hz_entry.get(), max_hz_entry.get()))
    calculate_button.pack(pady=20)

def open_rl_circuit():
    rl_window = Toplevel(root)
    rl_window.title("RL-Circuit")
    rl_window.geometry("600x550")

    # add text boxes for user input
    voltage_label = Label(rl_window, text="Voltage(V):")
    voltage_label.pack(pady=10)
    voltage_entry = Entry(rl_window, width=10)
    voltage_entry.pack(pady=5)
    resistance_label = Label(rl_window, text="Resistance(ohm):")
    resistance_label.pack(pady=10)
    resistance_entry = Entry(rl_window, width=10)
    resistance_entry.pack(pady=5)
    inductance_label = Label(rl_window, text="Inductance(milli henreinä):")
    inductance_label.pack(pady=10)
    inductance_entry = Entry(rl_window, width=10)
    inductance_entry.pack(pady=5)
    start_hz_label = Label(rl_window, text="Start frequency(hz):")
    start_hz_label.pack(pady=10)
    start_hz_entry = Entry(rl_window, width=10)
    start_hz_entry.pack(pady=5)
    step_hz_label = Label(rl_window, text="How big steps in hz:")
    step_hz_label.pack(pady=10)
    step_hz_entry = Entry(rl_window, width=10)
    step_hz_entry.pack(pady=5)
    max_hz_label = Label(rl_window, text="Max frequency(hz):")
    max_hz_label.pack(pady=10)
    max_hz_entry = Entry(rl_window, width=10)
    max_hz_entry.pack(pady=5)
    calculate_button = Button(rl_window, text="Calculate", command=lambda: run_rl(voltage_entry.get(), resistance_entry.get(), inductance_entry.get(), start_hz_entry.get(), step_hz_entry.get(), max_hz_entry.get()))
    calculate_button.pack(pady=20)

def run_rl(v, r, l, startf, stepf, maxf):
	# Input validation.
	try:
		v = int(v)
		r = int(r)
		l = int(l)
		startf = int(startf)
		stepf = int(stepf)
		maxf = int(maxf)

		if v < 0 or r < 0 or l < 0 or startf < 0 or stepf < 0  or maxf < 0:
			messagebox.showerror("Error", "Values must be bigger than zero !!")
		elif startf > maxf:
			messagebox.showerror("Error", "Starting freaquency can me bigger than max freaquency")
		else:
			# Giving values to c file.
			cfile.runRL(v, r, l, startf, stepf, maxf)
			display_results()

	except:
		messagebox.showerror("Error", "Input only integers\nand there can't be blank entries.")

def run_rc(v, r, c, startf, stepf, maxf):
	try:
		v = int(v)
		r = int(r)
		c = int(c)
		startf = int(startf)
		stepf = int(stepf)
		maxf = int(maxf)
		print(r, c, startf, stepf, maxf)

		if v < 0 or r < 0 or c < 0 or startf < 0 or stepf < 0  or maxf < 0:
			messagebox.showerror("Error", "Values must be bigger than zero !!")
		elif startf > maxf:
			messagebox.showerror("Error", "Starting freaquency can me bigger than max freaquency")
		else:
			# Giving values to c file
			cfile.runRC(v, r, c, startf, stepf, maxf)
			display_results()
	except:
		messagebox.showerror("Error", "Input only integers\nand there can't be blank entries.")

def display_results():

    # Open the file and read its contentszz
    with open("Results.txt", "r") as f:
        results = f.read()

    # Create a new window to display the results
    results_window = Toplevel(root)
    results_window.title("Results")
    results_window.geometry("500x500")

    # Add a Text widget to display the results
    results_text = Text(results_window, font=("Helvetica", 12))
    results_text.pack(fill=BOTH, expand=True)

    # Insert the results into the Text widget
    results_text.insert(END, results)



# create the main frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Add title label
title_label = Label(my_frame, text="Electric circuit calculator", font=("Helvetica", 24))
title_label.pack(pady=20)

# Add buttons that open new windows
RC_button = Button(my_frame, text="RC-Circuit", font=("Helvetica", 14), command=open_rc_circuit)
RC_button.pack(pady=20)

RL_button = Button(my_frame, text="RL-Circuit", font=("Helvetica", 14), command=open_rl_circuit)
RL_button.pack(pady=20)

root.mainloop()
