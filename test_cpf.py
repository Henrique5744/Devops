import unittest
from cpf import validar_cpf

class TestCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("52998224725"))

    def test_cpf_valido_com_formatacao(self):
        self.assertTrue(validar_cpf("529.982.247-25"))

    def test_cpf_invalido(self):
        self.assertFalse(validar_cpf("12345678900"))

    def test_cpf_todos_iguais(self):
        self.assertFalse(validar_cpf("11111111111"))

    def test_cpf_tamanho_errado(self):
        self.assertFalse(validar_cpf("123"))

    def test_cpf_com_letras(self):
        self.assertFalse(validar_cpf("abc.def.ghi-jk"))


if __name__ == "__main__":
    unittest.main()