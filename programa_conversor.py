
import pandas 

def cm_a_pulgadas(cm):
    return cm / 2.54


#leer el archivo excel:
df = pandas.read_excel("muebles_medidas.xlsx")

#añadir una columna al dataFrame que sea de pulgadas y se rellene con el calculo de cm /2.54
df ["Pulgadas"] = df ["Centimetros"].apply(cm_a_pulgadas)

df.to_excel("muebles_medidas_convertidad.xlsx", index=False)

print("Conversion completada y guardad en un nuevo archivo llamado 'muebles_medidas_convertidad.xlsx' ")
