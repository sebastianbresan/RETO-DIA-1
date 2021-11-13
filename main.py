import pandas as pd

excelReto = pd.read_csv('RETO-DIA-1.txt', delimiter='\t')

emails = excelReto.email.unique()

print(emails)
