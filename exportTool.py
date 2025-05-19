# PYSIDE6-SOVELLUS POSTGRESQL-NÄKYMIEN TIETOJEN TALLENTAMISEEN
# CSV- JA TSV-TIEDOSTOIHIN
# ============================================================


# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets # Qt-vimpaimet

# Itsetehdyt moduulit
from customModules import dbOperations

# mainWindow_ui:n tilalle käännetyn pääikkunan tiedoston nimi
# ilman .py-tiedostopäätettä
from exportTool_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Tietokantayhteys
        self.serverName = ''
        self.portNumber = ''
        self.databaseName = ''
        self.userName = ''
        self.password = ''

        # Tietokantaobjekti
        self.dbobjectType = ''
        self.dbObjectName = ''

        # Tietokantaobjektin sarakkeiden nimet
        self.columnNamesList = []
        self.resultSet = []

        # Virheilmoitustiedot
        self.errorWindowTitle = ""
        self.errorText = ""
        self.errorDetails = ""

        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # Kun painetaan Testaa-painiketta, näytetään tilarivillä tulos ja
        # päivtetään objektityypin valinnat. Jos virhe, näyteään msgbox
        # Painike asettaa tietokantaparametrit ja yhteysmerkkijonon

        self.ui.testConnectionPushButton.clicked.connect(self.connectDb)
        
        # TODO: Kun poistutaan objektityypin valinnasta, haetaan tyypin objketilista
        # ja päivitetään objektin nimi -valinnat ISSUE 13
        self.ui.objectTypeComboBox.currentIndexChanged.connect(self.getObjectNames)


        # TODO: Kun poistutaan / valinta on muuttunut objektilistasta 
        # näyteään päivitetään esikatselu ja näytetään Tallenna-painike
        self.ui.getDataPushButton.clicked.connect(self.updatePreview)

        # TODO: Tallennuspainikkeen painaminen käynnistää tallennusdialogin ISSUE 9

        
   
   
    # OHJELMOIDUT SLOTIT
    # ------------------
    def connectDb(self):

        # Päivitetään tietokantaan liittyvät ominaisuudet syötettyjen tietojen perusteella
        self.serverName = self.ui.serverLineEdit.text()
        self.portNumber = self.ui.portLineEdit.text()
        self.databaseName = self.ui.databaseLineEdit.text()
        self.userName = self.ui.userNameLineEdit.text()
        self.password = self.ui.passwordLineEdit.text()

        # Muodostetaan asetussanakirja
        settingsDictionary = {'server': self.serverName,
                      'port': self.portNumber,
                      'database': self.databaseName,
                      'userName': self.userName,
                      'password': self.password}
        
        # Luodaan tietokantayhteysolio
        try:
            dbConnection = dbOperations.DbConnection(settingsDictionary)
            table = 'information_schema.tables'
            columns = ['table_type']
            filterText = f"table_schema NOT IN ('information_schema', 'pg_catalog')"

            objectTypes = dbConnection.filterDistinctColumsFromTable(table,columns,filterText)
            self.ui.statusbar.showMessage('Yhteyden muodostus tietokantaan onnistui')
            print(objectTypes)

            # Tehdään monikkolistasta merkkijonolista
            self.ui.objectTypeComboBox.clear() # Tyhjentää vanhat vaihtoehdot
            cleanedObjectTypeList = ['Valitse']
            for value in objectTypes:
                objectType = value[0] # Ottaa monikon ensimmäisen arvon
                cleanedObjectTypeList.append(objectType)
            
            # Lisätään lista yhdistelmäruutuun
            self.ui.objectTypeComboBox.addItems(cleanedObjectTypeList)
        
        except Exception as e:
            self.errorWindowTitle = 'Yhteys tietokantaan ei onnistunut'
            self.errorText = 'Yhteyden muodostuksessa tapahtui virhe'
            self.errorDetails = str(e)
            self.openWarning()
        

    # TODO: Tee slotti, joka hakee information_schema-nimiavaruudesta listan
    # tietokantaobjekteista, jotka eivät ole information_schemassa tai pg_catalogissa
    #  a) tee  kysely ensin SQL-kielellä PGAdminissa ja kokeile
    #  b) käytä filterColumnsFromTable metodia tietojen hakemiseen ja tallenna ne
    #     pääohjelmaan muuttujaan self.tablesAndViews
    def getObjectNames(self):

        # Muodostetaan asetussanakirja
        settingsDictionary = {'server': self.serverName,
                      'port': self.portNumber,
                      'database': self.databaseName,
                      'userName': self.userName,
                      'password': self.password}
        
         # Luodaan tietokantayhteysolio
        try:
            dbConnection = dbOperations.DbConnection(settingsDictionary)
            table = 'information_schema.tables'
            columns = ['table_schema','table_name']
            tableType = self.ui.objectTypeComboBox.currentText()

            filterText  = f"table_type = '{tableType}' AND table_schema NOT IN ('information_schema', 'pg_catalog')"

            objectNames = dbConnection.filterDistinctColumsFromTable(table,columns,filterText)
            self.ui.statusbar.showMessage('Haettiin tietokantaobjektien nimet')
            
            print(objectNames)

            # Tehdään monikkolistasta merkkijonolista
            self.ui.objectNameComboBox.clear() # Tyhjentää vanhat vaihtoehdot
            cleanedObjectNameList = ['Valitse']
            for value in objectNames:
                objectSchema = value[0] # Ottaa monikon ensimmäisen arvon -> skeema
                objectName = value[1] # Ottaa monikon toisen arvon -> objektin nimi
                objectFullName = f'{objectSchema}.{objectName}' # Objektin polku: skeema.nimi
                cleanedObjectNameList.append(objectFullName)
            
            # Lisätään lista yhdistelmäruutuun
            self.ui.objectNameComboBox.addItems(cleanedObjectNameList)
        
        
        except Exception as e:
            self.errorWindowTitle = 'Yhteys tietokantaobjektien haku ei onnistunut'
            self.errorText = 'Objektien nimien haku ei onnistunut'
            self.errorDetails = str(e)
            self.openWarning()
            

    def updatePreview(self):

        # Muodostetaan asetussanakirja
        settingsDictionary = {'server': self.serverName,
                      'port': self.portNumber,
                      'database': self.databaseName,
                      'userName': self.userName,
                      'password': self.password}
        
        # Luetaan valitun tietokantaobjektin skeema ja nimi
        currentObjectSelection = self.ui.objectNameComboBox.currentText()
        
        # Luodaan tietokantayhteysolio
        try:
            dbConnection = dbOperations.DbConnection(settingsDictionary)
            self.resultSet = dbConnection.readAllColumnsFromTable(currentObjectSelection)
            print(self.resultSet)
    
        except:
            pass
        

        # Tyhjennetään vanhat tiedot käyttöliittymästä ennen uusien lukemista tietokannasta
        self.ui.previewTableWidget.clear()

        # Määritellään taulukkoelementin otsikot
        try:
            # Tulosjoukon rivimäärä
            numberOfRows = len(self.resultSet)
            self.ui.previewTableWidget.setRowCount(numberOfRows)

            # Tulosjoukon sarakemäärä
            columnCount = len(self.resultSet[0])
            self.ui.previewTableWidget.setColumnCount(columnCount)
            dbConnection = dbOperations.DbConnection(settingsDictionary)
            headerRow = dbConnection.getColumnNames(currentObjectSelection)
            self.ui.previewTableWidget.setHorizontalHeaderLabels(headerRow)
        
        except Exception as e:
            raise e
        
        # Asetetaan taulukon solujen arvot
        for row in range(numberOfRows): # Luetaan listaa riveittäin
            for column in range(len(self.resultSet[row])): # Luetaan monikkoa sarakkeittain
                
                # Muutetaan merkkijonoksi ja QTableWidgetItem-olioksi
                data = QtWidgets.QTableWidgetItem(str(self.resultSet[row][column])) 
                self.ui.previewTableWidget.setItem(row, column, data)
                self.ui.previewTableWidget.setHorizontalHeaderLabels(headerRow)

    # Virheilmoitusdialogi
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(self.errorWindowTitle)
        msgBox.setText(self.errorText)
        msgBox.setDetailedText(self.errorDetails)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

if __name__ == "__main__":

    # Luodaan sovellus
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä
    app.exec()


    