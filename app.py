import tkinter as tk
import subprocess
import os
import sys
import threading

if sys.platform == "win32":
    import ctypes
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # Relaunch the script with admin rights
        params = " ".join([f'"{x}"' for x in sys.argv])
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1)
        sys.exit()


def show_cwd():
    cwd = os.getcwd()
    output_label.config(text=f"Current Directory:\n{cwd}")


def list_files():
    files = os.listdir(os.getcwd())
    output_label.config(text="Files:\n" + "\n".join(files))


def open_cmd():
    # This will open a visible Command Prompt window
    subprocess.Popen(["cmd.exe"], creationflags=subprocess.CREATE_NEW_CONSOLE)


def open_firefox():
    try:
        subprocess.Popen("start firefox", shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open Firefox:\n{e}")


def open_control_panel():
    try:
        subprocess.Popen("control", shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open Control Panel:\n{e}")


def open_settings():
    try:
        subprocess.Popen("start ms-settings:", shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open Settings:\n{e}")


def open_task_manager():
    try:
        subprocess.Popen("taskmgr", shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open Task Manager:\n{e}")


def open_device_manager():
    try:
        subprocess.Popen("devmgmt.msc", shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open Device Manager:\n{e}")


def open_system_info():
    try:
        subprocess.Popen("msinfo32", shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open System Information:\n{e}")


def open_registry_editor():
    try:
        subprocess.Popen("regedit", shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open Registry Editor:\n{e}")


def open_notepad():
    try:
        subprocess.Popen("notepad", shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open Notepad:\n{e}")


def open_resource_monitor():
    try:
        subprocess.Popen("resmon", shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open Resource Monitor:\n{e}")


def open_vscode():
    try:
        # If 'code' is in PATH, this works:
        subprocess.Popen("code", shell=True)
        # Or use the full path if needed, e.g.:
        # subprocess.Popen(r"C:\Users\jenni\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    except Exception as e:
        output_label.config(text=f"Could not open VS Code:\n{e}")


def open_chrome_profile_selector():
    try:
        # This command opens Chrome's profile selection window
        subprocess.Popen(r'start chrome --profile-directory="Default"', shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open Chrome profile selector:\n{e}")


def open_grav_star_mouse_settings():
    try:
        # Replace the path below with the actual path to your Grav Star Mouse settings executable if needed
        subprocess.Popen(r'"C:\Program Files (x86)\GravStar\GravStarMouseSettings.exe"', shell=True)
    except Exception as e:
        output_label.config(text=f"Could not open Grav Star Mouse Settings:\n{e}")


def close_all_tools():
    processes = [
        "cmd.exe",
        "notepad.exe",
        "taskmgr.exe",
        "mmc.exe",         # Device Manager, System Info, Registry Editor, Control Panel
        "msinfo32.exe",
        "regedit.exe",
        "resmon.exe",
        # Add more if you add more tools
    ]
    closed = []
    for proc in processes:
        try:
            subprocess.run(f"taskkill /im {proc} /f", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            closed.append(proc)
        except Exception:
            pass
    output_label.config(text="Closed tools:\n" + "\n".join(closed))
    # Hide the closed message after 5 seconds
    output_label.after(5000, lambda: output_label.config(text=""))


def main():
    global output_label
    root = tk.Tk()
    root.title("Python Tools")
    root.geometry("440x460")

    # Set background to black and text to hacker green
    hacker_green = "#00FF00"
    root.configure(bg="black")

    label = tk.Label(root, text="Helpful Local Utilities", bg="black", fg=hacker_green)
    label.pack(pady=10)

    button_frame = tk.Frame(root, bg="black")
    button_frame.pack()

    btn_width = 22

    buttons = [
        ("Show Current Directory", show_cwd),
        ("List Files", list_files),
        ("Open Command Prompt", open_cmd),
        ("Open Firefox", open_firefox),
        ("Open Chrome Profile Selector", open_chrome_profile_selector),
        ("Open Control Panel", open_control_panel),
        ("Open Settings", open_settings),
        ("Open Task Manager", open_task_manager),
        ("Open Device Manager", open_device_manager),
        ("Open System Information", open_system_info),
        ("Open Registry Editor", open_registry_editor),
        ("Open Notepad", open_notepad),
        ("Open Resource Monitor", open_resource_monitor),
        ("Open VS Code", open_vscode),
        ("Open Grav Star Mouse Settings", open_grav_star_mouse_settings),
    ]

    # Place buttons in a 2-column grid
    for idx, (text, cmd) in enumerate(buttons):
        row = idx // 2
        col = idx % 2
        btn = tk.Button(
            button_frame,
            text=text,
            width=btn_width,
            command=cmd,
            bg="black",
            fg=hacker_green,
            activebackground="#003300",
            activeforeground=hacker_green,
            highlightbackground="black",
            highlightcolor=hacker_green,
            highlightthickness=1,
            borderwidth=2
        )
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

    output_label = tk.Label(root, text="", wraplength=400, justify="left", bg="black", fg=hacker_green)
    output_label.pack(pady=20)

    close_tools_button = tk.Button(
        root,
        text="Close All Opened Tools",
        width=btn_width*2+2,
        command=close_all_tools,
        bg="black",
        fg=hacker_green,
        activebackground="#003300",
        activeforeground=hacker_green,
        highlightbackground="black",
        highlightcolor=hacker_green,
        highlightthickness=1,
        borderwidth=2
    )
    close_tools_button.pack(pady=(0, 10))

    close_button = tk.Button(
        root,
        text="Close",
        width=btn_width*2+2,
        command=root.destroy,
        bg="black",
        fg=hacker_green,
        activebackground="#003300",
        activeforeground=hacker_green,
        highlightbackground="black",
        highlightcolor=hacker_green,
        highlightthickness=1,
        borderwidth=2
    )
    close_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()

