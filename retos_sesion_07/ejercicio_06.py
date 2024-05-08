from keyword import iskeyword

# Agregar 5 Ejemplos con otras funciones no vistas en la sesión

# str.zfill(width)

print("42".zfill(5))
print("-42".zfill(5))

# str.removesuffix(suffix, /)

print('MiscTests'.removesuffix('Tests'))
print('TmpDirMixin'.removesuffix('Tests'))

# str.removeprefix(prefix, /)

print('TestHook'.removeprefix('Test'))
print('BaseTestCase'.removeprefix('Test'))

# str.isupper()

print('BANANA'.isupper())
print('banana'.isupper())
print('baNana'.isupper())
print(' '.isupper())

# str.isidentifier()

print('spam'.isidentifier())
print('_spam'.isidentifier())
print('spam_'.isidentifier())
print('spam-egg'.isidentifier())
print('spam-egg'.isidentifier()) 
