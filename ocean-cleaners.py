menu_acoes = ["Cadastrar chamado", "Listar chamados", "Finalizar chamado"]
chamados: list[list[str]] = []

print(
    "\n"
    " ██████   ██████ ███████  █████  ███    ██      ██████ ██      ███████  █████  ███    ██ ███████ ██████  ███████ \n"
    "██    ██ ██      ██      ██   ██ ████   ██     ██      ██      ██      ██   ██ ████   ██ ██      ██   ██ ██      \n"
    "██    ██ ██      █████   ███████ ██ ██  ██     ██      ██      █████   ███████ ██ ██  ██ █████   ██████  ███████ \n"
    "██    ██ ██      ██      ██   ██ ██  ██ ██     ██      ██      ██      ██   ██ ██  ██ ██ ██      ██   ██      ██ \n"
    " ██████   ██████ ███████ ██   ██ ██   ████      ██████ ███████ ███████ ██   ██ ██   ████ ███████ ██   ██ ███████ \n"
    "\n\nOlá! Nós somos a Ocean Cleaners, uma plataforma que conecta a população com equipes de limpeza para áreas marítimas poluídas"
)


def input_inteiro(
    msg: str,
    intervalo_min: int = 0,
    intervalo_max: int = None,
) -> int:
    msg = f"\n[?] {msg}\n> "
    value = input(msg)

    # Pede o input novamente enquanto o texto não for numérico ou não estiver no intervalo definido na chamada da função
    while (
        not value.isnumeric()
        or int(value) < intervalo_min
        or (intervalo_max and int(value) > intervalo_max)
    ):
        print("[ERRO] Você deve informar um número inteiro no intervalo fornecido")
        value = input(msg)
    return int(value)


def input_texto(msg: str, tamanho_min: int = 1, tamanho_max: int = None) -> str:
    msg = f"\n[?] {msg}\n> "
    value = input(msg)

    # Pede o input novamente enquanto o texto não tiver o tamanho mínimo e máximo definidos
    while len(value) < tamanho_min or (tamanho_max and len(value) > tamanho_max):
        # Exibe a mensagem de erro citando também o tamanho mínimo e máximo (caso haja) esperados pela função
        print(
            f"[ERRO] O texto inserido deve ter no mínimo {tamanho_min} {f'e no máximo {tamanho_max} caracteres' if tamanho_max else 'caracteres'}"
        )
        value = input(msg)
    return value


def construir_lista_numerada(msg_menu: str, itens: list[str]) -> str:
    # Concatena à mensagem fornecida os itens da lista, de forma numerada iniciando em 1
    for i, item in enumerate(itens, 1):
        msg_menu += f"\n{i} - {item}"

    return msg_menu


def coletar_indice_menu(msg_menu: str, opcoes: list[str]) -> int:
    msg_menu = construir_lista_numerada(msg_menu, opcoes)

    # Retorna a opção escolhida pelo usuário subtraindo 1, para que a opção possa ser utilizada como índice de listas
    return input_inteiro(msg_menu, intervalo_min=1, intervalo_max=len(opcoes)) - 1


def criar_chamado() -> None:
    local_chamado = input_texto(
        "Para qual local deseja cadastrar um chamado?", tamanho_min=5
    )
    for local, autor in chamados:
        # Impede que um novo chamado seja criado para o mesmo local
        if local.lower() == local_chamado.lower():
            print(f"[ERRO] {autor} já cadastrou um chamado para esse local!\n")
            return None
    autor_chamado = input_texto(
        "Digite o nome de quem efetuou o chamado", tamanho_max=30
    )

    chamados.append([local_chamado, autor_chamado])


def pegar_listagem_chamados() -> str:
    # Transforma a matriz em uma lista plana seguindo o formato [["Local", "Autor"]] -> ["Local (Autor)"]
    return [f"{c[0]} ({c[1]})" for c in chamados]


while True:
    idx_opcao_escolhida = coletar_indice_menu("Escolha a ação desejada", menu_acoes)

    if menu_acoes[idx_opcao_escolhida] == "Cadastrar chamado":
        criar_chamado()
    elif menu_acoes[idx_opcao_escolhida] == "Listar chamados":
        listagem = construir_lista_numerada(
            '\n[!] Abaixo os locais com chamados cadastrados"',
            pegar_listagem_chamados(),
        )

        print(listagem)
    else:
        listagem_normalizada = pegar_listagem_chamados()
        idx_chamado_a_finalizar = coletar_indice_menu(
            "Qual chamado deseja finalizar?", listagem_normalizada
        )
        # Remove o chamado da lista
        chamados.pop(idx_chamado_a_finalizar)

        # Exibe uma mensagem de retorno pro usuário informadno qual chamado foi deletado
        print(
            f'[-] O chamado "{listagem_normalizada[idx_chamado_a_finalizar]}" foi finalizado'
        )

    resposta_continuar = input_texto("Você deseja fazer mais alguma operação? (s/n)")
    # Força o usuário a escolher somente as opções "s" ou "n"
    while resposta_continuar not in ["s", "n"]:
        print("[ERRO] Resposta inválida")
        resposta_continuar = input_texto(
            "Você deseja fazer mais alguma operação? (s/n)"
        )

    # Se o usuário não quiser continuar, exibe uma mensagem agradecendo e finaliza o programa
    if resposta_continuar == "n":
        print("\n[!] Obrigado por utilizar nossa plataforma! O programa foi finalizado")
        break
