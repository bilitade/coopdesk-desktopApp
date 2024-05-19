import psutil
import socket
import dns.resolver
import wmi

def get_ethernet_adapter_info():
    c = wmi.WMI()
    adapter_models = {}

    # Get adapter models and filter only Ethernet
    for nic in c.Win32_NetworkAdapter():
        if nic.NetConnectionID and ("Ethernet" in nic.NetConnectionID or nic.NetConnectionID.startswith("en") or nic.NetConnectionID.startswith("eth")):
            adapter_models[nic.NetConnectionID] = nic.Name

    ethernet_info = {}
    for interface, addrs in psutil.net_if_addrs().items():
        if interface in adapter_models and psutil.net_if_stats()[interface].isup:
            addrs = psutil.net_if_addrs()[interface]
            stats = psutil.net_if_stats()[interface]
            ethernet_info= {
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
            }
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    ethernet_info['mac_address'] = addr.address
                elif addr.family == socket.AF_INET:
                    ethernet_info['ip_address'] = addr.address
                    ethernet_info['netmask'] = addr.netmask
                  

    # Get DNS servers
    dns_resolvers = dns.resolver.Resolver()
    dns_servers = dns_resolvers.nameservers
    if dns_servers:
        for adapter in ethernet_info:
            ethernet_info['default_dns'] = dns_servers[0] if len(dns_servers) > 0 else None
            ethernet_info['alternative_dns'] = dns_servers[1] if len(dns_servers) > 1 else None

    return ethernet_info

if __name__ == "__main__":
    ethernet_adapters_info = get_ethernet_adapter_info()
    print(ethernet_adapters_info)