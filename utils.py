import shutil
import os
import pandas as pd
import consts
import dicts

# chamada que classifica o DataFrame e salva
def sort(arq, field):
    if os.path.exists(arq):
        df = pd.read_csv(arq)
        df.sort_values(
            [field],
            axis=0,
            ascending=[True],
            inplace=True,
            ignore_index=True
        )
        print(f"Classificando o arquivo {arq}")
        df.to_csv(arq)

# chamada para transformar os dados
def transform(field):
    if field ==  "Team":
        for x in dicts.data.keys():
            for year in dicts.year_rk.keys():
                year = int(year) - 1
                sort(consts.LOCAL_PATH.format(year, field, x), field)

# chamada que classifica o DataFrame e salva
def rmtree(_dict):
    for year in _dict.keys():
        year = int(year) - 1
        if os.path.exists(f'{year}'):
            shutil.rmtree(f'{year}')
            print(f'Diretorio {year} removido')
        
        if os.path.exists(f'{consts.MAIN_PATH}\\{year}'):
            shutil.rmtree(f'{consts.MAIN_PATH}\\{year}')
            print(f'Diretorio {consts.MAIN_PATH}\\{year} removido')

# chamada para criar um diretório vazio
def mkdir(dir):
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
            print(f'Diretorio {dir} criado')
        except:
            print('Erro ao Criar o Diretório')

# chamada para copiar um arquivo até o destino
def copy(from_path, to_path):
    if os.path.exists(from_path):
        shutil.copyfile(from_path, to_path)

# chamada para copiar um arquivo até o destino
def move(from_path, to_path):
    if os.path.exists(from_path):
        shutil.move(from_path, to_path)


# TODO: implementar uma def chamada move usando a biblioteca glob.
def move_all():
    pass