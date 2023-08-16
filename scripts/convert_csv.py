import sys
import pandas as pd

def convert_csv():
  xlsx_file_path = "upload/Sistema Gerencial.xlsx"
  abas = ["aditivos", "relatorios", "repasses", "termo-parceria-contrato-gestao"]
  for aba in abas:
    read_file = pd.read_excel (xlsx_file_path, aba)
    read_file.to_csv (f'dataset/data/{aba}.csv', index = None, header=True, sep = ';', decimal = ',', encoding = 'utf-8-sig', na_rep = "")

if __name__ == '__main__':
  convert_csv()

