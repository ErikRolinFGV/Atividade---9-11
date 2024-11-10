from atividade911 import Loja, Funcionario, Guitarra, Baixo, Violao

"""Driver Code da atividade911, com exemplos das funções"""
if __name__ == "__main__":
    # Criação de uma loja com localização composta
    loja_sp = Loja("São Paulo", "Brasil")
    loja_rj = Loja("Rio de Janeiro", "Brasil")
    loja_sp.definir_loja_mais_proxima(loja_rj)

    # Criação de funcionários e adição à loja
    func1 = Funcionario("Yuri", "12345678901", 3500, "Vendedor")
    func2 = Funcionario("Carlos Ivan", "10987654321", 4500, "Gerente")
    loja_sp.adicionar_funcionario(func1)
    loja_sp.adicionar_funcionario(func2)

    # Criação de instrumentos e adição ao estoque da loja
    guitarra = Guitarra("Fender", "Stratocaster", 6000, 6, "Single Coil")
    baixo = Baixo("Ibanez", "SR300", 3200, 4, "Ativo")
    violao = Violao("Yamaha", "FG800", 1500, 6, "Aço")
    loja_sp.adicionar_instrumento(guitarra)
    loja_sp.adicionar_instrumento(baixo)
    loja_sp.adicionar_instrumento(violao)

    # Teste de funcionalidades
    print("Localização da loja:", loja_sp.localizacao)
    print("Loja mais próxima:", loja_sp.loja_mais_proxima.localizacao)
    print("Estoque de instrumentos:", loja_sp.consultar_estoque())
    print("Funcionários por cargo:", loja_sp.consultar_funcionarios_por_cargo())

    # Transferência de funcionário entre lojas
    func1.transferir_para_loja(loja_rj)
    print("Funcionários da loja SP após transferência:", loja_sp.consultar_funcionarios_por_cargo())
    print("Funcionários da loja RJ:", loja_rj.consultar_funcionarios_por_cargo())