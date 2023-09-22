import tabula
import requests
import pandas as pd
from io import BytesIO
from rich import pretty, traceback; pretty.install(); traceback.install(show_locals=False)

url = "https://dados.cvm.gov.br/dados/FI/DOC/EVENTUAL/DADOS/eventual_fi_2023.csv"
df = pd.read_csv(url, encoding="latin-1", sep=";")
documentos = (
    df[[
        True if str(nome)[-3:] == "pdf" and tipo == "REGUL FDO" 
        else False 
        for nome, tipo in zip(df.NM_ARQ.values, df.TP_DOC.values)
    ]]
    .LINK_ARQ.values
)

tables = tabula.read_pdf(
    documentos[0],
    silent=True,
    pages="all", 
    multiple_tables=True,
    options="--format JSON --outfile RESULT.json"
)

tables = tabula.read_pdf(
    documentos[0],
    silent=True,
    pages="all", 
    multiple_tables=True,
    options="--format CSV --outfile RESULT.csv"
)




