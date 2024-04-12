## Makine Öğrenimi Temelleri

Makine Öğrenimi, bilgisayarların verilere bakarak öğrenmelerini ve öğrenmedikleri veriler üzerinde tahminler yapmalarını sağlayan teknolojidir.
Örneğin bir fotoğraftaki köpeği tanımak ve sonraki fotoğraflarda köpek gördüğünde bunları tespit etmek için, bir metindeki duyguyu tahmin etmek için, bir banka işlemindeki sahtekarlığı tespit etmek için kullanılabilir.

![Obje-Tespiti](obje_tespiti.png)

Makineler öğrenirken giriş olarak aldığı verilere bağımsız değişkenler denir, ve bunların içerisindeki desenleri ortaya çıkarırken çeşitli algoritmalar kullanılır. 

Bu algoritmalar ve matematiksel tekniklerin bütününe model denir, ve modeli tahmin yapabilmesi için eğitmemiz gerekir. Verilerin bir kısmıyla model eğitimi yaptıktan sonra bir kısmıyla da test yapmamız gerekir.

Bu, sanki modeli cevaplarını bildiğimiz bir sınava sokmak gibidir. Örneğin elimizde 10 tane çözümlü sınav sorusu varsa biz 6 tane soruyu modele cevapları ile beraber öğretiriz. Kalan 4 soruyu da cevaplarını vermeden çözmesini bekleyebiliriz. Bu iki soru grubuna eğitim ve test seti adı verilir.

![Egitim-Test](egitim_tst.png)


Bağımsız değişkenler genellikle `X` ile temsil edilir. Modelin tahmin etmeye çalıştığı değişkenlere de bağımlı değişken adı verilir ve bunlar `y` ile temsil edilir.

`Kayıp`, makinenin tahmin ettiği değer ile gerçek değer arasındaki farktır ve bunu minimize etmek isteriz. Örneğin aşağıdaki görselde sarı yuvarlaklar gerçek veri noktalarını, mavi çizgi bizim tahminimizi ve kırmızı oklar da kaybı temsil eder.
![Kayıp](kayıp.png)


Model, eğitim esnasında bağımsız değişken olan sütünlara ağırlık verir ve bu ağırlıklara göre desenleri öğrenir.
Örneğin bir dondurma satışı verisinde mevsim ve mevcut sıcaklık sütunu çoğu zaman diğer sütunlardan daha önemli olacaktır.

Etiket, cevabını bildiğimiz bağımlı değişken veridir. Örneğin bir mail verisinde bulunan bazı maillerin spam olduğunu biliyoruz. Mailin spam olduğunu belirten sütuna etiket denir ve makine bu etiketi eğitim için kullanır.

Ancak her veride önceden etiketlenmiş veri olmayabilir, bu durumda da çalışan bazı algoritmalar vardır. Örneğin kümeleme algoritması etiketli veriye ihtiyaç duymasa da benzer verileri gruplandırıp bu şekilde tahminler gerçekleştirebilir.

Etiketli veri kullanılarak yapılan makine öğrenimine `denetimli makine öğrenimi` denir. Denetimli makine öğrenimin en temel algoritması `Lineer Regresyon`'dur.

Lineer Regresyon algoritması, elimizdeki verilere en uygun doğruyu oluşturmaya çalışır. Böylece belirli özelliklere sahip verilerin gidişatını önceden tahmin edebiliriz. Mesela aşağıdaki grafikte kırmızı noktalar gerçek veri noktalarıyken mavi çizgi bizim tahmin ettiğimiz matematiksel lineer regresyon doğrusudur.
![Lineer-Reg](linreg.png)

Lineer Regresyon denklemi şu şekildedir: `Y = β₀ + W₁X₁ + W₂X₂ + ... + WₙXₙ` burada W'lar ilgili sütunların ağırlıklarıyken, X'ler veri noktaları yani satırlardır, β₀ da denklemin x eksenine uzaklığıdır.

Makine Öğrenimi üç ana aşamada incelenebilir: Temsil, Değerlendirme ve Optimizasyon. 
  - Temsil aşamasında veri işlemesi ile matematiksel modelleme gerçekleştirilir ve modelin eğitildiği aşama burasıdır.
  - Değerlendirme aşamasında modelin tahmin ve eğitim başarısı belirli metriklerle incelenir.
  - Optimizasyon evresinde ise modelin eğitimini geliştirmek için uzun süreli iyileştirmeler yapılır.

Veri işlemesi, verimizin uygun formata getirilmesi için önemlidir. Örneğin bazı sütunlarda eksik veya yanlış değerler olabilir, bazı sütunlar numerik bazı sütunlar metin şeklinde olabilir, bazı sütunlarda 0-10000 arası değerler varken bazı sütunlarda 0-10 arası değerler olabilir.

Öğrenme denkleminde bahsettiğimiz gibi her sütunun veri noktaları ağırlık değeriyle çarpılarak öğrenme yapılıyordu. Ancak bu sütunlar arasında veri noktaları aralığı uyuşmazlığı olursa makine yüksek değerli veri noktasının öğrenme esnasında daha çok önem arz edeceği sonucuna varabilir. Örneğin bir sütunda evin alanı 80 metrekare, bir sütunda evin yaşı 3 yaş ise denklemde evin alan değeri çok daha etkileyici olacaktır.

Bu sorunu çözmek için sütunları ölçeklendirebiliriz. Örneğin Min-Max Ölçeklendirmede her bir değer, veri setindeki en küçük değere bölünerek ve ardından bu bölme sonucuna göre veri setindeki en büyük değere bölünerek yeniden ölçeklendirilir. 

