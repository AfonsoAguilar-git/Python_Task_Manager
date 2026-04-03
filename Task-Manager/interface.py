from lista_de_tarefas import ListaDeTarefas
from utilizador import Utilizador
from tarefa import Tarefa
from sistema_gestao_tarefas import SistemaGestaoTarefa
from relatorio import Relatorio
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout ,QFormLayout , QWidget , QLabel, QLineEdit,QComboBox, QMessageBox ,QDateEdit , QListWidget , QHBoxLayout, QInputDialog
from PyQt5.QtCore import QDate , Qt , pyqtSignal




class SignupWindow(QMainWindow): #janela de signup(criar conta)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signup")
        self.setGeometry(500,300,450,500)

        # Widget principal (container)
        container = QWidget()
        self.setCentralWidget(container)

        # segundo widget (central_widget)
        central_widget = QWidget()
        
        # Layout do container
        container_layout = QVBoxLayout()
        container.setLayout(container_layout)
        container_layout.addWidget(central_widget) #adicao do segundo widget ao layout do container

        # layout do central widget (form_layout)
        form_layout = QFormLayout()
        central_widget.setLayout(form_layout)

        # Campo de escrita: Nome
        self.nome_input = QLineEdit()
        form_layout.addRow(QLabel("Nome:"), self.nome_input)

        # Campo de escrita: palavra-passe
        self.password_input = QLineEdit()
        form_layout.addRow(QLabel("Password:"), self.password_input)

        # Botão de sign in
        self.submit_button = QPushButton("Registar-se")
        form_layout.addRow(self.submit_button)
        self.submit_button.clicked.connect(self.registar_utilizador)

        # Adiciao de espaço antes do botão voltar atras
        spacer = QWidget()
        spacer.setFixedHeight(20)
        form_layout.addRow(spacer)

        # Botão de voltar atras
        self.back_button = QPushButton("Voltar")
        form_layout.addRow(self.back_button)
        self.back_button.clicked.connect(self.voltar)


    def registar_utilizador(self): #busca o texto dos campos de escrita e verifica o nome e conforme resultaod guarda o utilizador
        nome = self.nome_input.text()
        password = self.password_input.text()
        
        if nome and password:  # verifica se os campos nao estao vazios
            if Utilizador.verificar_nome_utilizador(nome):
                # mensagem de erro se nome de utilizador ja existe
                QMessageBox.warning(self, "Erro", "Nome de Utilizador já existente. Porfavor escolha outro nome de utilizador.")
            else:
                # guardar o novo utilizador se o nome de utilizador nao existe
                Utilizador.guardar_utilizador(nome, password)
                QMessageBox.information(self, "Successo", "Conta Criada!")
                self.login_window = LoginWindow() #criação de objeto login window e abertura do mesmo
                self.login_window.show()
                self.close()
        else:
            # Erro se os campos estiverem vazios
            QMessageBox.warning(self, "Erro", "Porfavor preencha todos os campos")
        
    def voltar(self):
        self.login_window = LoginWindow() #cria objeto de login window e abertura do mesmo
        self.login_window.show()
        self.close()




class LoginWindow(QMainWindow): #primeira janela do programa (login do sistema)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(500,300,450,500)

    # Widget principal (container)
        container = QWidget()
        self.setCentralWidget(container)

    # segundo widget (central_widget)
        central_widget = QWidget()
        
    # Layout do container
        container_layout = QVBoxLayout()
        container.setLayout(container_layout)
        container_layout.addWidget(central_widget) #adicao do segundo widget ao layout do container

    # layout do central widget (form_layout)
        form_layout = QFormLayout()
        central_widget.setLayout(form_layout)

    # Campo de escrita: Nome
        self.name_input = QLineEdit()
        form_layout.addRow(QLabel("Name:"), self.name_input)

    # Campo de escrita: palavra passe
        self.password_input = QLineEdit()
        form_layout.addRow(QLabel("Password:"), self.password_input)
    
    #espaço entre o campo de escrita e o botão de login
        space = QWidget()
        space.setFixedHeight(20)
        form_layout.addRow(space)
    
    # Botão de login
        self.login_button = QPushButton("login")
        form_layout.addRow(self.login_button)
        self.login_button.clicked.connect(self.login)
    
    # Botão de sign up
        self.signup_button = QPushButton("Criar Conta")
        form_layout.addRow(self.signup_button)
        self.signup_button.clicked.connect(self.signup)

    
    # criacao de objeto da signup window e abertura do mesmo
    def signup(self):
        self.signup_window = SignupWindow()
        self.signup_window.show()
        self.close()


    def login(self): #uso da informação escrita nos campos de texto para a verificação do utilizador ,se retornar true este é levado a janela principal do sistema ,se não mensagem de erro
        nome = self.name_input.text().strip()
        palavra_passe = self.password_input.text().strip()

        if Utilizador.verificar_credenciais(nome, palavra_passe):
            self.app_window = AppWindow(nome)
            self.app_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Credênciais Inválidas.")




