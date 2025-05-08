import time
import threading

def set_reminder(reminder_text, time_delay_seconds):
    time.sleep(time_delay_seconds)
    print(f"Reminder: {reminder_text}")