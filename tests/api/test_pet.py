# bibliotecas
import pytest
import requests

# variaveis publicas
url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


# definições das funções (defs)

def teste_incluir_pet():
    # Configura
    # Dados de entrada provem do pet1.json

    # Resultado Esperado
    status_code_esperado = 200
    pet_id_esperado = 1732181
    pet_nome_esperado = 'Night'
    pet_categoria_nome_esperado = 'cachorro'
    pet_tag_nome_esperado = 'vacinado'

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\cris_\\PycharmProjects\\134inicial\\tests\\vendors\\json\\pet1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_categoria_nome_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_nome_esperado
