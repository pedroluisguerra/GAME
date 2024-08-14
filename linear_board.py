from settings import BOARD_LENGTH, VICTORY_STRIKE
from lits_utils import *

class LinearBoard:
    '''
    clase que representa un tablero de una sola columna
    x un jugador
    o otro jugador
    None un espacio vacío
    '''
    def __init__(self):
        '''
        Una lista None
        '''
        self._column = [None for i in range(BOARD_LENGTH)]
        
    def add(self, char):
        '''
        Juega en la primera posición disponible
        '''
        #Siempre y cuando no esté lleno...
        if not self.is_full():
        #Buscamos la primera posición disponible (None)
        #Lo sustituimos por char
           i = self._column.index(None)
           self._column[i] = char       
    
    def is_full(self):
        return self._column[-1] != None
    
    
    def is_victory(self, char):
        return find_streak(self._column, char, VICTORY_STRIKE)
    
    def is_tie(self, char1, char2):
        '''
        No hay victoria ni del char1 ni del char2
        '''
        return (self.is_victory('x') == False) and (self.is_victory('o') == False)
        

