import json

def carregar_regras(path):
    with open(path,'r') as f:
        return json.load(f)

def classificar(produto, regras):
    texto = f"{produto['nome']} {produto['descricao']}".lower()
    for categoria, palavras in regras.items():
        if any(p in texto for p in palavras):
            return categoria
    return "Outros"

def transformar(df, regras):
    df['categoria'] = df.apply(lambda row: classificar(row, regras), axis=1)
    return df
