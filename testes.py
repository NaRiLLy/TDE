import numpy as np

notas = np.array([
    [85, 92, 78],
    [70, 80, 90],
    [62, 75, 80]
])

medias_alunos = np.mean(notas, axis=1)
