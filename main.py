import imports
import utils
import dicts

utils.rmtree(dicts.year_rk)    # remove todos os diretórios e seus descendentes

imports.import_data(dicts.data, dicts.year_rk, "Team")
imports.import_data(dicts.data_player, dicts.year_rk, "Player")