import tkinter as tk
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.LOW)
import time



led = LED(2)

morse_code = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'
                    }
					
def blink_led(duration):
    GPIO.output(2, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(2, GPIO.LOW)
    time.sleep(0.2) # Delay between blinks
    
def convert_to_morse(word):
    for char in word.upper():
        if char == ' ':
            time.sleep(0.6)  # Delay between words
        elif char in morse_code:
            code = morse_code[char]
            for c in code:
                if c == '.':
                    blink_led(0.2)  # Blink LED for dot
                elif c == '-':
                    blink_led(0.6)  # Blink LED for dash
                    
def button_click():
    input_word = text_box.get()
    convert_to_morse(input_word)        
       
root = tk.Tk()
root.title('Morse Code Generator')

text_box = tk.Entry(root, width=12)
text_box.pack(pady=10)

button = tk.Button(root, text='Generate Morse Code', command=button_click)
button.pack(pady=10)

root.mainloop()
    

       







