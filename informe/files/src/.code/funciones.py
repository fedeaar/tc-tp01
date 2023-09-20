def informacion(ps):
    """
    ps es la probabilidad de ocurrencia
    del simbolo s en la fuente.
    """
    i = -np.log2(ps)
    return i

def entropia(S):
    """
    S es una lista con las probabilidades
    de cada simbolo en la fuente.
    """
    e = np.sum([(ps) * informacion(ps) for ps in S])
    return e
