import os
import sys
import ctypes
import random
import time
import threading
from ctypes import windll
import tkinter as tk
from tkinter import messagebox
import subprocess

class L3HAPrank:
    def __init__(self):
        self.running = True
        self.icons_moved = []
        
    def show_popup(self, title, message):
        """Display annoying popups"""
        root = tk.Tk()
        root.withdraw()
        root.after(500, lambda: messagebox.showinfo(title, message))
        root.mainloop()
        
    def spam_popups(self):
        """Spam the user with popups"""
        messages = [
            ("⚠️ VIRUS ALERT", "SUBSCRIBE TO -SIRUS-\nYOU'VE BEEN PRANKED"),
            ("🎉 CONGRATULATIONS!", "SUBSCRIBE TO -SIRUS-\nNOW"),
            ("💀 SYSTEM WARNING", "SUBSCRIBE TO -SIRUS-\nOR ELSE"),
            ("🔴 CRITICAL ERROR", "DID YOU SUBSCRIBE YET?\n-SIRUS-"),
            ("⚡ POWER UP", "SUBSCRIBE TO -SIRUS-\nBEFORE IT'S TOO LATE"),
        ]
        
        for _ in range(5):
            if not self.running:
                break
            title, message = random.choice(messages)
            thread = threading.Thread(target=self.show_popup, args=(title, message))
            thread.daemon = True
            thread.start()
            time.sleep(2)
    
    def get_icon_positions(self):
        """Get current desktop icon positions"""
        try:
            result = subprocess.run(
                ['powershell', '-Command', 
                 'Get-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\Shell\\Bags\\1\\Desktop" | Select-Object -Property *'],
                capture_output=True,
                text=True
            )
            return True
        except:
            return False
    
    def move_icons(self):
        """Randomly move desktop icons around"""
        try:
            # Get screen dimensions
            screen_width = windll.user32.GetSystemMetrics(0)
            screen_height = windll.user32.GetSystemMetrics(1)
            
            # Simulate icon movements by refreshing desktop in weird ways
            for _ in range(3):
                if not self.running:
                    break
                    
                # Minimize all windows
                os.system('taskkill /F /IM explorer.exe')
                time.sleep(1)
                
                # Restart explorer
                os.system('start explorer.exe')
                time.sleep(2)
                
        except Exception as e:
            print(f"Icon move error: {e}")
    
    def invert_colors(self):
        """Invert screen colors temporarily"""
        try:
            # Use Windows accessibility shortcut
            windll.user32.keybd_event(0xA4, 0, 0, 0)  # Left Alt
            windll.user32.keybd_event(0xA4, 0, 2, 0)  # Left Alt up
            windll.user32.keybd_event(0x26, 0, 0, 0)  # Up arrow
            windll.user32.keybd_event(0x26, 0, 2, 0)  # Up arrow up
            windll.user32.keybd_event(0x26, 0, 0, 0)  # Up arrow
            windll.user32.keybd_event(0x26, 0, 2, 0)  # Up arrow up
            windll.user32.keybd_event(0x26, 0, 0, 0)  # Up arrow
            windll.user32.keybd_event(0x26, 0, 2, 0)  # Up arrow up
        except:
            pass
    
    def spam_sounds(self):
        """Play annoying system sounds"""
        try:
            for _ in range(3):
                if not self.running:
                    break
                windll.user32.MessageBeep(0xFFFFFFFF)
                time.sleep(1)
        except:
            pass
    
    def mess_with_cursor(self):
        """Make cursor jumpy"""
        try:
            for _ in range(5):
                if not self.running:
                    break
                x = random.randint(100, 1900)
                y = random.randint(100, 1080)
                windll.user32.SetCursorPos(x, y)
                time.sleep(0.5)
        except:
            pass
    
    def run_prank(self):
        """Execute all prank functions"""
        print("[*] L3HA Prank Starting...")
        print("[*] This is a harmless joke program!")
        print("[*] Press Ctrl+C to stop")
        
        # Start prank threads
        threads = [
            threading.Thread(target=self.spam_popups),
            threading.Thread(target=self.spam_sounds),
            threading.Thread(target=self.mess_with_cursor),
        ]
        
        for thread in threads:
            thread.daemon = True
            thread.start()
        
        try:
            # Keep program running
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[!] Stopping prank...")
            self.running = False
            time.sleep(2)
            print("[✓] Prank stopped. Desktop should return to normal.")
    
    def stop(self):
        """Stop the prank"""
        self.running = False

if __name__ == "__main__":
    print("=" * 50)
    print("L3HA - The Harmless Prank Program")
    print("=" * 50)
    print("\nWARNING: This program will:")
    print("  ✓ Show annoying popups")
    print("  ✓ Play sounds")
    print("  ✓ Make your cursor jump around")
    print("  ✓ Be generally chaotic")
    print("\nPress Enter to start (or Ctrl+C to cancel)")
    print("=" * 50)
    
    try:
        input()
    except KeyboardInterrupt:
        print("Cancelled!")
        sys.exit(0)
    
    prank = L3HAPrank()
    prank.run_prank()
