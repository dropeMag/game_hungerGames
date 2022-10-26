import random
from time import sleep

# lista com acontecimentos padrões do jogo =============================================================================
acoes_inicio_jogo = ["Foi para a cornucópia", "Foi para a cornucópia", "Pegou uma mochila e fugiu"]
mortesPadrao = ["Morreu ao cair de uma grande altura", "Morreu ao pisar em uma mina terrestre", "Morreu de insolação", "Morreu atingido(a) por um raio suspeito", "Morreu ao cometer suicídio"]
armasPadrao = ["uma espada larga", "uma espada curta", "um arco e flechas", "um martelo", "uma lança", "uma maça", "uma adaga", "um machado"]
alimentosPadrao = ["Comeu suas próprias unhas", "Comeu as fezes de outro tributo", "Comeu suas próprias fezes", "Comeu o corpo morto de "]
locaisDormirPadrao = ["Dormiu em uma árvore", "Dormiu no chão sem proteção", "Dormiu em um buraco no chão", "Dormiu em uma cabana improvisada", "Dormiu em cima de uma pedra"]
naoDormirPadrao = ["Ficou acordado a noite toda", "Fingiu que estava dormindo", "Teve insônia e não dormiu", "Tentou dormir, mas não conseguiu"]
emocoesPadrao = ["O tributo chorou de medo", "O tributo teve crise de ansiedade", "O tributo chorou pedindo a mamãe", "O tributo ficou gritando para ninguém", "O tributo gritou prometendo vencer", "O tributo ficou parado olhando para o nada", "O tributo começou a rir do nada"]
acoesNormaisPadrao = ["O tributo ficou andando em circulos por minutos", "O tributo cogitou beber a própria urina", "O tributo andou atrás de comida", "O tributo andou por horas sem parar", "O tributo notou que tinha se perdido", "O tributo conversou com sua própria mão", "O tributo viu algo se mexendo e correu", "O tributo ficou falando sozinho(a)", "O tributo treinou seus movimentos de luta", "O tributo conversou com uma pedra sobre o clima"]
acoesPerigosasPadrao = ["Começou a ter alucinações", "Se arriscou em uma altura alta", "Ficou gritando para alguém mata-lo(a)", "Ficou xingando a Capital", "Decidiu rolar no chão pelado(a)"]
cacarTributoPadrao = ["Tentou matar {}({}), mas falhou", "Coreu atrás de {}({}), mas não alcançou", "Pensou em matar {}({}), mas desistiu"]
matarTributoPadrao = ["Matou {}({})", "Peseguiu e matou {}({})", "Atacou {}({}), enquanto ele(a) defecava,", "Finalmente matou {}({}), depois de dias tentando,"]
encontrosPadrao = ["Observou e imaginou {}({}) pelado(a)", "Viu {}({}) cagando e, estranhamente, gostou", "Ficou admirado(a) com {}({}) mijando", "Pensou ter visto {}({})", "Trombou com {}({}) e saiu correndo", "Ficou stalkeando {}({}) enquanto banhava"]


# function para a criação de títulos ===================================================================================
def titulo_preenchido(txt, espaco=False):
    print(f'{txt:=^47}')
    if espaco:
        print('')


def titulo_vazio(txt, espaco=False):
    print(f' {txt:^47} ')
    if espaco:
        print('')


