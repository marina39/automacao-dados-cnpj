# Funções para ler e limpar os arquivos

import csv
import re

def extrair_lista_cnpjs(caminho_arquivo):
    lista_limpa = []

    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            # Transforma cada linha em um dicionário
            leitor = csv.DictReader(arquivo, delimiter=';')
            
            # Limpa espaços do cabeçalho
            if leitor.fieldnames:
                leitor.fieldnames = [nome.strip() for nome in leitor.fieldnames]
       
            for linha in leitor:
                valores = list(linha.values())

                if valores:
                    cnpj_bruto = valores[0]

                    if cnpj_bruto:
                        cnpj_so_numeros = re.sub(r'\D', '', cnpj_bruto)
                        lista_limpa.append(cnpj_so_numeros)
                    
        return lista_limpa
    
    except FileNotFoundError:
        print(f'Erro: Arquivo não encontrado em {caminho_arquivo}')
        return []
    except Exception as e:
        print('Erro ao ler o arquivo:', e)
        return []
