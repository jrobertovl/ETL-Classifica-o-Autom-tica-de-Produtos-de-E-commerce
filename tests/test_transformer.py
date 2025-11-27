from etl.transformer import transformar, carregar_regras
import pandas as pd

def test_transformer():
    df = pd.DataFrame([{'nome':'Fone','descricao':'Bluetooth'}])
    regras = {'Eletronicos':['fone']}
    out = transformar(df, regras)
    assert out.iloc[0]['categoria'] == 'Eletronicos'
