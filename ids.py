from scapy.all import *
import threading
import time

# Define lists to store detected intrusions and other packets
intrusions = []
non_intrusions = []
stop_sniffing_flag = False
sniffing_thread = None

# Define a function to detect specific types of packets
def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        packet_info = {
            "source_ip": packet[IP].src,
            "source_port": packet[TCP].sport,
            "destination_ip": packet[IP].dst,
            "destination_port": packet[TCP].dport,
            "protocol": "TCP" if packet.haslayer(TCP) else "Other"
        }
        if packet[TCP].flags == "S":
            packet_info["type"] = "Intrusion"
            intrusions.append(packet_info)
            if len(intrusions) > 6:
                intrusions.pop(0)
            print(f"Intrusion detected: {packet_info}")
        else:
            packet_info["type"] = "Non-intrusion"
            non_intrusions.append(packet_info)
            if len(non_intrusions) > 6:
                non_intrusions.pop(0)
            print(f"Non-intrusion packet: {packet_info}")
    else:
        print("Packet without IP or TCP layer:", packet.summary())

# Define a function to start packet sniffing
def start_sniffing():
    global stop_sniffing_flag
    stop_sniffing_flag = False
    print("Starting packet sniffing...")
    while not stop_sniffing_flag:
        sniff(filter="tcp", prn=packet_callback, store=0, timeout=5)
    print("Packet sniffing stopped.")

# Function to start sniffing in a separate thread
def initiate_sniffing():
    global sniffing_thread
    if sniffing_thread is None or not sniffing_thread.is_alive():
        sniffing_thread = threading.Thread(target=start_sniffing)
        sniffing_thread.start()

# Function to stop sniffing
def stop_sniffing():
    global stop_sniffing_flag
    stop_sniffing_flag = True

# Start sniffing thread (optional, only if you want to start sniffing on script start)
# initiate_sniffing()
