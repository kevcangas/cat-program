import json


#Programa principal
def run():
    
    rutina_1 = 'pie'
    rutina_2 = 'caminar'


    #Concatenación juntas traseras
    with open(r'./data/rutinas_py/' + rutina_1 + r'_PT.json') as f:
        PT_1 = json.load(f)
    
    with open(r'./data/rutinas_py/' + rutina_2 + r'_PT.json') as f:
        PT_2 = json.load(f)
    
    size_PT_1 = len(PT_1['q0v'])
    size_PT_2 = len(PT_2['q0v'])

    q0v = PT_1['q0v'][:size_PT_1//2] + [PT_1['q0v'][size_PT_1//2] for _ in range(0,300)] +PT_2['q0v'][size_PT_1+size_PT_1//2:2*size_PT_1] + PT_2['q0v'][2*size_PT_1:2*size_PT_1 + size_PT_1//2] + [PT_1['q0v'][size_PT_1//2] for _ in range(0,300)] + PT_1['q0v'][size_PT_1//2:]
    q1v = PT_1['q1v'][:size_PT_1//2] + [PT_1['q1v'][size_PT_1//2] for _ in range(0,300)] +PT_2['q1v'][size_PT_1+size_PT_1//2:2*size_PT_1] + PT_2['q1v'][2*size_PT_1:2*size_PT_1 + size_PT_1//2] + [PT_1['q1v'][size_PT_1//2] for _ in range(0,300)] + PT_1['q1v'][size_PT_1//2:]
    q2v = PT_1['q2v'][:size_PT_1//2] + [PT_1['q2v'][size_PT_1//2] for _ in range(0,300)] +PT_2['q2v'][size_PT_1+size_PT_1//2:2*size_PT_1] + PT_2['q2v'][2*size_PT_1:2*size_PT_1 + size_PT_1//2] + [PT_1['q2v'][size_PT_1//2] for _ in range(0,300)] + PT_1['q2v'][size_PT_1//2:]

    print(f"Tamaño pata delantera: {len(q0v)}")
    #Creación de JSON para su facil acceso
    juntas = {
        'q0v' : q0v,
        'q1v' : q1v,
        'q2v' : q2v
    }

    #Guardado del archivo JSON
    with open(r'data/rutinas_py/'+'caminando'+r'_PT.json', 'w+') as f:
        json.dump(juntas, f)  

    print("Calculo juntas traseras: Listo!")


    #Concatentación juntas delanteras
    with open(r'./data/rutinas_py/' + rutina_1 + r'_PD.json') as f:
        PD_1 = json.load(f)
    
    with open(r'./data/rutinas_py/' + rutina_2 + r'_PD.json') as f:
        PD_2 = json.load(f)
    
    size_PD_1 = len(PD_1['q0v'])
    
    q0v = PD_1['q0v'][:size_PD_1//2] + [PD_1['q0v'][size_PD_1//2] for _ in range(0,300)] + PD_2['q0v'][size_PT_1+size_PT_1//2:2*size_PT_1] + PD_2['q0v'][2*size_PT_1:2*size_PT_1 + size_PT_1//2] + [PD_1['q0v'][size_PD_1//2] for _ in range(0,300)] + PD_1['q0v'][size_PD_1//2:]
    q1v = PD_1['q1v'][:size_PD_1//2] + [PD_1['q1v'][size_PD_1//2] for _ in range(0,300)] + PD_2['q1v'][size_PT_1+size_PT_1//2:2*size_PT_1] + PD_2['q1v'][2*size_PT_1:2*size_PT_1 + size_PT_1//2] + [PD_1['q1v'][size_PD_1//2] for _ in range(0,300)] + PD_1['q1v'][size_PD_1//2:]
    q2v = PD_1['q2v'][:size_PD_1//2] + [PD_1['q2v'][size_PD_1//2] for _ in range(0,300)] + PD_2['q2v'][size_PT_1+size_PT_1//2:2*size_PT_1] + PD_2['q2v'][2*size_PT_1:2*size_PT_1 + size_PT_1//2] + [PD_1['q2v'][size_PD_1//2] for _ in range(0,300)] + PD_1['q2v'][size_PD_1//2:]

    print(f"Tamaño pata delantera: {len(q0v)}")
    #Creación de JSON para su facil acceso
    juntas = {
        'q0v' : q0v,
        'q1v' : q1v,
        'q2v' : q2v
    }

    #Guardado del archivo JSON
    with open(r'data/rutinas_py/'+'caminando'+r'_PD.json', 'w+') as f:
        json.dump(juntas, f)  

    print("Calculo juntas delanteras: Listo!")


#Entry point
if __name__ == '__main__':
    run()