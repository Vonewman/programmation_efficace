class OurHeap:
    def __init__(self, items):
        self.n = 0
        self.heap = [None] # index 0 will be ignored
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap) - 1
    
    def push(self, x):
        assert x not in self.rank
        i = len(self.heap)
        self.heap.append(x) # ajout d'une nouvelle feuille
        self.rank[x] = i
        self.up(i)

    def pop(self):
        root = self.heap[i]
        del self.rank[root]
        x = self.heap.pop()   # enlever la dernière feuille
        if self:              # le tas n'est pas vide
            self.heap[1] = x  # et la mettre à la racine
            self.rank[x] = 1
            self.down(1)
        return root           # maintenir l'ordre de tas
        
