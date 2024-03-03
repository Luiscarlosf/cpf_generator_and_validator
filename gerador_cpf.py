import random
from verificador_cpf import TratamentoCpf


def gerar_cpf():
    cpf_aleatorio = ''.join([str(random.randint(0, 9)) for _ in range(9)])

    lista_de_instancia = TratamentoCpf()
    tratamento_cpf = lista_de_instancia.tratamento_cpf(cpf_aleatorio)

    calculo_primeiro_digito = lista_de_instancia.calculo_primeiro_digito()
    tratamento_cpf += str(calculo_primeiro_digito)
    calculo_segundo_digito = lista_de_instancia.calculo_segundo_digito()

    # concatenação dos dígitos na variável de geração aleatória
    cpf_aleatorio = cpf_aleatorio + str(calculo_primeiro_digito) + str(calculo_segundo_digito)
    cpf_aleatorio = f'{cpf_aleatorio[0:3]}.{cpf_aleatorio[3:6]}.{cpf_aleatorio[6:9]}-{cpf_aleatorio[9:]}'
    return cpf_aleatorio


print('Executando o processo de geração de CPF...')
print(gerar_cpf())
