class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario  
 
    def getsalario(self):
        return self.__salario
 
    def setSalario(self, salario):
        if salario > 0:
            self.__salario = salario 
        else:
            print("Salário inválido.")
 
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = float(bonus)
 
    def calcular_salario_total(self):
        salario_base = self.getsalario()
        total = salario_base + self.bonus
        return total
 
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem
 
    def programar(self):
        print(f"{self.nome} está desenvolvendo em {self.linguagem}.")
 
class Estagiario(Funcionario):
    def __init__(self, nome, salario, carga_horaria):
        super().__init__(nome, salario)
        self.carga_horaria = carga_horaria
 
    def estudar(self):
        print(f"{self.nome} está estudando.")
 

ge = Gerente("luiz", 6000, 1000)
 
print(f"Funcionário: {ge.nome}")

print(f"Salário Base: R${ge.getsalario()}")
 
salario_com_bonus = ge.calcular_salario_total()
print(f"Salário Total com Bônus: R${salario_com_bonus}")
 
 