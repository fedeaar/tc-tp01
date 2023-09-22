from scapy.all import ARP, sniff

# Create an empty list to store ARP packet information
arp_packets = {}
# Define a callback function to process ARP packets
def procesar_paquetes(packet):
    if ARP in packet:
        direcciones = (packet[ARP].psrc, packet[ARP].pdst)
        if direcciones in arp_packets:
            arp_packets[direcciones] += 1
        else:
            arp_packets[direcciones] = 1

        print(f"ARP: {direcciones}")



# Start capturing ARP packets
try:
    print("Capturando Paquetes de ARP:")
    print("Presionar Ctrl+C para finalizar")
    sniff(filter="arp", prn=procesar_paquetes, store=False)
except KeyboardInterrupt:
    pass

print('\n')
for (src, dst) in arp_packets:
    print(f"SRC_IP: {src}, DST_IP: {dst} COUNT: {arp_packets[(src, dst)]}")

