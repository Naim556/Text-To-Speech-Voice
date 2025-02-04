# Text-To-Speech-Voice
This is a Python script that converts text to audio using the gtts library.

# English Explanation:

This Python script converts text into speech using the gTTS (Google Text-to-Speech) library. It includes a simple database system using sqlite3 to store and manage saved voice recordings.

The program offers several functionalities:

1. Creating Directories: It ensures that the necessary directories (Data and Voice) exist.

2. Database Setup: A SQLite database (voicelist.db) is created to store voice entries.

3. Add Voice: Users input text and language (English or Turkish), which is then converted into speech and saved as an MP3 file.

4. Remove Voice: Users can delete a stored voice by entering its name.

5. Display Voices: Lists all saved voice recordings with their names and associated text.

6. Play Voice: Allows users to play a saved MP3 file using system commands (os.system or subprocess).

7. Quit Program: Exits the application.

The user interacts with a simple menu and chooses actions via numeric inputs.

# Türkçe Açıklama:

Bu Python betiği, gTTS (Google Text-to-Speech) kütüphanesini kullanarak metni sese dönüştürür. sqlite3 ile bir veritabanı sistemi oluşturulmuştur ve kayıtlı sesleri yönetmek mümkündür.

Programın sunduğu temel özellikler şunlardır:

1. Dizinlerin Oluşturulması: Gerekli klasörlerin (Data ve Voice) mevcut olup olmadığını kontrol eder.

2. Veritabanı Kurulumu: SQLite veritabanı (voicelist.db) oluşturularak ses kayıtları saklanır.

3. Ses Ekleme: Kullanıcı, metin ve dil (İngilizce veya Türkçe) girerek bunu sese dönüştürüp MP3 olarak kaydedebilir.

4. Ses Silme: Kaydedilen bir sesi adını girerek silebilir.

5. Sesleri Listeleme: Kayıtlı tüm sesleri, adları ve metinleriyle birlikte gösterir.

6. Ses Çalma: Kaydedilen MP3 dosyalarını sistem komutları (os.system veya subprocess) ile çalar.

7. Programdan Çıkma: Uygulamayı kapatır.

Kullanıcı, bir menü üzerinden sayısal girişlerle seçim yaparak programı yönetir.

# توضیحات فارسی:

این اسکریپت پایتون از کتابخانه gTTS (Google Text-to-Speech) برای تبدیل متن به گفتار استفاده می‌کند. همچنین، یک سیستم پایگاه داده با sqlite3 دارد که امکان ذخیره و مدیریت صداهای ضبط‌شده را فراهم می‌کند.

قابلیت‌های برنامه شامل موارد زیر است:

1. ایجاد پوشه‌ها: بررسی می‌کند که پوشه‌های ضروری (Data و Voice) وجود داشته باشند.

2. راه‌اندازی پایگاه داده: یک پایگاه داده SQLite (voicelist.db) برای ذخیره صداها ایجاد می‌شود.

3. افزودن صدا: کاربر متن و زبان (انگلیسی یا ترکی) را وارد کرده، آن را به گفتار تبدیل کرده و به‌صورت فایل MP3 ذخیره می‌کند.

4. حذف صدا: کاربر می‌تواند با وارد کردن نام، یک فایل صوتی ذخیره‌شده را حذف کند.

5. نمایش صداها: تمام فایل‌های صوتی ذخیره‌شده را همراه با نام و متن آنها نمایش می‌دهد.

6. پخش صدا: فایل‌های MP3 ذخیره‌شده را با استفاده از دستورات سیستمی (os.system یا subprocess) پخش می‌کند.

7. خروج از برنامه: برنامه را می‌بندد.

کاربر از طریق یک منوی ساده و ورودی‌های عددی، عملیات موردنظر را انتخاب و اجرا می‌کند.
