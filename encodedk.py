
def encode():
    x = 0
    encode = str(input('Enter plain text to encode: '))
    primary = int(input('Enter primary key to encode to (0-99): '))
    secondary = int(input('Enter secondary key to encode to (0-9): '))

    length = len(encode)
    
    while length > x:
        if primary == 0:
            if secondary == 0:
                if encode[x] == 'a':
                    print('NanX', end='')
                elif encode[x] == 'b':
                    print('WTVS', end='')
                elif encode[x] == 'c':
                    print('C67g', end='')
                elif encode[x] == 'd':
                    print('Lw1n', end='')
                elif encode[x] == 'e':
                    print('r2aQ', end='')
                elif encode[x] == 'f':
                    print('iV8h', end='')
                elif encode[x] == 'g':
                    print('BYj5', end='')
                elif encode[x] == 'h':
                    print('q8Cy', end='')
                elif encode[x] == 'i':
                    print('MwPb', end='')
                elif encode[x] == 'j':
                    print('a34n', end='')
                elif encode[x] == 'k':
                    print('VRPT', end='')
                elif encode[x] == 'l':
                    print('c3Xf', end='')
                elif encode[x] == 'm':
                    print('oUis', end='')
                elif encode[x] == 'n':
                    print('jomG', end='')
                elif encode[x] == 'o':
                    print('UQXi', end='')
                elif encode[x] == 'p':
                    print('ZDCE', end='')
                elif encode[x] == 'q':
                    print('UXwZ', end='')
                elif encode[x] == 'r':
                    print('Mxeh', end='')
                elif encode[x] == 's':
                    print('E60o', end='')
                elif encode[x] == 't':
                    print('6Gcw', end='')
                elif encode[x] == 'u':
                    print('MSrd', end='')
                elif encode[x] == 'v':
                    print('r4tl', end='')
                elif encode[x] == 'w':
                    print('ttAz', end='')
                elif encode[x] == 'x':
                    print('PS7A', end='')
                elif encode[x] == 'y':
                    print('2MaL', end='')
                elif encode[x] == 'z':
                    print('xLp9', end='')
                elif encode[x] == 'A':
                    print('EBVy', end='')
                elif encode[x] == 'B':
                    print('JfRo', end='')
                elif encode[x] == 'C':
                    print('wwRF', end='')
                elif encode[x] == 'D':
                    print('2bMt', end='')
                elif encode[x] == 'E':
                    print('6xOh', end='')
                elif encode[x] == 'F':
                    print('R1Gy', end='')
                elif encode[x] == 'G':
                    print('bwqV', end='')
                elif encode[x] == 'H':
                    print('Rv7X', end='')
                elif encode[x] == 'I':
                    print('bVQP', end='')
                elif encode[x] == 'J':
                    print('emRC', end='')
                elif encode[x] == 'K':
                    print('okLK', end='')
                elif encode[x] == 'L':
                    print('KAsU', end='')
                elif encode[x] == 'M':
                    print('kvUx', end='')
                elif encode[x] == 'N':
                    print('PBCP', end='')
                elif encode[x] == 'O':
                    print('53lu', end='')
                elif encode[x] == 'P':
                    print('wDTS', end='')
                elif encode[x] == 'Q':
                    print('Vjr9', end='')
                elif encode[x] == 'R':
                    print('wHtn', end='')
                elif encode[x] == 'S':
                    print('1MbS', end='')
                elif encode[x] == 'T':
                    print('A7fl', end='')
                elif encode[x] == 'U':
                    print('lp9I', end='')
                elif encode[x] == 'V':
                    print('7OE1', end='')
                elif encode[x] == 'W':
                    print('UqCp', end='')
                elif encode[x] == 'X':
                    print('HPtZ', end='')
                elif encode[x] == 'Y':
                    print('tpd8', end='')
                elif encode[x] == 'Z':
                    print('zkzg', end='')
                elif encode[x] == '0':
                    print('NnU3', end='')
                elif encode[x] == '1':
                    print('VSOx', end='')
                elif encode[x] == '2':
                    print('Z3Vc', end='')
                elif encode[x] == '3':
                    print('OfSk', end='')
                elif encode[x] == '4':
                    print('nntM', end='')
                elif encode[x] == '5':
                    print('BPiO', end='')
                elif encode[x] == '6':
                    print('11o3', end='')
                elif encode[x] == '7':
                    print('MPym', end='')
                elif encode[x] == '8':
                    print('Yvyz', end='')
                elif encode[x] == '9':
                    print('FvS6', end='')
                elif encode[x] == ' ':
                    print('z6Q0', end='')
                elif encode[x] == '.':
                    print('2fLm', end='')

        x += 1

while True:
    encode()
    break_loop = str(input('Encode more data? Y/N: ')).upper()

    if break_loop == 'N':
        break
