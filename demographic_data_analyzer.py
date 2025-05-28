import pandas as pd


def calcular_datos_demograficos(print_data=True):
    # Leer datos del archivo CSV
    df = pd.read_csv("adult.data.csv")

    # Cuantas personas de cada raza están representados en este conjunto de datos
    # Debería ser una serie de Pandas con nombres de raza como etiquetas de índice.
    conteo_raza = df['raza'].value_counts()

    # Edad promedio de los hombres
    edad_promedioH = round( df.groupby('sexo')['edad'].mean()['Hombre'], 1 )

    # Porcentaje de personas con título
    porcentaje_bachiller = round( df['education'].value_counts(normalize=True)['Bachillerato'] * 100.0, 1 )

    # Que porcentaje de personas con educación avanzada (título, máster o doctorado) ganan más de 50K?
    # Que porcentaje de personas sin educación avanzada ganan más de 50K?


    #round(100* / , 1 )
    # con y sin educación avanzada
    educacion_alta =  df.loc[df['educacion'].isin(['Bachillerato', 'Maestria', 'Doctorado'])]
    educacion_baja = df.loc[~df['educacion'].isin(['Bachillerato', 'Maestria', 'Doctorado'])]

    # porcentaje con salario > 50K
    educacion_alta_ricos = round(100.0 * (educacion_alta['salario'] == '> 50K').sum() / len(educacion_alta), 1 )
    educacion_baja_ricos = round(100.0 * (educacion_baja['salario'] == '> 50K').sum() / len(educacion_baja), 1 )


    # cual es el número mínimo de horas que una persona trabaja por semana?
    horas_mini_min = df['Horas-por-semana'].min()

    # cual es el porcentaje de personas que trabajan el número mínimo de horas por semana y ganan más de 50K?
    trabajador_mini_min = df.loc[df['horas-por-semana'] == horas_mini_min]

    porcentaje_riqueza = round(100.0 * (trabajador_mini_min['salario'] == '> 50K').sum() / len(trabajador_mini_min) , 1 )

    # que país tiene el porcentaje más alto de personas que ganan más de 50K?
    pais_ganancia_alta = None
    porcentaje_pais_ganancia_alta = 0.0
    for pais, dato in df.groupby('pais-nativo'):
        porcentaje = (dato['salario'] == '>50K').sum() / dato['salario'].count()
        if porcentaje_pais_ganancia_alta < porcentaje:
            porcentaje_pais_ganancia_alta = porcentaje
            pais_ganancia_alta = pais
    porcentaje_pais_ganancia_alta = round(100 * porcentaje_pais_ganancia_alta,1)


    # identificar la ocupación más común de las personas de India que ganan más de 50K
    ocupacion_mas_alta = df[(df['salario'] == '>50K') & (df['pais-nativo'] == 'India')]['ocupacion'].value_counts().keys()[0]

    # NO MODIFICAR NADA DE AQUÍ EN ADELANTE

    if print_data:
        print("Number of each race:\n", conteo_raza) 
        print("Average age of men:", edad_promedioH)
        print(f"Percentage with Bachelors degrees: {porcentaje_bachiller}%")
        print(f"Percentage with higher education that earn >50K: {educacion_alta_ricos}%")
        print(f"Percentage without higher education that earn >50K: {educacion_baja_ricos}%")
        print(f"Min work time: {horas_mini_min} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {porcentaje_riqueza}%")
        print("Country with highest percentage of rich:", pais_ganancia_alta)
        print(f"Highest percentage of rich people in country: {porcentaje_pais_ganancia_alta}%")
        print("Top occupations in India:", ocupacion_mas_alta)

    return {
        'race_count': conteo_raza,
        'average_age_men': edad_promedioH,
        'percentage_bachelors': porcentaje_bachiller,
        'higher_education_rich': educacion_alta_ricos,
        'lower_education_rich': educacion_baja_ricos,
        'min_work_hours': horas_mini_min,
        'rich_percentage': porcentaje_riqueza,
        'highest_earning_country': pais_ganancia_alta,
        'highest_earning_country_percentage':
        porcentaje_pais_ganancia_alta,
        'top_IN_occupation': ocupacion_mas_alta
    }