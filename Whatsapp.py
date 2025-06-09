import pyautogui
import os
import time

def open_whatsapp():
    """Opens WhatsApp Desktop App. Update the path if needed."""
    try:
        os.startfile(r"C:\Users\Muhammad Ali\Desktop\WhatsApp.lnk")
        print("[INFO] Opening WhatsApp Desktop...")
        time.sleep(5)  # Allow time for WhatsApp to open
    except Exception as e:
        print("[ERROR] Unable to open WhatsApp:", e)

def send_whatsapp_message(contact_name: str, message: str):
    """Sends a message to a contact using WhatsApp Desktop."""
    try:
        open_whatsapp()

        # Adjust coordinates based on your screen (search bar location)
        pyautogui.click(x=291, y=122, duration=0.5)  # <-- Adjust if needed
        time.sleep(1.5)
        
        pyautogui.hotkey('ctrl', 'a')  # Select all
        time.sleep(0.2)
        pyautogui.press('backspace')   # Clear it
        time.sleep(0.5)
        
        # Type the contact name
        pyautogui.write(contact_name)
        time.sleep(2)
        
        pyautogui.click(x=231, y=182, duration=0.5)
        time.sleep(1)
        
        pyautogui.click(x=776, y=702, duration=0.5)
        time.sleep(1)
        
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(0.5)

        # ✍️ Step 7: Type and send the message
        pyautogui.write(message, interval=0.05)

        pyautogui.click(x=1335, y=697, duration=0.5)
        time.sleep(1)

        print(f"[INFO] Message sent to {contact_name}.")
    except Exception as e:
        print("[ERROR] Message failed to send:", e)

def whatsapp_chat_input():
    """Text-based input to send a WhatsApp message."""
    contact = input("Enter WhatsApp contact name: ")
    message = input("Enter the message to send: ")
    send_whatsapp_message(contact, message)