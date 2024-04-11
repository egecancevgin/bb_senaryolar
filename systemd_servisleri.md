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