class ChangePasswordWindow(QMainWindow):# janela de mudar a palavra passe(acessada atraves da janela principal (appwindow))
    def __init__(self, nome):
        super().__init__()
        self.setWindowTitle("Alterar Palavra-Passe")
        self.setGeometry(500,300,450,500)
        self.nome = nome #passa o nome do utilizador 


    # Widget principal (container)
        container = QWidget()
        self.setCentralWidget(container)

    # segundo widget (central_widget)
        central_widget = QWidget()
        
    # Layout do container
        container_layout = QVBoxLayout()
        container.setLayout(container_layout)
        container_layout.addWidget(central_widget)#adicao do segundo widget ao layout do container

    # layout do central widget (form_layout)
        form_layout = QFormLayout()
        central_widget.setLayout(form_layout)

    # Campo de escrita: palavra passe atual
        self.password_atual_input = QLineEdit()
        form_layout.addRow(QLabel("Password Atual:"), self.password_atual_input)

    # Campo de escrita: palavra passe nova
        self.password_nova_input = QLineEdit()
        form_layout.addRow(QLabel("Password Nova:"), self.password_nova_input)
    
    #espaço entre o campo de escrita e o botao de mudar palavra passe
        space = QWidget()
        space.setFixedHeight(20)
        form_layout.addRow(space)
    
    # Botão de mudar palavra passe
        self.login_button = QPushButton("Mudar Palavra-Passe")
        form_layout.addRow(self.login_button)
        self.login_button.clicked.connect(self.change_password)
    
    # Botão de voltar
        self.signup_button = QPushButton("voltar")
        form_layout.addRow(self.signup_button)
        self.signup_button.clicked.connect(self.close)


    def change_password(self): #busca as informaçoes nos campos de texto para verificar a palavra passe atual e altera-la
        password_atual = self.password_atual_input.text().strip()
        password_nova = self.password_nova_input.text().strip()

    # Verifica se ambos os campos estão preenchidos
        if not password_atual or not password_nova:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos.")
            return

    # Verifica se a palavra-passe atual está correta
        if not Utilizador.verificar_credenciais(self.nome, password_atual):
            QMessageBox.warning(self, "Erro", "A palavra-passe atual está incorreta.")
            return

    # Altera a palavra-passe
        sucesso, mensagem = Utilizador.alterar_palavra_passe(self.nome, password_nova)
        if sucesso:
            QMessageBox.information(self, "Sucesso", mensagem)
            self.close()  # Fecha a janela após a alteração bem-sucedida
        else:
            QMessageBox.warning(self, "Erro", mensagem)