# área designada para a criação de tributos ============================================================================
# nomes para tributos
nomes_masculinos = ["Miguel", "Davi", "Gabriel", "Arthur", "Lucas", "Matheus", "Pedro", "Guilherme", "Gustavo", "Rafael", "Felipe", "Bernardo", "Nicolas", "Cauã", "Vitor", "Eduardo", "Daniel", "Henrique", "Murilo", "Vinicius", "Samuel", "Pietro", "Leonardo", "Caio", "Heitor", "Lorenzo", "Isaac", "Lucca", "Thiago", "Theo", "Bruno", "Bryan", "Breno", "Emanuel", "Ryan", "Yuri", "Benjamin", "Erick", "Enzo", "Fernando", "Joaquim", "André", "Tomás", "Francisco", "Rodrigo", "Igor", "Antonio", "Ian", "Juan", "Diogo", "Otávio", "Nathan", "Calebe", "Danilo", "Luan", "Kaique", "Alexandre", "Iago", "Ricardo", "Raul", "Marcelo", "Cauê", "Benício", "Augusto", "Geovanni", "Renato", "Diego", "Renan", "Anthony", "Thales", "Henry", "Kevin", "Levi", "Enrico", "Hugo"]
nomes_femininos = ["Julia", "Sophia", "Isabella", "Manuela", "Giovanna", "Alice", "Laura", "Beatriz", "Mariana", "Yasmin", "Gabriela", "Rafaela", "Isabelle", "Lara", "Letícia", "Valentina", "Nicole", "Sarah", "Vitória", "Lívia", "Helena", "Lorena", "Clara", "Larissa", "Heloisa", "Marina", "Melissa", "Eduarda", "Rebeca", "Amanda", "Alícia", "Bianca", "Lavínia", "Ester", "Carolina", "Emily", "Cecília", "Pietra", "Milena", "Marcela", "Natália", "Maria", "Bruna", "Camila", "Luana", "Catarina", "Olivia", "Agatha", "Mirella", "Sophie", "Stella", "Stefany", "Isabel", "Kamilly", "Elisa", "Joana", "Mariane", "Bárbara", "Juliana", "Rayssa", "Alana", "Caroline", "Brenda", "Evelyn", "Débora", "Raquel", "Maitê", "Ana", "Nina", "Luiza", "Antonella", "Jennifer", "Betina", "Mariah", "Sabrina"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Novais", "Cândido", "do Amaral", "Moreira", "Serra", "Abravanel", "Rodrigues", "Mello", "Mel", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Alencar", "Costa", "Ribeiro", "Martins", "Carvalho", "Egue", "Almeida", "Lopes", "Soares", "Fernandes", "Vieira", "Barbosa", "Rocha", "Dias", "Nascimento", "Firmino", "Andrade", "Moreira", "Nunes", "Marques", "Machado", "Mendes", "Freitas", "Cardoso", "Villa", "Ramos", "Gonçalves", "Santana", "Pontes", "Teixeira", "Falcão", "Magalhães", "Campos"]
distritos = ["Artigos de Luxo", "Alvenaria e Armamento", "Tecnologia", "Pesca", "Energia", "Transporte", "Madeira", "Industria Téxtil", "Distribuição Agrícola", "Pecuária", "Agricultura", "Mineração"]


# function para criação de tributos
def geracao_tributos():
    lista_tributos_selecionados = list()
    numero_distrito = numero_tributo = 1
    while numero_tributo < 25:
        titulo_preenchido(f'DISTRITO {numero_distrito}')

        while True:
            # geração de nomes, idades e chances de vitória
            sobrenome = random.randint(0, len(sobrenomes)-1)
            idade = random.randint(12, 18)
            chances1 = random.randint(1, 6)
            chances2 = random.randint(chances1 + 1, 12)

            if numero_tributo % 2 == 0:
                nome = random.randint(0, len(nomes_masculinos)-1)
                nome_tributo = f'{nomes_masculinos[nome]} {sobrenomes[sobrenome]}'
                tributo_criado = {'nome': nomes_masculinos[nome], 'sobrenome': sobrenomes[sobrenome], 'idade': idade, 'distrito': numero_distrito, 'sorte': chances1/chances2, 'morto': False, 'vitimasTotal': list(), 'acaoTurno': list(), 'sono': 0, 'fome': 0}
            else:
                nome = random.randint(0, len(nomes_femininos)-1)
                nome_tributo = f'{nomes_femininos[nome]} {sobrenomes[sobrenome]}'
                tributo_criado = {'nome': nomes_femininos[nome], 'sobrenome': sobrenomes[sobrenome], 'idade': idade, 'distrito': numero_distrito, 'sorte': chances1/chances2, 'morto': False, 'vitimasTotal': list(), 'acaoTurno': list(), 'sono': 0, 'fome': 0}

            print(f'{numero_tributo:2}º: {nome_tributo:<21}  |  {idade} anos  |  {chances1}/{chances2}')
            lista_tributos_selecionados.append(tributo_criado.copy())
            numero_tributo += 1

            if numero_tributo % 2 != 0:
                titulo_vazio(' ')
                break

        numero_distrito += 1

    return lista_tributos_selecionados


