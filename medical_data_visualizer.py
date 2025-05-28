import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# añadir columna de 'sobrepeso'
df['overweight'] = (df['weight']/((df['height']/100)**2) > 25).astype(int)

# Normalizar los datos estableciendo que 0 siempre sea bueno y 1 siempre malo. Si el valor de "colesterol" o "gluc" es 1, establezca el valor en 0. Si el valor es mayor que 1, establezca el valor en 1.
df[['gluc','cholesterol']] = (df[['gluc','cholesterol']] > 1).astype(int)

# Dibujar la gráfica de barras
def dib_graf_barras():
    # crear el dataframe para la gráfica de barras
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # Agrupar y reformatear los datos para dividirlos por cardio. Muestre los recuentos de cada característica. Deberá renombrar una de las columnas para que la grafica de barras funcione correctamente.
    #df_cat = None

    # Dibujar la gráfica de barras con 'sns.catplot()'
    fig = sns.catplot(data = df_cat, kind='count',  x='variable', hue='value', col='cardio').set(ylabel = 'total').fig


    # No modifique nada de lo que hay debajo de este comentario
    fig.savefig('catplot.png')
    return fig


# Dibujar el mapa de calor
def dib_mapa_calor():
    # Limpia los datos eliminando las filas donde la presión arterial sistólica sea menor o igual a la presión arterial diastólica, y donde la altura y el peso estén fuera del 2.5% y 97.5% de sus respectivos percentiles.
    df_calor = df[ 
        ( df['ap_lo'] <= df['ap_hi'] ) & 
        ( df['height'] >= df['height'].quantile(0.025) ) & 
        ( df['height'] <= df['height'].quantile(0.975) ) & 
        ( df['weight'] >= df['weight'].quantile(0.025) ) & 
        ( df['weight'] <= df['weight'].quantile(0.975) ) 
    ]

    # Calcular la matriz de correlación
    Mat_corr = df_calor.corr()

    # Generar una máscara para la parte superior de la matriz de correlación
    Corr_Mask = np.triu(Mat_corr)


    # Configurar el tamaño de la figura
    fig, ax =  plt.subplots()
    
    # Dibujar el mapa de calor con 'sns.heatmap()'
    ax = sns.heatmap(Mat_corr, mask=Corr_Mask, annot=True, fmt='0.1f', square=True)


    # No modifique nada de lo que hay debajo de este comentario
    fig.savefig('heatmap.png')
    return fig