# Python-da bir o'zgaruvchan va ko'p o'lchovli funktsiyalar bo'yicha Monte-Karlo integratsiyasi

- Monte-Karlo integratsiyasi - bu funktsiyaning integratsiyasini raqamli baholash uchun asosiy Monte-Karlo usuli f( x ). Biz bu erda nazariyani Pythondagi misollar bilan birga muhokama qilamiz.
# Misol | Bir o'zgaruvchan
- Misol tariqasida, Python-da biz integratsiyani taxminiy hisoblash uchun quyidagilarni bajarishimiz mumkin 

![image](https://user-images.githubusercontent.com/99121169/194283707-33a0bd4e-f156-4562-8163-1255a0a60d82.png)

Biz quyidagi natijalarga erishamiz:

- Monte Karlo yechimi: 5.3323
- Analitik yechim: 5.3333

Bu erda Monte-Karlo yaqinlashuvi analitik yechimga juda yaqin. Vizual ravishda integratsiyaf( x ) =x2-2 dan 2 gacha quyida ko'k rangda ko'rsatilgan. Taxminan qizil rang bilan belgilangan to'rtburchakdir.

<img width="404" alt="Снимок экрана 2022-10-06 в 14 22 13" src="https://user-images.githubusercontent.com/99121169/194277575-3bd8dfd7-08a3-4821-a59f-0e9821d2cd77.png">


# Misol | Ko'p o'zgaruvchan

Ko'p o'lchovli funktsiyalar uchun integratsiyani ham amalga oshirishimiz mumkin. Jarayon avvalgisiga o'xshaydi. Biroq, chiziq bo'ylab namuna olish o'rniga (dan a uchun b), endi biz yuqori o'lchamli domendan namuna olishimiz kerak. Oddiylik uchun biz ko'p o'zgaruvchan funktsiyani bir xil bo'lgan domenga integratsiyalashni tasvirlaymiz.a va b har bir o'zgaruvchi uchun. Bu ikkita o'zgaruvchiga (x1 va x2) ega bo'lgan funktsiyada domen kvadrat shaklda ekanligini anglatadi; va uchta o'zgaruvchiga ega funksiya uchun kub shaklida.

<img width="703" alt="Снимок экрана 2022-10-06 в 14 22 58" src="https://user-images.githubusercontent.com/99121169/194277713-c4a1748e-719d-48e1-b388-0d877f852961.png">

Natijalar:

- f(x)= 10 - x1 2 - x2 2 uchun, -2 dan 2 gacha (barcha x uchun)
integrallangan Monte-Karlo yechimi: 117,346
Analitik yechim: 117,333

- f(x)= 10 - x1 2 - x2 2 - x3 2 uchun, -2 dan 2 gacha (barcha x uchun) integratsiyalangan
Monte-Karlo yechimi: 383,888
Analitik yechim: 384,000

# Misol | Boshqa domenlar bilan birlashtirilgan ko'p o'lchovli

Integratsiya amalga oshiriladigan domen yanada murakkab va undan namuna olish va uning hajmini hisoblash qiyin bo'lishi mumkin. Biz, masalan, kvadrat domen o'rniga dumaloq domen bo'yicha ikki o'zgaruvchan funksiyamizni birlashtira olamiz. Shunga qaramay, g'oya bir xil - yagona tanlab olish bilan biz domen bo'ylab namuna olishni va domen hajmining mahsuloti va domen bo'yicha funktsiyaning kutilayotgan qiymati orqali integratsiyani taxmin qilishni xohlaymiz.

Keling, bir xil ikki o'zgaruvchan funktsiyadan foydalanamizf( x ) = 10 − x12− x22va birlik doirasi bo'ylab integrasiya qiling. To'liq birlik doirasi bo'ylab yagona namuna olish kvadrat mintaqada (birlik doirasini qamrab olgan) namuna olishdan ko'ra qiyinroqdir. Bundan biz 1) domenning maydonini tanlab olingan kvadrat maydonining domen ichidagi tanlangan nuqtalar nisbati bo'yicha ko'paytmasi sifatida hisoblashimiz mumkin, 2) domen ichidagi tanlab olingan nuqtalarning o'rtacha f (x) sifatidagi kutish . Quyida namuna olishning vizual ko'rinishi (yashil rangda ko'rsatilgan birlik doirasi ichidagi namuna nuqtalari),

<img width="431" alt="Снимок экрана 2022-10-06 в 14 23 05" src="https://user-images.githubusercontent.com/99121169/194277798-e8cf9f53-2bd4-4934-9841-e572f9b8295a.png">

Pythonda bu shunday ko'rinadi:

<img width="732" alt="Снимок экрана 2022-10-06 в 14 23 17" src="https://user-images.githubusercontent.com/99121169/194277912-fab75f5d-70b8-420c-8376-3f349f41b2ec.png">


Natija:

- f(x)= 10 - x1 2 - x2 2 uchun, birlik aylanasi ustida birlashtirilgan
Monte-Karlo yechimi: 29,849
Analitik yechim: 29,845

# Biz ularni Python-da aniqlaymiz va Monte-Karlo integratsiyasini amalga oshiramiz

<img width="652" alt="Снимок экрана 2022-10-06 в 14 23 28" src="https://user-images.githubusercontent.com/99121169/194278020-4ebd2a46-466e-455a-b56d-13232317630f.png">

- Tasdiqlash sifatida biz pmvnEllellipsoidlar (doiralar kiritilgan) bo'yicha ko'p o'zgaruvchan normal taqsimotlarni birlashtira oladigan funksiyadan foydalanamiz.

Natijalar bir-biriga mos kelishi bilan:

- Ko‘p o‘zgaruvchan normal, birlik aylanasi bo‘yicha integratsiyalangan
Monte-Karlo yechimi uchun: 0,2020 pmvnEll’dan
yechim (shotGroups pkg R ichida): 0,2019
# Qo'shimcha sharhlar:

- Shubhasiz, taqdim etilgan misollar oddiy va ba'zilarida aniq holatlar uchun analitik echimlar va/yoki Python/R paketlari mavjud. Ammo ular Monte-Karlo integratsiyasi ortidagi mexanikani tushunish uchun foydalidir. Ko'rinib turibdiki, tasvirlangan Monte-Karlo usuli yopiq shaklli echimlarsiz murakkabroq funktsiyalarga osonlikcha umumlashtiriladi. Bundan tashqari, tanlab olishni amalga oshirishning ko'plab optimallashtirilgan usullari mavjud (masalan, tabaqalashtirilgan namuna olish, ahamiyatli namuna olish va h.k.) va agar qiziqsa, o'quvchilar ushbu mavzularni ko'proq o'qishlari tavsiya etiladi.
