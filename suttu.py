from customModules import dbOperations

# Lisätään henkilötiedot asiakastauluun

settingsDictionary = {'server': 'localhost',
                      'port': '5432',
                      'database': 'testaus',
                      'userName': 'postgres',
                      'password': 'Q2werty7'}

#dbConnection = dbOperations.DbConnection(settingsDictionary)
#dbConnection.addToTable('asiakas', {'etunimi': 'Erkki', 'sukunimi': 'Esimerkki'})

dbConnection2 = dbOperations.DbConnection(settingsDictionary)
asiakasLista = dbConnection2.readAllColumnsFromTable('asiakas')
print(asiakasLista)
print('\n')
print('Seuraavaksi suodatus')

dbConnection3 = dbOperations.DbConnection(settingsDictionary)
filterText = f"etunimi = 'Jakke'"
results = dbConnection3.filterColumsFromTable('asiakas', ['etunimi', 'sukunimi'], filterText)
print(results)

dbConnection4 = dbOperations.DbConnection(settingsDictionary)

criteriaValue = f"'Essi'"
newValue = f"'Eräjärvi'"
dbConnection4.modifyTableData('asiakas', 'sukunimi', newValue, 'etunimi', criteriaValue)

