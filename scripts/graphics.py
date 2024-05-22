import win32com.client

def get_graphics_info():
    wmi = win32com.client.GetObject("winmgmts:\\\\.\\root\\CIMV2")
    video_controllers = wmi.ExecQuery("SELECT * FROM Win32_VideoController")

    graphics_info = {}

    for controller in video_controllers:
        graphics_info = {
            "Name": controller.Name,
            "Adapter Type": controller.AdapterCompatibility,
            "Adapter Description": controller.Description,
            "Adapter RAM": f"{int(controller.AdapterRAM) / (1024**3):.2f} GB ({controller.AdapterRAM} bytes)",
            "Driver Version": controller.DriverVersion,
            "Resolution": f"{controller.CurrentHorizontalResolution} x {controller.CurrentVerticalResolution} x {controller.CurrentRefreshRate} hertz",
            "Bits/Pixel": str(controller.CurrentBitsPerPixel)
        }
     
        break

    return graphics_info