Bugünkü senaryoda yapacaklarımıza artık hazırız, makine öğrenimi projelerimizi PEP 8 standartlarına uygun bir şekilde yazmalıyız ki dağıtım aşamasında otomasyon testleri rahat yapılabilsin ve daha anlaşılır bir düzende yazmış olalım.

PEP 8 standartlarına göre işlemlerimizi metotları ayırmalıyız ve bu metotların görevlerini ilk satırına kısaca özetlemeliyiz. Ayrıca çok fazla karakterlere sahip satırları da bölmeliyiz ki okumak daha kolay olsun.

Bugünkü senaryomuzda bir araba veri setini kullanarak makineye arabaların karbondioksit salınımını tahmin ettireceğiz. Öncelikle gerekli modülleri terminalden indirmeliyiz ve yükleme aracımızı güncellemeliyiz. 

Aşağıdakileri komutları tek tek ve sırayla terminale girelim ve yükleme esnasında bizden girdi isterse Y veya e harflerini girelim:
``` sh
sudo apt update
sudo apt install python3-pip
pip install pandas
pip install scikit-learn
pip install matplotlib
```

Bunları hallettikten sonra proje dosyamızı oluşturalım. Terminale aşağıdaki komutu girelim:
``` sh
touch araba_salinim.py
```

Ekranımızın sol yukarısındaki 'WORKSPACE' kısmının altında dosyamız oluşturulmuş olacaktır. Bu dosyaya tıklayalım ve dosyanın en tepesine aşağıdaki kütüphane direktiflerini yazalım:
``` py
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
```

Gerekli kütüphane çağrılarını yaptıktan sonra artık veri düzenleme fonksiyonumuzu oluşturabiliriz. Kütüphane direktiflerimizin iki satır aşağısına veri_duzenle() fonksiyonunu yazalım. 

Bu fonksiyon içerisinde önce verimizin bulunduğu yeri kullanarak bu '.csv' uzantılı dosyayı Pandas DataFrame formatında okuyalım. Sonrasında NaN değerleri atalım ve indisleri resetleyelim. 

Ölçeklendirme yapmayı unutmayalım ki eğitim düzgün gerçekleşsin. Motor hacmi, silindir sayısı, şehir içi ve şehir dışı benzin kullanımları sütunlarını ölçeklendirmeye dahil edelim. Sonrasında Scikit-learn kütüphanesinden kullanacağımız MinMaxScaler'ı scaler değişkenine eşitleyelim ve DataFrame'in bu dört sütununu 'fit_transform' metodu ile ölçeklendirelim.

Son olarak veriye bir göz atmak için DataFrame.head() metodunu kullanalım. Metodumuz aşağıdaki gibi gözükmelidir, bu metot kütüphane direktiflerinin iki-üç satır aşağısında olmalıdır.

``` python
def veri_duzenle():
  """ Veriyi temizleyip ölçeklendirir ve ekranda görüntüler, sonrasında da döner."""
  url = "https://raw.githubusercontent.com/egecancevgin/bb_senaryolar/main/C02_emmissions.csv"
  df = pd.read_csv(url)
  df.dropna(inplace=True)
  df.reset_index(drop=True, inplace=True)
  features_to_scale = [
      'Engine Size(L)', 'Cylinders', 'Fuel Consumption City (L/100 km)', 
      'Fuel Consumption Hwy (L/100 km)'
  ]
  scaler = MinMaxScaler(feature_range=(1, 100))
  df[features_to_scale] = scaler.fit_transform(df[features_to_scale])
  print(df.head())
  return df
```

Bu metot tamamlandıktan sonra bir modeli_egit() metodu oluşturacağız, bu aşamada önce bağımsız değişkenleri X değişkenine, bağımlı değişkeni y değişkenine eşitleyelim. Sonrasında da scikit-learn kütüphanesinin train_test_split() metodunu kullanarak X eğitim verisi, X test verisi, y eğitim verisi ve y test verisine %80-%20 olmak üzere bölelim.

X eğitim ve y eğitim verileri eğitim aşamasında kullanılacak, X test ve y test verileri de test aşamasında kullanılacaktır. Bu örnekte %80 eğitim - %20 test olmak üzere veriyi böleceğiz.

Sonrasında scikit-learn kütüphanesinin `LinearRegression` metodunu kullanarak modelimizi oluşturacağız. Modeli eğitmek için 'X_train' ve y_train' eğitim verilerini girdi olarak verip '.fit()' metodu ile eğitimi gerçekleştirelim. Sonrasında da fonksiyonumuz hem modeli hem de bu böldüğümüz verileri dönsün.

Sonuç olarak metodumuz bu şekilde gözükecektir ve önceki metottan 2-3 satır aşağıda olması gerekmektedir:
``` python
def modeli_egit(df):
  """ Model eğitimini gerçekleştirir ve parçalanmış veriyle beraber eğitilmiş modeli döner."""
  X = df[
      [
          'Engine Size(L)', 'Cylinders', 'Fuel Consumption City (L/100 km)',
          'Fuel Consumption Hwy (L/100 km)'
      ]
  ]
  y = df['CO2 Emissions(g/km)']

  # Bashettiğimiz eğitim-test ayrımını yapalım
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42
  )

  # Model eğitimini gerçekleştirelim
  model = LinearRegression()
  model.fit(X_train, y_train)
  return model, X_train, X_test, y_train, y_test, X
```

