📌 Salary Prediction Flask App
Bu proje, 2025 Türkiye yazılım sektörü maaşlarını tahmin etmek için geliştirilmiş bir
Çoklu Doğrusal Regresyon (Multiple Linear Regression) modelinin
Flask tabanlı web arayüzü ile sunulmuş halidir.

Proje, Makine Öğrenmesi dersinin dönem ödevi kapsamında hazırlanmıştır.

📂 Proje İçeriği
Bu repository aşağıdaki dosya ve klasörleri içerir:
├── app.py                 → Flask web uygulaması
├── salary_model.pkl       → Eğitilmiş ML modeli (pickle formatında)
└── templates/
       └── index.html      → Web arayüzü (kullanıcı formu + sonuç ekranı)


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

Programlama dilleri

Sertifikalar

Şehir seviyesi

Mezuniyet durumu

gibi bilgileri forma girer → “Tahmin Et” butonuna basar → modelden gelen maaş tahmini ekranda gösterilir.

Arayüz tamamen Türkçedir.


▶️ Uygulamayı Çalıştırmak İçin

Terminale:

python app.py yazılmalıdır ardından tarayıcıdan http://127.0.0.1:5000 adresine giderek uygulamayı kullanabilirsiniz.


👨‍🎓 Hazırlayan

Ad Soyad: Muhammed Mert Sayan
Ders: Makine Öğrenmesi

🧾 Lisans
Bu proje akademik amaçla hazırlanmıştır.
