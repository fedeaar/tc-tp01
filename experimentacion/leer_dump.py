import re
import numpy as np

def informacion(ps):
    i = -np.log2(ps)
    return i

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

def mostrar_fuente(S):
    N = sum(S.values())
    simbolos = sorted(S.items(), key=lambda x: -x[1])
    print("\n".join([ "%s, q: %d, p: %.5f, i: %.5f" % (d, k, k/N, informacion(k/N)) for d,k in simbolos ]))
    
if __name__ == "__main__":

    path = "./fede-reposo.txt"
    S = leer_dump(path)
    print(S)
    print(mostrar_fuente(S))
    print(f"e={entropia(S)}")
