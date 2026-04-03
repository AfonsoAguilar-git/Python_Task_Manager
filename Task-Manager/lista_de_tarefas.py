from tarefa import Tarefa
from sistema_gestao_tarefas import SistemaGestaoTarefa

class ListaDeTarefas:
    def __init__(self, lista, nome):
        self.lista = lista
        self.utilizador = nome
        self.tarefas = self.carregar_tarefas() # cria a lista de tarefas ao carrega-las
        self.sistema = SistemaGestaoTarefa(nome)
        
    def carregar_tarefas(self): #carrega todas as tarefas e adicionas a lista "tarefas"
       tarefas = []
       try:
           with open('ficheiros_txt/lista_de_tarefas.txt', 'r') as file:
               for line in file:
                   if line.strip():  
                       parts = line.strip().split('|')
                       if len(parts) == 7: 
                           nome, lista, cat, titulo, desc, data, status = parts
                           if nome == self.utilizador and lista == self.lista: #procura todas as tarefas de uma lista do utilizador e cria um objeto tarefa e adiciona a lista
                               tarefa = Tarefa(nome, lista, cat, titulo, desc, data,status)
                               tarefas.append(tarefa)
           return tarefas #retorna a lista das tarefas
       except FileNotFoundError:
           return []
       
       
    def adicionar_tarefa(self, titulo, descricao, data, categoria=None, status="Pendente"): #adiciona tarefas(o status é automaticamente pendente)
       nova_tarefa = Tarefa(self.utilizador, self.lista, titulo, descricao, data, categoria, status) #adicao de um objeto da classe tarefa
       nova_tarefa.guardar_tarefa() #guarda a tarefa no ficheiro
       self.tarefas.append(nova_tarefa) #adiciona tarefa a lista
       return True


    def remover_tarefa(self, nome, nome_da_lista, titulo_tarefa): #remoção de tarefas
        for tarefa in self.sistema.get_tarefas_da_lista(nome_da_lista): #procura as tarefas da lista
            titulo = tarefa.split("-")[0].strip() #titulo é a primeira parte da tarefa
            descricao = tarefa.split("-")[1].strip() #descricao a segunda
            data = tarefa.split("-")[2].strip() #data a tereceira 
            if titulo == titulo_tarefa.strip(): # se o titulo coincidir este transforma a tarefa eliminda num objeto tarefa e de sguida apaga a (este é transformado num objeto para acessra o metodo da classe Tarefa)
                tarefa_eliminada = Tarefa(nome, nome_da_lista ,titulo,descricao ,data)
                tarefa_eliminada.apagar_tarefa()
                return True, "Tarefa removida com sucesso."
        return False, "Tarefa não encontrada."
