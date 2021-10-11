import sqlite3
from sqlite3.dbapi2 import connect

def conectar():
    banco = sqlite3.connect('banco.db')
    return banco

def criar_tabela_usuario():
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(usuario TEXT, senha TEXT, adm BOOLEAN)")
    banco.commit()
    banco.close()

def criar_tabela_produtos():
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS produtos(codigo TEXT, descricao TEXT)")
    banco.commit()
    banco.close()

def criar_tabela_nfse():
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS nfse(valor TEXT, data DATE)")
    banco.commit()
    banco.close()

def buscar_usuario(usuario):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM usuarios WHERE usuario='{usuario}'")
    return cursor.fetchone()

def inserir_usuario(usuario, senha, adm):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO usuarios VALUES('{usuario}', '{senha}', {adm})")
    banco.commit()
    banco.close()

def inserir_usuario_por_modelo(usuario_modelo):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO usuarios VALUES('{usuario_modelo.usuario}', '{usuario_modelo.senha}', {usuario_modelo.adm})")
    banco.commit()
    banco.close()

def criar_tabela_funcionario():
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS funcionarios(nome TEXT, funcao TEXT, matricula TEXT, usuario_id INTEGER, FOREIGN KEY(usuario_id) REFERENCES usuario(id))")
    banco.commit()
    banco.close()

def inserir_funcionario_por_modelo(modelo_funcionario):
    criar_tabela_funcionario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO funcionarios VALUES('{modelo_funcionario.nome}', '{modelo_funcionario.funcao}', {modelo_funcionario.matricula}, {modelo_funcionario.usuario_id})")
    banco.commit()
    banco.close()

def buscar_funcionario_por_matricula(matricula):
    criar_tabela_funcionario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM funcionarios WHERE matricula='{matricula}'")
    return cursor.fetchone()

def buscar_todos_funcionarios():
    criar_tabela_funcionario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM funcionarios")
    return cursor.fetchall()

def buscar_funcionarios_por_usuario():
    criar_tabela_funcionario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT f.rowid, f.nome, f.funcao, f.matricula, u.usuario FROM funcionarios f JOIN usuarios u ON u.rowid = f.usuario_id")
    return cursor.fetchall()

def buscar_funcionarios_por_id(id):
    criar_tabela_funcionario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM funcionarios WHERE rowid={id}")
    return cursor.fetchone()

def remover_funcionario_e_usuario(id_funcionario, id_usuario):
    criar_tabela_funcionario()
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"DELETE FROM funcionarios WHERE rowid={id_funcionario}")
    cursor.execute(f"DELETE FROM usuarios WHERE rowid={id_usuario}")
    banco.commit()
    banco.close()

def remover_funcionario_por_id(id_funcionario):
    criar_tabela_funcionario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"DELETE FROM funcionarios WHERE rowid={id_funcionario}")
    banco.commit()
    banco.close()



def buscar_funcionarios_por_nome(nome):
    criar_tabela_funcionario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM funcionarios WHERE nome LIKE '%{nome}%'")
    return cursor.fetchall()

def buscar_produtos():
    criar_tabela_produtos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM produtos")
    return cursor.fetchall()

def buscar_produtos_por_codigo(codigo):
    criar_tabela_produtos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM produtos WHERE codigo='{codigo}'")
    return cursor.fetchone()

def inserir_produto(codigo, descricao):
    criar_tabela_produtos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO produtos VALUES('{codigo}', '{descricao}')")
    banco.commit()
    banco.close()

def remover_produto_por_codigo(codigo):
    criar_tabela_produtos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"DELETE FROM produtos WHERE codigo='{codigo}'")
    banco.commit()
    banco.close()

def inserir_nfse(valor, data):
    criar_tabela_nfse()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO nfse VALUES('{valor}', '{data}')")
    banco.commit()
    banco.close()

def buscar_todas_nfse():
    criar_tabela_nfse()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM nfse")
    return cursor.fetchall()

    
if __name__ == "__main__":
    inserir_usuario("alex", "alex", True)
