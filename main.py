import yaml
from etl.extractor import extract
from etl.transformer import transformar, carregar_regras
from etl.loader import load
from utils.logger import get_logger

log = get_logger()

def run():
    log.info("Carregando configuração...")
    config = yaml.safe_load(open("config/settings.yaml"))

    regras = carregar_regras(config["rules"])
    log.info("Extraindo dados...")
    df = extract("data/sample/exemplo.csv")

    log.info("Transformando dados...")
    df = transformar(df, regras)

    log.info("Carregando dados finais...")
    load(df, "data/output/produtos_classificados.csv")
    log.info("ETL finalizado com sucesso!")

if __name__ == "__main__":
    run()
