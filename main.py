def print_oi(name):
    print(f'Oi, {name}')


if __name__ == '__main__':
    print_oi('Cristiano')


def somar(num_a, num_b):
    return num_a + num_b


def subtrair(num_a, num_b):
    return num_a - num_b


def multiplicar(num_a, num_b):
    return num_a * num_b


def dividir(num_a, num_b):
    try:
        return num_a / num_b
    except ZeroDivisionError:
        return 'Não dividiras por zero'


resultado = somar(5, 7)
print(f'A soma é: {resultado}')
