import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


stopwords_pt = [
    "a", "à", "ao", "aos",
    "as", "às",
    "o", "os",
    "um", "uma", "uns", "umas",
    "de", "da", "das", "do", "dos",
    "em", "na", "nas", "no", "nos",
    "e", "é",
    "que",
    "por", "para",
    "com",
    "sem",
    "se",
    "como",
    "mais",
    "mas",
    "ou",
    "já",
    "não",
    "nem",
    "sobre",
    "até",
    "entre",
    "pelo", "pela", "pelos", "pelas",
    "seu", "sua", "seus", "suas",
    "meu", "minha", "meus", "minhas",
    "teu", "tua", "teus", "tuas"
]

abreviacoes = {
    "gn": "gênesis",
    "gen": "gênesis",
    "ex": "êxodo",
    "exod": "êxodo",
    "lv": "levítico",
    "lev": "levítico",
    "nm": "números",
    "num": "números",
    "dt": "deuteronômio",
    "deut": "deuteronômio",
    "js": "josué",
    "jz": "juízes",
    "rt": "rute",
    "1sm": "II samuel",
    "2sm": "II samuel",
    "1rs": "I reis",
    "2rs": "II reis",
    "1cr": "I crônicas",
    "2cr": "II crônicas",
    "ed": "esdras",
    "ne": "neemias",
    "et": "ester",
    "jó": "jó",
    "sl": "salmos",
    "pv": "provérbios",
    "ec": "eclesiastes",
    "ct": "cânticos",
    "is": "isaías",
    "jr": "jeremias",
    "lm": "lamentações",
    "ez": "ezequiel",
    "dn": "daniel",
    "os": "oséias",
    "jl": "joel",
    "am": "amós",
    "ob": "obadias",
    "jn": "jonas",
    "mq": "miquéias",
    "na": "naum",
    "hc": "habacuque",
    "sf": "sofonias",
    "ag": "ageu",
    "zc": "zacarias",
    "ml": "malaquias",
    "mt": "mateus",
    "mc": "marcos",
    "lc": "lucas",
    "jo": "joão",
    "at": "atos",
    "rm": "romanos",
    "1co": "I coríntios",
    "2co": "II coríntios",
    "gl": "gálatas",
    "ef": "efésios",
    "fp": "filipenses",
    "cl": "colossenses",
    "1ts": "I tessalonicenses",
    "2ts": "II tessalonicenses",
    "1tm": "I timóteo",
    "2tm": "II timóteo",
    "tt": "tito",
    "fm": "filemom",
    "hb": "hebreus",
    "tg": "tiago",
    "1pe": "I pedro",
    "2pe": "II pedro",
    "1jo": "I joão",
    "2jo": "II joão",
    "3jo": "III joão",
    "jd": "judas",
    "ap": "apocalipse"
}


def load_biblia(caminho):
    biblia = {}

    livro_atual = None
    capitulo_atual = None

    with open(caminho, "r", encoding="utf-8") as arquivo:

        for linha in arquivo:
            linha = linha.strip()

            if not linha:
                continue

            match_capitulo = re.match(
                r"^(.+?)\s+(\d+)$",
                linha
            )

            if match_capitulo:
                livro_atual = match_capitulo.group(1).strip()
                capitulo_atual = int(match_capitulo.group(2))
                continue

            match_versiculo = re.match(
                r"^(\d+)\s+(.+)$",
                linha
            )

            if (
                match_versiculo
                and livro_atual
                and capitulo_atual
            ):
                numero_versiculo = match_versiculo.group(1)
                texto_versiculo = match_versiculo.group(2).strip()

                chave = (
                    f"{livro_atual} "
                    f"{capitulo_atual}:"
                    f"{numero_versiculo}"
                ).lower()

                biblia[chave] = texto_versiculo

    return biblia


def normalizar_referencia(referencia):
    referencia = referencia.strip().lower()
    referencia = referencia.replace(".", ":")
    referencia = " ".join(referencia.split())

    partes = referencia.split()

    if len(partes) < 2:
        return None

    livro = partes[0]
    capitulo_versiculo = partes[1]

    if livro in abreviacoes:
        livro = abreviacoes[livro]

    return f"{livro} {capitulo_versiculo}"


def buscar_versiculo(biblia, referencia):
    referencia_normalizada = normalizar_referencia(referencia)

    if referencia_normalizada is None:
        return None

    return biblia.get(referencia_normalizada)


def buscar_por_tema(
    pergunta,
    biblia,
    vectorizer,
    matriz_tfidf,
    quantidade=5
):
    pergunta_tfidf = vectorizer.transform([pergunta])

    similaridades = cosine_similarity(
        pergunta_tfidf,
        matriz_tfidf
    )

    indices = similaridades[0].argsort()[::-1][:quantidade]

    chaves = list(biblia.keys())
    resultados = []

    for indice in indices:
        referencia = chaves[indice]
        texto = biblia[referencia]
        pontuacao = similaridades[0][indice]

        resultados.append(
            (referencia, texto, pontuacao)
        )

    return resultados



biblia = load_biblia("biblia.txt")

versiculos = list(biblia.values())

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words=None
)

matriz_tfidf = vectorizer.fit_transform(versiculos)

print("Quantidade de versículos:", len(versiculos))
print("Formato da matriz:", matriz_tfidf.shape)


print("\nEscolha o tipo de busca:")
print("1 - Buscar por referência")
print("2 - Buscar por tema")

opcao = input("\nDigite uma opção: ").strip()


if opcao == "1":

    referencia = input(
        "\nDigite uma referência bíblica: "
    )

    versiculo = buscar_versiculo(
        biblia,
        referencia
    )

    if versiculo:
        referencia_formatada = normalizar_referencia(referencia)

        print("\nVersículo encontrado:")
        print(referencia_formatada)
        print(versiculo)
    else:
        print("\nVersículo não encontrado.")


elif opcao == "2":

    pergunta = input(
        "\nDigite um tema: "
    )

    resultados = buscar_por_tema(
        pergunta,
        biblia,
        vectorizer,
        matriz_tfidf
    )

    print("\nResultados:\n")

    for referencia, texto, pontuacao in resultados:
        print(referencia)
        print(texto)
        print(f"Similaridade: {pontuacao:.4f}")
        print("-" * 60)


else:
    print("\nOpção inválida.")


def gerar_resposta(mensagem, biblia, vectorize, matriz_tfidf):
    mensagem = mensagem.strip()

    if not mensagem:
        return "Digite uma refência biblica ou um tema"

    partes = mensagem.split(maxsplit=1)
    comando = partes[0].lower()

    if len(partes) == 1:
        return (
            "Use um dos formatos:\n"
            "/versiculo Jo 3:16\n"
            "/tema amor"
        )

    consulta = partes[1].strip()

    if comando == "/versiculo":
        versiculo = buscar_versiculo(biblia, consulta)

        if versiculo:
            referencia = normalizar_referencia(consulta)

            return(
                f"{referencia}\n\n"
                f"{versiculo}"
            )

        return "Não encontrei esse versículo"

    elif comando == "/tema":
        resultados = buscar_por_tema(
            consulta,
            biblia,
            vectorizer,
            matriz_tfidf,
            quantidade=5
        )

        resposta = "Versículos relacionados:\n\n"

        for referencia, texto, pontuacao in resultados:
            resposta += (
                f"{referencia}\n"
                f"{texto}\n"
            )

            return resposta.strip()

    else:
        return(
             "Comando não reconhecido.\n\n"
            "Use:\n"
            "/versiculo Jo 3:16\n"
            "/tema amor"
        )
