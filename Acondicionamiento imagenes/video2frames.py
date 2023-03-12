import cv2
import os

def video2framnes(framejump, day, cam):
    # Nombre del archivo de video
    filename = "D:/TRABAJOS RICARDO/Semestre_13/PFG/Repositorio/Mingle/downsample/30min_day" + str(day) + "_cam" + str(cam) +"_20fps_960x540.mp4"

    # Directorio donde se guardarán las imágenes
    dirbase = 'Frames/Entradas/Day'
    dirname = dirbase + str(day) + "/Cam" + str(cam) + "/"

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
            cv2.imwrite(dirname + "frame" + str(count) + "_day" + str(day) + "_cam" + str(cam) + ".png", frame)

        # Incrementa el contador
        count += 1

        # Lee el siguiente frame
        success, frame = cap.read()

    # Cierra el archivo de video
    cap.release()


#day_list = [1, 2, 3]
#cam_list = [1, 2, 3]
#
#for nday in day_list:
#    for ncam in cam_list:
#        video2framnes(framejump=20, day=nday, cam=ncam)
#        print(nday, ncam)

