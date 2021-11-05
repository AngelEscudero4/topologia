from practica1.Complejo import Complejo
import triangDelaunay as pr2

import numpy as np
import matplotlib as plt
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

'''
----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------
                            PRACTICA 2
----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------
'''

'''
PARA EJECUTAR ELEGIR NUMERO DE EJEMPLO QUE SE QUIERE HACER
'''
ejemplo = 1
points = []

# EJEMPLO 1
if ejemplo == 1:
    points = np.array([(0.38021546727456423, 0.46419202339598786), (0.7951628297672293, 0.49263630135869474),
                       (0.566623772375203, 0.038325621649018426), (0.3369306814864865, 0.7103735061134965),
                       (0.08272837815822842, 0.2263273314352896), (0.5180166301873989, 0.6271769943824689),
                       (0.33691411899985035, 0.8402045183219995), (0.33244488399729255, 0.4524636520475205),
                       (0.11778991601260325, 0.6657734204021165), (0.9384303415747769, 0.2313873874340855)])

# EJEMPLO 2
elif ejemplo == 2:
    points = np.array([[0.8957641450573793, 0.2950833519989374],
                       [0.028621391963087994, 0.9440875759025237],
                       [0.517621505875702, 0.1236620161847416],
                       [0.7871047164191424, 0.7777474116014623],
                       [0.21869796914805273, 0.7233589914276723],
                       [0.9891035292480995, 0.6032186214942837],
                       [0.30113764052453484, 0.613321425324272],
                       [0.18407448222466916, 0.7868606964403773],
                       [0.4496777667376678, 0.874366215574117],
                       [0.08225571534539433, 0.616710205071694]])

# EJEMPLO 3
elif ejemplo == 3:
    points = np.array([(0.8753299639906736, 0.5452963206013219),
                       (0.915335120559448, 0.8622822047328554),
                       (0.9411759819184322, 0.2748278885761678),
                       (0.7052034033196758, 0.8122389578499669),
                       (0.9734431558329487, 0.5500672178217452),
                       (0.101349658961157, 0.6072126518098413),
                       (0.6099428935549683, 0.5095146187792166),
                       (0.6810379648990679, 0.6343196355745316),
                       (0.763747595111296, 0.6389758508715849),
                       (0.6521290891236327, 0.28340359060768416),
                       (0.4569706839687516, 0.5970966728571825),
                       (0.3339042514617916, 0.7888181435443109),
                       (0.24447615661103717, 0.18247811626397858),
                       (0.6961254832425103, 0.9974914431850389),
                       (0.2452860638322797, 0.2974794924024807),
                       (0.09631846692736679, 0.2887656085651358),
                       (0.638575556222527, 0.26034722595932536),
                       (0.803241921795395, 0.24803894619975986),
                       (0.8809182300057703, 0.3389661339754195),
                       (0.3565859265456749, 0.25327819736066515)])

# EJEMPLO 4
elif ejemplo == 4:
    points = np.array([[0.7649936, -6.49105706],
                       [-0.26047978, 3.17414802],
                       [5.16486466, -2.77709227],
                       [6.3630621, 2.08442442],
                       [1.63681198, 4.95671697],
                       [-4.47103343, -0.4944843],
                       [-2.12035066, 4.80887876],
                       [-3.44986384, -3.25828704],
                       [-3.55428879, 3.18415674],
                       [-0.27202076, 3.89295058],
                       [-2.9512385, 5.76602403],
                       [6.36747098, -1.44195299],
                       [3.36400365, 4.33230353],
                       [3.23972602, -3.44494391],
                       [-3.29551494, 0.50827386],
                       [-1.55188576, 3.42645393],
                       [-3.62672644, -3.14264111],
                       [3.54177077, -4.42486894],
                       [-6.39734363, 1.37489294],
                       [4.46578318, -0.76225718]])

vor = Voronoi(points)

alpha = pr2.alphaComplejo(points)

print('(25). Filtracion del complejo ordenado por umbral\n', alpha.filtrationOrder())
print('(26). Lista de umbrales\n', alpha.pesos)

pr2.filtracionAlphaComplejoPlot(alpha, 0.26, 'complejo_r026', points)

'''
Para hector es esto:

for value in alpha.thresholdvalues():
K=alpha.sublevel(value)
plotalpha(points,K)
plt.show()
'''

pr2.printearAlphaComplejoGIF(alpha, points)

VR = pr2.VietorisRips(points)
print(VR.filtrationOrder())
print(VR.pesos)
