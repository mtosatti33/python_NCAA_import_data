import pandas as pd
import utils as utils
import consts as consts

datacol = []

# chamada que importa dados do Site stats.ncaa.com
def import_data(_dict, _dict_period, field):
    for x, y in _dict.items():
        for year, rk in _dict_period.items():
            year = int(year) - 1
            try:
                print(f"Importando dados {x} do ano {year}/{year + 1}") 
                df = pd.read_html(consts.SITE.format(int(year), rk, y))

                utils.mkdir(f'{year}')
                utils.mkdir(f'{year}\\{field}')

                utils.mkdir(f'{consts.MAIN_PATH}\\{year}')
                utils.mkdir(f'{consts.MAIN_PATH}\\{year}\\{field}')

                df[0].to_csv(consts.LOCAL_PATH.format(year, field ,x))
                utils.copy(consts.LOCAL_PATH.format(year, field, x), consts.PATH.format(year, field, x))

            except Exception:
                print("Erro ao importar")
                with open('log.txt', 'a') as log:
                    log.write(f'Stat não importado: {x} do ano {year}/{year + 1}.\n')

    
    utils.transform(field)

