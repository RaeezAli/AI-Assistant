import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
import datetime

# Dummy speak function (replace with your pyttsx3 speak if needed)
def speak(text):
    output_area.insert(tk.END, f"Jarvis: {text}\n")
    output_area.see(tk.END)

# Simulated command handler
def handle_command():
    command = command_entry.get().lower()
    command_entry.delete(0, tk.END)
    output_area.insert(tk.END, f"You: {command}\n")
    
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "exit" in command:
        root.quit()
    else:
        speak("Command not recognized.")

# GUI layout
root = tk.Tk()
root.title("Jarvis AI Assistant")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="🧠 Jarvis Assistant", font=("Helvetica", 18, "bold"), fg="cyan", bg="#1e1e1e")
title.pack(pady=10)

output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 12), height=20, bg="#2b2b2b", fg="white")
output_area.pack(padx=10, pady=5)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

command_entry = tk.Entry(frame, width=50, font=("Helvetica", 12))
command_entry.pack(side=tk.LEFT, padx=5)

submit_btn = tk.Button(frame, text="Run", font=("Helvetica", 12), command=lambda: threading.Thread(target=handle_command).start())
submit_btn.pack(side=tk.LEFT)

# Start GUI
root.mainloop()
