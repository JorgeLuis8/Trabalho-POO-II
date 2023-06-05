class Usuairo:
    def __init__(self,nome,email,endereco,cpf,senha):
        self._nome = nome
        self._email = email
        self._endereco = endereco
        self._cpf = cpf
        self._senha = senha
    @property
    def get_nome(self):
        return self._nome
    @property
    def get_email(self):
        return self._email
    @property	
    def get_endereco(self):
        return self._endereco
    @property
    def get_cpf(self):
        return self._cpf
    @property
    def get_senha(self):
        return self._senha
    @get_nome.setter
    def set_email(self, email):
        self._nome = email
    @get_senha.setter
    def set_senha(self, senha):
        self._senha = senha
