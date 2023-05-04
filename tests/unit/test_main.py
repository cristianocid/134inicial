import csv

import pytest

from main import somar, subtrair, multiplicar, dividir


def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Aquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')


def teste_somar():
    # 1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido
    print(f'Resultado esperado: {resultado_esperado}, Resultado obtido: {resultado_obtido}')


def teste_subtrair():
    # 1 - Configura
    numero_a = 4
    numero_b = 2
    resultado_esperado = 2

    # 2 - Executa
    resultado_obtido = subtrair(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido
    print(f'Resultado esperado: {resultado_esperado}, Resultado obtido: {resultado_obtido}')


def teste_multiplicar():
    # 1 - Configura
    numero_a = 2
    numero_b = 4
    resultado_esperado = 8

    # 2 - Executa
    resultado_obtido = multiplicar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido
    print(f'Resultado esperado: {resultado_esperado}, Resultado obtido: {resultado_obtido}')


def teste_dividir_positivo():
    # 1 - Configura
    numero_a = 27
    numero_b = 3
    resultado_esperado = 9

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido
    print(f'Resultado esperado: {resultado_esperado}, Resultado obtido: {resultado_obtido}')


def teste_dividir_negativo():
    # 1 - Configura
    numero_a = 27
    numero_b = 0
    resultado_esperado = 'Não dividiras por zero'

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido
    print(f'Resultado esperado: {resultado_esperado}, Resultado obtido: {resultado_obtido}')


lista_de_valores_soma = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7)
]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores_soma)
def teste_somar_lista(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos a lista como massa de teste
    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido
    print(f'Resultado esperado: {resultado_esperado}, Resultado obtido: {resultado_obtido}')


lista_de_valores_subtrair = [
    (8, 7, 1),
    (40, 30, 10),
    (25, 0, 25),
    (-5, 12, -17)
]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores_subtrair)
def teste_subtrair_lista(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos a lista como massa de teste
    # 2 - Executa
    resultado_obtido = subtrair(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido
    print(f'Resultado esperado: {resultado_esperado}, Resultado obtido: {resultado_obtido}')


lista_de_valores_multiplicar = [
    (2, 7, 14),
    (20, 30, 600),
    (25, 0, 0),
    (-2, 12, -24)
]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores_multiplicar)
def teste_multiplicar_lista(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos a lista como massa de teste
    # 2 - Executa
    resultado_obtido = multiplicar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido
    print(f'Resultado esperado: {resultado_esperado}, Resultado obtido: {resultado_obtido}')


lista_de_valores_dividir = [
    (14, 7, 2),
    (40, 10, 4),
    (25, 0, 0),
    (-10, 5, -2)
]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores_dividir)
def teste_dividir_lista(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos a lista como massa de teste
    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido
    print(f'Resultado esperado: {resultado_esperado}, Resultado obtido: {resultado_obtido}')


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('C:\\Users\\cris_\\PycharmProjects\\134inicial\\tests\\vendors\\csv\\massa_teste_somar.csv'))
def teste_somar_csv(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos a lista como massa de teste
    # 2 - Executa
    resultado_obtido = somar(int(numero_a), int(numero_b))

    # 3 - Valida
    assert int(resultado_esperado) == int(resultado_obtido)
    print(f'Resultado esperado: {resultado_esperado}, Resultado obtido: {resultado_obtido}')

# TDD = Test Driven Development
#       Desenvolvimento Direcionado a Teste
#
# - Criar todos os testes de unidade no começo
# - Executar todos os testes pelo menos 1 vez por dia
#
# Imagine que você no 1° dia (nada pronto)
# Você executa todos os testes - o que acontece?
# Dia 01 - Falhou 100 - Passou 000
# Dia 02 - Falhou 095 - Passou 005
# Dia 03 - Falhou 090 - Passou 010
# Dia 04 - Falhou 088 - Passou 012
# Dia 05 - Falhou 081 - Passou 019
# Dia 06 - Falhou 075 - Passou 025
# Informação sobre o progresso
# Insistir mais um dia      1 + 1 = 2?
# Pedir ajuda               1 + 2 = 3
# Devolver e pegar outra    1 + 1 = 2!
# Tudo certo!               1 + 2 = 4
# TDD: Teste é uma medida de progresso

# CI: Continuous Integration
# IC: Integração Continua

# (Build) --> Suite de Testes ------> (Build)
#               Automatizada  Passou
# Ambiente                            Entâo, move >> Ambiente
# de Desenvolvimento                                 de Teste

# CD: Continuous Delivery
# EC: Entrega Continua

# (Build) --> Suite --> (Build) ----->
#   Dev      de Teste    Teste  Muitos Produção
#                               Testes
