import tabula
import zipfile
import os


file = 'http://www.ans.gov.br/images/stories/Plano_de_saude_e_Operadoras/tiss/Padrao_tiss/tiss3/Padrao_TISS_Componente_Organizacional_202006.pdf'

tables = tabula.read_pdf(file, pages = '81-87', multiple_tables = True)

print(tables[0])
print('***************')
print(tables[1])
print(tables[2])
print(tables[3])
print(tables[4])
print(tables[5])
print(tables[6])
print('***************')
print(tables[7])

incNameFile = 0
for table in tables:
    table.to_csv('Teste_Intuitive_Care_Jeniffer_Morier' + str(incNameFile) + '.csv', encoding='utf-8')
    incNameFile += 1

fantasy_zip = zipfile.ZipFile('C:\\Users\\jenif\\PycharmProjects\\TransfDeDados\\venv\\Teste_Intuitive_Care_Jeniffer_Morier.zip', 'w')

for folder, subfolders, files in os.walk('C:\\Users\\jenif\\PycharmProjects\\TransfDeDados\\venv'):
    for file in files:
        if file.endswith('.csv'):
            fantasy_zip.write(os.path.join(folder, file),
                    os.path.relpath(os.path.join(folder, file), 'C:\\Users\\jenif\\PycharmProjects\\TransfDeDados\\venv'),
                    compress_type=zipfile.ZIP_DEFLATED)

fantasy_zip.close()

print("arquivo zip criado com sucesso!")