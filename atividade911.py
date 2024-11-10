# Classe para representar um Cargo
class Cargo:
    # Lista de cargos válidos
    CARGOS_VALIDOS = ["Gerente", "Vendedor", "Estoquista", "Assistente"]

    def __init__(self, nome):
        if nome not in Cargo.CARGOS_VALIDOS:
            raise ValueError(f"Cargo inválido. Escolha entre: {Cargo.CARGOS_VALIDOS}")
        self.nome = nome

    def __str__(self):
        return self.nome

# Classe para representar a localização de uma loja 
class Localizacao:
    # A Localizacao é um componente da Loja
    def __init__(self, cidade, pais):
        self.cidade = cidade
        self.pais = pais

    def __str__(self):
        return f"{self.cidade}, {self.pais}"

# Classe para representar um Instrumento
class Instrumento:
    # Classe que define os atributos comuns a todos os instrumentos
    def __init__(self, marca, modelo, preco, num_cordas):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.num_cordas = num_cordas

    def __str__(self):
        return f"{self.marca} {self.modelo}, {self.num_cordas} cordas - R$ {self.preco}"

# Subclasses para tipos específicos de instrumentos
class Guitarra(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas, tipo_captador):
        super().__init__(marca, modelo, preco, num_cordas)
        self.tipo_captador = tipo_captador

class Baixo(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas, ativo_passivo):
        super().__init__(marca, modelo, preco, num_cordas)
        self.ativo_passivo = ativo_passivo

class Violao(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas, tipo_corda):
        super().__init__(marca, modelo, preco, num_cordas)
        self.tipo_corda = tipo_corda

# Classe para representar um Funcionário
class Funcionario:
    # Define atributos do funcionário e inicializa com um cargo válido
    def __init__(self, nome, cpf, salario, cargo):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = Cargo(cargo)  
        self.loja_atual = None

    def transferir_para_loja(self, nova_loja):
        # Transferência entre lojas, mantendo a relação com a loja antiga
        if self.loja_atual:
            self.loja_atual.remover_funcionario(self)
        self.loja_atual = nova_loja
        nova_loja.adicionar_funcionario(self)

# Classe para representar uma Loja
class Loja:
    def __init__(self, cidade, pais):
        self.localizacao = Localizacao(cidade, pais)
        self.funcionarios = []
        self.estoque = []
        self.loja_mais_proxima = None

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        funcionario.loja_atual = self

    def remover_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)
        funcionario.loja_atual = None

    def adicionar_instrumento(self, instrumento):
        self.estoque.append(instrumento)

    def remover_instrumento(self, tipo_instrumento):
        # Método para remover um instrumento arbitrário de um tipo específico
        for i, inst in enumerate(self.estoque):
            if isinstance(inst, tipo_instrumento):
                return self.estoque.pop(i)

    def consultar_estoque(self):
        # Conta o número de cada tipo de instrumento no estoque
        estoque_count = {"Guitarra": 0, "Baixo": 0, "Violao": 0}
        for inst in self.estoque:
            if isinstance(inst, Guitarra):
                estoque_count["Guitarra"] += 1
            elif isinstance(inst, Baixo):
                estoque_count["Baixo"] += 1
            elif isinstance(inst, Violao):
                estoque_count["Violao"] += 1
        return estoque_count

    def consultar_funcionarios_por_cargo(self):
        # Conta a quantidade de funcionários por cargo
        cargos = {}
        for func in self.funcionarios:
            cargo_nome = str(func.cargo)
            if cargo_nome not in cargos:
                cargos[cargo_nome] = 0
            cargos[cargo_nome] += 1
        return cargos

    def definir_loja_mais_proxima(self, loja):
        # Define a loja mais próxima, como um relacionamento auxiliar
        self.loja_mais_proxima = loja