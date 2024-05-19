import win32com.client

def get_important_system_info():
    try:
        wmi = win32com.client.GetObject("winmgmts:\\\\.\\root\\CIMV2")

        # Get Operating System information
        os_info = wmi.ExecQuery("SELECT * FROM Win32_OperatingSystem")[0]
        os_data = {
            "OS Name": os_info.Caption,
            "Version": os_info.Version,
            "OS Manufacturer": os_info.Manufacturer,
            "Installed RAM": f"{int(os_info.TotalVisibleMemorySize) / 1024/1024 :.2f} GB",
           
        }

        # Get Computer System information
        comp_info = wmi.ExecQuery("SELECT * FROM Win32_ComputerSystem")[0]
        comp_data = {
            "System Name": comp_info.Name,
            "System Manufacturer": comp_info.Manufacturer,
            "System Model": comp_info.Model,
            "System Type": comp_info.SystemType,        }

        # Get Processor information
        processor_info = wmi.ExecQuery("SELECT * FROM Win32_Processor")[0]
        proc_data = {
            "Processor Name": processor_info.Name,
            "Processor Manufacturer": processor_info.Manufacturer,
            "Processor Max Clock Speed": f"{processor_info.MaxClockSpeed} MHz",
            "Number of Cores": processor_info.NumberOfCores,
            "Number of Logical Processors": processor_info.NumberOfLogicalProcessors
        }

        # Merge dictionaries
        system_data = {**proc_data,**comp_data, **os_data, }
        return system_data

    except Exception as e:
        print("An error occurred while retrieving system information:", str(e))
        return None

if __name__ == "__main__":
    system_info = get_important_system_info()
    if system_info:
        for key, value in system_info.items():
            print(f"{key}: {value}")