class AppWindow(QMainWindow): #janela principal do sistema 
    def __init__(self, nome):
        super().__init__()
        self.nome = nome #passa o nome do utilizador 
        self.sistema = SistemaGestaoTarefa(nome) #cria um objeto do sistema gestao tarefas passando o nome do utilizador 
        self.setWindowTitle("Gestor De Tarefas")
        self.setGeometry(500,300,450,500)

    # Widget principal (central_widget)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

    # Layout do central_widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
    
    # empurra o resto dos elementos para baixo 
        layout.addStretch()

    # label da lista de tarefas
        self.lista_label = QLabel("Listas de tarefas:")
        layout.addWidget(self.lista_label)
    
    # combobox da escolha das listas 
        self.lista_input = QComboBox()
        self.lista_input_update() # atualização dos items da combo box
        self.lista_input.setFixedWidth(300)
        layout.addWidget(self.lista_input)
    
    # empurra o resto dos elementos para baixo (espaço entre a combobox e os botões do sistema)
        layout.addStretch()
    
    # botão de criar tarefa   
        self.add_task_button = QPushButton("Criar Tarefa")
        self.add_task_button.clicked.connect(self.add_task_window)
        layout.addWidget(self.add_task_button)
    
    # botão de ver a lsta selecionada
        self.view_list_button = QPushButton("Ver lista selecionada")
        self.view_list_button.clicked.connect(self.view_list_window)
        layout.addWidget(self.view_list_button)
        
    # botão de gerar relatorios
        self.create_relatorio_button = QPushButton("Gerar relatório da lista selecionada")
        self.create_relatorio_button.clicked.connect(self.create_relatorio)
        layout.addWidget(self.create_relatorio_button)


    # empurra o resto dos elementos para baixo(espaço entre os botões de funcionalidades e os botões do utilizador (mudar palavra passe e logout))
        layout.addStretch()

    # botão de mudar palavra-passe
        self.change_password_button = QPushButton("Alterar Palavra-passe")
        self.change_password_button.clicked.connect(self.change_passe_window)
        layout.addWidget(self.change_password_button)
    
    # botão de logout
        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)


    # atualização da combobox , limpa as escolhas e vai buscar as listas ao sistema gestao tarefas
    def lista_input_update(self):
        self.lista_input.clear()
        listas = self.sistema.get_listas_utilizador(self.nome) #conexão ao sistema gestao tarefas
        self.lista_input.addItems(listas) #adição das listas


    
    def add_task_window(self): #criação de um objeto da add task window e abertura da mesma (não fecha a página )
        self.addtask_window = AddTaskWindow(self.nome)
        self.addtask_window.task_created.connect(self.lista_input_update) #conectar a task window com um signal(task_created) para a atualização da combobox listas
        self.addtask_window.show()
    
    def create_relatorio(self): #geração do relatório para o ficheiro relatorio.txt
        lista = self.lista_input.currentText() #seleciona a lista escolhida na combo box para gerar relatório
        relatorio_lista = Relatorio(self.nome , lista) #cria objeto de relatorio passando o nome do utilizador e a lista selecionada

        if not lista.strip():#se nao tiver lista selecionada
            QMessageBox.warning(self,"warning","Porfavor selecione uma lista")
            return

        resposta = QMessageBox.question( # pergunta se o utilizador pretende um relatorio das tarefas pendentes ou todas
                self,
                f"Geração de relatório da lista:{lista}",
                f"Gerar relatório das tarefas pendentes?",
                QMessageBox.Yes | QMessageBox.No 
            )
        
                     
        if resposta == QMessageBox.Yes:  # se prefer pendentes, chama gerar_relatorio_yes
            relatorio_lista.gerar_relatorio_yes()
            QMessageBox.information(
                self,
                "Sucesso",
                f"Relatório das tarefas pendentes da lista: {lista} gerado no ficheiro relatorio.txt",
            )

        if resposta == QMessageBox.No:  # se prefer todas, chama gerar_relatorio_no
            return 

        

    def change_passe_window(self): #criação de um objeto da change password window e abertura da mesma (não fecha a página )
        self.change_passe_window = ChangePasswordWindow(self.nome) #passa o nome do utilizador
        self.change_passe_window.show()
        


    def view_list_window(self): #criação de um objeto da view list window e abertura da mesma (não fecha a página )
        lista = self.lista_input.currentText() #seleciona a lista escolhida na combo box para visualizar
        if not lista.strip():#se nao tiver lista selecionada
            QMessageBox.warning(self,"warning","Porfavor selecione uma lista")
            return
        
        self.view_list_window = ViewListWindow(self.nome, lista) #passa o nome do utilizador e a lista selecionada
        self.view_list_window.list_removed.connect(self.lista_input_update) #conectar a view list window com um signal(list_removed) para a atualização da combobox listas
        self.view_list_window.show()
    
    def logout(self): # criação de um objeto da login window e abertura da mesma
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()




