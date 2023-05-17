import json


#Programa principal
def run():
    
    rutina_1 = input("Introduce la rutina inicial: ")
    rutina_2 = input("introduce la rutina a unir: ")


    #Concatenación juntas traseras
    with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/' + rutina_1 + r'_PT.json') as f:
        PT_1 = json.load(f)
    
    with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/' + rutina_2 + r'_PT.json') as f:
        PT_2 = json.load(f)
    
    size_PT_1 = len(PT_1[0])
    size_PT_2 = len(PT_2[0])

    q0v = PT_1[0][:size_PT_1//2] + PT_2[0][:size_PT_2//2] + PT_2[0][size_PT_2//2:] + PT_1[0][size_PT_1//2:]
    q1v = PT_1[1][:size_PT_1//2] + PT_2[1][:size_PT_2//2] + PT_2[1][size_PT_2//2:] + PT_1[1][size_PT_1//2:]
    q2v = PT_1[2][:size_PT_1//2] + PT_2[2][:size_PT_2//2] + PT_2[2][size_PT_2//2:] + PT_1[2][size_PT_1//2:]

    #Creación de JSON para su facil acceso
    juntas = {
        'q0v' : q0v,
        'q1v' : q1v,
        'q2v' : q2v
    }

    #Guardado del archivo JSON
    with open(r'data/rutinas_py/'+rutina_2+r'_PT.json', 'w+') as f:
        json.dump(juntas, f)  

    print("Calculo juntas traseras: Listo!")


    #Concatentación juntas delanteras
    with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/' + rutina_1 + r'_PD.json') as f:
        PD_1 = json.load(f)
    
    with open(r'/home/gato/TT2/programa_gato/data/rutinas_py/' + rutina_2 + r'_PD.json') as f:
        PD_2 = json.load(f)
    
    size_PD_1 = len(PD_1[0])
    size_PD_2 = len(PD_2[0])

    q0v = PD_1[0][:size_PD_1//2] + PD_2[0][:size_PD_2//2] + PD_2[0][size_PD_2//2:] + PD_1[0][size_PD_1//2:]
    q1v = PD_1[1][:size_PD_1//2] + PD_2[1][:size_PD_2//2] + PD_2[1][size_PD_2//2:] + PD_1[1][size_PD_1//2:]
    q2v = PD_1[2][:size_PD_1//2] + PD_2[2][:size_PD_2//2] + PD_2[2][size_PD_2//2:] + PD_1[2][size_PD_1//2:]

    #Creación de JSON para su facil acceso
    juntas = {
        'q0v' : q0v,
        'q1v' : q1v,
        'q2v' : q2v
    }

    #Guardado del archivo JSON
    with open(r'data/rutinas_py/'+rutina_2+r'_PD.json', 'w+') as f:
        json.dump(juntas, f)  

    print("Calculo juntas delanteras: Listo!")


#Entry point
if __name__ == '__main__':
    run()