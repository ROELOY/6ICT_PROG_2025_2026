def voeg_toe_anders(x,y):
    "return de som van x en y op een andere manier"


print( voeg_toe_anders(3,5) )    # 8
print( voeg_toe_anders(2,9) )    # 11
print( voeg_toe_anders(-3,5) )   # 2

# oplossing

def voeg_toe_anders(x,y):
    "return de som van x en y op een andere manier"
    som = x + y
    return som

print( voeg_toe_anders(3,5) )    # 8
print( voeg_toe_anders(2,9) )    # 11
print( voeg_toe_anders(-3,5) )   # 2