class AddTaskWindow(QMainWindow): #janela de adição/criação de tarefas 
    task_created = pyqtSignal() #sinal de atualizar combobox da appwindow
    
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.sistema = SistemaGestaoTarefa(nome)
        self.setWindowTitle("Criar tarefa")
        self.setGeometry(500,300,450,500)

    # Widget principal (container)
        container = QWidget()
        self.setCentralWidget(container)

    # Layout do container
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        container.setLayout(layout)
        

    # label do título
        title_label = QLabel("Título:")
        layout.addWidget(title_label)
    
    # campo de escrita do titulo   
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Título da tarefa")
        self.title_input.setFixedWidth(300)
        layout.addWidget(self.title_input)

    # label da descrição
        description_label = QLabel("Descrição:")
        layout.addWidget(description_label)
    
    # campo de escrita da descricao    
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Descrição da tarefa")
        self.description_input.setFixedWidth(300)
        layout.addWidget(self.description_input)
        
    # label da data de criação
        creation_date_label = QLabel("Data de criação:")
        layout.addWidget(creation_date_label)
    
    # campo da data de criação
        self.creation_date_input = QDateEdit()
        self.creation_date_input.setDate(QDate.currentDate())
        self.creation_date_input.setReadOnly(True)
        self.creation_date_input.setFixedWidth(300)
        layout.addWidget(self.creation_date_input)
    
    # label da categoria
        categoria_label = QLabel("Categoria:")
        layout.addWidget(categoria_label)
    
    # combobox da categoria (escrita de uma nova categoria ou escolha de uma existente)
        self.categoria_input = QComboBox()
        self.categoria_input.setFixedWidth(300)
        self.categoria_input.setEditable(True)
        self.categoria_input.addItems(["Nova categoria..."] + self.sistema.get_categorias_utilizador(self.nome))
        self.categoria_input.currentIndexChanged.connect(self.on_categoria_changed) #troca da capacidade de editar a combobox (editar se for para uma categoria nova)
        layout.addWidget(self.categoria_input)

    # label da lista
        lista_label = QLabel("Lista:")
        layout.addWidget(lista_label)

    #combobox da lista ((escrita de uma nova lista ou escolha de uma existente))    
        self.lista_input = QComboBox()
        self.lista_input.setFixedWidth(300)
        self.lista_input.setEditable(True)
        self.lista_input.addItems(["Nova lista..."] + self.sistema.get_listas_utilizador(self.nome))
        self.lista_input.currentIndexChanged.connect(self.on_lista_changed) #troca da capacidade de editar a combobox (editar se for para uma lista nova)
        layout.addWidget(self.lista_input)

    # empurra o resto dos elementos para baixo(separação entre os campos de criação de tarefa e os botões) 
        layout.addStretch()

    # Botão de criar tarefa
        self.create_list_button = QPushButton("Criar tarefa")
        self.create_list_button.clicked.connect(self.create_task)
        layout.addWidget(self.create_list_button)

    # botão de voltar atras
        self.back_button = QPushButton("Voltar")
        self.back_button.clicked.connect(self.close)
        layout.addWidget(self.back_button)
    
   
    
    def on_categoria_changed(self, index): #controlo de quando se pode editar a combobox das categorias
        if index == 0: #se for a primeira escolha("nova categoria") pode se editar , se não não se pode editar
            self.categoria_input.setEditable(True)
            self.categoria_input.clearEditText()
            self.categoria_input.setCurrentText("")
        else:
            self.categoria_input.setEditable(False)

   
    def on_lista_changed(self, index):  #controlo de quando se pode editar a combobox das listas
       if index == 0: # se for a primeira escolha("nova lista") pode se editar , se não não se pode editar
           self.lista_input.setEditable(True)
           self.lista_input.clearEditText()  
           self.lista_input.setCurrentText("") 
       else:
           self.lista_input.setEditable(False)


    # Criação das tarefas
    def create_task(self):
        titulo = self.title_input.text().strip() # busca o titulo escrito
        descricao = self.description_input.text().strip() # busca a descrição escrita
            
        if self.lista_input.currentIndex() == 0:
           lista = self.lista_input.currentText().strip()# Nova lista - busca o texto escrito
           if not lista:
               QMessageBox.warning(self, "Erro", "Por favor, digite um nome para a nova lista.")
               return
        else:
           lista = self.lista_input.currentText()# Lista existente - busca o texto selecionado

        if not titulo or not descricao or not lista:
            QMessageBox.warning(self, "Erro", "Por favor preencha todos os campos!")
            return

        data = self.creation_date_input.date().toString("dd/MM/yyyy") # busca a data de criação
        
        categoria = self.categoria_input.currentText()# categoria existente - busca o texto selecionado

        if self.categoria_input.currentIndex() == 0:
            categoria = self.categoria_input.currentText().strip()# categoria nova - busca o texto escrito
        
        if not categoria:
               QMessageBox.warning(self, "Erro", "Por favor, digite um nome para a nova categoria.")
               return
            
        lista_tarefas = ListaDeTarefas(lista, self.nome) #criacao de um objeto lista de tarefas ,passando o nome do utilizador e a lista fornecida
        lista_tarefas.adicionar_tarefa(titulo, descricao, data, categoria) # adicao da tarefa a esse objeto (lista)
        QMessageBox.information(self, "Success", "Task created successfully!")
        self.task_created.emit() # emição do sinal da atualização da combo box do ecra appwindow (janela principal)
        self.close()
     
    # fecho da janela
    def back_window(self):
        self.close()




