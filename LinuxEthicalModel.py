import os
import signal
import psutil


def lock_all_processes():    # Get a list of all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:           
            if proc.info['pid'] == 1 or 'systemd' in proc.info['name']:    # Skip critical system processes (init, systemd, etc.)
                continue    
            
            os.kill(proc.info['pid'], signal.SIGSTOP) # Send SIGSTOP signal to pause the process
            print(f"Stopped process: {proc.info['name']} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):    # Handle processes that are already terminated or cannot be accessed           
            continue


def unlock_all_processes():   # Unlock all processes by sending SIGCONT signal
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['pid'] == 1 or 'systemd' in proc.info['name']:
                continue

           
            os.kill(proc.info['pid'], signal.SIGCONT)    # Send SIGCONT signal to resume the process
            print(f"Resumed process: {proc.info['name']} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

# Example usage:
if __name__ == "__main__":
    lock_all_processes()
    # for unlocking all processes later, you can call unlock_all_processes()
    # unlock_all_processes()
