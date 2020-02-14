import fdb
import xml.etree.ElementTree as ET

#parswonie do obiektu

tree = ET.parse ('Results_20200204094938.xml')
xmlVar = tree.getroot()
lista = []
for i in lista:
	print(i)
lista.append(xmlVar.attrib["XMLCreationDateTime"])
#print(XMLCreationDateTime)
lista.append(xmlVar[0].attrib["MethodName"])
#print(MethodName)
lista.append(xmlVar[0][0][0][1].text)
#print(OpisProby)
lista.append(xmlVar[0][0][1][1].text)
#print(NrGatunku)
lista.append(xmlVar[0][0][2][1].text)
#print(Wymiar)
lista.append(round (float (xmlVar[0][2][0][1][0][2][0].text),4))
#print(xmlVarC)
lista.append(round (float (xmlVar[0][2][0][1][1][2][0].text),4))
#print(xmlVarSi)
lista.append(round (float (xmlVar[0][2][0][1][2][2][0].text),4))
#print(xmlVarMn)
lista.append(round (float (xmlVar[0][2][0][1][3][2][0].text),4))
#print(xmlVarP)
lista.append(round (float (xmlVar[0][2][0][1][4][2][0].text),4))
#print(xmlVarS)
lista.append(round (float (xmlVar[0][2][0][1][5][2][0].text),4))
#print(xmlVarCr)
lista.append(round (float (xmlVar[0][2][0][1][6][2][0].text),4))
#print(xmlVarMo)
lista.append(round (float (xmlVar[0][2][0][1][7][2][0].text),4))
#print(xmlVarNi)
lista.append(round (float (xmlVar[0][2][0][1][8][2][0].text),4))
#print(xmlVarAl)
lista.append(round (float (xmlVar[0][2][0][1][9][2][0].text),4))
#print(xmlVarCo)
lista.append(round (float (xmlVar[0][2][0][1][10][2][0].text),4))
#print(xmlVarCu)
lista.append(round (float (xmlVar[0][2][0][1][11][2][0].text),4))
#print(xmlVarNb)
lista.append(round (float (xmlVar[0][2][0][1][12][2][0].text),4))
#print(xmlVarTi)
lista.append(round (float (xmlVar[0][2][0][1][13][2][0].text),4))
#print(xmlVarV)
lista.append(round (float (xmlVar[0][2][0][1][14][2][0].text),4))
#print(xmlVarW)
lista.append(round (float (xmlVar[0][2][0][1][15][2][0].text),4))
#print(xmlVarPb)
lista.append(round (float (xmlVar[0][2][0][1][16][2][0].text),4))
#print(xmlVarSn)
lista.append(round (float (xmlVar[0][2][0][1][17][2][0].text),4))
#print(xmlVarAs)
lista.append(round (float (xmlVar[0][2][0][1][18][2][0].text),4))
#print(xmlVarZr)
lista.append(round (float (xmlVar[0][2][0][1][19][2][0].text),5))
#print(xmlVarBi)
lista.append(round (float (xmlVar[0][2][0][1][20][2][0].text),4))
#print(xmlVarCa)
lista.append(round (float (xmlVar[0][2][0][1][21][2][0].text),4))
#print(xmlVarCe)
lista.append(round (float (xmlVar[0][2][0][1][22][2][0].text),4))
#print(xmlVarSb)
lista.append(round (float (xmlVar[0][2][0][1][23][2][0].text),4))
#print(xmlVarSe)
lista.append(round (float (xmlVar[0][2][0][1][24][2][0].text),4))
#print(xmlVarTe)
lista.append(round (float (xmlVar[0][2][0][1][25][2][0].text),4))
#print(xmlVarTa)
lista.append(round (float (xmlVar[0][2][0][1][26][2][0].text),4))
#print(xmlVarB)
lista.append(round (float (xmlVar[0][2][0][1][27][2][0].text),4))
#print(xmlVarZn)
lista.append(round (float (xmlVar[0][2][0][1][28][2][0].text),4))
#print(xmlVarLa)
lista.append(round (float (xmlVar[0][2][0][1][29][2][0].text),4))
#print(xmlVarN)
lista.append(round (float (xmlVar[0][2][0][1][30][2][0].text),4))
#print(xmlVarFe)
lista.append(round (float (xmlVar[0][2][0][1][31][1][0].text),4))

class Firebird_database():
    def __init__(self,hos,por,db,usr,passw):
        self.conn = fdb.connect(host=hos, port=por, database=db, user=usr, password=passw)
        self.cur = self.conn.cursor()
    def CREATETABLE(self):
        # Execute the CREATETABLE statement:
        self.cur.execute("CREATE TABLE XXX_LAB (XMLCreationDateTime VARCHAR(50),MethodName VARCHAR(50),OpisProby SMALLINT,NrGatunku VARCHAR(50),Wymiar SMALLINT,C DECIMAL(5,5),SI DECIMAL(5,5),MN DECIMAL(5,5),P DECIMAL(5,5),S DECIMAL(5,5),CR DECIMAL(5,5),MO DECIMAL(5,5),NI DECIMAL(5,5),AL DECIMAL(5,5),CO DECIMAL(5,5),CU DECIMAL(5,5),NB DECIMAL(5,5),TI DECIMAL(5,5),V DECIMAL(5,5),W DECIMAL(5,5),PB DECIMAL(5,5),SN DECIMAL(5,5),ASS DECIMAL(5,5),ZR DECIMAL(5,5),BI DECIMAL(5,5),CA DECIMAL(5,5),CE DECIMAL(5,5),SB DECIMAL(5,5), SE DECIMAL(5,5),TE DECIMAL(5,5),TA DECIMAL(5,5),B DECIMAL(5,5),ZN DECIMAL(5,5),LA DECIMAL(5,4),N DECIMAL(5,5),FE DECIMAL(5,5),NBVTI DECIMAL(5,5))")
        self.conn.commit()
    def INSERT(self):
        # Execute the SELECT statement:
        self.cur.execute ("INSERT INTO XXX_LAB (XMLCreationDateTime,MethodName,OpisProby,NrGatunku,Wymiar,C,SI,MN,P,S,CR,MO,NI,AL,CO,CU,NB,TI,V,W,PB,SN,ASS,ZR,BI,CA,CE,SB,SE,TE,TA,B,ZN,LA,N,FE,NBVTI) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(lista))
        self.conn.commit()
    def SELECT(self):
        # Execute the SELECT statement:
        self.cur.execute("SELECT * from XXX_LAB")
        print (self.cur.fetchall())
        self.conn.commit()
    def DELETEALL(self):
        #Usuwanie wszytkich rekordow z tabeli:
        self.cur.execute("DELETE FROM XXX_LAB")
        self.conn.commit()
    def DROPTABLE(self):
        #Usuwanie wszytkich calej tabeli:
        self.cur.execute("DROP TABLE XXX_LAB")
        self.conn.commit()
F = Firebird_database('192.168.202.99', 3050, '/var/local/baza/RBB_SA.gdb', 'SYSDBA', 'masterkey')
#F.INSERT()
F.SELECT()
#F.CREATETABLE()
#F.DELETEALL()
#F.DROPTABLE()
##print(len(lista))
