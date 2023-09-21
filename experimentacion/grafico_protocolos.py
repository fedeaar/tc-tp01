import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    ('UNICAST', 2048): 95430,
    ('UNICAST', 2054): 4120,
    ('UNICAST', 34525): 310,
    ('BROADCAST', 2054): 130,
    ('BROADCAST', 2048): 10,
}

# Separar los datos en listas de etiquetas y valores
labels = [f'{key[0]}, {key[1]}' for key in data.keys()]
values = list(data.values())

# Crear el gráfico de barras
plt.bar(labels, values)

# Etiquetas y título
plt.xlabel('Tipo de Tráfico, Número')
plt.ylabel('Valor')
plt.title('Gráfico de Barras')

# Rotar las etiquetas del eje x para mejorar la legibilidad
plt.xticks(rotation=45, ha="right")
plt.yscale('log')
# Mostrar el gráfico
plt.tight_layout()
plt.show()
