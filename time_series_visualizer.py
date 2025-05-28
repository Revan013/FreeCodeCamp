import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Importa los datos del archivo CSV
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date" , parse_dates=True)

# Limpia los datos
df = df[ df["value"].between( df["value"].quantile(.025), df["value"].quantile(.975) ) ]
meses= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def draw_line_plot():
    # Dibuja el gráfico de líneas
    fig, ax = plt.subplots(figsize=(15,5))
    ax = sns.lineplot(data = df, legend="brief")
    ax.set(title='Visitas diarias a la página del foro de freeCodeCamp (5/2016-12/2019)')
    ax.set(xlabel = "Fecha",ylabel = "Visitas de la página")
    # Guarda la imagen y devuelve fig (no cambiar esta parte)
    fig.savefig('line_plot.png')
    return fig

def dib_graf_barras():
    # Copia el DataFrame y agrega columnas de año y mes
    df_barras = df.copy()
    df_barras["year"] = df.index.year.values
    df_barras["month"] = df.index.month_name()
    # Dibuja el gráfico de barras
    fig, ax = plt.subplots(figsize=(15,5))
    
    ax = sns.barplot(x="year", hue="month", y="value", data=df_barras, hue_order = meses, ci=None )
    ax.set(xlabel = "Años",ylabel = "Visitas Promedio de la Página")
    # Guarda la imagen y devuelve fig (no cambiar esta parte)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepara los datos para el box plot
    df_cajas = df.copy()
    df_cajas.reset_index(inplace=True)
    df_cajas['year'] = [d.year for d in df_cajas.date]
    df_cajas['month'] = [d.strftime('%b') for d in df_cajas.date]

    # Dibuja el box plot usando seaborn
    df_cajas['monthnumber'] = df.index.month
    df_cajas = df_cajas.sort_values('monthnumber')
    fig, ax = plt.subplots(1,2,figsize=(16,6))
    sns.boxplot(y = "value", x = "year", data = df_cajas, ax = ax[0] ) 
    ax[0].set(xlabel="Año", ylabel="Visitas de la Página", title="Diagrama de caja anual (tendencia)")
    sns.boxplot(y = "value", x = "month", data = df_cajas, ax = ax[1])
    ax[1].set(xlabel="Mes", ylabel="Visitas de la Página", title="Diagrama de caja mensual (estacionalidad)")
    # Guarda la imagen y devuelve fig (no cambiar esta parte)
    fig.savefig('box_plot.png')
    return fig