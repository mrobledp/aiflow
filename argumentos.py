import sys

print(type(sys.argv))
print(132*'*')
print('Los argumentos de la línea de comando son:')
for i in sys.argv:
    print(i)
print(132*'*')
