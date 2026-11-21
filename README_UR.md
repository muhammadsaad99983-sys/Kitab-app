# APK / AAB بنانے کا طریقہ
1. Node.js اور Android Studio انسٹال کریں۔
2. اس فولڈر میں ٹرمینل کھول کر چلائیں:
   npm install
   npx cap add android
   npx cap sync
   npx cap open android
3. Android Studio میں: Build ← Build APK(s) (فون میں انسٹال کے لیے)
4. پلے اسٹور کے لیے: Build ← Generate Signed Bundle (AAB) — اپنی keystore بنائیں اور محفوظ رکھیں۔

# پلے اسٹور کی شرائط
- appId (com.yourname.kutubkhana) اپنا منفرد نام رکھیں (capacitor.config.json)
- AAB فائل اپلوڈ کریں (APK نہیں)، targetSdk تازہ ترین ضرورت کے مطابق رکھیں
- آئیکن 512×512، فیچر گرافک 1024×500، کم از کم 2 اسکرین شاٹ
- پرائیویسی پالیسی کا لنک (www/privacy.html کو کسی ویب سائٹ پر رکھیں)
- Data safety فارم بھریں، مواد کی ریٹنگ سوالنامہ مکمل کریں
- صرف وہ کتب رکھیں جن کا کاپی رائٹ آپ کے پاس ہو یا اجازت ہو، ورنہ ایپ ہٹائی جا سکتی ہے
- کتب بدلنے کے لیے www/books.json میں متن لکھیں
- آف لائن فونٹ کے لیے Noto Nastaliq Urdu فونٹ فائل www میں رکھ کر style.css میں @font-face لگائیں
