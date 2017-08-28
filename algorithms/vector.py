"""
Implementação de Estruturas de Dados do livro Data Structures & Algorithms in Python
"""

class Vector:
    """Representa um vetor multidimensional"""

    def __init__(self, d):
        """Cria um vetor de d diemnsões com coordenadas 0"""
        self._coords = [0] * d # (0,...,0)
    
    def  __len__(self):
        """Retorna o número de dimensões do vetor"""
        return len(self._coords)

    def __getitem__(self, pos):
        """Retorna o valor da coordenada na posição"""
        return self._coords[pos]

    def __setitem__(self, pos, val):
        """Seta o valor da coordenada em pos para val"""
        self._coords[pos] = val

    def __add__(self, other):
        """Retorna a soma de dois vetores"""
        if len(self) != len(other):
            raise ValueError('As dimensões devem ser iguais')

        result = Vector(len(self)) # inicia um novo array do tamanho do próprio
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __eq__(self, other):
        """Retorna True se possuir as mesmas coordenadas que o outro vetor"""
        return self._coords == other._coords

    def __ne__(self, other):
        """Retorna True se o vetor não é igual ao outro"""
        return not self == other

    def __str__(self):
        """String representando o vetor"""
        return '<{}>'.format(self._coords)
