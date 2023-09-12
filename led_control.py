import tkinter as tk
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)   # Red LED
GPIO.setup(10, GPIO.OUT)  # Green LED
GPIO.setup(12, GPIO.OUT)  # blue LED

# Function to control LEDs
def control_red_led():
    control_led(8)

def control_green_led():
    control_led(10)

def control_blue_led():
    control_led(12)

def control_led(led_pin):
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(led_pin, GPIO.HIGH)

# Function to turn off all LEDs
def turn_off_all_leds():
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)

# Function to clean up GPIO on exit
def on_exit():
    GPIO.cleanup()
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("LED Controller")

# Create a label
label = tk.Label(root, text="Select LED to Turn On:", font=("Helvetica", 16))
label.pack(pady=10)

# Create radio buttons for LEDs
led_var = tk.IntVar()
led_var.set(0)  # Initialize with no selection

red_radio = tk.Radiobutton(root, text="Red LED", font=("Helvetica", 14), variable=led_var, value=8, command=control_red_led)
green_radio = tk.Radiobutton(root, text="Green LED", font=("Helvetica", 14), variable=led_var, value=10, command=control_green_led)
blue_radio = tk.Radiobutton(root, text="Blue LED", font=("Helvetica", 14), variable=led_var, value=12, command=control_blue_led)

red_radio.pack(pady=10)
green_radio.pack(pady=10)
blue_radio.pack(pady=10)

# Create a "Turn Off All LEDs" button
off_button = tk.Button(root, text="Turn Off All LEDs", command=turn_off_all_leds, font=("Helvetica", 12))
off_button.pack(pady=10)

# Add some padding and set the background color
root.configure(bg="#89cfef")
root.geometry("300x400")

# Set the exit event handler
root.protocol("WM_DELETE_WINDOW", on_exit)

# Start the GUI main loop
root.mainloop()