# área designada para a criação de arenas ==============================================================================
# listas com os biomas e suas respectivas características únicas
listaArenas = ['Floresta Tropical', 'Deserto', 'Savana', 'Taiga']
# floresta tropical
arenaFloresta_mortes = ["Morreu por picada de insetos", "Morreu ao comer uma planta venenosa", "Morreu de uma infecção bacteriana", "Morreu assassinado(a) por um javali"]
arenaFloresta_alimentos = ["Comeu uma fruta saborosa", "Comeu carne de uma ave que caçou", "Comeu carne de peixe", "Comeu carne de um javali que achou morto"]
# deserto
arenaDeserto_mortes = ["Morreu ao comer um cacto venenoso", "Morreu ao ser caçado(a) por coiotes", "Morreu ao ser picado(a) por escorpião", "Morreu ao ser picado(a) por uma cobra"]
arenaDeserto_alimentos = ["Comeu carne de uma cobra", "Comeu carne de um coiote que achou morto", "Comeu um cacto"]
# savana
arenaSavana_mortes = ["Morreu sendo caçado(a) por hienas", "Morreu ao comer uma planta venenosa", "Morreu por picada de insetos", "Morreu de uma infecção bacteriana"]
arenaSavana_alimentos = ["Comeu carne de uma ave que caçou", "Comeu carne de uma hiena que achou morto", "Comeu carne de um cervo que caçou", "Comeu uma fruta saborosa"]
# taiga
arenaTaiga_mortes = ["Morreu de hipotermia", "Morreu sendo caçado(a) por lobos", "Morreu sendo caçado(a) por urso", "Morreu ao comer uma planta venenosa"]
arenaTaiga_alimentos = ["Comeu carne de peixe", "Comeu carne de um alce que caçou", "Comeu carne de uma ave que caçou"]

# organização das características por listas
listaMortesArenas = [arenaFloresta_mortes, arenaDeserto_mortes, arenaSavana_mortes, arenaTaiga_mortes]
listaAlimentosArenas = [arenaFloresta_alimentos, arenaDeserto_alimentos, arenaSavana_alimentos, arenaTaiga_alimentos]


# function para a criação da arena
def gerar_arena():
    arena_selecionada = random.randint(0, len(listaArenas)-1)

    # remove a árvore dos locais para dormir no deserto
    if arena_selecionada == 1:
        locaisDormirPadrao.pop(0)

    # adição de características únicas das arenas
    for info in listaMortesArenas[arena_selecionada]:
        mortesPadrao.append(info)

    for info in listaAlimentosArenas[arena_selecionada]:
        alimentosPadrao.append(info)

    return listaArenas[arena_selecionada]


# function para a geração de uma edição
def gerar_edicao():
    numero_edicao = random.randint(1, 75)
    return numero_edicao


