# Bíblia Bot

Bot desenvolvido em Python que permite consultar versículos bíblicos por referência ou pesquisar versículos relacionados a determinado tema. O projeto também possui uma integração experimental com o **WhatsApp Web**, utilizando Selenium.

## Funcionalidades

* Consulta de versículos por referência bíblica.
* Busca de versículos por tema utilizando TF-IDF e similaridade de cosseno.
* Suporte a abreviações de livros bíblicos.
* Normalização de referências bíblicas.
* Integração com o WhatsApp Web.
* Resposta automática a comandos enviados em uma conversa aberta.
* Manutenção da sessão do WhatsApp por meio de um perfil separado do Chrome.

## Tecnologias utilizadas

* Python
* Selenium
* WebDriver Manager
* Scikit-learn
* TF-IDF
* Similaridade de cosseno
* Google Chrome
* WhatsApp Web

## Estrutura do projeto

```text
BibliaBot/
│
├── biblia.py
├── biblia.txt
├── bot.py
├── teste_bot.py
├── perfil_whatsapp/
└── README.md
```

### Descrição dos arquivos

| Arquivo            | Descrição                                                                                            |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| `biblia.py`        | Contém o carregamento da Bíblia, a busca por referência, a busca por tema e a geração das respostas. |
| `biblia.txt`       | Arquivo de texto contendo o conteúdo da Bíblia Sagrada.                                              |
| `bot.py`           | Executa a integração do bot com o WhatsApp Web por meio do Selenium.                                 |
| `teste_bot.py`     | Permite testar as consultas diretamente pelo terminal, sem utilizar o WhatsApp.                      |
| `perfil_whatsapp/` | Diretório utilizado para armazenar a sessão do WhatsApp Web.                                         |
| `README.md`        | Documentação do projeto.                                                                             |

## Requisitos

Antes de executar o projeto, é necessário ter instalado:

* Python 3.10 ou superior;
* Google Chrome;
* Uma conta do WhatsApp;
* Acesso ao WhatsApp Web.

Também é recomendado utilizar um ambiente virtual Python.

## Instalação

Clone o projeto ou abra a pasta do projeto no VS Code.

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install selenium webdriver-manager scikit-learn
```

## Testando o bot pelo terminal

Antes de utilizar o WhatsApp, é possível testar a lógica do bot diretamente pelo terminal.

Execute:

```bash
python teste_bot.py
```

O programa poderá receber comandos como os exemplos abaixo.

### Buscar um versículo

```text
/versiculo Jo 3:16
```

Exemplo de outros formatos:

```text
/versiculo João 3:16
/versiculo Sl 23:1
/versiculo Gn 1:1
```

### Buscar por tema

```text
/tema amor
```

Outros exemplos:

```text
/tema fé
/tema esperança
/tema perdão
/tema ansiedade
```

Para encerrar o programa:

```text
sair
```

## Utilizando o bot no WhatsApp

Execute o arquivo principal:

```bash
python bot.py
```

O Selenium abrirá uma janela do Google Chrome com o WhatsApp Web.

### Passos para iniciar

1. Execute o arquivo `bot.py`.
2. Aguarde o WhatsApp Web carregar.
3. Escaneie o QR Code, caso seja necessário.
4. Abra manualmente a conversa em que deseja testar o bot.
5. Volte ao terminal do VS Code.
6. Pressione `ENTER` quando o programa solicitar.
7. Envie uma mensagem utilizando um dos comandos disponíveis.

### Comandos disponíveis

Buscar um versículo:

```text
/versiculo Jo 3:16
```

Buscar versículos por tema:

```text
/tema amor
```

O bot processará o comando e enviará a resposta automaticamente na conversa aberta.

## Como funciona a busca por tema

A busca temática utiliza o método **TF-IDF**, que transforma os textos dos versículos em vetores numéricos.

Em seguida, a consulta enviada pelo usuário também é transformada em um vetor. O bot calcula a **similaridade de cosseno** entre a consulta e os versículos da Bíblia.

Os versículos com maior similaridade são considerados os mais relacionados ao tema pesquisado.

O resultado é uma lista com os versículos mais próximos da consulta realizada.

## Limitações atuais

* O bot funciona inicialmente com uma conversa do WhatsApp aberta manualmente.
* O bot não identifica automaticamente todos os contatos ou grupos.
* A estrutura interna do WhatsApp Web pode mudar, fazendo com que os seletores do Selenium deixem de funcionar.
* O bot responde apenas a mensagens que começam com `/versiculo` ou `/tema`.
* A busca temática é baseada em similaridade textual, não em uma interpretação teológica profunda.
* A consulta por referência depende do formato e da normalização implementados no projeto.
* O bot deve ser monitorado durante a execução.
* O uso automatizado do WhatsApp deve respeitar as regras e políticas da plataforma.

## Exemplos de uso

### Consulta por referência

Entrada:

```text
/versiculo Jo 3:16
```

Saída esperada:

```text
João 3:16

Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito,
para que todo aquele que nele crê não pereça, mas tenha a vida eterna.
```

### Consulta por tema

Entrada:

```text
/tema amor
```

Saída esperada:

```text
Versículos relacionados:

João 3:16
Porque Deus amou o mundo de tal maneira...

1 Coríntios 13:4
O amor é paciente, o amor é bondoso...

...
```

## Possíveis melhorias futuras

* Identificação automática de novas mensagens recebidas.
* Processamento de mensagens comuns, como `Olá` ou `Ajuda`.
* Criação de um comando de ajuda.
* Suporte mais robusto a livros com nomes compostos.
* Melhoria da busca semântica utilizando modelos de linguagem.
* Registro das mensagens processadas.
* Prevenção mais robusta contra mensagens duplicadas.
* Suporte a múltiplas conversas.
* Criação de uma interface gráfica.
* Integração com uma API de modelos de linguagem.
* Implantação do bot em um servidor.

## Aviso

Este projeto foi desenvolvido para fins educacionais e experimentais, com o objetivo de estudar:

* Manipulação de arquivos de texto;
* Estruturas de dados em Python;
* Processamento de linguagem natural;
* Recuperação de informação;
* Similaridade textual;
* Automação de navegador;
* Integração com o WhatsApp Web utilizando Selenium.
