import wmi
import time
import psutil

def get_cpu_usage():
    c = wmi.WMI()
    cpu_usage = 0
    for cpu in c.Win32_PerfFormattedData_PerfOS_Processor():
        cpu_usage += int(cpu.PercentProcessorTime)
    return cpu_usage


def get_memory_usage():
    c = wmi.WMI()
    memory_total = 0
    memory_free = 0
    for memory in c.Win32_OperatingSystem():
        memory_total = int(memory.TotalVisibleMemorySize)
        memory_free = int(memory.FreePhysicalMemory)
    memory_used = memory_total - memory_free
    memory_percent = (memory_used / memory_total) * 100
    return memory_percent

def get_disk_activity():
    disk_io_counters = psutil.disk_io_counters()
    current_read_count = disk_io_counters.read_count
    current_write_count = disk_io_counters.write_count
    current_time = time.time()

    # Calculate time elapsed since previous measurement
    time_elapsed = current_time - get_disk_activity.previous_time

    # Calculate read and write counts during the interval
    read_count_diff = current_read_count - get_disk_activity.previous_read_count
    write_count_diff = current_write_count - get_disk_activity.previous_write_count

    # Calculate total number of operations during the interval
    total_operations = read_count_diff + write_count_diff

    # Get the number of CPU cores
    num_cores = psutil.cpu_count()

    # Calculate the maximum theoretical disk activity (assuming 100% utilization of all cores)
    max_disk_activity = num_cores * 100

    # Calculate the normalized disk activity percentage
    disk_activity_percentage = (total_operations / (time_elapsed * max_disk_activity)) * 100

    # Update previous values for next iteration
    get_disk_activity.previous_read_count = current_read_count
    get_disk_activity.previous_write_count = current_write_count
    get_disk_activity.previous_time = current_time

    return disk_activity_percentage 

# Initialize static variables
get_disk_activity.previous_read_count = psutil.disk_io_counters().read_count
get_disk_activity.previous_write_count = psutil.disk_io_counters().write_count
get_disk_activity.previous_time = time.time()

if __name__ == "__main__":
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_activity = get_disk_activity()
        print(f"CPU Usage: {cpu_usage:.2f}%")
        print(f"Memory Usage: {memory_usage:.2f}%")
        print(f"Disk Activity: {disk_activity:.2f}%")
        time.sleep(1)  # Update every second
