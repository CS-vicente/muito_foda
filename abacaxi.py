import os
import unicodedata

def normalizar(texto):
    corpo = unicodedata.normalize('NFKD', texto)
    return "".join([c for c in corpo if not unicodedata.combining(c)]).lower().strip()

saldo = 0.00
sistema = "Inicializado"
confirmacao = "a"
dia = 13
disponibilidade = 1
mes = 4
status_receita = False

acervo = {
    "Dom Casmurro": 35.00, "1984": 42.00, "O Pequeno Príncipe": 25.00,
    "Orgulho e Preconceito": 30.00, "O Alquimista": 38.00, "Cem Anos de Solidão": 55.00,
    "A Metamorfose": 20.00, "Grande Sertão: Veredas": 60.00, "O Senhor dos Anéis": 85.00,
    "Crime e Castigo": 48.00, "O Grande Gatsby": 32.00, "Ensaio Sobre a Cegueira": 45.00,
    "O Sol é Para Todos": 39.00, "Admirável Mundo Novo": 41.00, "A Hora da Estrela": 28.00,
    "Moby Dick": 50.00, "Ulysses": 70.00, "O Retrato de Dorian Gray": 33.00,
    "Dom Quixote": 65.00, "O Código Da Vinci": 40.00
}

estoque_mercado = {
    "Alimentos": {
        "Arroz 5kg": 25.50, "Feijão 1kg": 8.90, "Macarrão": 4.50, "Açúcar 1kg": 5.20,
        "Café 500g": 18.00, "Óleo de Soja": 7.50, "Sal 1kg": 3.00, "Farinha de Trigo": 5.80,
        "Leite Condensado": 6.20, "Biscoito Recheado": 3.50
    },
    "Bebidas": {
        "Refrigerante 2L": 9.50, "Suco de Laranja": 12.00, "Água Mineral 500ml": 2.50,
        "Água Mineral 1.5L": 4.50, "Cerveja Lata": 5.50, "Vinho Tinto": 45.00,
        "Energético": 10.00, "Chá Gelado": 7.00, "Leite Integral": 5.50, "Café Solúvel": 15.00
    },
    "Produtos Gerais": {
        "Detergente": 2.50, "Sabão em Pó": 15.00, "Papel Higiênico": 12.50,
        "Shampoo": 14.00, "Creme Dental": 4.00, "Desinfetante": 8.50,
        "Esponja de Aço": 2.00, "Sabonete": 3.20, "Amaciante 2L": 16.00, "Desodorante": 11.00
    },
    "Hortifruti": {
        "Banana Dúzia": 7.00, "Maçã kg": 10.00, "Batata kg": 6.50, "Cebola kg": 5.00,
        "Tomate kg": 8.00, "Alface Unidade": 3.50, "Cenoura kg": 4.50, "Alho 100g": 4.00,
        "Ovos 12un": 12.00, "Limão kg": 6.00
    },
    "Padaria": {
        "Pão Francês kg": 16.00, "Pão de Forma": 8.50, "Bolo de Cenoura": 15.00,
        "Queijo Prato 100g": 7.50, "Presunto 100g": 6.00, "Manteiga 200g": 10.50
    }
}

estoque_farmacia = {
    "Gerais": {
        "Paracetamol": 12.50, "Dipirona": 8.00, "Ibuprofeno": 15.30, "Omeprazol": 22.00,
        "Loratadina": 14.90, "Buscopan": 18.20, "Eno": 3.50, "Engov": 5.00,
        "Dorflex": 10.00, "Vitamina C": 25.00
    },
    "Controlados": {
        "Amoxicilina": 35.00, "Sertralina": 45.00, "Rivotril": 52.00
    }
}

registro_receitas = [
    "550e8400-e29b-41d4-a716-446655440000",
    "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "123e4567-e89b-12d3-a456-426614174000",
    "z99-abc-12345-X9-!!!-9999"
]

def fazer_input(mensagem):
    global sistema
    entrada = input(mensagem)
    if entrada.lower() == "finalizar":
        sistema = "finalizado"
        return "SAIR_GERAL"
    if entrada.lower() == "voltar":
        return "VOLTAR_FASE"
    return entrada

print ("")
print ("---- Escreva 'Finalizar' para sair ou 'Voltar' para retornar ao menu anterior. ----")
print ("")

