📌 Salary Prediction Flask App
Bu proje, 2025 Türkiye yazılım sektörü maaşlarını tahmin etmek için geliştirilmiş bir
Çoklu Doğrusal Regresyon (Multiple Linear Regression) modelinin
Flask tabanlı web arayüzü ile sunulmuş halidir.

Proje, Makine Öğrenmesi dersinin dönem ödevi kapsamında hazırlanmıştır.

📂 Proje İçeriği
SalaryPredictionApp/
├── static/
│   └── yazilimgorsel.jpg        # Arka plan görseli
├── templates/
│   └── index.html              # Web arayüzü (kullanıcı formu + sonuç ekranı)
├── app.py                      # Flask web uygulaması
├── salary_model.pkl            # Eğitilmiş ML modeli (pickle formatında)
└── README.md                   # Proje açıklaması

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

✔ Duplicate (tekrarlı) kayıt temizleme

Yinelenen satırlar silindi

✔ String temizliği

Bozuk veya gereksiz ifadeler ayıklandı

Normalizasyon işlemleri yapıldı

✔ Aykırı değer (outlier) analizi

Boxplot/kural bazlı inceleme

Uygun eşik üzerinde kırpma işlemleri

✔ Kategorik verilerin kodlanması

Şehir seviyesi ve eğitim durumu için One-Hot Encoding uygulandı

seviye (Büyükşehir) baseline olarak bırakıldı

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
