import json

mhsBaru = int((input('Masukkan jumlah mahasiswa baru: ')))
for i in range(mhsBaru):
    nama = input('Masukkan nama Anda: ')
    list_mhswa = list()
    dict_mhs = dict()
    dict_biodata = dict()
    jml_hobi = int(input('Masukkan jumlah hobi: '))
    list_hobi = list()
    for j in range(jml_hobi):
        hobi = input('Masukkan hobi ke-{}: '.format(str(j + 1)))
        list_hobi.append(hobi)
    dict_biodata['Hobi'] = list_hobi
    prestasi = input('Masukkan prestasi Anda: ')
    dict_biodata['Prestasi'] = prestasi
    dict_mhs['BioData'] = dict_biodata
    list_mhswa.append(dict_mhs)
    with open('mahasiswa.json', 'r') as datafile:
        data = json.load(datafile)
        data[nama] = list_mhswa
    with open('mahasiswa.json', 'w') as datafile:
        json.dump(data, datafile)
    print('=== Data berhasil ditambahkan ===\n')