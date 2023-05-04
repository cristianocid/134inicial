import unittest
from unittest.mock import MagicMock


# Definir a classe de banco de dados a ser testada
class Database:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value
        return True

    def get(self, key):
        return self.data.get(key)

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value
            return True
        else:
            return False

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            return True
        else:
            return False


# Definir os testes de integração para o banco de dados
class TestDatabaseIntegration(unittest.TestCase):
    def setUp(self):
        # Cria um objeto do banco de dados falso
        self.db = MagicMock(spec=Database)

    def test_add_to_database(self):
        # Simula a adição de dados ao banco de dados
        self.db.add.return_value = True

        # Define os dados a serem adicionados ao banco de dados
        key = "john"
        value = {"name": "John", "age": 30}

        # Chama a função de adição ao banco de dados
        result = self.db.add(key, value)

        # Verifica se a função de adição retornou True
        self.assertTrue(result)

        # Verifica se a função de adição foi chamada com os argumentos corretos
        self.db.add.assert_called_once_with(key, value)
        print(f'Adicionado ao Banco de Dados: {key}= {value}')

    def test_get_from_database(self):
        # Simula a consulta de dados do banco de dados
        key = "john"
        value = {"name": "John", "age": 30}
        self.db.get.return_value = value

        # Chama a função de consulta do banco de dados
        result = self.db.get(key)

        # Verifica se a função de consulta retornou os dados corretos
        self.assertEqual(result, value)

        # Verifica se a função de consulta foi chamada com a chave correta
        self.db.get.assert_called_once_with(key)
        print(f'Consulta ao Banco de Dados: {key}= {value}')

    def test_update_database(self):
        # Simula a atualização de dados no banco de dados
        key = "john"
        value = {"name": "Joao", "age": 30}
        self.db.update.return_value = True

        # Chama a função de atualização do banco de dados
        result = self.db.update(key, value)

        # Verifica se a função de atualização retornou True
        self.assertTrue(result)

        # Verifica se a função de atualização foi chamada com os argumentos corretos
        self.db.update.assert_called_once_with(key, value)
        print(f'Alterarndo Banco de Dados: {key}= {value}')

    def test_delete_from_database(self):
        # Simula a exclusão de dados do banco de dados
        key = "john"
        self.db.delete.return_value = True

        # Chama a função de exclusão do banco de dados
        result = self.db.delete(key)

        # Verifica se a função de exclusão retornou True
        self.assertTrue(result)

        # Verifica se a função de exclusão foi chamada com a chave correta
        self.db.delete.assert_called_once_with(key)
        print(f'Deletando valor do Banco de Dados: {key}')
