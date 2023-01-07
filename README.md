*Site ve Hesaba Özel Parola Üreteci

Bu uygulama, sitenin URL'sini ve kullanıcı adınızı alıp seçeceğiniz bir algoritmayla şifrelemesi ve bunu parola olarak size sunmasını sağlar. Böylelikle her siteye özel parolanız olur.

*Nasıl Kullanılır

Uygulamayı çalıştırın.
Site URL'sini girin.
Kullanıcı adınızı girin.
Şifreleme algoritmasını seçin (SHA-1, SHA-224, SHA-256, SHA-384, SHA-512 veya MD5).
"Parola Oluştur" düğmesine tıklayın.
Oluşturulan parolayı kullanarak giriş yapın veya hesap oluşturun.

*Önemli Notlar
Uygulamada kullanılan şifreleme algoritmaları, günümüzde güvenlik açısından yeterli olmayabilir. Bu nedenle, parolalarınızı sık sık değiştirmeyi ve güçlü parolalar kullanmayı öneririz.
Uygulama, verilerinizi hiçbir şekilde saklamaz veya paylaşmaz. Sadece size özel olarak oluşturulan parolayı gösterir.

*Gereksinimler
Python 3.x
hashlib kütüphanesi

*Kurulum
- Bu repoyu klonlayın veya indirin.
- Terminalde, uygulamanın bulunduğu dizine gidin.
- python `password_generator.py` komutunu çalıştırın.

*Örnek Kullanım

- $ python password_generator.py
- Site URL'sini girin: example.com
- Kullanıcı adınızı girin: user123
- Şifreleme algoritmasını seçin (sha1 / sha224 / sha256 / sha384 / sha512 veya md5): sha256
- Parolanız: f0e4c2f76c58916ec258f246851bea091d14d4247a2fc3e18694461b1816e13b

*Lisans

Bu proje MIT Lisansı altında lisanslıdır. Detaylar için LICENSE dosyasına bakın.

