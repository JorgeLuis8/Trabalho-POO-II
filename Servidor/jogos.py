class Jogos:
    def __init__(self,nome,ano_lancamento,desc) -> None:
        self._nome = nome
        self._ano_lancamento =ano_lancamento
        self._desc = desc
    @property
    def nome(self):
        return self._nome
    @property
    def ano_lancamento(self):
        return self._ano_lancamento
    @property
    def desc(self):
        return self._desc
    @desc.setter
    def set_desc(self, desc):
        self._desc = desc