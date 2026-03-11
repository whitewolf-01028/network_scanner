import nmap

def scan_network(target):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=target, arguments='-sV')

    results = []

    for host in scanner.all_hosts():
        host_data = {
            "host": host,
            "state": scanner[host].state(),
            "ports": []
        }

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()

            for port in ports:
                state = scanner[host][proto][port]['state']
                host_data["ports"].append((port, state))

        results.append(host_data)

    return results