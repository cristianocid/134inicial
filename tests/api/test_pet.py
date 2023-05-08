# bibliotecas
import json
import pytest
import requests

from tests.utils.file_manager import ler_csv

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
        data=open('/vendors\\json\\pet1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_categoria_nome_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_nome_esperado


def teste_consultar_pet():
    # Configura
    # Entrada
    pet_id = 1732181

    # Resultado Esperado
    status_code_esperado = 200
    pet_id_esperado = 1732181
    pet_nome_esperado = 'Night'
    pet_categoria_nome_esperado = 'cachorro'
    pet_tag_nome_esperado = 'vacinado'

    # Executa
    resultado_obtido = requests.get(
        url=url + '/' + str(pet_id),
        headers=headers
    )
    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_categoria_nome_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_nome_esperado


def teste_alterar_pet():
    # Configura
    # Dados de entrada provem do pet2.json

    # Resultado Esperado
    status_code_esperado = 200
    pet_id_esperado = 1732181
    pet_nome_esperado = 'Lua'
    pet_categoria_nome_esperado = 'cachorro'
    pet_tag_nome_esperado = 'castrado'

    # Executa
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('/vendors\\json\\pet2.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_categoria_nome_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_nome_esperado


def teste_excluir_pet():
    # Configura
    # Entrada
    pet_id = 1732181

    # Resultado Esperado
    status_code_esperado = 200
    pet_code_esperado = 200
    pet_type_esperado = 'unknown'
    pet_message_esperado = '1732181'

    # Executa
    resultado_obtido = requests.delete(
        url=url + '/' + str(pet_id),
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == pet_code_esperado
    assert corpo_do_resultado_obtido['type'] == pet_type_esperado
    assert corpo_do_resultado_obtido['message'] == pet_message_esperado


@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags_id,tags_name,status',
                         ler_csv('C:\\Users\\cris_\\PycharmProjects\\134inicial\\tests\\vendors\\csv\\massa_incluir_pet.csv'))
def teste_incluir_pet_em_massa(pet_id, category_id, category_name, pet_name, tags_id, tags_name, status
                               ):
    # Configura
    # Dados de entrada provem do massa_incluir_pet.csv.json
    # Montagem do JSON dinamico
    corpo_json =  '{'
    corpo_json += f'  "id": {pet_id},'
    corpo_json += '  "category": {'
    corpo_json += f'    "id": {category_id},'
    corpo_json += f'    "name": "{category_name}"'
    corpo_json += '  },'
    corpo_json += f'  "name": "{pet_name}",'
    corpo_json += '  "photoUrls": ['
    corpo_json += '    "string"'
    corpo_json += '  ],'
    corpo_json += '  "tags": ['
    corpo_json += '    {'
    corpo_json += f'      "id": {tags_id},'
    corpo_json += f'      "name": "{tags_name}"'
    corpo_json += '    }'
    corpo_json += '  ],'
    corpo_json += f'  "status": "{status}"'
    corpo_json += '}'

    # Resultado Esperado
    # Os dados de entrada tambem servirão como resultados
    # esperados, visto que o retorno é um eco
    status_code_esperado = 200

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    assert corpo_do_resultado_obtido['tags'][0]['name'] == tags_name
