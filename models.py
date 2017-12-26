# -*- coding: utf-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

        def imprimir(self):
            print "Nome : %s, Telefone: %s, Empresa: %s, Curtidas: %s" % (self.nome, self.telefone, self.empresa, self.__curtidas)   

        def curtir(self):
            self.__curtidas+=1

        def obter_curtidas(self):
            return self.__curtidas
            
class Data(object):
   def __init__(self, dia, mes, ano):
      self.dia = dia
      self.mes = mes
      self.ano = ano

   def imprime(self):
      print '%s/%s/%s' % (self.dia, self.mes, self.ano)

class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def imprime(self):
        imc = self.peso / (self.altura **2)
        print 'O IMC de %s é: %s ' %(self.nome, imc)