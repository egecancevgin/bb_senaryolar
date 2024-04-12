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
touch araba_salınım.py
```





