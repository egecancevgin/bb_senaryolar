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
