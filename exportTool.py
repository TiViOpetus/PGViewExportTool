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

        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # TODO: Kun painetaan Testaa-painiketta, näytetään tilarivillä tulos ja
        # päivtetään objektityypin valinnat. Jos virhe, näyteään msgbox
        # Painike asettaa tietokantaparametrit ja yhteysmerkkijonon

        self.ui.testConnectionPushButton.clicked.connect(self.connectDb)
        
        # TODO: Kun poistutaan objektityypin valinnasta, haetaan tyypin objketilista
        # ja päivitetään objektin nimi -valinnat
        self.ui.objectTypeComboBox.currentIndexChanged.connect(self.getObjectNames)


        # TODO: Kun poistutaan / valinta on muuttunut objektilistasta 
        # näyteään Hae-painike

        # TODO: Kun hae-painiketta painetaan, päivitetään esikatselu-taulukko
        # ja näytetään tallenna-painike

        
   
   
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
            self.ui.objectNameComboBox.clear()
            cleanedObjectTypeList = ['Valitse']
            for value in objectTypes:
                objectType = value[0]
                cleanedObjectTypeList.append(objectType)
            
            self.ui.objectTypeComboBox.addItems(cleanedObjectTypeList)
        except Exception as e:
            # TODO: muokkaa virheilmoitus paremmaksi
            self.openWarning()
        

    # TODO: Tee slotti, joka hakee information_schema-nimiavaruudesta listan
    # tietokantaobjekteista, jotka eivät ole information_schemassa tai pg_catalogissa
    #  a) tee  kysely ensin SQL-kielellä PGAdminissa ja kokeile
    #  b) käytä filterColumnsFromTable metodia tietojen hakemiseen ja tallenna ne
    #     pääohjelmaan muuttujaan self.tablesAndViews
    def getObjectNames(self):
        filterText  = f"table_schema NOT IN ('information_schema', 'pg_catalog')"
    # Muutetaan tulostettuLabel:n sisältö: teksti ja väri
    

    # TODO: korjaa tämä niin, että tekstit tulee argumentteina Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Hirveetä!')
        msgBox.setText('Jotain kamalaa tapahtui')
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


    