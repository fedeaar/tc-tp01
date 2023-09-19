#!/usr/bin/env python3
from scapy.all import *
import numpy as np

S1 = {}

def informacion(ps):
    i = -np.log2(ps)
    return i

def entropia(S): # S = [ps ... ]
    N = sum(S.values())
    e = np.sum([ps * informacion(ps/N) for ps in S.values()])
    return e

def mostrar_informacion(S):
    N = sum(S.values())
    for s in S:
        print(f"s={s} p={S[s]} i={informacion(S[s]/N)}")
    print(f"e={entropia(S)}")

def mostrar_fuente(S):
    N = sum(S.values())
    simbolos = sorted(S.items(), key=lambda x: -x[1])
    print("\n".join([ "%s : %.5f" % (d,k/N) for d,k in simbolos ]))

def callback(pkt):
    if pkt.haslayer(Ether):
        dire = "BROADCAST" if pkt[Ether].dst=="ff:ff:ff:ff:ff:ff" else "UNICAST"
        tipo = IP if pkt.haslayer(IP) else Ether
        proto = pkt[Ether].type # El campo type del frame tiene el protocolo
        print(f"{pkt[tipo].src} -({dire}, {proto})-> {pkt[tipo].dst}")
        s_i = (dire, proto) # Aca se define el simbolo de la fuente
        if s_i not in S1:
            S1[s_i] = 0.0
        S1[s_i] += 1.0

if __name__ == "__main__":
    
    sniff(prn=callback, count=10000)
    mostrar_fuente(S1)
    mostrar_informacion(S1)
