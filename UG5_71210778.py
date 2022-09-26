class Mobil :
    _merk = ""
    _tipe = ""
    _kapasitasBBM = None
    _jenisBahanBakar = None

    def __init__(self, merk,tipe) :
        self._merk = merk
        self._tipe = tipe
#Setter
    def set_kapasitasBBM(self, kapasitasBBM) :
        self._kapasitasBBM = kapasitasBBM
    
    def set_jenisBahanBakar(self, jenisBahanBakar) :
        self._jenisBahanBakar = jenisBahanBakar

    def set_merk (self,merk) :
        self._merk = merk
    
    def set_tipe (self,tipe) :
        self._tipe = tipe
#Getter
    def get_merk (self) :
        return self._merk
    def get_tipe(self) :
        return self._tipe
    def get_kapasitasBBM(self):
        return self._kapasitasBBM
    def get_jenisBahanBakar (self):
        return self._jenisBahanBakar
#printInfo
    def printInfo(self) :
        print ('==========INFO==========')
        print('Merk   : ',self._merk)
        print('Tipe :',self._tipe)
        print('Bahan Bakar :',self._jenisBahanBakar)
        print('Kapasitas BBM :',self._kapasitasBBM)
#isiBBM
    def isiBBM(self,tiapLiter):
        if self._kapasitasBBM  == None  or self._jenisBahanBakar == None:
            print ("EROR! Kapasitas BBM atau Jenis Bahan Bakar belum diinputkan")
        else :   
            print("Mengisi :",self.get_kapasitasBBM())
            print("Total Harga :",self.get_kapasitasBBM()* tiapLiter)

#main
Mobil1 = Mobil("Toyota","Pajero")
Mobil2 = Mobil("Nissan","GrandLivina")
#TestCase
Mobil1.printInfo()
Mobil1.set_jenisBahanBakar("Bensin")
Mobil1.set_kapasitasBBM(20)
Mobil1.printInfo()
Mobil1.isiBBM(14500)
#mobil 2
Mobil2.printInfo()
Mobil1.set_jenisBahanBakar("Pertamax")
Mobil2.set_kapasitasBBM(9)
Mobil2.printInfo()
Mobil2.isiBBM(20000)