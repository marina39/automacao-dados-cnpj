from src.leitor import extrair_lista_cnpjs
from src.buscador import iniciar_navegador, extrair_dados_cnpj
import time
import pandas as pd

def executar():
    arquivo_entrada = 'dados/input.csv'
    arquivo_saida = 'dados/resultados_cnpjs.csv'

    lista_cnpjs = extrair_lista_cnpjs(arquivo_entrada)
    if not lista_cnpjs:
        print('❌ Nenhum CNPJ encontrado.')
        return
    
    driver = iniciar_navegador()
    resultados = []

    try:
        for cnpj in lista_cnpjs:
            print(f'🔍 Processando CNPJ: {cnpj}')
            dados = extrair_dados_cnpj(driver, cnpj)

            if dados:
                resultados.append(dados)
            
            time.sleep(2)

        # Salvando resultados em CVS usando Pandas
        if resultados:
            df = pd.DataFrame(resultados)
            df.to_csv(arquivo_saida, index=False, sep=';', encoding='utf-8-sig')
            print(f'✅ Automação concluída! Dados salvos em {arquivo_saida}')
        else:
            print('⚠️ Nenhuma informação foi capturada.')

    finally:
        driver.quit()
      
if __name__ == '__main__':
    executar()
