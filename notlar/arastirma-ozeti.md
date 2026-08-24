# Araştırma özeti

24 Ağustos 2026. Kaynak: Hacker News yorumları (2025-12 → 2026-08), GitHub ölçümleri,
akademik çalışmalar. **Reddit erişilemedi** — en büyük uygulayıcı külliyatı bu raporda yok,
bu bir boşluk.

## Kararları belirleyen bulgular

**Kural dosyası büyüdükçe uyum düşüyor.** Bağımsız birçok kişi: *"spec'imin %90'ını sildim,
işler çarpıcı biçimde düzeldi."* Altı aydır tam uyum bildiren kişi bunu dosyası küçük
olduğu için aldığını söylüyor. Belgelenmiş bir yörünge: 1.818 satır monolit → 3.000 satır
her zaman yüklü → **~160 satır her zaman yüklü, gerisi ihtiyaç anında.**

**Doğrulayıcıyı ajan yazmamalı ve değiştirememeli.** Ajanlar geçmeyen testi siliyor:
*"test geçmiyor, düzeltemiyorum — silelim."* Birden çok kişi bağımsız yakalamış.
100 turluk dayanıklılık testinde modeller geri bildirim olmadan **5–6 turda** çöküyor;
test geri bildirimiyle tamamlanan tur **12 katına** çıkıyor.
(arXiv 2606.19613)

**Terk etme sebebi 1: doğrulama vergisi.** Kontrollü çalışma: 16 deneyimli geliştirici
AI ile **%19 daha yavaş** çalışmış, %20 daha hızlı olduklarına inanmışlar.
(metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
Kazanç yeni kodda gerçek, olgun kod tabanında küçülüyor ya da tersine dönüyor.
(arXiv 2608.20446)

**Terk etme sebebi 2: köstebek döngüsü.** Ajan yeni hatayı düzeltirken eskisini geri
getiriyor; kimse kodu döngüyü kıracak kadar anlamıyor. Asıl bırakma anı bu.

**Bitirenlerin ortak cümlesi:** *"Yalnız küçük görevler. Her görev tek okumada gözden
geçirilebilecek kadar küçük olmalı."* Ve o boyutta commit.

**Kodu atmak refactor'dan ucuz** — 1.200 satır ve zayıf test yerine, bilgiyi alıp
2–3 saatte 300 satır, %40'ı test.

**Config'in yaşayıp yaşamadığını gösteren tek şey takvim.** Ayrı aylara yayılan commit =
kullanılıyor. Tek patlama sonra sessizlik = yayınlanmış ama kullanılmıyor. En kalabalık
kurulumlar tam olarak donmuş olanlar: 818 skill + 118 ajan → 8 günde 70 commit, sonra
6 ay sessizlik. 61 ajan → hepsi tek ayda, 12 aydır donmuş.

**Gerçek üretim depoları neredeyse çıplak.** 17 tanınmış proje: 3'ünde `.claude/` dizini,
1'inde MCP, 2'sinde hook (birer-ikişer). Sahip oldukları şey tek bir kural dosyası.
128 bin depoluk taramada rehber dosyası ekleyip **bir daha hiç değiştirmeyenler %21,8.**
(arXiv 2601.18341)

**Hook gerçekte %13'te var** ve kullanıldığı yerde neredeyse hep tek iş: düzenlemeden
sonra formatter/linter. 50+ ajanlı olup ajan dosyaları aylarca düzenlenmiş **tek depo
bulunamadı.**

**Ve terk noktası yer değiştirmiş.** 2026'nın şikâyeti yarım kod değil, kullanıcısı olmayan
bitmiş ürün: *"neredeyse hepsi geliştirmeye odaklanmış, kod üreten koca uzay gemileri
kuruyorlar… ve neredeyse hiçbirinin parası ya da trafiği yok."* Yanındaki cümle:
*"aslında pazarlama yapmalıyım ama önce şu süper sistemimi bitireyim."*
(levels.io/indie-hackers-ai-factories-no-money-traffic)

## Bulunamayanlar

- Tek kişilik projelerde tamamlanma/terk oranına dair **gerçek veri yok.** Dolaşan bütün
  rakamlar kurumsal AI programlarına ait, satıcı anketi, ya da on bir projelik örneklem.
- Global-vs-proje bazlı yapılandırma stratejisi üzerine **ciddi tartışma yok.** Üç ayrı
  araştırmada da aynı sonuç: kopyalanacak örnek yok.
- Bir skill'in gerçekten çağrılıp çağrılmadığını ölçen çalışma yok. Bütün çalışmalar
  dosyanın *varlığını* ölçüyor — ki bu, kullanılan config ile kopyalanmış config'i
  ayıramayan tek metrik.
