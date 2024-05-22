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
            ethernet_info = {
                'connection_status': 'connected' if stats.isup else 'disconnected',
                'speed':f"{stats.speed} Mbps",
                'mtu': stats.mtu,
                'mac_address': 'N/A',
                'ip_address': 'N/A',
                'netmask': 'N/A',
                'broadcast_ip': 'N/A',
                'default_dns': 'N/A',
                'alternative_dns': 'N/A',
                'default_gateway': 'N/A',
                'model': adapter_models[interface]
            }
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    ethernet_info['mac_address'] = addr.address
                elif addr.family == socket.AF_INET:
                    ethernet_info['ip_address'] = addr.address
                    ethernet_info['netmask'] = addr.netmask
            
            # Get default gateway
            gateways = psutil.net_if_addrs()
            gws = psutil.net_if_stats()
            default_gateway = psutil.net_if_stats()
            if 'default' in default_gateway and default_gateway['default'].get(socket.AF_INET):
                ethernet_info['default_gateway'] = default_gateway['default'][socket.AF_INET][0]

            break  # Assuming you only want information about the first connected Ethernet interface

    # Get DNS servers
    dns_resolvers = dns.resolver.Resolver()
    dns_servers = dns_resolvers.nameservers
    if dns_servers:
        ethernet_info['default_dns'] = dns_servers[0] if len(dns_servers) > 0 else None
        ethernet_info['alternative_dns'] = dns_servers[1] if len(dns_servers) > 1 else None

    return ethernet_info
