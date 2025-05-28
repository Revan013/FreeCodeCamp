import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def dib_grafica():
    # Leer datos del archivo CSV
    df = pd.read_csv('epa-sea-level.csv')
    # Crear el gráfico de dispersión
    fig, ax = plt.subplots()
    ax.scatter(x= "Año", y = "Nivel del mar ajustado por CSIRO", data = df)
    # Crear la primera línea de mejor ajuste
    pendiente, interc, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    años = pd.Series(range(1880,2050))
    ax.plot(años, interc + pendiente*años, 'r', label='primera línea de mejor ajuste')
    # Crear 
    df2 = df.loc[df["Year"] >= 2000]
    pendiente2, interc2, r_value2, p_value2, std_err2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    años2 = pd.Series(range(2000,2050))
    ax.plot(años2, interc2 + pendiente2*años2, 'b', label='segunda línea de mejor ajuste')
    # Add labels and title
    ax.set(xlabel="Año", ylabel="Nivel del Mar (pulgadas)", title="Aumento del Nivel del Mar")
    # Guardar el gráfico y regresar los datos (NO MODIFICAR)
    plt.savefig('sea_level_plot.png')
    return plt.gca()