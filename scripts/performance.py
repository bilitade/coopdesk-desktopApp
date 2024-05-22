import psutil

class Performance:
    def get_cpu_percent(self):
        return psutil.cpu_percent()

    def get_cpu_frequency(self):
        cpu_freq = psutil.cpu_freq()
        return cpu_freq.current

    def get_memory_info(self):
        memory = psutil.virtual_memory()
        memory_total_gb = round(memory.total / (1024 ** 3), 2)  # Convert to GB
        memory_used_gb = round(memory.used / (1024 ** 3), 2)  # Convert to GB
        
        return memory.percent, memory_total_gb, memory_used_gb