class ViewListWindow(QMainWindow): #janela de visualização de listas
    list_removed = pyqtSignal() #sinal de atualizar combobox da appwindow caso as tarefas de uma lista tenham sido todas apagadas
    def __init__(self, nome, lista):
        super().__init__()
        self.nome = nome
        self.lista = lista
        self.sistema = SistemaGestaoTarefa(nome)
        self.setWindowTitle("Tarefas")
        self.setGeometry(500,300,450,500)

    # Widget principal (container)
        container = QWidget()
        self.setCentralWidget(container)

    # Layout do container
        layout = QVBoxLayout()
        container.setLayout(layout)

    # layout dos elemntos da filtragem de tarefas 
        filter_layout = QHBoxLayout()
       
    # Label da lista
        label = QLabel(f"{lista}:")
        layout.addWidget(label)

    # label da filtragem por categoria 
        label_categoria = QLabel("Filtragem por categoria:")
        filter_layout.addWidget(label_categoria)

    # layout dos botoes a baixo da Qlist
        bottom_layout = QHBoxLayout()

    # combobox da filtragem por categoria 
        self.categoria_filter = QComboBox()
        self.categoria_filter.addItems(["Não filtrar"] + self.sistema.get_categorias_lista(self.nome, self.lista))#vai buscar as categorias da lista usando o sistema gestao de tarefas
        filter_layout.addWidget(self.categoria_filter)

    # label da filtragem por status
        self.label_status = QLabel("Filtragem por status:")
        filter_layout.addWidget(self.label_status)

    # combobox da filtragem por status
        self.status_filter = QComboBox()
        self.status_filter.addItems(["Não filtrar"] + ["Pendente"] + ["Concluida"])
        filter_layout.addWidget(self.status_filter)

    # Botao filtrar
        self.filtrar_button = QPushButton("Filtrar")
        self.filtrar_button.clicked.connect(self.filtrar_tarefas)
        filter_layout.addWidget(self.filtrar_button)

    # Adição do layout das opções de filtragem ao layout principal  
        layout.addLayout(filter_layout)

    # Qlist - "quadro" das tarefas da lista (visualizam das tarefas)
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)
        self.display_tasks()# atualização do quadro das tarefas

    # botao atualizar tarefa selecionada
        self.update_tarefa_button = QPushButton("Atualizar Tarefa selecionada")
        self.update_tarefa_button.clicked.connect(self.update_tarefa)
        bottom_layout.addWidget(self.update_tarefa_button)


    # botao de remover tarefa selecionada
        self.remove_tarefa_button = QPushButton("Remover Tarefa Selecionada")
        self.remove_tarefa_button.clicked.connect(self.remove_tarefa)
        bottom_layout.addWidget(self.remove_tarefa_button)


    # botao de marcar tarefa como concluida/pendente
        self.status_tarefa_button = QPushButton("Marcar Tarefa como Conluída/Pendente")
        self.status_tarefa_button.clicked.connect(self.update_status_tarefa)
        bottom_layout.addWidget(self.status_tarefa_button)

    # adição do layout das opções abaixo da Qlist ao layout principal
        layout.addLayout(bottom_layout)

    # botao de voltar atras
        self.back_button = QPushButton("Voltar")
        self.back_button.clicked.connect(self.close)
        layout.addWidget(self.back_button)



    def filtrar_tarefas(self): #filtração das tarefas de acordo com as comboboxs de filtragem
        categoria = self.categoria_filter.currentText()
        status = self.status_filter.currentText()

        # cria lista de tarefas filtradas  com todas as tarefas da lista
        tarefas_filtradas = self.sistema.get_tarefas_da_lista(self.lista)

        # Aplica o filtro de categoria, se necessário
        if categoria != "Não filtrar":
            tarefas_filtradas = [
                tarefa for tarefa in tarefas_filtradas
                if categoria in tarefa
            ]

        # Aplica o filtro de status, se necessário
        if status != "Não filtrar":
            tarefas_filtradas = [
                tarefa for tarefa in tarefas_filtradas
                if status in tarefa
            ]

        # Exibe as tarefas filtradas
        self.display_tasks(tarefas_filtradas)
    
    
    # obter as tarefas para display  usando o nome e lista
    def display_tasks(self, tarefas=None):
        self.task_list.clear()
        if tarefas is None:
            tarefas = self.sistema.get_tarefas_da_lista(self.lista)
        for task in tarefas:
            self.task_list.addItem(task)


    def update_tarefa(self): #cria ojeto edit task window e abre o mesmo passando os atributos (nome, lista) e a tarefa
        tarefa = self.task_list.currentItem()
        if tarefa:
            self.edit_task_window = EditTaskWindow(self.nome ,self.lista ,tarefa)
            self.edit_task_window.task_updated.connect(self.display_tasks)# update das tarefas comforme a mudança da tarefa na janela de ediçã de tarefa
            self.edit_task_window.task_updated.connect(self.update_categoria_filter)#update do filtro da categoria comforme a mudança da categoria na janela de edição de tarefas
            self.edit_task_window.show()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, selecione uma tarefa para editar.")


    def update_status_tarefa(self): #mudança de status da tarefa selecionada
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_text = selected_item.text()
            titulo = task_text.split(' - ')[0] 
            tarefa = Tarefa(self.nome, self.lista, titulo, "", "", "")# procura a tarefa baseado no nome do utilizador ,lista e titulo
            tarefa.trocar_status_tarefa(self.nome, self.lista, titulo)
            self.filtrar_tarefas() # Atualiza a lista de tarefas tendo em conta possiveis filtros
        else:
            QMessageBox.warning(self, "Erro", "Por favor, selecione uma tarefa.")


    def update_categoria_filter(self): #atualização dos filtros da combobox das categorias
        self.categoria_filter.clear()
        self.categoria_filter.addItems(["Não filtrar"] + self.sistema.get_categorias_lista(self.nome, self.lista))


    def remove_tarefa(self): #remoção da tarefa selecionada
        tarefa_selecionada = self.task_list.currentItem()
        if tarefa_selecionada:
            # Extrair título da tarefa
            titulo_tarefa = tarefa_selecionada.text().split(' - ')[0]

            # Confirmar exclusão
            resposta = QMessageBox.question(
                self,
                "Confirmar remoção",
                f"Tem certeza de que deseja remover a tarefa '{titulo_tarefa}'?",
                QMessageBox.Yes | QMessageBox.No
            )

            if resposta == QMessageBox.Yes:
                lista_tarefas = ListaDeTarefas(self.lista ,self.nome) #criacao de objeto lista de tarefas para acessar o metodo de remover tarefas da lista
                sucesso, mensagem = lista_tarefas.remover_tarefa(self.nome,self.lista, titulo_tarefa)

                if sucesso:
                    QMessageBox.information(self, "Sucesso", mensagem)
                    self.display_tasks()  # Atualizar a lista de tarefas
                else:
                    QMessageBox.warning(self, "Erro", mensagem)

                if self.task_list.count() == 0: #se tarefa removida for a ultima da lista o ecra fecha e a combobox das listas na appwindow atualiza via sinal
                    QMessageBox.information(self, "Lista vazia", "Todas as tarefas foram removidas. A janela será fechada.")
                    self.list_removed.emit() #sinal para atualizar a combobox na appwindow
                    self.close()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, selecione uma tarefa para remover.")




