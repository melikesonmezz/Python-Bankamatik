#bankamatik uygulaması
#banka hesaptaki para yetmiyorsa kullanıcı ekhesaptan para istiyorsa oradan para verecek

SadikHesap={
 'ad':'Ayşe Yasemin',
 'hesapNo':'123456789',
 'bakiye':3000,
 'ekHesap':2000
}

AliHesap={
 'ad':'Ali Namık',
 'hesapNo':'123456789',
 'bakiye':2000,
 'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f'Merhaba {hesap["ad"]}')
    
    if (hesap['bakiye']>=miktar):
        print('paranızı alabilirsiniz.')
    else:
        toplam=hesap['bakiye']+hesap['ekHesap']

        if (toplam>=miktar):
            ekHesapKullanimi=input('ek hesap kullanılsın mı? e/h')
            if (ekHesapKullanimi=='e'):
                print('paranızı alabilirsiniz.')
            else:
                print(f'{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bakiye bulunmaktadır.')
            
        else:
            print('üzgününüz bakiye yetersiz.')
paraCek(SadikHesap,4000)



