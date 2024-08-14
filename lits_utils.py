def find_one(list, needle):
    '''
    Devuelve True si encuentra una o más ocurrencias de needle en list
    
    # inicializamos el bool que representa la condición de haber encontrado o no y el índice
    found = False
    index = 0
    # Mientras no encuentre o hayamos terminado con la lista
    while not found and index < len(list):
    # Miramos a ver si está en la posición actual y actualizamos la condición
      if needle == list[index]:
         found = True
      # Avanzamos al siguiente elemento
      index = index + 1
    # Devolvemos si hemos encontrado o no
    '''
    return find_n(list, needle, 1)

def find_n(list, needle, n):
   '''
   Devuelve True si en list hay en n o más ocurrencias de needle
   False si hay menos o si n < 0
   '''
   # Si n < 0 devolvemos False
   if n >= 0:
     # Inicializamos el índice y el contador
     index = 0
     count = 0
     # Mientras no hayamos encontrado al elemento n veces o no hayamos terminado la lista...
     while count < n and index < len(list):
        # si lo encontrados, actualizamos el contador
        if needle == list[index]:
         count = count + 1
        # Avanzamos al siguiente elemento
        index = index +1 
        # Devolvemos el resutado de comparar el contador con n
     return count >= n
   
   else:
      return False
   
def find_streak(list, needle, n):
   """
    Devuelve True si en list hay n o más needles seguidos
    False, para todo lo demás
    """
    # si n >= 0
   if n >= 0:
        #Inicializo el indice, el contador y el indicador de racha
        index = 0
        count = 0
        streak = False

        # Mientras no haya encontradoa n seguidos u la lista no se haya acabao....
        while count < n and index < len(list):
            # si lo encuentro, activo el indicado de rachas y actualizo el contador
            if needle == list[index]:
                streak = True
                count = count + 1
            else:
                # si no lo encuentro, desactivo el indicador de de racha y pongo a cero el contador
                streak = False
                count =0
            
            # avanzo al siguiente elemento
            index = index + 1
        
        # devolvemos el resultado de comparar el contador con n SIEMPRE Y CUANDO  estemos en racha
        return count >= n and streak
   else:
        # para valores de n < 0, no tiene sentido
        return False