class EditTaskWindow(QMainWindow): #janela de edição de tarefas
    task_updated = pyqtSignal()
    def __init__(self, nome, lista, tarefa):
        super().__init__()
        self.setWindowTitle("Editar tarefa")
        self.setGeometry(500,300,450,500)
        self.nome = nome
        self.lista = lista
        self.tarefa = tarefa
        self.sistema = SistemaGestaoTarefa(nome) 

        # Widget principal (container)
        container = QWidget()
        self.setCentralWidget(container)
        
        # Layout do container
        layout = QVBoxLayout()
        container.setLayout(layout)
       
        #label do titulo  
        self.label_title_update = QLabel("Título:")
        layout.addWidget(self.label_title_update)
        
        # campo de escrita titulo
        self.title_update_input = QLineEdit()
        self.title_update_input.setText(tarefa.text().split(' - ')[0])# o titulo anterior é automaticamente inserido
        layout.addWidget(self.title_update_input)


        #label da descrição
        self.label_descricao_update = QLabel("Descrição:")
        layout.addWidget(self.label_descricao_update)

        # campo de escrita descrição
        self.descricao_update_input = QLineEdit()
        self.descricao_update_input.setText(tarefa.text().split(' - ')[1])# a descrição antiga é automaticamente inserida
        layout.addWidget(self.descricao_update_input)

        # label da categoria
        categoria_label = QLabel("Categoria:")
        layout.addWidget(categoria_label)

        # combobox das categorias
        self.categoria_input = QComboBox()
        self.categoria_input.setFixedWidth(300)
        self.categoria_input.setEditable(True)
        self.categoria_input.addItems(["Nova categoria..."] + self.sistema.get_categorias_utilizador(self.nome))
        self.categoria_input.currentIndexChanged.connect(self.on_categoria_changed)# troca da capacidade de editar a combobox (editar se for para uma categoria nova)
        layout.addWidget(self.categoria_input)


        #botao confirmar edição
        self.confirm_update_button = QPushButton("Editar Tarefa")
        self.confirm_update_button.clicked.connect(self.change_tarefa)
        layout.addWidget(self.confirm_update_button)


        #botao de voltar atras
        self.back_button = QPushButton("Voltar")
        self.back_button.clicked.connect(self.close)
        layout.addWidget(self.back_button)




    def on_categoria_changed(self, index): # controlo de quando se pode editar a combobox das categorias
        if index == 0:# se for a primeira escolha("nova categoria") pode se editar , se não não se pode editar
            self.categoria_input.setEditable(True)
            self.categoria_input.clearEditText()
            self.categoria_input.setCurrentText("")
        else:
            self.categoria_input.setEditable(False)


    def change_tarefa(self): #edição da tarfa selecionada
        novo_titulo = self.title_update_input.text().strip()#novo titulo inserido no campo de escrita
        nova_descricao = self.descricao_update_input.text().strip()#nova descricao inserida no campo de escrita
        nova_categoria = self.categoria_input.currentText().strip()#nova categoria escolhida na combobox das categorias 

        if not novo_titulo or not nova_descricao or not nova_categoria: #verifica se todas as opcões foram preenchidas
            QMessageBox.warning(self, "Erro", "Por favor preencha todos os campos!")
            return

        # uso do metodo atualizar tarefa da class sistema gestao tarefa usando os novos parametros da tarefa 
        sucesso, mensagem = SistemaGestaoTarefa.atualizar_tarefa( 
        nome_usuario=self.nome,
        lista_tarefa=self.lista,
        titulo_original=self.tarefa.text().split(' - ')[0],
        novo_titulo=novo_titulo,
        nova_descricao=nova_descricao,
        nova_categoria=nova_categoria
        )

        if sucesso:
            QMessageBox.information(self, "Sucesso", mensagem)
            self.task_updated.emit()  # Emitir sinal para atualizar a lista de tarefas na viewlistWindow
            self.close()
        else:
            QMessageBox.warning(self, "Erro", mensagem)

    

    
