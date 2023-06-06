from playsound import playsound

#Reproduce el audio que se encuentre en la ruta
def reproducir_audio(ruta_audio='/home/gato/TT2/programa_gato/data/audios/gato_2.mp3'):
    playsound(ruta_audio)


#Entry point
if __name__ == '__main__':
    print('This is a module')