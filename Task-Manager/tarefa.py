class Tarefa:
    def __init__(self, utilizador, lista, titulo, descricao, data, categoria=None, status="Pendente"):
        self.utilizador = utilizador
        self.lista = lista
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.categoria = categoria
        self.status = status


   #guarda a tarefa no ficheiro lista_de_tarefas non formato: nome|lista|categoria|titulo|descricao|data|status
    def guardar_tarefa(self): 
        with open("ficheiros_txt/lista_de_tarefas.txt", "a") as f:
            f.write(f"{self.utilizador}|{self.lista}|{self.categoria}|{self.titulo}|{self.descricao}|{self.data}|{self.status}\n")


   #metodo para a remoção de tarefas
    def apagar_tarefa(self): 
        try:
            # Lê todas as linhas do ficheiro
            with open('ficheiros_txt/lista_de_tarefas.txt', 'r') as file:
                linhas = file.readlines()

            # Cria uma lista de tarefas, excluindo a tarefa a ser apagada
            tarefas_atualizadas = []
            for linha in linhas:
                partes = linha.strip().split('|')
                if len(partes) == 7:
                    nome, lista, _,titulo, _, _, _ = partes
                    if not (nome == nome and lista == self.lista and titulo == self.titulo):
                        tarefas_atualizadas.append(linha)  # Adiciona a tarefa à lista se não for a que deve ser apagada

            # Se a tarefa foi encontrada e removida, reescreve o arquivo
            with open('ficheiros_txt/lista_de_tarefas.txt', 'w') as file:
                file.writelines(tarefas_atualizadas)

        except FileNotFoundError:
            print("Arquivo de tarefas não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar apagar a tarefa: {e}")



   #metodo para a troca de status
    def trocar_status_tarefa(self, nome_usuario, nome_lista, titulo_tarefa):
        tarefas_atualizadas = []
        tarefa_encontrada = False

        with open("ficheiros_txt/lista_de_tarefas.txt", "r") as arquivo: # le as tarefas todas do ficheiro
            for linha in arquivo:
                partes = linha.strip().split("|")
                if len(partes) == 7:
                    nome, lista, categoria, titulo, descricao, data, estado = partes #separa tarefa por partes
                    if nome == nome_usuario and lista == nome_lista and titulo == titulo_tarefa: #procura se a tarefa selecionada no ficheiro atraves de nome , lista e titulo
                        tarefa_encontrada = True
                        novo_estado = "Concluida" if estado == "Pendente" else "Pendente" #se o estado for pendente , troca para concluida se for outro(unica opcao =concluida), troca para pendente
                        linha_atualizada = "|".join([nome, lista, categoria, titulo, descricao, data, novo_estado])
                    else:
                        linha_atualizada = linha.strip()
                    tarefas_atualizadas.append(linha_atualizada)
                else:
                    tarefas_atualizadas.append(linha.strip())

        if tarefa_encontrada:
            with open("ficheiros_txt/lista_de_tarefas.txt", "w") as arquivo:
                for linha in tarefas_atualizadas:
                    arquivo.write(linha + "\n")
            return True
        else:
            return False
