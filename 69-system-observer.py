


## Step 1 : get some system status info like % top

# Processes: 559 total, 4 running, 555 sleeping, 2255 threads                                                                                                              20:30:27
# Load Avg: 1.46, 1.55, 1.58  
# CPU usage: 6.77% user, 6.61% sys, 86.60% idle  
# SharedLibs: 405M resident, 51M data, 34M linkedit.
# MemRegions: 123053 total, 3525M resident, 147M private, 2906M shared. 
# PhysMem: 16G used (2610M wired), 235M unused.
# VM: 3346G vsize, 2320M framework vsize, 19848132(0) swapins, 21833373(0) swapouts.   
# Networks: packets: 67102256/70G in, 91952747/16G out.
# Disks: 41860687/819G read, 22787394/466G written.

import os
import psutil
import platform
from datetime import datetime



# def get_size(bytes, suffix="B"):
#   """
#   Scale bytes to its proper format
#   e.g:
#       1253656 => '1.20MB'
#       1253656678 => '1.17GB'
#   """
#   factor = 1024
#   for unit in ["", "K", "M", "G", "T", "P"]:
#     if bytes < factor:
#       return f"{bytes:.2f}{unit}{suffix}"
#     bytes /= factor

# ========  System Information  ==========
# print("="*40, "System Information", "="*40)
# uname = platform.uname()
# print(f"System: {uname.system}")
# print(f"Node Name: {uname.node}")
# print(f"Release: {uname.release}")
# print(f"Version: {uname.version}")
# print(f"Machine: {uname.machine}")
# print(f"Processor: {uname.processor}")

# ==========  Boot Time  =================
# print("="*40, "Boot Time", "="*40)
# boot_time_timestamp = psutil.boot_time()
# bt = datetime.fromtimestamp(boot_time_timestamp)
# print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# ======= CPU Information ================
# print("="*40, "CPU Info", "="*40)
# print("Physical cores:", psutil.cpu_count(logical=False))
# print("Total cores:", psutil.cpu_count(logical=True))

# CPU frequencies
# cpufreq = psutil.cpu_freq()
# print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
# print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
# print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

# CPU usage
# print("CPU Usage Per Core:")
# for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
#     print(f"Core {i}: {percentage}%")
# print(f"Total CPU Usage: {psutil.cpu_percent()}%")

# Getting load over15 minutes
# load1, load5, load15 = psutil.getloadavg()
# cpu_usage = (load15/os.cpu_count()) * 100
# print("The CPU usage in 1 min is : ", load1)

# get system times for : 
# times() -> (utime, stime, cutime, cstime, elapsed_time)
# print('======= system times =============')
# print(os.times.__doc__)
# times = os.times()
# print(times)

# >>>>>>>>>>> one second check cpu usage <<<<<<<<<<<<<<
# cpus = psutil.cpu_percent(interval=1)
# print(cpus)

# cpu_times = psutil.cpu_times()
# print(cpu_times)

# =========  Memory Information  ==========
# print("="*40, "Memory Information", "="*40)
# # get the memory details
# svmem = psutil.virtual_memory()
# print(f"Total: {get_size(svmem.total)}")
# print(f"Available: {get_size(svmem.available)}")
# print(f"Used: {get_size(svmem.used)}")
# print(f"Percentage: {svmem.percent}%")
# print("="*20, "SWAP", "="*20)
# # get the swap memory details (if exists)
# swap = psutil.swap_memory()
# print(f"Total: {get_size(swap.total)}")
# print(f"Free: {get_size(swap.free)}")
# print(f"Used: {get_size(swap.used)}")
# print(f"Percentage: {swap.percent}%")

# =========  Disk Information  ============
# print("="*40, "Disk Information", "="*40)
# print("Partitions and Usage:")
# # get all disk partitions
# partitions = psutil.disk_partitions()
# for partition in partitions:
#     print(f"=== Device: {partition.device} ===")
#     print(f"  Mountpoint: {partition.mountpoint}")
#     print(f"  File system type: {partition.fstype}")
#     try:
#         partition_usage = psutil.disk_usage(partition.mountpoint)
#     except PermissionError:
#         # this can be catched due to the disk that
#         # isn't ready
#         continue
#     print(f"  Total Size: {get_size(partition_usage.total)}")
#     print(f"  Used: {get_size(partition_usage.used)}")
#     print(f"  Free: {get_size(partition_usage.free)}")
#     print(f"  Percentage: {partition_usage.percent}%")
# # get IO statistics since boot
# disk_io = psutil.disk_io_counters()
# TODO: Drawing computer status with urwid
# http://urwid.org/

# and collecting data with:
# https://psutil.readthedocs.io/en/latest/
# https://github.com/giampaolo/psutil

# Reference:
# https://www.thepythoncode.com/article/get-hardware-system-information-python
# https://www.thepythoncode.com/code/make-process-monitor-python



# using top command in MacOS:
# % top -l3 -n10 > library/top_data.txt

# top command doc:
# https://ss64.com/osx/top.html


# install psutil:
# % pip install psutil

# print(f"Total read: {get_size(disk_io.read_bytes)}")
# print(f"Total write: {get_size(disk_io.write_bytes)}")


# =========  Network information  =========
# print("="*40, "Network Information", "="*40)
# # get all network interfaces (virtual and physical)
# if_addrs = psutil.net_if_addrs()
# for interface_name, interface_addresses in if_addrs.items():
#     for address in interface_addresses:
#         print(f"=== Interface: {interface_name} ===")
#         if str(address.family) == 'AddressFamily.AF_INET':
#             print(f"  IP Address: {address.address}")
#             print(f"  Netmask: {address.netmask}")
#             print(f"  Broadcast IP: {address.broadcast}")
#         elif str(address.family) == 'AddressFamily.AF_PACKET':
#             print(f"  MAC Address: {address.address}")
#             print(f"  Netmask: {address.netmask}")
#             print(f"  Broadcast MAC: {address.broadcast}")
# # get IO statistics since boot
# net_io = psutil.net_io_counters()
# print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
# print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")


# ==========  Process list  =================

# for proc in psutil.process_iter(['pid', 'name', 'username']):
#   print(proc.info)

