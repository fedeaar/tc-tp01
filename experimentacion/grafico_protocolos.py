import matplotlib.pyplot as plt
import numpy as np
import leer_dump

def graficar(data1, data2, data3):
    # Crear un diccionario combinado con valores predeterminados de 0
    combined_data = {}
    for key in set(data1.keys()).union(data2.keys()).union(data3.keys()):
        combined_data[key] = [x[key] / np.sum(list(x.values())) for x in [data1, data2, data3]]

    # Separar los datos combinados en listas de etiquetas y valores
    categories = [f'{key[0]}, {key[1]}' for key in combined_data.keys()]
    values1, values2, values3 = zip(*combined_data.values())

    # Crear el gráfico de barras
    plt.figure()
    width = 0.2  # Ancho de las barras

    # Barras para el conjunto de datos 1
    plt.bar(np.arange(len(categories)), values1, width, label='red 1')

    # Barras para el red 2
    plt.bar(np.arange(len(categories)) + width, values2, width, label='red 2')

    # Barras para el red 3
    plt.bar(np.arange(len(categories)) + 2 * width, values3, width, label='red 3')

    # Configuración del eje x
    plt.xticks(np.arange(len(categories)) + width, categories, rotation=45)

    # Etiquetas y título
    plt.xlabel('Simbolo')
    plt.ylabel('Probabilidad')
    plt.title('Gráfico de Barras de las tres redes')
    plt.yscale('log')

    # Leyenda
    plt.legend()

    # Mostrar el gráfico de barras combinado
    plt.tight_layout()
    plt.show()

    
def graficar_reposo():
    S1 = leer_dump.leer_dump("./out/fede-reposo.txt")    
    S2 = leer_dump.leer_dump("./out/natan-reposo.txt")
    S3 = leer_dump.leer_dump("./out/manu-reposo.txt")
    graficar(S1, S2, S3)    

def graficar_intenso():
    S1 = leer_dump.leer_dump("./out/fede-intenso.txt")    
    S2 = leer_dump.leer_dump("./out/natan-intenso.txt")
    S3 = leer_dump.leer_dump("./out/manu-intenso.txt")
    graficar(S1, S2, S3)    

if __name__ == "__main__":

   graficar_reposo()
   graficar_intenso()