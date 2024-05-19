import psutil
import socket
import dns.resolver
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
                'is_up': stats.isup,
                'speed': stats.speed,
                'mtu': stats.mtu,
                'mac_address': None,
                'ip_address': None,
                'netmask': None,
                'broadcast_ip': None,
                'default_dns': None,
                'alternative_dns': None,
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

    # Get DNS servers
    dns_resolvers = dns.resolver.Resolver()
    dns_servers = dns_resolvers.nameservers
    if dns_servers:
        wifi_info.update({
            'default_dns': dns_servers[0] if len(dns_servers) > 0 else None,
            'alternative_dns': dns_servers[1] if len(dns_servers) > 1 else None
        })

    return wifi_info

if __name__ == "__main__":
    wifi_info = get_wifi_info()
    print("WiFi Adapter Info:")
    print(wifi_info)
