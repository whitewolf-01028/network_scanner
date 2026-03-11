import tkinter as tk
from scanner import scan_network

def start_gui():

    def start_scan():
        target = entry.get()
        output.delete("1.0", tk.END)

        results = scan_network(target)

        for host in results:
            output.insert(tk.END, f"\nHost: {host['host']}\n")
            output.insert(tk.END, f"State: {host['state']}\n")

            for port, state in host["ports"]:
                output.insert(tk.END, f"Port {port}: {state}\n")

    window = tk.Tk()
    window.title("Python Network Scanner")

    tk.Label(window, text="Enter Target IP or Network").pack()

    entry = tk.Entry(window, width=30)
    entry.pack()

    scan_btn = tk.Button(window, text="Scan", command=start_scan)
    scan_btn.pack()

    output = tk.Text(window, height=20, width=60)
    output.pack()

    window.mainloop()