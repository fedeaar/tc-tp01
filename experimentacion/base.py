#!/usr/bin/env python3
from scapy.all import *
import time

S1 = {}

def callback(pkt):
    if pkt.haslayer(Ether):
        dire = "BROADCAST" if pkt[Ether].dst=="ff:ff:ff:ff:ff:ff" else "UNICAST"
        tipo = IP if pkt.haslayer(IP) else Ether
        proto = pkt[Ether].type # El campo type del frame tiene el protocolo
        print(f"{pkt[tipo].src} -({dire}, {proto})-> {pkt[tipo].dst}")

if __name__ == "__main__":
    inicio = time.time()
    sniff(prn=callback, count=10000)
    fin = time.time()
    print(fin - inicio)
