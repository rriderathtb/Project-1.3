import tkinter as tk
from tkinter import messagebox, scrolledtext
from detector import Detector
import threading

class PreventXGUI:
    def __init__(self):
        self.detector = Detector()
        
        # Window Setup
        self.window = tk.Tk()
        self.window.title("PreventX | Network Security Monitor")
        self.window.geometry("600x450")
        self.window.configure(bg="#1e1e1e")  # Dark background

        # Header
        self.header = tk.Label(
            self.window, text="PREVENT-X DASHBOARD", 
            font=("Courier New", 18, "bold"), fg="#00ff00", bg="#1e1e1e"
        )
        self.header.pack(pady=15)

        # Status Indicator
        self.status_label = tk.Label(
            self.window, text="Status: IDLE", 
            font=("Arial", 10), fg="white", bg="#333333", width=20
        )
        self.status_label.pack(pady=5)

        # Log Area (To see what's happening)
        self.log_area = scrolledtext.ScrolledText(
            self.window, width=70, height=12, 
            bg="#000000", fg="#00ff00", font=("Consolas", 9)
        )
        self.log_area.pack(pady=10, padx=10)
        self.log_area.insert(tk.END, "[*] System Ready. Awaiting start...\n")
        self.log_area.configure(state='disabled')

        # Button Frame
        btn_frame = tk.Frame(self.window, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(
            btn_frame, text="START MONITORING", bg="#28a745", fg="white",
            font=("Arial", 10, "bold"), width=18, command=self.start_detection
        )
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = tk.Button(
            btn_frame, text="STOP & EXIT", bg="#dc3545", fg="white",
            font=("Arial", 10, "bold"), width=18, command=self.stop_detection
        )
        self.stop_btn.grid(row=0, column=1, padx=10)

        self.window.mainloop()

    def update_log(self, message):
        """Helper to add messages to the UI log"""
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, f"{message}\n")
        self.log_area.see(tk.END)
        self.log_area.configure(state='disabled')

    def start_detection(self):
        self.status_label.config(text="Status: MONITORING", fg="#00ff00")
        self.update_log("[+] Packet Sniffing initialized...")
        self.start_btn.config(state='disabled')
        
        # Run detector in a separate thread so the UI doesn't freeze
        threading.Thread(target=self.detector.start, daemon=True).start()
        messagebox.showinfo("PreventX", "Monitoring started in background.")

    def stop_detection(self):
        self.update_log("[-] Shutting down system...")
        if messagebox.askokcancel("Quit", "Do you want to stop monitoring and exit?"):
            self.window.destroy()
            quit()