import psutil
import socket
import wmi

def get_wifi_info():
    c = wmi.WMI()
    wifi_models = {}

    # Get adapter models and filter only WiFi
    for nic in c.Win32_NetworkAdapter():
        if nic.NetConnectionID and "Wi-Fi" in nic.NetConnectionID:
            wifi_models[nic.NetConnectionID] = nic.Name

    wifi_info = {}

    # Function to get WiFi adapter information
    def get_info(interface, adapter_models, adapter_info):
        if psutil.net_if_stats()[interface].isup:
            addrs = psutil.net_if_addrs()[interface]
            stats = psutil.net_if_stats()[interface]
            adapter_info.update({
                'is_up': 'connected' if stats.isup else 'disconnected',
                'speed': f"{stats.speed} Mbps",
                'mac_address': 'N/A',
                'ip_address': 'N/A',
                'netmask': 'N/A',
                'broadcast_ip': 'N/A',
                'default_dns': 'N/A',
                'alternative_dns': 'N/A',
                'model': adapter_models[interface]
            })
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    adapter_info['mac_address'] = addr.address
                elif addr.family == socket.AF_INET:
                    adapter_info['ip_address'] = addr.address
                    adapter_info['netmask'] = addr.netmask

    # Get WiFi adapter information
    for interface in wifi_models:
        get_info(interface, wifi_models, wifi_info)
        # Only consider the first active Wi-Fi adapter
        break

    # Function to parse network interface addresses for DNS servers
    def get_dns_servers(interface_name):
        dns_servers = []
        for nic in psutil.net_if_addrs().get(interface_name, []):
            if nic.family == socket.AF_INET:
                dns_servers.append(nic.address)
        return dns_servers

    # Get DNS servers specific to the WiFi interface
    for interface in wifi_models:
        dns_servers = get_dns_servers(interface)
        if dns_servers:
            wifi_info.update({
                'default_dns': dns_servers[0] if len(dns_servers) > 0 else None,
                'alternative_dns':str( dns_servers[1]) if len(dns_servers) > 1 else 'N/A'
            })
        break

    return wifi_info


