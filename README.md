<p align="center"><img width=12.5% src="https://github.com/ibrahimenesduran/phoenix-wp-bulk-sender/blob/main/images/logo.png"></p>

<h3 align="center">Phoenix | Whatsapp Toplu Mesaj</h3>

<p align="center">
  <a>
    <img src="https://img.shields.io/badge/python-v3.6+-blue.svg">
  </a>  
  <a>
    <img src="https://img.shields.io/badge/node-v16.0+-yellow.svg">
  </a>
  <a>
    <img src="https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg">
  </a>
  <a href="https://github.com/ibrahimenesduran/phoenix-wp-bulk-sender/issues">
    <img src="https://img.shields.io/github/issues/ibrahimenesduran/phoenix-wp-bulk-sender.svg">
  </a>
  <a>
    <img src="https://img.shields.io/badge/contributions-welcome-orange.svg">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg">
  </a>
</p>

## Özellikler

* Otomatik numara kontrol sistemi
* İşlem sonucunda ulaşılmayan numaraları görme
* Ayarlanabilen mesajların arasındaki bekleme süresi
* Aynı numaraya mesaj atma engelleme sistemi

## Nasıl kullanacağız

1- Programın kurulumunu yapacağınız sistemde [Python](https://www.python.org/downloads/) ve [Node.js](https://nodejs.org/en/download/) yüklü olması gerekmektedir. Eğer yüklü değilse linklerden kurulumunu yapabilirsiniz.

2- Kurulumları sağladıktan sonra: 

```bash
# Repository'i indiriniz.
$ git clone https://github.com/ibrahimenesduran/phoenix-wp-bulk-sender.git

# İndirdiğiniz repository'i açınız
$ cd phoenix-wp-bulk-sender

# Source klasörüne giriniz
$ cd source

```
### Server kurulumu

1- Server kısmının kurulumunu sağlayın.

```bash
# Server dosyasına giriniz
$ cd server

# Gerekli kütüphaneleri yükleyiniz
$  npm install express
$  npm install moment
$  npm install --save @wppconnect-team/wppconnect

# server.js'yi başlatınız.
$ node server.js
```

2- Ekrana gelen QR kodu whatsapp'a okutunuz.

3- Artık arka tarafta çalışmaya hazır.

### Client kurulumu

1- Client kısmının kurulumunu sağlayın.

```bash
# Client dosyasına giriniz
$ cd client

# Gerekli kütüphaneleri yükleyiniz
$  pip install termcolor requests

# client.py'yi başlatınız.
$ python client.py
```

2- Gerekli adımları konsol ekranından takip ediniz.