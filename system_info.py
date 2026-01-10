import platform
import os
import shutil
import time
import getpass  # add this

def bytes_to_gb(bytes):
    return round(bytes / (1024 ** 3), 2)

def get_system_info():
    print("=" * 40)
    print("      SYSTEM INFORMATION")
    print("=" * 40)

    print(f"OS            : {platform.system()} {platform.release()}")
    print(f"Architecture  : {platform.machine()}")
    print(f"Processor     : {platform.processor()}")

    # RAM
    try:
        if os.path.exists("/proc/meminfo"):
            with open("/proc/meminfo") as f:
                meminfo = f.read()
            total_mem = int(
                [line for line in meminfo.splitlines() if "MemTotal" in line][0]
                .split()[1]
            )
            print(f"Total RAM     : {round(total_mem / 1024 / 1024, 2)} GB")
        else:
            print("Total RAM     : Not available")
    except:
        print("Total RAM     : Error")

    # Disk
    total, used, free = shutil.disk_usage("/")
    print(f"Disk Total    : {bytes_to_gb(total)} GB")
    print(f"Disk Used     : {bytes_to_gb(used)} GB")
    print(f"Disk Free    : {bytes_to_gb(free)} GB")

    # Current user (fixed)
    print(f"Current User  : {getpass.getuser()}")

    # Uptime
    try:
        with open('/proc/uptime') as f:
            uptime_seconds = float(f.readline().split()[0])
        print(f"Uptime        : {round(uptime_seconds, 2)} seconds")
    except Exception as e:
        print(f"Uptime        : Not available ({e})")

    print("=" * 40)

if __name__ == "__main__":
    get_system_info()
