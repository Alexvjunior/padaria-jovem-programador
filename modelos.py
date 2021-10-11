class Usuario():
    def __init__(self) -> None:
        self.usuario = None
        self.senha = None
        self.adm = None
        self.id = None

    def banco_para_modelo(self, usuario_banco):
        self.id = usuario_banco[0]
        self. usuario = usuario_banco[1]
        self.senha = usuario_banco[2]
        self.adm = usuario_banco[3]

class Funcionario():
    def __init__(self) -> None:
        self.id = None
        self.nome = None
        self.funcao = None
        self.matricula = None
        self.usuario_id = None

    def banco_para_modelo(self, funcionario_banco):
        self.id = funcionario_banco[0]
        self.nome = funcionario_banco[1]
        self.funcao = funcionario_banco[2]
        self.matricula = funcionario_banco[3]
        self.usuario_id = funcionario_banco[4]