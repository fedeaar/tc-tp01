import matplotlib.pyplot as plt
import numpy as np
import leer_dump

def graficar(S1, S2, S3):
    simbolos = set()
    simbolos.update(S1.keys())
    simbolos.update(S2.keys())
    simbolos.update(S3.keys())

    x = np.arange(len(simbolos))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in simbolos.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Length (mm)')
    ax.set_title('Penguin attributes by species')
    ax.set_xticks(x + width, simbolos)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 250)

    plt.show()
    
def graficar_reposo():
    S1 = leer_dump.leer_dump("./out/fede-reposo.txt")    
    S2 = leer_dump.leer_dump("./out/natan-reposo.txt")
    S3 = leer_dump.leer_dump("./out/manu-reposo.txt")
    graficar(S1, S2, S3)    

if __name__ == "__main__":

   graficar_reposo()