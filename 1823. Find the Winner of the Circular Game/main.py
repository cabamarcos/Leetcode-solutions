class Solution(object):
    def findTheWinner(self, n, k):
        lista = list(range(1, n + 1))
        i = 0

        while len(lista) > 1:
            i = (i + k - 1) % len(lista)
            lista.pop(i)

        return lista[0]
