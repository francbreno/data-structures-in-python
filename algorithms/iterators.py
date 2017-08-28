"""
Implementação de Estruturas de Dados do livro Data Structures & Algorithms in Python
"""

class SequenceIterator:
    """Um iterator simples. Uma versão simplificada da classe built in range"""
    def __init__(self, sequence):
        """Cria um iterator para a sequência informada"""
        self._seq = sequence
        self._k = -1 # primeiro next incrementa pra 0

    def __next__(self):
        """Retorna o próximo elemento. Caso não exista lança uma StopIteration"""
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        """Retorna um iterator que, por padrão, é o próprio iterator"""
        return self

class Range:
    """Versão simplificada da classe built in Range"""
    def __init__(self, start, stop=None, step=1):
        """Inicializa a instância"""
        if step == 0:
            raise ValueError('Step não pode ser 0')
        
        if stop is None:
            start, stop = 0, start
        
        self._length = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._step = step

    def __len__(self):
        """Retorna o número de entradas no intervalo"""
        return self._length

    def __getitem__(self, k):
        """Retorna o valor no índice k"""
        if k < 0:
            k += len(self)
        
        if not (0 <= k < self._length):
            raise IndexError('Índice fora do intervalo')

        return self._start + k * self._step

    