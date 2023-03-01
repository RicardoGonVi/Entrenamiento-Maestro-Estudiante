import cv2
import os

# Nombre del archivo de video
filename = "D:/TRABAJOS RICARDO/Semestre_13/PFG/Repositorio/Mingle/downsample/30min_day1_cam1_20fps_960x540.mp4"
filename = "C:/Users/ragv1/OneDrive/Escritorio/video_cam3_22-02-2023 11_42_01.avi"



# Directorio donde se guardarán las imágenes
dirname = 'Frames'

# Saltos entre frames
framejump = 1

# Crea el directorio si aún no existe
if not os.path.exists(dirname):
    os.makedirs(dirname)

# Abre el archivo de video
cap = cv2.VideoCapture(filename)

# Obtiene el número de frames por segundo del video
#fps = cap.get(cv2.CAP_PROP_FPS)

# Lee el primer frame del video
success, frame = cap.read()

# Contador para darle nombre a las imágenes
count = 0

# Lee frames hasta que no hay más
while success:

    # Si ha pasado suficiente tiempo desde el último frame guardado
    if count % (framejump) == 0:

        # Guarda el frame actual como imagen
        cv2.imwrite(os.path.join(dirname, 'frame{:04d}.jpg'.format(count)), frame)

    # Incrementa el contador
    count += 1

    # Lee el siguiente frame
    success, frame = cap.read()

# Cierra el archivo de video
cap.release()
