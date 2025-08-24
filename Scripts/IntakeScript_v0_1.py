import platform
import psutil
import GPUtil



def get_size(bytes, suffix="B"):
    """
    Scale bytes to proper format
    """
    
    factor = 1024 # Base amount of bits
    for unit in ["", "K", "M", "G", "T", "P"]: # Included petabytes in case I have acces to a server at any point
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

platname = platform.uname()

f = open (f"{platform}.txt", "a")

cpufreq = psutil.cpu_freq() #cpu frequencies
svmem = psutil.virtual_memory() #virtual memory
swap = psutil.swap_memory() #swap total if exist

# ORDER FOR THE CSV
# 1. System
# 2. Node
# 3. Release
# 4. version
# 5. Machine
# 6. Processor
# 7. CPU Physical Corres
# 8. CPU Logical Cores
# 9. CPU max frequency
# 10. CPU min frequency
# 11. Virtual Memory Size
# 12. Virtual Memory Open
# 13. Virtual Memory Used
# 14. Virtual Memory Percent
# 15. Swap Memory Size
# 16. Swap Memory Open
# 17. Swap Memory Used
# 18. Swap Memory Percent
# 19. Storage device information
# 20. Network information
# 21. GPU information



# This is steps 1-18
f.write(f"{platname.system},{platname.node},{platname.release},{platname.version},{platname.machine},{platname.processor},{psutil.cpu_count(logical=False)},{psutil.cpu_count(logical=True)},{cpufreq.max:.2f}Mhz,{cpufreq.min:.2f}Mhz,{get_size(svmem.total)},{get_size(svmem.available)},{get_size(svmem.used)},{svmem.percent}%,{get_size(swap.total)},{get_size(swap.free)},{get_size(swap.used)},{swap.percent}%,")


# This is the information in step 19
partitions = psutil.disk_partitions()

for partition in partitions:
    f.write(f"{partition.device},{partition.mountpoint},{partition.fstype},")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    f.write(f"{get_size(partition_usage.total)},{get_size(partition_usage.used)},{get_size(partition_usage.free)},{partition_usage.percent}%,")

disk_io = psutil.disk_io_counters()
f.write(f"{get_size(disk_io.read_bytes)},{get_size(disk_io.write_bytes)},")


# This is the information in step 20
if_addrs = psutil.net_if_addrs()

for interface_name, interface_address in if_addrs.items():
    for address in interface_address:
        f.write(f"{interface_name},")
        if str(address.family) == 'AddressFamily.AF_INET':
            f.write(f"{address.address},{address.netmask},{address.broadcast},")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            f.write(f"{address.address},{address.netmask},{address.broadcast},")


# This is the information in Step 21
gpus = GPUtil.getGPUS()

for gpu in gpus:
    gpu_id = gpu.id
    gpu_name = gpu.name
    gpu_total_memory =  f"{gpu.mnemoryUsed}MB"
    gpu_uuid = gpu.uuid
    f.write(f"{gpu_id},{gpu_name},{gpu_total_memory},{gpu_uuid}")