# área designada para criar os dias dos tributos =======================================================================
# function que gera o primeiro dia com o banho de sangue
def gerar_primeiro_dia(lista_tributos, lista_tributos_vivos, lista_mortos_do_dia):
    # ações para o primeiro dia de jogos
    banho_de_sangue = list()

    # pisar na bomba
    for trib3 in lista_tributos:
        if trib3['sorte'] <= 0.08:
            trib3['morto'] = True
            trib3['formaMorte'] = f"explosão ao sair do pilar antes da hora"

    # forma as primeiras escolhas
    for trib2 in lista_tributos_vivos:
        escolha_inicial = random.choice(acoes_inicio_jogo)
        trib2['escolhaInicial'] = escolha_inicial

        # criar o banho de sangue
        if trib2['escolhaInicial'] == "Foi para a cornucópia":
            tributo_na_cornucopia = trib2
            banho_de_sangue.append(tributo_na_cornucopia)

            # pegar uma arma
            if trib2['sorte'] > 0.3 and trib2 == tributo_na_cornucopia:
                tributo_pega_arma = random.choice(armasPadrao)
                trib2['arma'] = tributo_pega_arma

    # dar chances para matar alguém
    for tribBanhoSangue in banho_de_sangue:
        assassino = random.choice(banho_de_sangue)

        if 'arma' in assassino.keys():
            matar_alguem = random.randint(1, 2)
        else:
            matar_alguem = random.randint(1, 4)

        if matar_alguem == 1:
            while True:
                vitima = random.choice(banho_de_sangue)
                if vitima != assassino:
                    break
            assassino['vitimasTotal'].append(vitima)
            vitima['morto'] = True
            vitima['formaMorte'] = f"{assassino['nome']}({assassino['distrito']})"
            banho_de_sangue.remove(vitima)
        else:
            continue

    # printa os acontecimentos
    for trib in lista_tributos:
        print(f"{trib['nome']}({trib['distrito']}):")

        # ações para o primeiro dia de jogos
        if 'escolhaInicial' in trib.keys():
            print(f' - {trib["escolhaInicial"]}')

        if 'arma' in trib.keys():
            print(f' - Pegou {trib["arma"]}')

        if len(trib['vitimasTotal']) > 0:
            for vit in trib["vitimasTotal"]:
                if 'arma' in trib.keys():
                    print(f' - Matou {vit["nome"]}({vit["distrito"]}) com {trib["arma"]}')
                else:
                    print(f' - Matou {vit["nome"]}({vit["distrito"]}) no soco')

        if trib['morto'] and trib in lista_tributos_vivos:
            print(f' - Foi morto(a) por {trib["formaMorte"]}')
            lista_mortos_do_dia.append(trib)
            listaTributosVivos.remove(trib)

        titulo_vazio(' ')
        sleep(1.2)

    return lista_tributos_vivos, lista_mortos_do_dia


