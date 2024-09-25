import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import csv
import pandas as pd

lista_origem = []
planilha_destino = []
linha = []

# -----> Ínicio da leitura do arquivo de origem <-----
def ler_arquivo(arquivo:csv):
    with open(arquivo, 'r') as a:
        for linha in a:
            lista_origem.append(linha)
        lista_origem.pop(0)
    return lista_origem

#aguarda a página carregar
def aguardando():
    driver.implicitly_wait(20)

def visualizando():
    sleep(3)
                
ler_arquivo('cnpjs.csv')
# -----> Fim da leitura do arquivo de origem <-----

# -----> Ínicio da inicialização do driver <-----
options = Options()
driver = uc.Chrome(options=options)
# -----> Fim da inicialização do driver <-----

# -----> Ínicio da coleta de dados <-----
driver.get('https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp')

def elemento(tabela, coluna):
    dado = driver.find_elements(by=By.TAG_NAME, value='table')[tabela]\
        .find_elements(by=By.TAG_NAME, value='td')[coluna - 1]\
        .find_element(by=By.TAG_NAME, value='b')
    return dado

def elemento_unico(tabela):
    dado_unico = driver.find_elements(by=By.TAG_NAME, value='table')[tabela]\
        .find_element(by=By.TAG_NAME, value='b')
    return dado_unico

indice = 0
for cnpj in lista_origem:
    aguardando()
    sleep(10) #clicar manualmente em "sou humano"
    driver.find_element(by=By.ID, value='cnpj').send_keys(lista_origem[indice])
    visualizando()

    numero_inscricao = elemento(2, 1)
    linha.append(numero_inscricao.text)

    data_abertura = elemento(2, 3)
    linha.append(data_abertura.text)

    nome_empresarial = elemento_unico(3)
    linha.append(nome_empresarial.text)

    nome_fantasia = elemento(4, 1)
    linha.append(nome_fantasia.text)

    porte = elemento(4, 3)
    linha.append(porte.text)

    atividade = elemento_unico(5)
    linha.append(atividade.text)

    atividade_secundaria = elemento_unico(6)
    linha.append(atividade_secundaria.text)

    natureza_juridica = elemento_unico(7)
    linha.append(natureza_juridica.text)

    logradouro = elemento(8, 1)
    linha.append(logradouro.text)

    numero = elemento(8, 3)
    linha.append(numero.text)

    complemento = elemento(8, 5)
    linha.append(complemento.text)

    cep = elemento(9, 1)
    linha.append(cep.text)

    bairro = elemento(9, 3)
    linha.append(bairro.text)

    municipio = elemento(9, 5)
    linha.append(municipio.text)

    uf = elemento(9, 7)
    linha.append(uf.text)

    email = elemento(10, 1)
    linha.append(email.text)

    telefone = elemento(10, 3)
    linha.append(telefone.text)

    ente_federativo_responsavel = elemento_unico(11)
    linha.append(ente_federativo_responsavel.text)

    situacao_cadastral = elemento(12, 1)
    linha.append(situacao_cadastral.text)

    data_situacao_cadastral = elemento(12, 3)
    linha.append(data_situacao_cadastral.text)

    motivo_situacao_casdatral = elemento_unico(13)
    linha.append(motivo_situacao_casdatral.text)

    situacao_especial = elemento(14, 1)
    linha.append(situacao_especial.text)

    data_situacao_especial = elemento(14, 3)
    linha.append(data_situacao_especial.text)

    driver.back()

    planilha_destino.append(linha)
    linha = []
    indice = indice + 1
# -----> Fim da coleta de dados <-----

# -----> Encerrando o driver <-----
driver.quit()

df = pd.DataFrame(planilha_destino)
df.columns = ['NÚMERO DE INSCRIÇÃO',\
    'DATA DE ABERTURA',\
    'NOME EMPRESARIAL',\
    'TÍTULO DO ESTABELECIMENTO (NOME DE FANTASIA)',\
    'PORTE',\
    'CÓDIGO E DESCRIÇÃO DA ATIVIDADE ECONÔMICA PRINCIPAL',\
    'CÓDIGO E DESCRIÇÃO DAS ATIVIDADES ECONÔMICAS SECUNDÁRIAS',\
    'CÓDIGO E DESCRIÇÃO DA NATUREZA JURÍDICA',\
    'LOGRADOURO',\
    'NÚMERO',\
    'COMPLEMENTO',\
    'CEP',\
    'BAIRRO/DISTRITO',\
    'MUNICÍPIO',\
    'UF',\
    'ENDEREÇO ELETRÔNICO',\
    'TELEFONE',\
    'ENTE FEDERATIVO RESPONSÁVEL (EFR)',\
    'SITUAÇÃO CADASTRAL',\
    'DATA DA SITUAÇÃO CADASTRAL',\
    'MOTIVO DE SITUAÇÃO CADASTRAL',\
    'SITUAÇÃO ESPECIAL',\
    'DATA DA SITUAÇÃO ESPECIAL'
    ]

df.to_csv('destino.csv', sep=';', index=False, encoding='utf-8-sig')

print('OK')
