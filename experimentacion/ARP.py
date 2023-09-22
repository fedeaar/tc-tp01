from scapy.all import ARP, sniff

# Create an empty list to store ARP packet information
arp_packets = {}
# Define a callback function to process ARP packets
def procesar_paquetes(packet):
    if ARP in packet:
        psrc = packet[ARP].psrc
        pdst = packet[ARP].pdst
        direcciones = (psrc, pdst)
        if direcciones in arp_packets:
            arp_packets[direcciones] += 1
        else:
            arp_packets[direcciones] = 1

        print(f"-({psrc}, {pdst})->;)")



# Start capturing ARP packets
try:
    sniff(filter="arp", prn=procesar_paquetes, store=False, count=1000)
except KeyboardInterrupt:
    pass
