# PAZARDAN - E-Ticaret Platformu

PAZARDAN, çiftçileri doğrudan tüketicilerle buluşturmayı amaçlayan bir e-ticaret platformudur. Bu proje, aracıları ortadan kaldırarak taze ürünlerin uygun fiyatlarla sunulmasını sağlar.

## Özellikler
- Çiftçi ve tüketici hesap yönetimi
- Ürün listeleme ve filtreleme
- Online ödeme entegrasyonu
- Geri bildirim ve değerlendirme sistemi
- Sipariş takibi

## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/kullaniciadi/pazardan.git
cd pazardan
```

### 2. Sanal Ortam Oluşturun ve Bağımlılıkları Yükleyin
```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Çevre Değişkenlerini Ayarlayın
`.env` dosyanızı oluşturup aşağıdaki değişkenleri ekleyin:
```
SECRET_KEY=django-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/pazardan
STRIPE_SECRET_KEY=your-stripe-secret-key
```

### 4. Veritabanını Ayarlayın
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Uygulamayı Başlatın
```bash
python manage.py runserver
```

Uygulama, `http://127.0.0.1:8000/` adresinde çalışacaktır.

## Kullanılan Teknolojiler
- Python, Django
- PostgreSQL
- Stripe API (Ödeme İşlemleri)
- HTML, CSS, JavaScript

## Katkıda Bulunma
Katkıda bulunmak için lütfen aşağıdaki adımları izleyin:
1. Bu repoyu forklayın.
2. Kendi branşınızı oluşturun (`git checkout -b yeni-ozellik`).
3. Değişiklikleri yapıp commitleyin (`git commit -m 'Yeni özellik eklendi'`).
4. Push yapın (`git push origin yeni-ozellik`).
5. Bir pull request açın.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.

## 👤 İletişim

Büşra Albayrak
- LinkedIn: [Büşra Albayrak](https://www.linkedin.com/in/büşra-albayrak-59b62a252/)
- Instagram: [@busra.cyber](https://www.instagra
 
