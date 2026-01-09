import platform
import os
import shutil
import argparse
import json

def bytes_to_gb(bytes):
    return round(bytes / (1024 ** 3), 2)

def get_os_info():
    return {
        "os": f"{platform.system()} {platform.release()}",
        "architecture": platform.machine(),
        "processor": platform.processor()
    }

def get_ram_info():
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if "MemTotal" in line:
                    total_mem = int(line.split()[1])
                    return {"total_ram_gb": round(total_mem / 1024 / 1024, 2)}
    except:
        return {"total_ram_gb": "Not available"}

def get_disk_info():
    total, used, free = shutil.disk_usage("/")
    return {
        "disk_total_gb": bytes_to_gb(total),
        "disk_used_gb": bytes_to_gb(used),
        "disk_free_gb": bytes_to_gb(free)
    }

def print_info(info, json_output=False):
    if json_output:
        print(json.dumps(info, indent=2))
    else:
        for k, v in info.items():
            print(f"{k:15}: {v}")

def main():
    parser = argparse.ArgumentParser(
        description="System Info CLI Tool"
    )
    parser.add_argument("--os", action="store_true", help="Show OS information")
    parser.add_argument("--ram", action="store_true", help="Show RAM information")
    parser.add_argument("--disk", action="store_true", help="Show Disk information")
    parser.add_argument("--all", action="store_true", help="Show all system info")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")

    args = parser.parse_args()

    info = {}

    if args.os or args.all:
        info.update(get_os_info())

    if args.ram or args.all:
        info.update(get_ram_info())

    if args.disk or args.all:
        info.update(get_disk_info())

    if not info:
        parser.print_help()
        return

    print_info(info, args.json)

if __name__ == "__main__":
    main()

