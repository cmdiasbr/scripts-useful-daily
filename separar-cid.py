import numpy as np
import os
import shutil
import csv
import sys
import pandas as pd
from pdb import set_trace as pause

csv_file = "final.csv"
# pasta onde ira localizar as imagens conforme o csv
existing_path_prefix = "/home/camila/JUNCAO-CSVS/teste" 
# cria nova pasta com subpastas que contem cid
new_path_prefix = "/home/camila/JUNCAO-CSVS/teste/imagens_cid"
if not os.path.exists(new_path_prefix):
    os.mkdir(new_path_prefix)


data = pd.read_csv(csv_file, encoding='utf-8')
data = data.to_numpy(dtype=np.str)
for line in data:
    solicitacao_id = line[0]
    termo_id	= line[1]
    anexos	= line[2] # endereço que esta no csv
    codigo= line[4] # codigo cid do csv
    path_to_save = os.path.join(new_path_prefix, codigo)
    if not os.path.exists(path_to_save):
        os.mkdir(path_to_save)
    anexos_img = anexos.replace('[','').replace(']','').replace(' ', '').replace("'", '').split(',')
    for anx in anexos_img:
        if anx.find('.jpg') or anx.find('.JPG') or anx.find('.png'):
            if os.path.exists(anx):
                shutil.copy(anx, path_to_save)
                # criar um txt com solicitacao_id para ligar ao dataset de texto posteriormente
            else:
                print('file not found:', anx)

        else:           
            print('not a .jpg file', anx)
