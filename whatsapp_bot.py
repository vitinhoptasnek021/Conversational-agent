import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from biblia import (
    biblia,
    vectorizer,
    matriz_tfidf,
    gerar_resposta
)


options = webdriver.ChromeOptions()

options.add_argument(
    "--user-data-dir=C:/Users/vitin/VS_CODE/PUC/Agentes conversacionais/perfil_whatsapp"
)

options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")
options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 60)

driver.get("https://web.whatsapp.com")

print("Abra o WhatsApp Web e escaneie o QR Code, se necessário.")
input("Quando o WhatsApp estiver carregado, pressione ENTER aqui...")


def obter_mensagens_recebidas():
    """
    Retorna as mensagens recebidas visíveis no chat atualmente aberto.
    """

    elementos = driver.find_elements(
        By.CSS_SELECTOR,
        'span[data-testid="selectable-text"]'
    )

    mensagens = []

    for elemento in elementos:
        try:
            texto = elemento.text.strip()

            if texto:
                mensagens.append(texto)

        except Exception:
            continue

    return mensagens


def enviar_mensagem(texto):
    """
    Envia uma mensagem no chat atualmente aberto.
    """

    caixa_mensagem = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "div[contenteditable='true'][data-tab]"
            )
        )
    )

    caixa_mensagem.click()
    caixa_mensagem.send_keys(texto)
    caixa_mensagem.send_keys(Keys.ENTER)


ultima_mensagem = ""

print("Bot iniciado.")
print("Abra manualmente o chat que deseja testar.")
print("Pressione CTRL + C no terminal para encerrar.")


ultima_mensagem = ""

print("Bot iniciado. Aguardando mensagens...")


while True:
    try:
        mensagens = obter_mensagens_recebidas()

        print("Mensagens encontradas:", mensagens)

    
        mensagens_comandos = [
            mensagem
            for mensagem in mensagens
            if mensagem.strip().lower().startswith(
                ("/versiculo", "/tema")
            )
        ]

        if mensagens_comandos:
            mensagem_atual = mensagens_comandos[-1]

            if mensagem_atual != ultima_mensagem:
                ultima_mensagem = mensagem_atual

                print(f"Mensagem recebida: {mensagem_atual}")

                resposta = gerar_resposta(
                    mensagem_atual,
                    biblia,
                    vectorizer,
                    matriz_tfidf
                )

                print(f"Resposta: {resposta}")

                enviar_mensagem(resposta)

        time.sleep(3)

    except KeyboardInterrupt:
        print("\nBot encerrado pelo usuário.")
        break

    except Exception as erro:
        print(f"Erro temporário: {erro}")
        time.sleep(3)


driver.quit()