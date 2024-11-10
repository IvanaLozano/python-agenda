
import pandas 

data = {
    "Piezas": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros": [40, 120, 60, 80, 160]

}

df = pandas.DataFrame(data)

#Guardar el DataFrame en un archivo de Excel
df.to_excel("muebles_medidas.xlsx", index=False)