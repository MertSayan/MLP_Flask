📌 Salary Prediction Flask App
Bu proje, 2025 Türkiye yazılım sektörü maaşlarını tahmin etmek için geliştirilmiş bir
Çoklu Doğrusal Regresyon (Multiple Linear Regression) modelinin
Flask tabanlı web arayüzü ile sunulmuş halidir.

Proje, Makine Öğrenmesi dersinin dönem ödevi kapsamında hazırlanmıştır.

🖼 Proje Önizlemesi

<img width="1891" height="944" alt="image" src="https://github.com/user-attachments/assets/9b08b203-a8b9-4999-a83f-ec0b35f43fe5" />


🎯 Projenin Amacı

Amaç, yazılım geliştiricilerin maaşlarını aşağıdaki özelliklere göre tahmin etmektir:

Deneyim yılı

Yaptığı Proje sayısı

Bildiği Programlama dili sayısı

Uzaktan çalışma durumu

Sertifika sayısı

Şehir seviyesi (1–2–3 seviye; İstanbul-Ankara-İzmir vb. farkları yansıtır) (Gelişmiş şehir vs farkı)

Mezuniyet durumu (Lisans / Diğer)

Bu öznitelikler sektör gerçeklerine göre belirlenmiş olup, maaş üzerinde istatistiksel olarak anlamlı etkiler göstermektedir.



🧪 Veri Ön İşleme (Data Preprocessing)

Notebook dosyasında aşağıdaki işlem adımları uygulanmıştır:

✔ Eksik değer analizi

Kayıp değerler tespit edildi

Ortalama/medyan ile doldurma işlemleri uygulandı

<img width="850" height="211" alt="image" src="https://github.com/user-attachments/assets/73185a78-14a2-4f22-85a3-5c91a082ef61" />


✔ Duplicate (tekrarlı) kayıt temizleme

Yinelenen satırlar silindi

<img width="756" height="417" alt="image" src="https://github.com/user-attachments/assets/1a5a7975-7a4c-4b10-bcac-e5ee5f1000cc" />


✔ String temizliği

Bozuk veya gereksiz ifadeler ayıklandı

<img width="929" height="546" alt="image" src="https://github.com/user-attachments/assets/d2925aa5-42a4-49d3-9b8d-5cdff92c5007" />

Normalizasyon işlemleri yapıldı

✔ Aykırı değer (outlier) analizi

<img width="1082" height="678" alt="image" src="https://github.com/user-attachments/assets/7e515f02-2f7f-4e6d-a22b-68b3ec0ce3c7" />


Boxplot/kural bazlı inceleme

Uygun eşik üzerinde kırpma işlemleri

✔ Kategorik verilerin kodlanması

Şehir seviyesi ve eğitim durumu için One-Hot Encoding uygulandı

seviye (Büyükşehir) baseline olarak bırakıldı

<img width="1748" height="522" alt="image" src="https://github.com/user-attachments/assets/ea0fcd5a-b9b3-4afc-94d3-f21a51b96b43" />


✔ Özellik seçimi

Backward Elimination yöntemi kullanılarak anlamlı feature’lar bırakıldı


📊 Model: Multiple Linear Regression

Eğitim sürecinde:

R² skoru: 0.79

MAE: 8022 TL

MSE: 108M

Modelin sektörel maaş tahminlerini gerçekçi şekilde yansıttığı görülmüştür.


🌐 Flask Web Arayüzü

Kullanıcı:

Deneyim yılı

Proje sayısı

Bildiği proglamlama dili sayısı

Sertifika sayısı

Şehir seviyesi (İstanbul-Ankara gibi şehirler mi, Balıkesir vb. gibi şehirler mi yoksa Erzurum vb. gibi şehirler mi seçeneği)

Mezuniyet durumu (Lisans mezunu / Lisans Mezunu Değil)

gibi bilgileri forma girer → “Tahmin Et” butonuna basar → modelden gelen maaş tahmini ekranda gösterilir.

Arayüz tamamen Türkçedir.

<img width="1896" height="947" alt="image" src="https://github.com/user-attachments/assets/d5a2acb2-ef54-4bcc-b496-6417d7f72735" />

▶️ Uygulamayı Çalıştırmak İçin

Sol üstten view kısmından terminal e basarak terminal açılır ve 

Terminale:

python app.py yazılmalıdır ardından tarayıcıdan http://127.0.0.1:5000 adresine giderek uygulamayı kullanabilirsiniz.


👨‍🎓 Hazırlayan

Ad Soyad: Muhammed Mert Sayan
Ders: Makine Öğrenmesi
Numarası: 2212721028

🧾 Lisans
Bu proje akademik amaçla hazırlanmıştır.
