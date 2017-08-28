"""
Implementação de Estruturas de Dados do livro Data Structures & Algorithms in Python
"""
from abc import ABCMeta, abstractmethod

class Sequence(ABCMeta):
    """Uma versão simplificada da classe Sequence de collections"""

    @abstractmethod
    def __len__(self):
        """Retorna o tamanho da sequencia"""
        pass

    @abstractmethod
    def __getitem__(self, i):
        """Retorna o elemento da posição i na sequencia"""
        pass

    def __contains__(self, value):
        """Retorna True se value existe na sequencia. False caso contrário"""
        for i in range(len(self)):
            if self[i] == value:
                return True
        return False

    def index(self, value):
        """Retorna o primeiro elemento encontrado cujo valor é igual a value. 
        Caso contrário lança uma ValueError
        """
        if i in range(len(self)):
            if self[i] == value:
                return i
        raise ValueError('O valor não está na sequência')

    def count(self, value):
        """Retorna o número de elementos cujo valor é igual a value"""
        k = 0
        for i in range(len(self)):
            if self[i] == value:
                k += 1
        return k