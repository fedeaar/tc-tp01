import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
data1 = {
    ('UNICAST', 2048): 9430,
    ('UNICAST', 2054): 932,
    ('UNICAST', 34525): 234,
    ('BROADCAST', 2048): 453,
}

data2 = {
    ('UNICAST', 2048): 95430,
    ('UNICAST', 2054): 4120,
    ('BROADCAST', 2054): 130,
}

data3 = {
    ('UNICAST', 2048): 342,
    ('UNICAST', 2054): 124123,
    ('UNICAST', 34525): 234,
    ('BROADCAST', 2054): 2342344,
    ('BROADCAST', 2048): 11230,
}

# Crear un diccionario combinado con valores predeterminados de 0
combined_data = {}
for key in set(data1.keys()).union(data2.keys()).union(data3.keys()):
    combined_data[key] = [data1.get(key, 0), data2.get(key, 0), data3.get(key, 0)]

# Separar los datos combinados en listas de etiquetas y valores
categories = [f'{key[0]}, {key[1]}' for key in combined_data.keys()]
values1, values2, values3 = zip(*combined_data.values())

# Crear el gráfico de barras
plt.figure()
width = 0.2  # Ancho de las barras

# Barras para el conjunto de datos 1
plt.bar(np.arange(len(categories)), values1, width, label='Conjunto de Datos 1')

# Barras para el conjunto de datos 2
plt.bar(np.arange(len(categories)) + width, values2, width, label='Conjunto de Datos 2')

# Barras para el conjunto de datos 3
plt.bar(np.arange(len(categories)) + 2 * width, values3, width, label='Conjunto de Datos 3')

# Configuración del eje x
plt.xticks(np.arange(len(categories)) + width, categories, rotation=45)

# Etiquetas y título
plt.xlabel('Combinación de Clave')
plt.ylabel('Valor')
plt.title('Gráfico de Barras de los 3 Conjuntos de Datos')
plt.yscale('log')

# Leyenda
plt.legend()

# Mostrar el gráfico de barras combinado
plt.tight_layout()
plt.show()
