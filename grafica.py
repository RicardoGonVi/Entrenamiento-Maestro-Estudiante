import os
import csv
import numpy as np
import matplotlib.pyplot as plt

# Función que obtiene el número antes de la palabra fps del nombre de un archivo
def filename2number(name_file, frase2search):

    # Busca la palabra fps en el nombre del archivo
    fps_pos = name_file.find(frase2search)

    # Busca el primer digito existente antes de la palabra fps
    digit_pos = fps_pos - 1
    while digit_pos >= 0 and (name_file[digit_pos].isdigit() or name_file[digit_pos] == "."):
        digit_pos -= 1

    # Extrae el número completo antes de la palabra fps
    number = name_file[digit_pos+1 : fps_pos]
    return float(number)

def grafic(dir_path, th_value):
    # Listas de las salidas
    average_list = []
    std_dev_list = []
    fps_list = []

    # Loop de todos los archivos del directorio
    for filename in os.listdir(dir_path):

        # Revisando que sea un .csv
        if filename.endswith(".csv"):
            
            # Agrupando todos los .csv con el mismo threshold
            if filename2number(filename, "th") == th_value:

                # Agregando los fps del archivo a la lista
                fps_list.append(1/filename2number(filename, "fps"))

                # Abriendo el archivo
                with open(os.path.join(dir_path, filename)) as csvfile:

                    # Leyendo el archivo
                    reader = csv.reader(csvfile)

                    # Obteniendo los valores de la primera columna
                    first_col = [float(row[0]) for row in reader]

                    # Calculando la media y las desv estandar
                    average_list.append(np.mean(first_col))
                    std_dev_list.append(np.std(first_col))

    fps_list.sort()
    average_list.sort(reverse=True)
    # Plot the results
    plt.plot(fps_list, average_list, "-o", label = "Threshold: " + str(th_value))
    plt.xlabel("Segundos (s)")
    plt.ylabel("Promedio de píxeles sin variar (%)")
    plt.legend()
    #plt.title("Promedio de píxeles sin variar vs tiempo transcurrido entre cada frame")
    #plt.show()
    plt.savefig("Graficas/Tendencia_th" + str(th_value) + ".png")
    plt.close("all")


# Setea el directorio
directory_path = "D:/TRABAJOS RICARDO/Semestre_13/PFG/Github/Entrenamiento-Maestro-Estudiante/Diff2frames/"

# Lista de posibles th
th_list = [0,1,25,127]

for nTh in th_list:
    grafic(directory_path, nTh)