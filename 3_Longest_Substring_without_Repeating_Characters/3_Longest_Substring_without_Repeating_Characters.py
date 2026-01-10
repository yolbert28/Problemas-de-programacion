
def Longest_Substring_without_Repeating_Characters(s: str):
    
    # Cuenta la cantidad de caracteres consecutivos
    characters_counter = 0
    
    # Almacena el número máximo de caracteres que ha tenido un substring
    max_count = 0
    
    # Almacena el substring con la cantidad máxima de caracteres
    substring = ""
    
    # Aquí se almacenaran los caracteres que vayamos encontrando
    characters = set()
    
    # Almacena el substring que se esta evaluando
    aux_substring = ""
    
    for character in s:
        if character not in characters:
            characters.add(character)
            characters_counter += 1
            aux_substring += character
            
            if characters_counter > max_count:
                substring = aux_substring
                max_count = characters_counter
        else:
            # Esta parte fue adaptada para cumplir con la respuesta del ejemplo 3, pero tambien se puede resolver como:
            # characters.clear()
            # characters_counter = 0
            # aux_substring = ""
            
            characters.clear()
            characters.add(character)
            characters_counter = 1
            aux_substring = character
    
    print(substring)






s = "pwwkew"

Longest_Substring_without_Repeating_Characters(s)