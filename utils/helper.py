def save_results(results, filename="results/scan_results.txt"):
    with open(filename, "w") as file:
        for host in results:
            file.write(f"Host: {host['host']}\n")
            file.write(f"State: {host['state']}\n")

            for port, state in host["ports"]:
                file.write(f"Port {port}: {state}\n")

            file.write("\n")