import sys


class TratamentoCpf:
    def __init__(self):
        self.lista_cpf = []

    def tratamento_cpf(self, cpf):
        cpf_formatado = cpf.replace('.', '').replace('-', '')
        self.lista_cpf = list(cpf_formatado)

        return self.lista_cpf

    def calculo_primeiro_digito(self):
        multiplicador = 10
        soma_total = 0
        for i in self.lista_cpf[0:9]:
            multiplicado = multiplicador * int(i)
            soma_total += multiplicado
            multiplicador -= 1

        cal_final = (soma_total * 10) % 11
        primeiro_digito = 0 if cal_final > 9 else cal_final

        return primeiro_digito

    def calculo_segundo_digito(self):
        multiplicador = 11
        soma_total = 0
        for i in self.lista_cpf[0:10]:
            multiplicado = multiplicador * int(i)
            soma_total += multiplicado
            multiplicador -= 1

        cal_final = (soma_total * 10) % 11
        segundo_digito = 0 if cal_final > 9 else cal_final

        return segundo_digito


if __name__ == '__main__':
    lista_de_instancia = TratamentoCpf()
    cpf_inserido_usuario = input('Digite o CPF: ')
    if cpf_inserido_usuario[0] * len(cpf_inserido_usuario) != cpf_inserido_usuario:
        cpf_tratado = lista_de_instancia.tratamento_cpf(cpf_inserido_usuario)
    else:
        print('O CPF inserido está com dados sequenciais.')
        sys.exit()

    cal_primeiro_digito = lista_de_instancia.calculo_primeiro_digito()
    cal_segundo_digito = lista_de_instancia.calculo_segundo_digito()

    if (cal_primeiro_digito == int(lista_de_instancia.lista_cpf[9])) and \
            (cal_segundo_digito == int(lista_de_instancia.lista_cpf[10])):
        print('O CPF inserido é válido')
    else:
        print('O CPF inserido é inválido')