while sistema.lower() != "finalizado" :
    escolha = fazer_input("Bem vindo a central! Qual dos serviços abaixo você deseja? \n1-Banco\n2-Biblioteca\n3-Super-Mercado\n4-Médico\n \nInsira o número desejado: ")
   
    if escolha == "SAIR_GERAL": break
    os.system('cls')
   
    if escolha == "adm1":
        saldo = 100
    elif escolha == "adm2":
        saldo = 1000
    elif escolha == "adm3":
        saldo = 10000

    while escolha == "1" or escolha.lower() == "banco" or escolha.lower() == "1-banco":
        print("Serviço escolhido: Banco.")
        banco = fazer_input("Quais dos serviços do banco você deseja?\n Sacar\n Depositar\n Transferir\n Emprestimo\n Saldo\n")
       
        if banco == "SAIR_GERAL": break
        if banco == "VOLTAR_FASE":
            os.system('cls')
            escolha = "reset"
            break
       
        if banco.lower() == "saldo":
            os.system('cls')
            print("\n Saldo restante: R$",saldo)
        if banco.lower() == "sacar":
            entrada_saque = fazer_input(f"Dinheiro disponivel para saque: {saldo:.2f} Quanto deseja sacar? ")
            if entrada_saque == "SAIR_GERAL": break
            if entrada_saque == "VOLTAR_FASE":
                os.system('cls')
                continue
           
            try:
                Saque = float(entrada_saque)
                if Saque > saldo:
                    os.system('cls')
                    print("Saldo indisponivel")
                elif Saque <= 0:
                    os.system('cls')
                    print("Valor invalido! Insira um valor superior a 0.")
                else:
                    os.system('cls')
                    print(f"Saque no valor de R$ {Saque} realizado com sucesso!")
                    saldo = saldo - Saque
                    escolha = "a"
            except ValueError:
                print("Erro: Insira apenas valores numéricos.")

        elif banco.lower() == "depositar":
            valor_dep = fazer_input("Insira o valor que está sendo depositado: R$")
            if valor_dep == "SAIR_GERAL": break
            if valor_dep == "VOLTAR_FASE":
                os.system('cls')
                continue
            try:
                os.system('cls')
                saldo = float(valor_dep)
                print(f"Valor de R$ {saldo} depositado com sucesso!")
            except ValueError:
                print("Erro: Valor inválido.")

        elif banco.lower() == "transferir":
            v_transf = fazer_input("Insira o valor da transferencia: ")
            if v_transf == "SAIR_GERAL": break
            if v_transf == "VOLTAR_FASE":
                os.system('cls')
                continue
            try:
                valor_transferencia = float(v_transf)

                while valor_transferencia > saldo:
                    print(f"Valor indisponivel. Saldo: R$ {saldo}")
                    v_novo = fazer_input("Insira o novo valor ou 'voltar': ")
                    if v_novo == "SAIR_GERAL": break
                    if v_novo == "VOLTAR_FASE": break
                    try:
                        valor_transferencia = float(v_novo)
                    except ValueError:
                        print("Erro: Digite um número.")

                cpf_input = fazer_input("Insira o CPF: ")
                if cpf_input == "SAIR_GERAL": break
                if cpf_input == "VOLTAR_FASE":
                    os.system('cls')
                    continue
                try:
                    cpf = float(cpf_input)
                    if cpf > 99999999999 or cpf < 10000000000:
                        print("CPF Invalido.")
                    else:
                        confirmacao = "a"
                        while confirmacao.lower() not in ["s", "n"]:
                            confirmacao = fazer_input(f"Confirma R$ {valor_transferencia} para CPF: {cpf}? (S/N): ")
                            if confirmacao == "SAIR_GERAL": break
                            os.system('cls')
                            if confirmacao.lower() == "s": print("Efetuada.")
                            elif confirmacao.lower() == "n": print("Cancelada.")
                except ValueError:
                    print("Erro: CPF deve conter apenas números.")
            except ValueError:
                print("Erro: Valor inválido.")

        elif banco.lower() == "emprestimo":
            v_emp = fazer_input("Valor do emprestimo: R$")
            if v_emp == "SAIR_GERAL": break
            if v_emp == "VOLTAR_FASE":
                os.system('cls')
                continue
            try:
                valor_emprestimo = float(v_emp)
                os.system('cls')
                print("O valor mensal será de:")
                if valor_emprestimo <= 500: print(round(valor_emprestimo/12))
                elif valor_emprestimo <= 1000: print((valor_emprestimo*0.07)+(valor_emprestimo/12))
               
                confirmacao = "a"
                while confirmacao.lower() not in ["s", "n"]:
                    confirmacao = fazer_input("Deseja confirmar seu emprestimo? (S/N) ")
                    if confirmacao == "SAIR_GERAL": break
                    os.system('cls')
                    if confirmacao.lower() == "s":
                        print("Emprestimo efetuado.")
                        saldo += valor_emprestimo
            except ValueError:
                print("Erro: Valor inválido.")

    while escolha == "2" or escolha.lower() == "biblioteca" or escolha.lower() == "2-biblioteca":
        print("Serviço escolhido: Biblioteca.")
        biblioteca = fazer_input("Deseja: Emprestar / Comprar / Acervo / Voltar: ")
       
        if biblioteca == "SAIR_GERAL": break
        if biblioteca == "VOLTAR_FASE":
            os.system('cls')
            escolha = "reset"
            break

        if biblioteca.lower() == "comprar":
            livro_desejado = fazer_input("Qual o livro que deseja comprar? ")
            if livro_desejado == "SAIR_GERAL": break
           
            if livro_desejado in acervo:
                valor_livro = acervo[livro_desejado]
                print(f"O livro custa R$ {valor_livro:.2f}")
                confirmar = fazer_input("Confirmar compra? (S/N): ")
                os.system('cls')
                if confirmar.lower() == 's':
                    if saldo >= valor_livro:
                        saldo -= valor_livro
                        del acervo[livro_desejado]
                        print(f"Sucesso! Saldo: R$ {saldo:.2f}")
                    else:
                        print("Saldo insuficiente!")
            else:
                os.system('cls')
                print("Livro não encontrado ou fora de estoque.")

        elif biblioteca.lower() == "emprestar":
            livro_desejado = fazer_input("Qual o livro que deseja emprestar? ")
            if livro_desejado == "SAIR_GERAL": break
           
            if livro_desejado in acervo:
                entrada_tempo = fazer_input("Por quanto tempo deseja emprestar? (Semanas) ")
                if entrada_tempo == "SAIR_GERAL": break
                if entrada_tempo == "VOLTAR_FASE":
                    os.system('cls')
                    continue
                try:
                    tempo = int(entrada_tempo)
                    valor_livro = acervo[livro_desejado]
                    print(f"O emprestimo deste livro por {tempo} custaria R$ {valor_livro*tempo:.2f}")
                    confirmar = fazer_input("Confirmar emprestimo? (S/N): ")
                    os.system('cls')
                    if confirmar.lower() == 's':
                        if saldo >= valor_livro*tempo:
                            saldo -= valor_livro*tempo
                            del acervo[livro_desejado]
                            print(f"Sucesso! Saldo: R$ {saldo:.2f}")
                        else:
                            print("Saldo insuficiente!")
                except ValueError:
                    print("Erro: Digite um número inteiro para as semanas.")
            else:
                os.system('cls')
                print("Livro não encontrado ou fora de estoque.")

        elif biblioteca.lower() == "acervo":
            os.system('cls')
            print("")
            for livro, preco in acervo.items():
                print(f"Livro: {livro:.<25} Preço: R$ {preco:>6.2f}")
            print("")

    while escolha == "3" or escolha.lower() in ["mercado", "super-mercado"]:
        print("\nServiço escolhido: Super-Mercado.")
        Mercado = fazer_input("Qual serviço deseja acessar? Comprar / Ver itens / Voltar \n")
       
        if Mercado == "SAIR_GERAL" or Mercado == "VOLTAR_FASE":
            os.system('cls')
            escolha = "reset"
            break

        if Mercado.lower() == "comprar":
            compra = fazer_input("Qual produto deseja comprar? ").lower()
           
            achou = False
            for secao, itens in estoque_mercado.items():
                for nome_real in itens:
                    if compra == nome_real.lower():
                        valor_produto = itens[nome_real]
                        print(f"Produto: {nome_real} | Valor: R$ {valor_produto:.2f}")
                       
                        confirmar = fazer_input("Confirmar compra? (S/N): ").lower()
                        if confirmar == "SAIR_GERAL": break
                        os.system('cls')
                        if confirmar == 's' and saldo >= valor_produto:
                            saldo -= valor_produto
                            del estoque_mercado[secao][nome_real]
                            print("Compra efetuada!")
                        elif confirmar == 's':
                            print("Saldo insuficiente!")
                        elif confirmar == 'n':
                            print("Compra cancelada")
                        achou = True
                        break
                if achou: break
            if not achou:
                os.system('cls')
                print("Produto não encontrado em nenhuma seção.")

        elif Mercado.lower() == "ver itens":
            os.system('cls')
            for secao, itens in estoque_mercado.items():
                print(f"\n--- {secao} ---")
                for produto, preco in itens.items():
                    print(f"{produto:.<25} R$ {preco:>6.2f}")

    while escolha == "4" or escolha.lower() == "médico":
        print("\nServiço escolhido: Médico.")
        medico = fazer_input("Qual serviço deseja acessar? Agendamento / Farmácia / Voltar \n")
       
        if medico == "SAIR_GERAL": break
        if medico == "VOLTAR_FASE":
            os.system('cls')
            escolha = "reset"
            break

        if medico.lower() == "agendamento":
            print(f"Próximo dia disponível para consulta: {dia}/{mes}")
            confirmar = fazer_input("Confirmar consulta? (S/N): ")
            if confirmar == "SAIR_GERAL": break
            if confirmar == "VOLTAR_FASE":
                os.system('cls')
                continue

            os.system('cls')
            if confirmar.lower() == 's':
                dia += 1
                if dia > 30:
                    dia = 1
                    mes += 1
                print("Consulta agendada!")
            else:
                print("Consulta cancelada.")

        elif normalizar(medico) == "farmacia":
            os.system('cls')
            while True:
                escolha2 = fazer_input("O que deseja fazer na Farmácia?\n Ver produtos \n Comprar remédio \n Registrar receita \n Voltar \n")
               
                if escolha2 == "SAIR_GERAL":
                    medico = "SAIR_GERAL"
                    break
                if escolha2 == "VOLTAR_FASE":
                    os.system('cls')
                    break

                if normalizar(escolha2) in ["ver produtos", "produtos", "ver produto"]:
                    os.system('cls')
                    for secao, itens in estoque_farmacia.items():
                        print(f"\n--- {secao} ---")
                        for remedio, preco in itens.items():
                            print(f"{remedio:.<25} R$ {preco:>6.2f}")
               
                elif normalizar(escolha2) in ["comprar remedio", "comprar", "remedio"]:
                    compra = fazer_input("Qual medicamento deseja comprar? ").title()
                   
                    if compra == "SAIR_GERAL":
                        medico = "SAIR_GERAL"
                        break
                    if compra == "VOLTAR_FASE":
                        os.system('cls')
                        continue

                    achou_f = False
                    for secao, itens in estoque_farmacia.items():
                        if compra in itens:
                            valor_remedio = itens[compra]

                            if secao == "Controlados":
                                print(f"!!! {compra} é um medicamento CONTROLADO !!!")
                                if status_receita == False:
                                    os.system('cls')
                                    print("Venda bloqueada. É obrigatória a apresentação da receita.")
                                    achou_f = True
                                    break
                           
                            print(f"Produto: {compra} | Valor: R$ {valor_remedio:.2f}")
                            confirmar = fazer_input("Confirmar compra? (S/N): ").lower()
                           
                            if confirmar == "SAIR_GERAL":
                                medico = "SAIR_GERAL"
                                break
                            if confirmar == "VOLTAR_FASE":
                                os.system('cls')
                                achou_f = True
                                break

                            os.system('cls')
                            if confirmar == 's' and saldo >= valor_remedio:
                                saldo -= valor_remedio
                                del estoque_farmacia[secao][compra]
                                print(f"Compra realizada! Saldo atual: R$ {saldo:.2f}")
                            elif confirmar == 's':
                                print("Saldo insuficiente!")
                            achou_f = True
                            break
                    if not achou_f:
                        os.system('cls')
                        print("Medicamento não encontrado no estoque.")
               
                elif normalizar(escolha2) in ["registrar receita", "receita", "registrar"]:
                    receita = fazer_input("Insira o registro de sua receita: ")
                   
                    if receita == "SAIR_GERAL":
                        medico = "SAIR_GERAL"
                        break
                    if receita == "VOLTAR_FASE":
                        os.system('cls')
                        continue

                    os.system('cls')
                    if receita.strip() in registro_receitas:
                        print("Você foi registrado e agora pode comprar os medicamentos que esta receita te autoriza.")
                        status_receita = True
                    else:
                        print("Registro Inválido.")
            if medico == "SAIR_GERAL": break
print("Sistema Encerrado.")