# function que gera os dias e as noites normais
def gerar_dias_normais(lista_tributos_vivos, lista_mortos_do_dia, lista_mortos_total, turno_momento):
    vivos_ate_agora = lista_tributos_vivos[:]
    lista_tributos_aleatoria = random.sample(lista_tributos_vivos, len(lista_tributos_vivos))
    contador_mortes = 0
    contador_tributos = len(lista_tributos_vivos)

    # gera os acontecimentos
    for trib2 in lista_tributos_aleatoria:
        for ato in range(0, 3):
            # morrer de fome
            if trib2['fome'] == 22:
                trib2['morto'] = True
                trib2['acaoTurno'].append("Morreu de fome")
                vivos_ate_agora.remove(trib2)
                break

            # morrer de loucura
            if trib2['sono'] == 22:
                trib2['morto'] = True
                trib2['acaoTurno'].append("Ficou louco(a) e se matou")
                vivos_ate_agora.remove(trib2)
                break

            # ver se o tributo foi assassinado ou vitorioso
            if ato == 2 and trib2['morto']:
                trib2['acaoTurno'].append(f'Foi morto(a) por {trib2["assassino"]["nome"]}({trib2["assassino"]["distrito"]})')
                break
            elif ato == 2 and contador_mortes == len(lista_tributos_vivos)-1:
                trib2['acaoTurno'].append('Tributo foi declarado VITORIOSO')
                break

            # decide se o tributo dorme
            elif ato == 2 and turno_momento == 2:
                dormir_ou_nao = random.randint(1, 2)
                if dormir_ou_nao == 1:
                    escolha_dormir = random.choice(locaisDormirPadrao)
                    trib2['sono'] = 0
                else:
                    escolha_dormir = random.choice(naoDormirPadrao)
                    trib2['sono'] += 1
                trib2['acaoTurno'].append(escolha_dormir)

            # cria as escolhas personalizadas de cada tributo
            else:
                acao_do_tributo = random.randint(1, 17)

                # define se o tributo morre ou não
                if acao_do_tributo <= 2:
                    if acao_do_tributo == 1 or trib2['morto']:
                        trib2['acaoTurno'].append(f'Quase {random.choice(mortesPadrao).lower()}')
                    else:
                        if contador_mortes < len(lista_tributos_vivos)-1:
                            trib2['acaoTurno'].append(f'{random.choice(mortesPadrao)}')
                            trib2['morto'] = True
                            vivos_ate_agora.remove(trib2)
                            contador_mortes += 1
                            break
                        else:
                            trib2['acaoTurno'].append('Tributo foi declarado VITORIOSO')
                            break

                # define se o tributo vai comer ou não
                elif acao_do_tributo <= 4:
                    if acao_do_tributo == 3:
                        comida_do_tributo = random.choice(alimentosPadrao)
                        # define se foi ou não canibalismo
                        if comida_do_tributo == "Comeu o corpo morto de ":
                            tributo_morto_comido = random.choice(lista_mortos_total)
                            trib2['acaoTurno'].append(f"Comeu o corpo morto de {tributo_morto_comido['nome']}({tributo_morto_comido['distrito']})")
                        else:
                            trib2['acaoTurno'].append(comida_do_tributo)
                        trib2['fome'] = 0
                    else:
                        trib2['acaoTurno'].append('Procurou algo para comer, mas não achou')
                        trib2['fome'] += 1

                # define se o tributo vai demonstrar emoções
                elif acao_do_tributo <= 6:
                    trib2['acaoTurno'].append(random.choice(emocoesPadrao))

                # define as ações do tributo
                elif acao_do_tributo <= 8:
                    if trib2['sono'] == 0:
                        trib2['acaoTurno'].append(random.choice(acoesNormaisPadrao))
                    else:
                        trib2['acaoTurno'].append(random.choice(acoesPerigosasPadrao))

                # define se o tributo vai matar outro ou não
                elif acao_do_tributo <= 10:
                    if contador_tributos > 2 and not trib2['morto']:
                        tributo_cacado = random.choice(vivos_ate_agora)
                        while tributo_cacado == trib2:
                            tributo_cacado = random.choice(vivos_ate_agora)
                        # matar outro tributo
                        if acao_do_tributo == 9:
                            if 'arma' in trib2.keys():
                                matar_outro_tributo = random.choice(matarTributoPadrao).format(tributo_cacado["nome"], tributo_cacado["distrito"])
                                trib2['acaoTurno'].append(f'{matar_outro_tributo} com {trib2["arma"]}')
                            else:
                                matar_outro_tributo = random.choice(matarTributoPadrao).format(tributo_cacado["nome"], tributo_cacado["distrito"])
                                trib2['acaoTurno'].append(f'{matar_outro_tributo} com as próprias mãos')

                            tributo_cacado['morto'] = True
                            tributo_cacado['assassino'] = trib2
                            trib2['vitimasTotal'].append(tributo_cacado)
                            vivos_ate_agora.remove(tributo_cacado)
                        else:
                            cacar_outro_tributo = random.choice(cacarTributoPadrao).format(tributo_cacado["nome"], tributo_cacado["distrito"])
                            trib2['acaoTurno'].append(f'{cacar_outro_tributo}')
                    else:
                        trib2['acaoTurno'].append('Saiu à procura de alguém para matar, mas não achou')

                # define se recebe ou não paraquedas
                elif acao_do_tributo <= 12:
                    if acao_do_tributo == 11 and trib2['sorte'] >= 0.65:
                        presente = random.randint(1, 4)
                        # recebe comida
                        if presente == 1:
                            trib2['acaoTurno'].append('Recebeu um paraquedas com comida')
                            trib2['fome'] = 0
                        # recebe energético
                        elif presente == 2:
                            trib2['acaoTurno'].append('Recebeu um paraquedas com energético')
                            trib2['sono'] = 0
                        # recebe arma
                        elif presente == 3:
                            arma_do_paraquedas = random.choice(armasPadrao)
                            trib2['acaoTurno'].append(f'Recebeu um paraquedas com {arma_do_paraquedas}')
                            trib2['arma'] = arma_do_paraquedas
                        # recebe remédio
                        elif presente == 4:
                            trib2['acaoTurno'].append('Recebeu um paraquedas com remédio')
                    elif acao_do_tributo == 11 and trib2['sorte'] < 0.65:
                        trib2['acaoTurno'].append('Recebeu um paraquedas mas não conseguiu pega-lo')
                    else:
                        trib2['acaoTurno'].append('Pensou ter recebido um paraquedas')

                # define se os tributos se encontram
                elif acao_do_tributo <= 14:
                    tributo_avistado = random.choice(lista_tributos_vivos)
                    while tributo_avistado == trib2:
                        tributo_avistado = random.choice(lista_tributos_vivos)

                    encontro_outro_tributo = random.choice(encontrosPadrao).format(tributo_avistado["nome"], tributo_avistado["distrito"])
                    trib2['acaoTurno'].append(encontro_outro_tributo)

                # define se o tributo volta à cornucópia
                elif acao_do_tributo <= 16:
                    if acao_do_tributo == 15:
                        trib2['acaoTurno'].append("Pensou em voltar à Cornucópia, mas desistiu da ideia")
                    else:
                        arma_pega_cornucopia = random.choice(armasPadrao)
                        trib2['acaoTurno'].append(f'Voltou à Cornucópia e pegou {arma_pega_cornucopia}')
                        trib2['arma'] = arma_pega_cornucopia

                # define se o tributo tira um cochilo
                else:
                    trib2['acaoTurno'].append('Decidiu passar o resto do dia deitado(a)')
                    break
        contador_tributos -= 1
    vivos_ate_agora = lista_tributos_vivos[:]

    # printa os acontecimentos do dia/da noite
    for trib in lista_tributos_vivos:
        print(f"{trib['nome']}({trib['distrito']}):")

        for ato in trib['acaoTurno']:
            print(f' - {ato}')

        trib['acaoTurno'].clear()
        titulo_vazio(' ')
        sleep(1.2)

    for trib3 in vivos_ate_agora:
        if trib3['morto']:
            lista_tributos_vivos.remove(trib3)
            lista_mortos_do_dia.append(trib3)

    return lista_tributos_vivos, lista_mortos_do_dia


