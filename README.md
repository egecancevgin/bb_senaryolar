# bbklarim
Benim Bulut Bilişimciler Senaryolarım

1- Systemd Servisleri

``` sh
$ ls -lah /etc/systemd/system

$ systemctl list-units --type=service

$ cd /etc/systemd/system

$ sudo apt update
$ sudo apt install nginx

$ nano nginx.service

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


$ sudo systemctl stop apache2 

$ sudo systemctl daemon-reload

$ sudo systemctl start nginx

$ sudo systemctl restart prometheus

$ sudo systemctl status grafana

$ sudo systemctl enable nginx

$ sudo systemctl disable nginx


$ journalctl 

$ journalctl -b

$ journalctl -xe

```

2- Makine Öğrenimi Temelleri

Makine öğrenimi,

Model nedir nasıl öğrenir

Ağırlık nedir


Aşamaları:
 - Representation
 - Evaluation
 - Optimizasyon

Makine nasıl öğrenir,

Kayıp nedir,

Kayıp / Zaman Grafiği, Learning Rate, Gradient Descent ve SGD

Lineer Regresyon ve onun denklemi

PEP8 ve temiz kodlama

Veri temizleme ve elimizdeki verinin analizi,

Metrikler

Hiperparametre optimizasyonu
