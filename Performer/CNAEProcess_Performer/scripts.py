# Autora: Jana Machado
# Data: 12/05/23
# Arquivo: scripts.py - Script em python que será chamado dentro da automação CnaeIbgeProcesses para ler a planilha,
#transformar o texto das descrições para minúsculo, remover acentos das colunas de texto e tudo que for diferente de número das
#colunas de códigos exceto da coluna 'Código Seção'.

# Importações das libs pandas e re: biblioteca re para substituir tudo que não for dígito;
# biblioteca pandas para leitura, manipulação e salva a tabela com os dados CNAE;
# biblioteca unidecode para converter caracteres Unicode.
import pandas as pd
import re
import unidecode



# Carregamento da Planilha 'cnae_atividades.xlsx'
df = pd.read_excel("cnae_atividades.xlsx")

# Tratamento dos textos das colunas de Descrições: 'Seção', 'Dvisão', 'Grupo', 'Classe' e 'Subclasse' para minúsculo.
df["Seção"] = df["Seção"].apply(lambda x: unidecode.unidecode(x.lower()))
df["Divisão"] = df["Divisão"].apply(lambda x: unidecode.unidecode(x.lower()))
df["Grupo"] = df["Grupo"].apply(lambda x: unidecode.unidecode(x.lower()))
df["Classe"] = df["Classe"].apply(lambda x: unidecode.unidecode(x.lower()))
df["Subclasse"] = df["Subclasse"].apply(lambda x: unidecode.unidecode(x.lower()))

# Tratamento dos textos das colunas de Descrições: 'Seção', 'Dvisão', 'Grupo', 'Classe' e 'Subclasse' para retirar acentos.
df = df.applymap(lambda x: unidecode.unidecode(x) if type(x) == str else x)

# Tratamento das colunas de Códigos para remover tudo o que for diferente de números.
codigo_cols = ["Código Divisão", "Código Grupo", "Código Classe", "Código Subclasse"]
for col in codigo_cols:
    # Substituindo números de 0-9 por caractere vazio: "".
    df[col] = df[col].apply(lambda x: re.sub(r"[^0-9]","",str(x)))

# Salvar planilha 'cnae_atividades.xlsx' tratada.
df.to_excel("cnae_atividades_fixed.xlsx", index=False)

