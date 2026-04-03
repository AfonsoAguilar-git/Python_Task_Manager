from sistema_gestao_tarefas import SistemaGestaoTarefa

class Relatorio(): #classe que gera os relatorios( é gerado um relatorio por lista de utilizador )
    def __init__(self, nome, lista):
        self.nome = nome
        self.lista = lista
        self.sistema = SistemaGestaoTarefa(nome)


    
    def gerar_relatorio_yes(self): #Gera um relatório de todas as tarefas pendentes de uma lista do utilizador.
    
        tarefas = self.sistema.get_tarefas_da_lista_pendentes(self.lista) #vai buscar todas as tarefas pendentes da lista que se pretende fazer o relatorio
       
        relatorio = f"Relatório - Utilizador: {self.nome} - Lista: {self.lista}\n" #escreve uma primaira linha a dizer o utilizador e a lista
        relatorio += "-" * 50 + "\n" # cria uma separação para as tarefas
        for tarefa in tarefas:
            relatorio += f"{tarefa}\n" #escreve as tarefas
        
        # Adiciona uma linha extra no final do relatório( separação de outros relatorios)
        relatorio += "\n"

        with open("ficheiros_txt/relatorio.txt", "a", encoding= "UTF-8") as f:
            f.write(relatorio) #escreve o relatorio no ficheiro


    def gerar_relatorio_no(self): #Gera um relatório de todas as tarefas de uma lista do utilizador.
    
        tarefas = self.sistema.get_tarefas_da_lista(self.lista) #vai buscar todas as tarefas da lista que se pretende fazer o relatorio
       
        relatorio = f"Relatório - Utilizador: {self.nome} - Lista: {self.lista}\n" #escreve uma primaira linha a dizer o utilizador e a lista
        relatorio += "-" * 50 + "\n" # cria uma separação para as tarefas
        for tarefa in tarefas:
            relatorio += f"{tarefa}\n" #escreve as tarefas
        
        # Adiciona uma linha extra no final do relatório( separação de outros relatorios)
        relatorio += "\n"

        with open("ficheiros_txt/relatorio.txt", "a", encoding= "UTF-8") as f:
            f.write(relatorio) #escreve o relatorio no ficheiro
