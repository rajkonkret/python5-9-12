with open('test.log', 'w', encoding='utf-8') as f:
    f.write('powitanie\n')
    f.write('jeszcz jedno\n')
    f.write('TEkst testowy\n')

f.close()

with open('test.log', "a", encoding='utf-8') as f:
    f.write("Dośdane\n")

f.close()

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()
    print(lines)
f.close()

with open('test.log', 'r') as f:
    lines = f.read()
    print(lines)
f.close()