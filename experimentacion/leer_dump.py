import re
import numpy as np

def informacion(ps):
    i = -np.log2(ps)
    return i

def leer_IPs(S):
    ips = {}
    for s in S:
        ip1, ip2 = s[0], s[1]
        if ip1 not in ips:
            ips[ip1] = 0.0
        ips[ip1] += S[s]
        if ip2 not in ips:
            ips[ip2] = 0.0
        ips[ip2] += S[s]
    return ips

def entropia(S): # S = { s: q }
    N = sum(S.values())
    e = np.sum([(k/N) * informacion(k/N) for k in S.values()])
    return e

def leer_dump(path):
    S = {}
    pattern = re.compile(r'\-\((\w+), (\d+)\)\-\>')
    time_pattern = re.compile(r'time\:(.*)')
    with open(path, 'r', errors='ignore') as file:
        time = None
        for line in file:
            match_time = time_pattern.search(line)
            if (match_time != None):
                time = match_time.group(1)
                continue
            match = pattern.search(line)
            dire = match.group(1)
            proto = match.group(2)           
            s_i = (dire, proto) # Aca se define el simbolo de la fuente
            if s_i not in S:
                S[s_i] = 0.0
            S[s_i] += 1.0
        
    return S, time

def leer_ARP(path):
    S = {}
    pattern = re.compile(r'\((\d+\.\d+\.\d+\.\d+), (\d+\.\d+\.\d+\.\d+)\)')
    with open(path, 'r', errors='ignore') as file:
        for line in file:
            matches = pattern.findall(line)
            for match in matches:
                src = match[0]  # Extract the source IP
                dst = match[1]  # Extract the destination IP
                s_i = (src, dst)  # Define the symbol for the source-destination pair

                if s_i not in S:
                    S[s_i] = 0.0
                S[s_i] += 1.0
        
    return S

def mostrar_fuente(S):
    N = sum(S.values())
    simbolos = sorted(S.items(), key=lambda x: -x[1])
    print("\n".join([ "%s, q: %d, p: %.5f, i: %.5f" % (d, k, k/N, informacion(k/N)) for d,k in simbolos ]))

    
if __name__ == "__main__":

    path1 = "./out/fede-ARP.txt"
    path2 = "./out/natan-ARP.txt"
    path3 = "./out/manu-ARP.txt"
    S1 = leer_ARP(path1)
    S2 = leer_ARP(path2)
    S3 = leer_ARP(path3)
    mostrar_fuente(S1)
    mostrar_fuente(S2)
    mostrar_fuente(S3)

