import cv2

# Nombre del archivo de video
filename = "D:/TRABAJOS RICARDO/Semestre_13/PFG/Repositorio/Mingle/downsample/30min_day1_cam1_20fps_960x540.mp4"

# Cantidad de frames por guardar durante cada segundo de video
desiredfps = 1

# Cargando el archivo
cap = cv2.VideoCapture(filename)

# Obtiene el número de frames por segundo del video
fps = cap.get(cv2.CAP_PROP_FPS)

# Obteniendo el primer frame
ret, frame1 = cap.read()

# Contador para darle nombre a las imágenes
count = 0

# Loop del video
while True:
    # Obteniendo el siguiente frame
    ret, frame2 = cap.read()
    
    # Termina loop cuando se recorren todos los frames
    if not ret:
        break
    
    # Si ha pasado suficiente tiempo desde el último frame comparado
    if count % (fps/desiredfps) == 0:

        # Convirtiendo las imgs a escala de grises
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        # Calculando la diferencia entre frames
        diff = cv2.absdiff(gray1, gray2)

        # Binarizando la imagen
        _, diff = cv2.threshold(diff, 255*0.1, 255, cv2.THRESH_BINARY)

        # Mostrando la imagen de diferencia
        #cv2.imshow('Difference', diff)

        # Wait for a key press
        if cv2.waitKey(1) == ord('q'):
            break

        # Contador de pixeles iguales
        pixeles_negros = gray1.size - cv2.countNonZero(diff)
        percentage = float(pixeles_negros/gray1.size*100)

        # Save the number of zero pixels to a CSV file
        with open('pixeles_negros.csv', 'a') as f:
            f.write(str(percentage) + '\n')

        # Set frame2 as the new frame1
        frame1 = frame2

    # Incrementa el contador
    count += 1



# Release the video capture and close the window
cap.release()
print("Píxeles x frame: ", gray1.size)
cv2.destroyAllWindows()
