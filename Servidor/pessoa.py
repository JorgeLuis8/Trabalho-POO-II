class Usuario:
    def __init__(self,nome,email,endereco,userName,senha):
        self._nome = nome
        self._email = email
        self._endereco = endereco
        self._user = userName
        self._senha = senha
    @property
    def nome(self):
        return self._nome
    @property
    def email(self):
        return self._email
    @property
    def endereco(self):
        return self._endereco
    @property
    def userName(self):
        return self._UserName
    @property
    def senha(self):
        return self._senha
    @email.setter
    def email(self,email):
        self._email = email
    @endereco.setter
    def endereco(self,endereco):
        self._endereco = endereco
    @userName.setter
    def userName(self,userName):
        self._UserName = userName
    @senha.setter
    def senha(self,senha):
        self._senha = senha
    
