import matplotlib.pyplot as plt
import numpy as np
import leer_dump

def graficar(data1, data2, data3, opciones):
    
    combined_data = {}
    for key in set(data1.keys()).union(data2.keys()).union(data3.keys()):
        combined_data[key] = [opciones["apply"](key, x) for x in [data1, data2, data3]]

    keys = list(combined_data.keys())
    keys.sort()
    categories = [f'{key[0][0]}: {key[1]}' for key in keys]
    values1, values2, values3 = zip(*[combined_data[key] for key in keys])

    plt.figure()
    width = 0.2  # Ancho de las barras

    plt.bar(np.arange(len(categories)), values1, width, label='red 1')
    plt.bar(np.arange(len(categories)) + width, values2, width, label='red 2')
    plt.bar(np.arange(len(categories)) + 2 * width, values3, width, label='red 3')


    plt.xticks(np.arange(len(categories)) + width, categories, rotation=45, fontsize=15)
    plt.xlabel('Símbolo', fontsize=15)
    plt.ylabel(opciones["ylabel"], fontsize=15)
    # plt.title(opciones["titulo"])
    # plt.yscale('log')

    plt.legend(fontsize=15)
    plt.tight_layout()
    plt.savefig(opciones["save-as"])

def graficar_medidas(experimento):
    S1, ts1 = leer_dump.leer_dump(f"./out/natan-{experimento}.txt")    
    S2, ts2 = leer_dump.leer_dump(f"./out/manu-{experimento}.txt")
    S3, ts3 = leer_dump.leer_dump(f"./out/fede-{experimento}.txt")

    print(f"red 1, expermiento: {experimento}")
    print(leer_dump.mostrar_fuente(S1))
    print(f"e={leer_dump.entropia(S1)}")

    print(f"red 2, expermiento: {experimento}")
    print(leer_dump.mostrar_fuente(S2))
    print(f"e={leer_dump.entropia(S2)}")

    print(f"red 3, expermiento: {experimento}")
    print(leer_dump.mostrar_fuente(S3))
    print(f"e={leer_dump.entropia(S3)}")

    graficar(S1, S2, S3, {
        "save-as": f"./out/{experimento}-probabilidad.jpg",
        "titulo": f"Probabilidad de ocurrencia por símbolo, redes en {experimento}",
        "apply": lambda key, x: x.get(key, 0) / np.sum(list(x.values())),
        "ylabel": "probabilidad"
    })    
    graficar(S1, S2, S3, {
        "save-as": f"./out/{experimento}-informacion.jpg",
        "titulo": f"Información por símbolo, redes en {experimento}",
        "apply": lambda key, x: leer_dump.informacion(x.get(key, 0) / np.sum(list(x.values()))),
        "ylabel": "información"
    })
    print("entropia en %s para S1: %.5f, S2: %.5f, S3: %.5f" % 
          (experimento, leer_dump.entropia(S1), leer_dump.entropia(S2), leer_dump.entropia(S3)))
    print("tiempo en lograr 10000 tramas en %s para S1: %s, S2: %s, S3: %s" % 
          (experimento, ts1, ts2, ts3))


if __name__ == "__main__":

   graficar_medidas("actividad")
   graficar_medidas("reposo")
