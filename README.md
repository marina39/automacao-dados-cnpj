# 🏦 Automação de Consulta de CNPJ - Selenium Python

Este projeto foi desenvolvido para automatizar a extração de dados cadastrais de empresas diretamente do site da Receita Federal. O foco do projeto foi aplicar técnicas de **Web Scraping**, gestão de perfis de navegador e superação de barreiras de automação.

## 🚀 Desafios Técnicos e Maturidade

Durante o desenvolvimento, o sistema de segurança do site da Receita Federal (Captcha/Cookies) apresentou comportamentos de bloqueio para sessões automatizadas, mesmo com o uso de técnicas avançadas como `selenium-stealth` e gerenciamento de perfis reais. 

**Decisão de Projeto:** Optei por manter a lógica de automação original, documentando o ponto de interrupção como um limite técnico imposto pelo servidor alvo. Isso demonstra a compreensão de que, em automação de dados, nem sempre o desafio reside no código, mas na política de segurança do site consultado.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **Venv (Virtual Environment)**: Utilizado para garantir o isolamento das dependências e a reprodutibilidade do projeto.
* **Selenium WebDriver**: Para navegação e interação com elementos dinâmicos.
* **Selenium Stealth**: Para reduzir a detecção do bot pelo site.
* **Webdriver Manager**: Para gestão automática dos drivers do Chrome.
* **Pandas/CSV**: Para manipulação e armazenamento dos dados extraídos.

---

## 📋 Funcionalidades

- [x] Inicialização do navegador com configuração de disfarce de automação.
- [x] Leitura de lista de CNPJs via arquivo de entrada.
- [x] Preenchimento automático do campo de busca.
- [x] Interrupção inteligente (`input`) para resolução manual de Captcha, garantindo que o fluxo só continue após a validação humana.
- [x] Estrutura preparada para captura de dados em tabelas aninhadas.

---

## 📂 Estrutura do Projeto

```text
automacao-dados-cnpj/
├── venv/                     # Ambiente virtual (isolamento de pacotes)
├── data/
│   ├── lista_cnpjs.csv       # Arquivo de entrada
│   └── resultados.csv        # Arquivo gerado com os dados
├── src/
│   ├── buscador.py           # Core da automação (Selenium)
│   └── leitor.py             # Funções de leitura/escrita de arquivos
├── main.py                   # Orquestrador do fluxo
└── requirements.txt
└── README.md
