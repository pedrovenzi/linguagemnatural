vocab = {id_novo: bytes([id_novo]) for id_novo in range(256)}

def contar_pares(tokens):
    freq = {}
    for par in zip(tokens, tokens[1:]):
        freq[par] = freq.get(par, 0) + 1
    return freq

#contagem = contar_pares(tokens)

#par_maximo = max(contagem, key=contagem.get)
#print(par_maximo)

def fundir_pares(tokens, par, id_novo_token):
    """
    In the list of integers (ids), replace all consecutive occurrences
    of pair with the new integer token idx
    Example: ids=[1, 2, 3, 1, 2], pair=(1, 2), idx=4 -> [4, 3, 4]
    """
    novos_tokens = []
    i = 0
    while i < len(tokens):
        # if not at the very last position AND the pair matches, replace it
        if tokens[i] == par[0] and i < len(tokens) - 1 and tokens[i+1] == par[1]:
            novos_tokens.append(id_novo_token)
            i += 2
        else:
            novos_tokens.append(tokens[i])
            i += 1
    return novos_tokens

def tokenizar(texto, tamanho_vocab):
    tokens = list(texto.encode("utf-8"))
    # print(f"{[chr(t) for t in tokens]}")

    fusoes = {}
    num_fusoes = tamanho_vocab - 256

    for fusao in range(num_fusoes):
        freq_pares = contar_pares(tokens)
        if not freq_pares:
            break
        par_max = max(freq_pares, key=freq_pares.get)
        id_novo_token = 256 + len(fusoes)
        fusoes[par_max] = id_novo_token
        tokens = fundir_pares(tokens, par_max, id_novo_token)

    for (p0, p1), id_novo_token in fusoes.items():
        vocab[id_novo_token] = vocab[p0] + vocab[p1]
 
    tokens_final = set()
    for token in tokens:
        token_str = vocab[token].decode("utf-8", errors="replace")
        if token_str not in tokens_final:
            print(token_str)
            tokens_final.add(token_str)


#tokenizar(texto, tamanho_vocab=300)