# aqui começa o jogo de fato (script principal) ========================================================================
# seleciona os tributos que participaram dos jogos
titulo_preenchido(' TRIBUTOS SELECIONADOS ', espaco=True)

# criação de tributos
listaTodosTributos = geracao_tributos()
listaTributosVivos = listaTodosTributos[:]

# sistema de apostas
while True:
    try:
        print('Em qual tributo você apostará?')
        numeroAposta = int(input(' Tributo Nº '))
        titulo_vazio(' ')
    except(ValueError, TypeError):
        print('\033[31mAPOSTA INVÁLIDA! ESCOLHA UM NÚMERO VÁLIDO!\033[m')
    else:
        aposta_nomeTributo = listaTodosTributos[numeroAposta-1]["nome"] + ' ' + listaTodosTributos[numeroAposta-1]["sobrenome"]
        aposta_distritoTributo = listaTodosTributos[numeroAposta-1]["distrito"]
        break

while True:
    try:
        print(f'Quanto você apostará em {aposta_nomeTributo}')
        aposta_valor = float(input(' R$ '))
        titulo_vazio(' ')
    except(ValueError, TypeError):
        print('\033[31mAPOSTA INVÁLIDA! ESCOLHA UM VALOR VÁLIDO!\033[m')
    else:
        print(f'R${aposta_valor:.2f} apostados em {aposta_nomeTributo}({aposta_distritoTributo})\n')
        titulo_preenchido(' APOSTAS ENCERRADAS ', espaco=True)
        break

# mensagem de bons jogos vorazes
sleep(2)
titulo_vazio('BONS JOGOS VORAZES')
sleep(2)
titulo_vazio('E QUE A SORTE ESTEJA SEMPRE A SEU FAVOR', espaco=True)
sleep(2)

# criação e divulgação da arena
arenaSelecionada = gerar_arena()
edicaoSelecionada = gerar_edicao()

titulo_preenchido(' INTRODUÇÃO ', espaco=True)

