from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

def iniciar_navegador():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')

    #Remover rastros básicos de automação
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=options)

    stealth(driver,
        languages=['pt=BR', 'pt'],
        vendor='Google Inc.',
        platform='Win32',
        webgl_vendor='Intel Inc.',
        renderer='Intel Iris OpenGL Engine',
        fix_hairline=True,
    )

    return driver

def capturar_texto(driver, tabela, coluna=None):
    try:
        # Pega a tabela pelo índice
        tab = driver.find_elements(By.TAG_NAME, 'table')[tabela]

        if coluna is not None:
            # Se passou coluna, busca dentro da TD específica
            elemento = tab\
                .find_elements(By.TAG_NAME, 'td')[coluna -1]\
                .find_element(By.TAG_NAME, 'b')
        else:
            # Se não, busca o <b> direto na tabela
            elemento = tab.find_element(By.TAG_NAME, 'b')

        return elemento.text.strip()
    except Exception:
        return '' # Retorna string vazia se não encontrar
    
def extrair_dados_cnpj(driver, cnpj): 
    try:
        # Navegar até o site da receita
        print(f'🏢 Acessando o site da receita para o CPNJ: {cnpj}.')
        driver.get('https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp')

        # Localiza o campo e digita o CNPJ
        campo_cnpj = driver.find_element(By.ID, 'cnpj')
        campo_cnpj.send_keys(cnpj)
        print(f'✅ CNPJ {cnpj} inserido no campo')

        # Pausa para o ação manual - Captcha
        print('🚦 ATENÇÃO REQUERIDA: Resolva o Captcha e clique em "Consultar".')
        input('👉 Quando a ficha aparecer na tela, volte aqui e aperte ENTER...')
        print('🚀 Ficha detectada. Inciando extração dos dados...')
       
        # Mapeamento dos dados a serem extraídos
        dados = {
            'NÚMERO DE INSCRIÇÃO': capturar_texto(driver, 2, 1),
            'DATA DE ABERTURA': capturar_texto(driver, 2, 3),
            'NOME EMPRESARIAL': capturar_texto(driver, 3),
            'NOME FANTASIA': capturar_texto(driver, 4, 1),
            'PORTE:': capturar_texto(driver, 4, 3),
            'ATIVIDADE ECONÔMICA PRINCIPAL': capturar_texto(driver, 5),
            'ATIVIDADES ECONÔMICAS SECUNDÁRIAS': capturar_texto(driver, 6),
            'NATUREZA JURÍDICA': capturar_texto(driver, 7),
            'LOGRADOURO': capturar_texto(driver, 8, 1),
            'NÚMERO': capturar_texto(driver, 8, 3),
            'COMPLEMENTO': capturar_texto(driver, 8, 5),
            'CEP': capturar_texto(driver, 9, 1),
            'BAIRRO/DISTRITO': capturar_texto(driver, 9, 3),
            'MUNICÍPIO': capturar_texto(driver, 9, 5),
            'UF': capturar_texto(driver, 9, 7),
            'E-MAIL': capturar_texto(driver, 10, 1),
            'TELEFONE': capturar_texto(driver, 10, 3),
            'ENTE FEDERATIVO RESPONSÁVEL': capturar_texto(driver, 11),
            'SITUAÇÃO CADASTRAL': capturar_texto(driver, 12, 1),
            'DATA SITUAÇÃO CADASTRAL': capturar_texto(driver, 12, 3),
            'MOTIVO SITUAÇÃO CADASTRAL': capturar_texto(driver, 13),
            'SITUAÇÃO ESPECIAL': capturar_texto(driver, 14, 1),
            'DATA SITUAÇÃO ESPECIAL': capturar_texto(driver, 14, 3)
        }
        return dados
    
    except Exception as e:
        print(f'Erro ao extrair dados para o CNPJ {cnpj}: {e}')
        return None
