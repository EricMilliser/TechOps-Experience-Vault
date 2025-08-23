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


f.write(f"System: {platname.system},Node Name: {platname.node},Release: {platname.release},Version: {platname.version},Machine: {platname.machine},Processor: {platname.processor},Physical Cores: {psutil.cpu_count(logical=False)},Total Cores: {psutil.cpu_count(logical=True)},Max Frequency: {cpufreq.max:.2f}Mhz,Min Frequency: {cpufreq.min:.2f}Mhz,Virtual Memory Total: {get_size(svmem.total)},Virtual Memory Available: {get_size(svmem.available)},Virtual Memory Used: {get_size(svmem.used)},Virtual Memory Percentage: {svmem.percent}%,Swap Memory Total: {get_size(swap.total)},Swap Memory Free: {get_size(swap.free)},Swap Memory Used: {get_size(swap.used)},Swap Memory Percentage: {swap.percent}%,")

partitions = psutil.disk_partitions()

for partition in partitions:
    f.write(f"Storage Device: {partition.device},Mountpoint: {partition.mountpoint},File System Type: {partition.fstype},")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    f.write(f"Total Size: {get_size(partition_usage.total)},Used: {get_size(partition_usage.used)},Free: {get_size(partition_usage.free)},Percentage: {partition_usage.percent}%,")

disk_io = psutil.disk_io_counters()
f.write(f"Total read: {get_size(disk_io.read_bytes)},Total write: {get_size(disk_io.write_bytes)},")

if_addrs = psutil.net_if_addrs()

for interface_name, interface_address in if_addrs.items():
    for address in interface_address:
        f.write(f"Inferface: {interface_name},")
        if str(address.family) == 'AddressFamily.AF_INET':
            f.write(f"IP Address: {address.address},Netmask {address.netmask},Broadcase IP: {address.broadcast},")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            f.write(f"MAC Addres: {address.address},Netmask: {address.netmask}, Broadcast MAC: {address.broadcast},")

gpus = GPUtil.getGPUS()

for gpu in gpus:
    gpu_id = gpu.id
    gpu_name = gpu.name
    gpu_total_memory =  f"{gpu.mnemoryUsed}MB"
    gpu_uuid = gpu.uuid
    f.write(f"GPU ID: {gpu_id},GPU Name: {gpu_name},GPU Total Memory: {gpu_total_memory},GPU UUID: {gpu_uuid}")
