
class SistemaGestaoTarefa: #sistema de gestao de tarefas com o atributo de nome para fazer a distincao entre utilizadores
    def __init__(self, nome):
        self.nome = nome
        
         
    def get_categorias_utilizador(self, nome): #procura e retorna todas as categorias pertencentes a um utilizador

        categorias = set()  # uso do set para evitar duplicados
        try:
            with open('ficheiros_txt/lista_de_tarefas.txt', 'r') as file:
                for line in file:
                    if line.strip():  
                        parts = line.strip().split('|')
                        if len(parts) >= 3:  # verificar se a linha tem mais que tres partes (as 3s primeiras sao nome,lista,categoria)
                            user, _, cat = parts[:3]
                            if user == nome and cat and cat != "None": #se o nome for igual adiciona as catgorias ao set previamente definido 
                                categorias.add(cat)
            return sorted(list(categorias))  # Retorna a lista das categorias
        except (FileNotFoundError, ValueError):
            return []
        


    def get_categorias_lista(self, nome, listas): #procura e retorna as categorias de uma lista de um user(usado na filtragem das categorias de uma lista especifica)

        categorias = set()   # uso do set para evitar duplicados
        try:
            with open('ficheiros_txt/lista_de_tarefas.txt', 'r') as file:
                for line in file:
                    if line.strip():  
                        parts = line.strip().split('|')
                        if len(parts) >= 3:  # verificar se a linha tem mais que tres partes (as 3s primeiras sao nome,lista,categoria)
                            user, lista, cat = parts[:3]
                            if user == nome and lista == listas and cat and cat != "None": #se o nome for iguale lista for igual adiciona as catgorias ao set previamente definido 
                                categorias.add(cat)
            return sorted(list(categorias))  # Retorna a lista das categorias
        except (FileNotFoundError, ValueError):
            return []
    

    def get_listas_utilizador(self, nome): #procura e retorna todas as listas de um utilizador
    
       listas = set()  # Uso do set para evitar duplicados
       try:
           with open('ficheiros_txt/lista_de_tarefas.txt', 'r') as file:
               for line in file:
                   if line.strip():  
                       partes = line.strip().split('|')
                       if len(partes) >= 2:  # verificar se a linha tem mais que duas partes (as 2s primeiras sao nome,lista)
                           user, lista = partes[:2]
                           if user == nome: # se o nome for igual adiciona as listas a lista previamente definida
                               listas.add(lista)
           return sorted(list(listas)) # retorna a lista de listas
       except FileNotFoundError:
           return []
       
    
    def get_tarefas_da_lista(self, nome_da_lista): # procura e retorna as tarefas de uma lista de um utilizador
        tarefas = []
      
        # Ler o arquivo e filtrar tarefas da lista do utilizador
        with open("ficheiros_txt/lista_de_tarefas.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split("|")
                if len(partes) == 7:
                    nome, lista, categoria , titulo, descricao, data, estado = partes
                    if nome == self.nome and lista == nome_da_lista: # se nome for igual e lista for igual entao adiciona as tarefas no formato"tiutlo-descricao-data-categoria-estado"
                        tarefas.append(f"{titulo} - {descricao} - {data} - {categoria} - {estado}")

        return tarefas #retorna as tarefas
    

    def get_tarefas_da_lista_pendentes(self, nome_da_lista):#procura e retorna todas as tarefas pendentes de uma lista deum utilizador
        tarefas = []
         
        with open("ficheiros_txt/lista_de_tarefas.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split("|")
                if len(partes) == 7:
                    nome, lista, categoria , titulo, descricao, data, estado = partes
                    if nome == self.nome and lista == nome_da_lista and estado == "Pendente": # se nome for igual e lista for igual e estado for dependente entao adiciona as tarefas no formato"tiutlo-descricao-data-categoria-estado"
                        tarefas.append(f"{titulo} - {descricao} - {data} - {categoria} - {estado}")
        return tarefas #retorna as tarefas
    
  
   #atualização do titulo descricao e categoria de uma tarefa dentro de uma lista de um utilizador
    def atualizar_tarefa(nome_usuario, lista_tarefa, titulo_original, novo_titulo, nova_descricao, nova_categoria):
        try:
            linhas_atualizadas = []
            tarefa_atualizada = False

            with open('ficheiros_txt/lista_de_tarefas.txt', 'r') as file:
                for linha in file:
                    partes = linha.strip().split('|')
                    if len(partes) == 7:
                        nome, lista, _, titulo, _, data, estado = partes
                        if (nome == nome_usuario and lista == lista_tarefa and titulo == titulo_original):#procura a linha por atualizar
                            # Substitui pelos novos valores
                            linha = f"{nome_usuario}|{lista_tarefa}|{nova_categoria}|{novo_titulo}|{nova_descricao}|{data}|{estado}\n"
                            tarefa_atualizada = True
                    linhas_atualizadas.append(linha)#adiciona todas as linhas 

            if tarefa_atualizada:
                with open('ficheiros_txt/lista_de_tarefas.txt', 'w') as file:
                    file.writelines(linhas_atualizadas) #reescreve o ficheiro com a lista das novas linhas incluido a tarefa atualizada
                return True, "Tarefa atualizada com sucesso!"
            else:
                return False, "Tarefa não encontrada."
        except FileNotFoundError:
            return False, "Arquivo de tarefas não encontrado."
        except Exception as e:
            return False, f"Ocorreu um erro: {str(e)}"