print(f'Edição: {edicaoSelecionada}ª')
print(f'Arena: {arenaSelecionada}')
print(f'Tributos Vivos: {len(listaTodosTributos)}')

# jogos comecem
listaMortosTotal = list()
listaMortosDoDia = list()
diasPassado = 0
turnoMomento = 1
sleep(3)

while True:
    titulo_vazio(' ')

    # gera o primeiro dia de jogos
    if diasPassado == 0:
        titulo_preenchido(f' DIA {diasPassado+1} ')
        sleep(3)
        gerar_primeiro_dia(listaTodosTributos, listaTributosVivos, listaMortosDoDia)
        turnoMomento = 2
        diasPassado += 1
    # gera o restante dos dias e noites
    else:
        if turnoMomento == 1:
            titulo_preenchido(f' DIA {diasPassado} ')
            sleep(3)
            gerar_dias_normais(listaTributosVivos, listaMortosDoDia, listaMortosTotal, turnoMomento)
            turnoMomento = 2
        elif turnoMomento == 2:
            titulo_preenchido(f' NOITE {diasPassado} ')
            sleep(3)
            gerar_dias_normais(listaTributosVivos, listaMortosDoDia, listaMortosTotal, turnoMomento)
            turnoMomento = 1

    # atualiza a lista de mortos
    for mortos in listaMortosDoDia:
        if mortos not in listaMortosTotal:
            listaMortosTotal.append(mortos)

    # interrompe e declara vencedor
    if len(listaMortosTotal) == 23:
        break

    # confirma a continuação
    input('\nenter para continuar')

    # finaliza o dia e limpa os mortos
    if turnoMomento == 1:
        titulo_preenchido(f' {diasPassado}º DIA FINALIZADO ')
        print(f'Tributos Ainda Vivos: {len(listaTributosVivos)}')
        print(f'Tibutos Mortos Hoje: {len(listaMortosDoDia)}')
        listaMortosDoDia.clear()
        diasPassado += 1
        input('\nenter para continuar')

# declaração do vencedor dos jogos =====================================================================================
titulo_vazio(' ')
titulo_preenchido(' FIM DE JOGO ', espaco=True)

# dados do vencedor
vencedor_tributo = listaTributosVivos[0]["nome"] + " " + listaTributosVivos[0]["sobrenome"]
vencedor_distrito = listaTributosVivos[0]["distrito"]

# divulgação do vencedor
print(f'Tributo Vencedor: {vencedor_tributo}')
print(f'Distrito: {vencedor_distrito} - {distritos[vencedor_distrito-1]}')
print(f'Mortes de {listaTributosVivos[0]["nome"]}:')
if len(listaTributosVivos[0]['vitimasTotal']) > 0:
    for mortes in listaTributosVivos[0]['vitimasTotal']:
        print(f' - {mortes["nome"]} {mortes["sobrenome"]}({mortes["distrito"]})')
else:
    print('  Ninguém')

input('\nenter para continuar')

# mostra os mortos dos jogos ===========================================================================================
titulo_vazio(' ')
titulo_preenchido(' MORTOS POR ORDEM ', espaco=True)

for ordem, mortos in enumerate(listaMortosTotal):
    print(f'{ordem+1:2}º - {mortos["nome"]} {mortos["sobrenome"]}({mortos["distrito"]})')

input('\nenter para continuar')

# verifica se o jogador ganhou ou perdeu a aposta ======================================================================
titulo_vazio(' ')
titulo_preenchido(' RESULTADO APOSTA ', espaco=True)

# printa dados da aposta
print(f'Tributo Apostado: {aposta_nomeTributo} ({aposta_distritoTributo})')
print(f'Valor da Aposta: R$ {aposta_valor:.2f}')

if aposta_nomeTributo == (listaTributosVivos[0]["nome"] + " " + listaTributosVivos[0]["sobrenome"]):
    print('Resultado: Ganhou')
    print(f'Valor Ganho: R$ {aposta_valor * random.randint(12, 24):.2f}')
else:
    print('Resultado: Perdeu')
    print(f'Valor Perdido: R$ {aposta_valor:.2f}')

input('\nenter para finalizar o jogo')
