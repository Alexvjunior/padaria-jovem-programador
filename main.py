import sys, banco
from modelos import Usuario, Funcionario
from PyQt5 import uic, QtWidgets
from datetime import date

def login():
    usuario_tela = tela_login.inputUsuario.text()
    senha_tela = tela_login.inputSenha.text()
    usuario_banco = banco.buscar_usuario(usuario_tela)
    if usuario_banco == None:
        tela_aviso.labelAviso.setText("Usuário não existe!")
        tela_aviso.show()
    elif usuario_banco[2] != senha_tela:
        tela_aviso.labelAviso.setText("Confira suas credenciais!")
        tela_aviso.show()
    elif usuario_banco[3] == 1:
        usuario_modelo_1.banco_para_modelo(usuario_banco)
        tela_login.close()
        tela_usuario_adm.show()
        inserir_todos_funcionario_usuarios_tabela()
        inserir_todos_funcionario_tabela()
        inserir_todos_produtos_tabela()
    else:
        tela_login.close()
        tela_usuario_funcionario.show()
        inserir_item_combobox()
        inserir_tabela_nfse_resultado()


def logout():
    tela_usuario_adm.close()
    tela_login.show()


def adicionar():
    usuario_modelo_1.senha = tela_usuario_adm.inputSenha.text()
    usuario_modelo_1.usuario = tela_usuario_adm.inputUsuario.text()
    usuario_modelo_1.adm = False
    usuario_banco = banco.buscar_usuario(usuario_modelo_1.usuario)

    funcionario_modelo_1.nome = tela_usuario_adm.inputNome.text()
    funcionario_modelo_1.funcao = tela_usuario_adm.inputFuncao.text()
    funcionario_modelo_1.matricula = tela_usuario_adm.inputMatricula.text()
    funcionario_banco = banco.buscar_funcionario_por_matricula(funcionario_modelo_1.matricula)
    if usuario_modelo_1.senha == "" or usuario_modelo_1.usuario == "" or funcionario_modelo_1.nome == "" or funcionario_modelo_1.funcao == "" or funcionario_modelo_1.matricula == "":
        tela_aviso.labelAviso.setText("Insira todas as informações!")
        tela_aviso.show()
    elif usuario_banco is not None:
        tela_aviso.labelAviso.setText("Usuário já cadastrado!")
        tela_aviso.show()
    elif funcionario_banco is not None:
        tela_aviso.labelAviso.setText("Matricula já cadastrada no sistema!")
        tela_aviso.show()
    else:
        banco.inserir_usuario_por_modelo(usuario_modelo_1)
        usuario_banco = banco.buscar_usuario(usuario_modelo_1.usuario)
        usuario_modelo_1.id = usuario_banco[0]
        funcionario_modelo_1.usuario_id = usuario_banco[0]
        banco.inserir_funcionario_por_modelo(funcionario_modelo_1)
        inserir_dados_tabela()

def inserir_dados_tabela():
    tabela = tela_usuario_adm.tabelaUsuarios
    tabela.insertRow(tabela.rowCount())
    tabela.setItem(tabela.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(f"{usuario_modelo_1.id}"))
    tabela.setItem(tabela.rowCount()- 1, 1, QtWidgets.QTableWidgetItem(usuario_modelo_1.usuario))
    tabela.setItem(tabela.rowCount()- 1, 2, QtWidgets.QTableWidgetItem(funcionario_modelo_1.nome))
    tabela.setItem(tabela.rowCount()- 1, 3, QtWidgets.QTableWidgetItem(funcionario_modelo_1.funcao))
    tabela.setItem(tabela.rowCount()- 1, 4, QtWidgets.QTableWidgetItem(funcionario_modelo_1.matricula))


    
def excluir():
    tabela = tela_usuario_adm.tabelaUsuarios
    linha = tabela.currentRow()
    if linha < 0:
        tela_aviso.labelAviso.setText("Selecione um item para excluir")
        tela_aviso.show()
    id_funcionario = int(tabela.item(linha,0).text())
    funcionario_banco = banco.buscar_funcionarios_por_id(id_funcionario)
    tabela.removeRow(linha)
    banco.remover_funcionario_e_usuario(id_funcionario, funcionario_banco[3])

def excluir_funcionario():
    tabela = tela_usuario_adm.tabelaFuncionario
    linha = tabela.currentRow()
    if linha < 0:
        tela_aviso.labelAviso.setText("Selecione um item para excluir")
        tela_aviso.show()
    else:
        id_funcionario = int(tabela.item(linha,0).text())
        tabela.removeRow(linha)
        banco.remover_funcionario_por_id(id_funcionario)




def inserir_todos_funcionario_usuarios_tabela():
    funcionario_usuario = banco.buscar_funcionarios_por_usuario()
    tabela = tela_usuario_adm.tabelaUsuarios
    tabela.setRowCount(len(funcionario_usuario))
    row = 0
    for fu in funcionario_usuario:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{fu[0]}"))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{fu[4]}"))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{fu[1]}"))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{fu[2]}"))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{fu[3]}"))
        row+=1

def inserir_todos_funcionario_tabela():
    funcionario = banco.buscar_todos_funcionarios()
    tabela = tela_usuario_adm.tabelaFuncionario
    tabela.setRowCount(len(funcionario))
    row = 0
    for fu in funcionario:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{fu[0]}"))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{fu[1]}"))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{fu[2]}"))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{fu[3]}"))
        row+=1


