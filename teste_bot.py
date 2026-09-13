from biblia import (
    biblia,
    vectorizer,
    matriz_tfidf,
    gerar_resposta
)

while True: 
    mensagem = input("\nDigite uma mensagem: ")

    if mensagem.lower() == "sair":
        break

    resposta = gerar_resposta(
        mensagem,
        biblia,
        vectorizer,
        matriz_tfidf
    )

    print("\nResposta do bot: ")
    print(resposta)