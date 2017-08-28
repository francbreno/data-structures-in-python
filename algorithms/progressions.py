"""
Implementação de Estruturas de Dados do livro Data Structures & Algorithms in Python
"""

class Progression:
    """Iterator que produz uma progressão numérica genérica"""

    def __init__(self, start=0):
        """Inicializa com _current tendo o valor inicial"""
        self._current = start
    
    def _advance(self):
        """Atualiza o valor corrente, _current, da progressão.
        
        Deve ser sobrescrito pelas subclasses para o tipo de progressão desejada.
        """
        self._current += 1

    def __next__(self):
        """Retorna o próximo elemento da progressão ou Lança StopIteration() se valor corrent é None"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """Um iterator deve retornar ele mesmo como o iterator da classe"""
        return self

    def print_progression(self, n):
        """Imprime os n primeiro valores da progressão"""
        print(' '.join(str(next(self)) for i in range(n)))

class ArithmeticProgression(Progression):
    """Iterator que produz uma progressão aritmética"""

    def __init__(self, increment=1, start=0):
        """Inicializa a progressão definindo seu elemento inicial e o incremento

            increment   A constante a ser adiciona para cada elemento para obter o próximo (defalt 1)
            start       O primeiro elemento (posição) da progressão (default 0)   
        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Atualiza o valor corrente adicionando o incremento"""
        self._current += self._increment

class GeometricProgression(Progression):
    """Iterator que produz uma progressão geométrica"""
    
    def __init__(self, base=2, start=1):
        """Inicializa a progressão definindo a base e o início
        
        base    O valor constante que irá multiplicar cada termo da progressão (default 2)
        start   O primeiro termo da progressão (defatul 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Atualiza o valor corrente multiplicando pela base"""
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator que produz uma progressão(série) de Fibonacci"""

    def __init__(self, first=0, second=1):
        """Inicializa a progressão definindo o primeiro e segundo elementos
        
        first   O primeiro termo da progressão (default 0)
        second  O segundo termo da progressão (default 1)
        """
        super().__init__(first)
        self._prev = second - first # synthetic previous

    def _advance(self):
        """Atualiza o valor corrente somandos os 2 anteriores"""
        self._prev, self._current = self._current, self._prev + self._current