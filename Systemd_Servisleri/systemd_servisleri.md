## Systemd Servisleri

`systemd`, Linux dağıtımlarında kullanılan bir sistem yönetim çerçevesidir.
Systemd servisleri, sistem başlangıcında otomatik olarak başlatılırlar ve arka planda çalışırlar.
Örneğin, web sunucusu, veritabanı sunucusu veya özel uygulamalar systemd servisleri olarak tanımlanabilir.

Arka planda çalışmasını istediğimiz, bizim işlerimizi doğrudan etkilemeyen çalışanlar gibidir.
Bu servisleri kullanarak çoğu işimizi otomatize edebiliriz, ve bu da daha verimli işler yapmamızı sağlar.

`/etc/systemd/system` dizini altında bu oluşturacağımız servisler bulunur. Servis dosyaları '.service' uzantılı olurlar.
Bu dosyalar içerisinde üç genel bölüm vardır:
- `Unit`: Servisin adı, açıklaması, gereksinimleri ve kullanıcı kimliği gibi bilgiler bulunur.  
- `Service`: Servisin nasıl başlatılacağı, nasıl durdurulacağı, çalıştırılacak komut, bağımlılıklar ve ortam değişkenleri bu bölümdedir.
- `Install`: Servisin hangi hedeflerle başlatılacağını belirtir, örneğin çok kullanıcılı şekilde.

`systemctl` komutu, bu servislerin yönetimini sağlayan ana komuttur. Bu komuta çeşitli argümanlar ekleyerek servislerin durumu kontrol edilebilir, başlatılıp durdurulabilir, ve yenilenebilir.

Bazı flag'leri şunlardır:
- `start`, belirtilen servisi başlatmaya yarar.
- `stop`, belirtilen servisi durdurmaya yarar.
- `restart`, belirtilen servisi yeniden başlatır.
- `status`, belirtilen servislerin durumunu gösterir.
- `enable`, belirtilen servisin sistem başlangıcında otomatik başlatılmasını sağlar.
- `disable`, belirtilen servisin otomatik başlatılmasını engeller.
- `list-units`, tüm yüklenmiş birimleri listeler.
- `daemon-reload`, değişiklikleri yükler ve systemd daemon'u yeniden başlatır.

`journalctl` komutu, systemd'nin günlük sistemiyle etkileşim kurmayı sağlar. Sistem günlükleri görüntülenebilr, filtrelenebilir, sorgulanabilir ve izlenebilir.

Bazı flag'leri şunlardır:
- `-b`, son sistem başlangıcından itibaren günlük girdilerini görüntüler.
- `-e`, en son günlük girdileri görüntüler.
- `-x`, çıktıyı genişletir ve daha detaylı anlatır.
- `-u`, belirli bir servise ait günlük girdileri görüntüler.

Şimdi senaryomuza geçelim, oluşturacağımız servis bir Nginx sunucusu. Nginx, esnek bir web sunucusu ve bir ters proxy sunucusudur. Popüler olarak web sitelerinin barındırılması ve yük dengeleme amacıyla kullanılır. 

Öncelikle şu hedef dizininmize bir göz atalım ve ne var ne yok görelim:
``` bash
ls -lah /etc/systemd/system
```

Gördüğünüz üzere birçok servis ve konfigürasyon dosyası bulunmakta. Şimdi de sistemde aktif servisleri listelemek için `systemctl` komutunu bir deneyelim:
``` bash
systemctl list-units --type=service
```

Servisleri inceledikten sonra hedef dizinimize gidelim:
``` bash
cd /etc/systemd/system
```

Şimdi Nginx'i kurmak için apt aracımızı güncelleyelim ve hem Nginx, hem de metin editörü olan Nano yüklememizi gerçekleştirelim:
``` sh
sudo apt update
sudo apt install nginx
sudo apt install nano
```

İşlem tamamlandıktan sonra Nginx'in yüklenip yüklenmediğini versiyonunu sorarak kontrol edelim:
``` sh
nginx -v
```

Eğer yüklemelerde sorun yoksa ve çalıştığımız dizin `/etc/systemd/system` ise, sonunda `nginx.service` ismindeki servis dosyamızı oluşturmaya geçebiliriz:
``` sh
nano nginx.service
```

Bu komutu yazdıktan sonra çıkan ekrana öncelikle açıklamamızı, sistemin başlatılacağı yolu, ve kalan detayları yazıp kaydedip çıkalım: (Çoğu sistemde Ctrl X ve Y/E tuşlarına basarak)
``` sh
[Unit]
Description=Nginx HTTP Sunucusu
After=network.target

[Service]
Type=forking
ExecStart=/usr/sbin/nginx
ExecReload=/usr/sbin/nginx -s reload
ExecStop=/usr/sbin/nginx -s stop

[Install]
WantedBy=multi-user.target
```

Şimdi servisimizi systemctl komutu ile başlatalım, önce daemon'u yenileyelim:
``` sh
sudo systemctl daemon-reload
sudo systemctl start nginx
```

Şimdi de enable edelim, ki otomatik başlasın, sonra da artık statüsüne bakalım çalışıp çalışmadığı orada görünecektir:
``` sh
sudo systemctl enable nginx
sudo systemctl status nginx
```

Sırada bu günlükleri detaylı bir biçimde incelemek var.
`journalctl` komutunu kullanalım ve son dökümleri inceleyelim:
``` sh
journalctl -xe 
```

Bir sorun gözükmüyor ise servisimiz sağlıklı çalışıyor diyebiliriz. Bir sonraki senaryoda görüşmek üzere hoşçakalınn :)


