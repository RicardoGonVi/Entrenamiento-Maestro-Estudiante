import cv2

# Nombre del archivo de video
filevideo = "D:/TRABAJOS RICARDO/Semestre_13/PFG/Repositorio/Mingle/downsample/30min_day1_cam1_20fps_960x540.mp4"

# Genera un archivo con los % de diferencia entre dos framse de un video
def ceropixels_vs_t2frames(desiredfps, thvalue):

    # Cargando el archivo
    cap = cv2.VideoCapture(filevideo)

    # Obtiene el número de frames por segundo del video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Obteniendo el primer frame
    ret, frame1 = cap.read()

    # Contador para saber cuantos frames se han procesado
    count = 0

    # Archivo donde se guardan los resultados
    fileresults = "Diff2frames/Prueba" + str(fps/desiredfps) + "fps" + str(thvalue) + "th.csv"

    # Loop del video
    while True:
        # Obteniendo el siguiente frame
        ret, frame2 = cap.read()
        
        # Termina loop cuando se recorren todos los frames
        if not ret:
            break
        
        # Calcula la diferencia entre 2 frames cada x frames / s
        if count % (desiredfps) == 0 and count != 0:

            # Convirtiendo las imgs a escala de gris
            gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            # Calculando la diferencia entre frames
            diff = cv2.absdiff(gray1, gray2)

            # Binarizando la imagen
            _, diff = cv2.threshold(diff, thvalue, 255, cv2.THRESH_BINARY)

            # Mostrando la imagen de diferencia
            #cv2.imshow('Difference', diff)

            # Wait for a key press
            #if cv2.waitKey(1) == ord('q'):
            #    break

            # Contador de pixeles iguales
            pixeles_negros = gray1.size - cv2.countNonZero(diff)
            percentage = float(pixeles_negros/gray1.size*100)

            # Save the number of zero pixels to a CSV file
            with open(fileresults, 'a') as f:
                f.write(str(percentage) + '\n')

            # Set frame2 as the new frame1
            frame1 = frame2

        # Incrementa el contador
        count += 1

    # Release the video capture and close the window
    cap.release()
    print("Píxeles x frame: ", gray1.size)
    cv2.destroyAllWindows()


#desiredfps_list = [20, 10, 5, 1]
thvalue_list = [0, 1, 25, 127]
desiredfps_list = [40, 80, 160, 320]
combination_list = []

for nFPS in desiredfps_list:
    for nTH in thvalue_list:
        ceropixels_vs_t2frames(nFPS, nTH)
