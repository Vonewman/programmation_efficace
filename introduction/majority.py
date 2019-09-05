def majority(L):
    """
    Ce programme permet de trouver l'élément majoritaire d'un tableau
    """
    compte = {}
    for mot in compte:
        if mot in compte:
            compte[mot] += 1
        else:
            compte[mot] = 1
    valmin, argmin = min((-compte[mot], mot) for mot in compte)
    return argmin
    

