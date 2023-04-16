import tkinter as tk
from gpiozero import LED
import RPi.GPIO 
RPi.GPIO.setmode(RPi.GPIO.BCM)
import time


dot = 0.1
dash = 0.3
space = 0.1
letterSpace = 0.2
wordspace = 0.5
led = LED(2)

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
					
def encrypt(word):
    cipher = ''
    for letter in word:
        if letter.upper() != ' ':
 
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher
	

def blinkName():
    word = text_box.get()
    cipher = encrypt(word)
    for letter in cipher:
        if letter == '.':
            led.on()
            time.sleep(dot)
            led.off()
            time.sleep(space)
        elif letter == '-':
            led.on()
            time.sleep(dot)
            led.off()
            time.sleep(space)
        elif letter == ' ':
            led.on()
            time.sleep(wordspace)
            led.off()
            time.sleep(space)
        time.sleep(letterSpace)
        
       
root = tk.Tk()
root.title('Morse Code Generator')

text_box = tk.Entry(root, width=12)
text_box.pack(pady=10)

button = tk.Button(root, text='Generate Morse Code', command=blinkName)
button.pack(pady=10)

root.mainloop()
    

       







