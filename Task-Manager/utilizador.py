class Utilizador:
    def __init__ (self, nome, palavra_passe):
        self.nome_utilizador = nome.strip()  #atributos do utilizador : nome e palavra-passe
        self.__palavra_passe__ = palavra_passe.strip() 
        

   #verifica se ja existe um nome igual ,se sim retorna True se nao retorna False (nao pode haver nomes repetidos)
    def verificar_nome_utilizador(nome): 
        try:
            with open('ficheiros_txt/utilizadores.txt', 'r') as file:
                for line in file:
                    stored_nome = line.strip().split(':')[0]  
                    if stored_nome.strip() == nome.strip():
                        return True
            return False
        except FileNotFoundError:
            return False
        

    
   #guarda o nome e passe no ficheiros utilizadores.txt no formato "nome:passe"
    def guardar_utilizador(nome, palavra_passe): 
        with open('ficheiros_txt/utilizadores.txt', 'a') as file:
            file.write(f"{nome.strip()}:{palavra_passe.strip()}\n")



   #verificação do login , se nome e passe escritos igualarem nome e passe de uma linha entao retorna true ,se nao retorna false 
    def verificar_credenciais(nome, palavra_passe): 
        try:
            with open('ficheiros_txt/utilizadores.txt', 'r') as file:
                for line in file:
                    stored_nome, stored_pass = line.strip().split(':')
                    if stored_nome.strip() == nome and stored_pass.strip() == palavra_passe:
                        return True
            return False
        except FileNotFoundError:
            return False
        

    '''
    mudança de palavra passe , primeiro o conteudo do ficheiro é lido , depois este procura o utilizador usando o nome 
    e se o encontrar substitui a passe pela a nova,qualquer linha que nao é o utilizador é rescrita como estava anteriormente
    '''
    def alterar_palavra_passe(nome, nova_palavra_passe): #mudança de palavra passe
        try:
            with open('ficheiros_txt/utilizadores.txt', 'r') as file:
                linhas = file.readlines()
            
            with open('ficheiros_txt/utilizadores.txt', 'w') as file:
                for line in linhas:
                    stored_nome,_ = line.strip().split(':')
                    if stored_nome.strip() == nome.strip():
                        file.write(f"{stored_nome}:{nova_palavra_passe.strip()}\n")
                    else:
                        file.write(line)
            return True, "Palavra-passe alterada com sucesso!"
        except FileNotFoundError:
            return False, "Erro: Arquivo de utilizadores não encontrado."