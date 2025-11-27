# 🤖 ETL – Classificação Automática de Produtos de E-commerce
O projeto foi criado para demonstrar boas práticas de engenharia de dados, incluindo:
Estrutura profissional de diretórios
Separação clara entre Extract, Transform e Load
Configurações externas
Testes automatizados
Arquivos de regras editáveis (sem necessidade de alterar código)
Logs
Pacote pronto para evolução

## 🚀 Objetivo do Projeto
## ✅ Criar um sistema ETL capaz de:
- Extrair informações de produtos (CSV, banco de dados, APIs etc.)
- Transformar esses dados aplicando regras inteligentes de classificação
- Carregar os dados processados em outro sistema ou arquivo final
- O pipeline utiliza regras configuráveis em JSON, facilitando manutenções e ampliando as possibilidades de uso.
  
## 🧠 Exemplo de Uso
- Este ETL percorre um catálogo de produtos e determina automaticamente sua categoria, com base em palavras-chave encontradas no nome e descrição do item.

Entrada:

|  Id  | nome                                                        | -------------|
| :----: | --------------------------------------------------------- | -------------|
| 1 | Fone de ouvido |  Fone bluetooth preto                      |

|  id    | nome                                     |                                            |
| :----: | ------------------------------------------------------------------------------------- |
| 1      | Fone de ouvido	                          |  Fone bluetooth preto                      |
| 2	     | Camiseta preta	                          |  Roupa masculina básica                    |

Saída:
|  id    | nome                             | descricao	              |  categoria               |
| :----: | ------------------------------------------------------------------------------------- |
| 1	     | Fone de ouvido	                  | Fone bluetooth preto	  |  Eletronicos             |
| 2	     | Camiseta preta	                  | Roupa masculina básica	|  Roupas                  |

- Atendimento automatizado de FAQs de RH
- Integração com documentos da organização
- Execução de fluxos Power Automate (Ex: Solicitação de férias)
- Implantação via Teams e Web Chat

## 📁 Estrutura do Projeto

```
etl-classificacao-produtos/
│
├── data/
│   ├── input/                  # Onde ficam dados brutos
│   ├── output/                 # Resultados gerados pelo ETL
│   └── sample/                 # Exemplos e pequenos datasets
│
├── etl/
│   ├── extractor.py            # Módulo de extração
│   ├── transformer.py          # Módulo de transformação/classificação
│   ├── loader.py               # Módulo de carregamento
│   └── rules/
│       └── categorias.json     # Regras de classificação (editável)
│
├── config/
│   └── settings.yaml           # Configurações gerais do pipeline
│
├── utils/
│   └── logger.py               # Logger padronizado
│
├── tests/
│   └── test_transformer.py     # Testes com pytest
│
├── main.py                     # Script principal do ETL
├── requirements.txt            # Dependências Python
└── README.md                   # Documentação
```

## ⚙️ Instalação
1. Clonar o repositório

      git clone https://github.com/jrobertovl/ETL-Classifica-o-Autom-tica-de-Produtos-de-E-commerce.git

3. cd etl-classificacao-produtos

4. Instalar dependências

      pip install -r requirements.txt

## ▶️ Como Executar o ETL
  Execute o script principal:

  python main.py

  Os dados processados serão salvos em:

  data/output/produtos_classificados.csv

## 🛠️ Personalizando Regras de Classificação

O arquivo etl/rules/categorias.json contém a lógica de classificação:
  
    {
    "Eletronicos": ["fone", "notebook", "carregador"],
    "Roupas": ["camiseta", "calça", "bermuda", "vestido"],
    "Casa & Cozinha": ["panela", "prato", "assadeira", "copos"]
    }

Para criar novas categorias, basta adicionar:
  
  "Esportes": ["bola", "tênis", "rede", "halter"]

## 🧪 Rodando os Testes
Este projeto usa pytest.

Execute:
pytest -v

## 📌 Boas Práticas Aplicadas
    ✔ Arquitetura limpa e separada por responsabilidade
    ✔ Regras externas e configuráveis
    ✔ Logging padronizado
    ✔ Estrutura completa para GitHub
    ✔ Testes automatizados
    ✔ Código fácil de expandir (pode virar microserviço, Lambda, Airflow etc.)

## 💡 Possíveis Extensões Futuras
    Dashboard com métricas de classificação (Streamlit)
    Deploy em AWS Lambda
    Uso de banco de dados SQLite/PostgreSQL
    Integração com Airflow ou Prefect
    Refinamento com Machine Learning (Naive Bayes, SVM, embeddings etc.)
    API REST para classificação em tempo real

## 🧑‍💻 Autor
<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="https://avatars.githubusercontent.com/u/79292597?s=96&v=4"
    />
    <p>&nbsp&nbsp&nbspJosé Roberto Vasconcellos Lopes<br>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/jrobertovl">GitHub</a>&nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/jrobertovl">LinkedIn</a>&nbsp;|&nbsp;
    <a href="https://www.instagram.com/jrobertovl/">Instagram</a>&nbsp;|&nbsp;
    <a href="https://api.whatsapp.com/send?phone=5591982003052">WhatsApp</a>
    </p>
</p>
<br/><br/>
<p>

---

⌨️ com 💜 por [José Roberto Vasconcellos Lopes](https://github.com/jrobertovl)
