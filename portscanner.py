import socket

def get_accessible_ports(address, min_port, max_port):
    found_ports = []
    for port in range(min_port, max_port + 1):
        print(f"Checking port {port}...")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(15) #setting timeout for the connection
                result = sock.connect_ex((address, port)) # Returns the error indicator
            
                if result == 0:
                    print(f"Port {port} is open")
                    found_ports.append(port)
                else:
                    print(f"Port {port} is closed or filtered. Error: {result}")
        except socket.error as e:
            print(f"Socket error on port {port}: {e}")
        except Exception as e:
            print(f"General error on port {port}: {e}")
                
    return found_ports


def main():
    address = input("Enter the address to scan: ")
    min_port = int(input("Enter the minimum port number: "))
    max_port = int(input("Enter the maximum port number: "))
    ports = get_accessible_ports(address, min_port, max_port)
    
    if ports:
        print("Open ports: ")
        for p in ports:
            print(p)
    else:
        print("No open ports found.")
        
if __name__== "__main__":
    main()