def inserir_todos_produtos_tabela():
    produtos_banco = banco.buscar_produtos()
    tabela = tela_usuario_adm.tabelaProduto
    tabela.clear()
    tabela.setRowCount(len(produtos_banco))
    row = 0
    for fu in produtos_banco:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{fu[0]}"))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{fu[1]}"))
        row+=1


def buscar_funcionario():
    nome = tela_usuario_adm.inputNomeFuncionario.text()
    if nome == "":
        tela_aviso.labelAviso.setText("Insira um nome para buscar!")
        tela_aviso.show()
    else:
        funcionarios_banco = banco.buscar_funcionarios_por_nome(nome)
        tabela = tela_usuario_adm.tabelaFuncionario
        tabela.clear()
        row = 0
        tabela.setRowCount(len(funcionarios_banco))
        for fu in funcionarios_banco:
            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{fu[0]}"))
            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{fu[1]}"))
            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{fu[2]}"))
            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{fu[3]}"))
            row+=1


def adicionar_produto():
    codigo = tela_usuario_adm.inputCodigo.text()
    descricao = tela_usuario_adm.inputDescricao.text()

    produto_banco = banco.buscar_produtos_por_codigo(codigo)
    if codigo == "" or descricao == "" :
        tela_aviso.labelAviso.setText("Insira todas as informações!")
        tela_aviso.show()
    elif produto_banco is not None:
        tela_aviso.labelAviso.setText("Produto com esse código já cadastrado!")
        tela_aviso.show()
    else:
        banco.inserir_produto(codigo, descricao)
        produto_banco = banco.buscar_produtos_por_codigo(codigo)
        inserir_todos_produtos_tabela()

    
def excluir_produto():
    tabela = tela_usuario_adm.tabelaProduto
    linha = tabela.currentRow()
    if linha < 0:
        tela_aviso.labelAviso.setText("Selecione um item para excluir")
        tela_aviso.show()
    else:
        codigo_produto = int(tabela.item(linha,0).text())
        banco.remover_produto_por_codigo(codigo_produto)
        tabela.removeRow(linha)

def adicionar_nota():
    produto = tela_usuario_funcionario.comboBox.currentText()
    valor = float(tela_usuario_funcionario.inputValor.text())
    quantidade = int(tela_usuario_funcionario.inputQuant.text())
    tabela = tela_usuario_funcionario.tabelaNfse
    tabela.insertRow(tabela.rowCount())
    tabela.setItem(tabela.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(f"{produto}"))
    tabela.setItem(tabela.rowCount()- 1, 1, QtWidgets.QTableWidgetItem(f"{valor}"))
    tabela.setItem(tabela.rowCount()- 1, 2, QtWidgets.QTableWidgetItem(f"{quantidade}"))
    resultado = float(tela_usuario_funcionario.labelValor.text().replace("R$", "").replace(",","."))
    resultado = resultado + (valor * quantidade)
    tela_usuario_funcionario.labelValor.setText(f"R${resultado}")




def inserir_item_combobox():
    combo = tela_usuario_funcionario.comboBox
    produtos_banco = banco.buscar_produtos()
    for p in produtos_banco:
        combo.addItem(p[1])

def zerar_nota():
    tabela = tela_usuario_funcionario.tabelaNfse
    tabela.setRowCount(0)
    tabela.clear()
    tela_usuario_funcionario.labelValor.setText(f"R$0,00")

def finalizar_nfse():
    valor = tela_usuario_funcionario.labelValor.text()
    if valor == "R$0,00":
        tela_aviso.labelAviso.setText("Adicione Produtos na NFSe")
        tela_aviso.show()
    else:
        data = date.today()
        banco.inserir_nfse(valor, data)
        tela_aviso.labelAviso.setText("NFSe Inserida")
        tela_aviso.show()
        tela_usuario_funcionario.tabelaNfse.clear()

def inserir_tabela_nfse_resultado():
    nfse = banco.buscar_todas_nfse()
    tabela = tela_usuario_funcionario.tabelaNfseResultado
    tabela.setRowCount(len(nfse))
    row = 0
    for fu in nfse:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{fu[0]}"))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{fu[1]}"))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{fu[2]}"))
        row+=1

if __name__ == "__main__":
    qt = QtWidgets.QApplication(sys.argv)
    usuario_modelo_1 = Usuario()
    funcionario_modelo_1 = Funcionario()

    # Carregar as telas
    tela_login = uic.loadUi('tela-login.ui')
    tela_aviso = uic.loadUi('tela-aviso.ui')
    tela_usuario_adm = uic.loadUi('tela-usuario-adm.ui')
    tela_usuario_funcionario = uic.loadUi('tala-usuario-funcionario.ui')

    # Função tela login
    tela_login.btnEntrar.clicked.connect(login)

    # Função tela admin
    tela_usuario_adm.btnLogout.clicked.connect(logout)
    tela_usuario_adm.btnAdicionar.clicked.connect(adicionar)
    tela_usuario_adm.btnExcluir.clicked.connect(excluir)
    tela_usuario_adm.btnBuscar.clicked.connect(buscar_funcionario)
    tela_usuario_adm.btnExcluirFuncionario.clicked.connect(excluir_funcionario)
    tela_usuario_adm.btnAdicionarProduto.clicked.connect(adicionar_produto)
    tela_usuario_adm.btnExcluirProduto.clicked.connect(excluir_produto)

    # Funções tela usuario funcionario
    tela_usuario_funcionario.btnAdicionar.clicked.connect(adicionar_nota)
    tela_usuario_funcionario.btnZerar.clicked.connect(zerar_nota)
    tela_usuario_funcionario.btnFinalizar.clicked.connect(finalizar_nfse)


    tela_login.show()
    qt.exec_()
