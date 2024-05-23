import win32com.client

def get_primary_disk_info():
    try:
        wmi = win32com.client.GetObject("winmgmts:\\\\.\\root\\CIMV2")

        # Get Primary Disk Drive information
        disk_drive_info = wmi.ExecQuery("SELECT * FROM Win32_DiskDrive")[0]
        primary_disk_data = {
            "Description": disk_drive_info.Description,
            "Manufacturer": disk_drive_info.Manufacturer,
            "Model": disk_drive_info.Model,
            "Size": f"{int(disk_drive_info.Size) / (1024**3):.2f} GB ({disk_drive_info.Size} bytes)",
            "Partitions":str( disk_drive_info.Partitions),
            "Media Type": disk_drive_info.MediaType,
            "Bytes/Sector": str(disk_drive_info.BytesPerSector)
        }

        return primary_disk_data

    except Exception as e:
        print("An error occurred while retrieving disk information:", str(e))
        return None
print(get_primary_disk_info())