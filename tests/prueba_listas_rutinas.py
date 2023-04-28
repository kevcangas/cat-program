from mat4py import loadmat


PT = loadmat(r'data/rutinas/reposo_PT.mat')
print(PT['q1v'])


PT = loadmat(r'data/rutinas/pie_PD.mat')
for i in PT['q0v']:
    print(i*180/3.1416+90)