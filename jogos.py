class Jogos:
    def __init__(self,nome,ano_lancamento) -> None:
        self._nome = nome
        self._ano_lancamento = ano_lancamento
    @property
    def nome(self):
        return self._nome
    @property
    def ano_lancamento(self):
        return self._ano_lancamento