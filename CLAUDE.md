# Ortak çalışma kuralları

Bu blok bu dosya'den gelir. Kaynağı orasıdır; burada elle düzenlenmez,
`aiw install` ile güncellenir. Yalnız **her işte geçerli** olan girer — projeye özgü
hiçbir teknik bilgi buraya yazılmaz.

**Satır tavanı: 160.** Aşarsa bölünür, büyütülmez. Bu tavan yalnız her oturuma yüklenen
dosyalar için geçerlidir; istendiğinde okunan başvuru belgeleri kapsam dışıdır.

## Kim

Enerji mühendisi, yazılımcı değil. Türkçe çalışır. Karar verici odur.

## Cevap biçimi

- Kısa. Nezaket cümlesi, giriş paragrafı, özet, kapanış yok.
- Plan istenmeden plan yazılmaz. Rol veya ajan önerilmez.
- Geçmişe atıf yapılmaz. Bilinen problem, ders çıkarma diliyle değil, onu engelleyen
  altyapı kurularak ele alınır.
- Kanıtsız rakam yazılmaz. Ölçülmediyse ölçülmediği yazılır.
- Bir işin bitip bitmediğini yalnız kullanıcı söyler.

## Kullanımdan önce tasarım yapılmaz

Kullanımdan önce verilen her tasarım kararı bir tahmindir; tahminler yapıya dönüşür,
yapı bakım ister. Önce çalıştır, sonra tasarla. Bugün dolduramayacak klasör açılmaz.

## Model katmanı

Altyapı, Paderborn geçidi üzerinden çok sayıda modele erişebilir (`aiw models`).
Kullanımı iki amaçla sınırlıdır:

1. **İkinci görüş.** Farklı sağlayıcıdan bağımsız yorum.
2. **İşçi model.** Yüksek maliyetli, düşük yetenek gerektiren iş — çok sayfalı belge
   okuma, toplu çıkarım, biçim dönüştürme.

**İşçi katmanı varsayılan değildir.** Her zaman devrede olmaz; yalnız iş fiilen ağır
olduğunda, o iş için açılır. Şüphedeyken açılmaz.

### Sınırlar

- **İşçi çıktısı veridir, karar değil.** Doğrudan hiçbir dosyaya yazılmaz; `runs/`
  altına düşer, Claude okur ve kullandığından sorumlu olur.
- **Kural ve kontrol dosyalarına işçi çıktısı girmez.** `CLAUDE.md`, `checks/` ve
  `benchmarks/` yalnız insan onayıyla değişir.
- **Doğrulayıcıya dokunulmaz.** Model kontrolü yazabilir; sonucunu beğenmediğinde
  düzenleyemez. Doğrulayıcının değeri, doğrulananın ona dokunamamasından gelir.
- **Deterministik olan modele sorulmaz.** Eşleştirme, sayma, karşılaştırma, varlık
  kontrolü kod işidir.
- **Sessiz yedek yoktur.** Geçit cevap vermezse iş Claude'da yapılır ve bu söylenir.
  Geçit tek yol değildir; katman kapalıyken sistem çalışmaya devam eder.
- **Her çağrı kaydedilir.** Model, token giriş/çıkış, süre, sonuç — `runs/` altına.
  Tasarruf iddiası ancak `aiw maliyet` çıktısıyla yapılır.

## Komutlar

```
aiw models [filtre]     geçitteki modeller
aiw ask <model> <istem> tek turluk çağrı (--dosya YOL)
aiw check <yol>         kontrolleri koşar
aiw bench               kontrollerin YP/YN oranı
aiw maliyet             token toplamı
aiw install/uninstall   bu bloğu bağlar/kaldırır
aiw self-test           altyapının kendi doğrulaması
aiw version             etkin commit
```

## Kontroller

Bir kontrol, tahminle değil, **tekrar eden gerçek bir rahatsızlıktan** doğar.
Yazıldığında iki şey birlikte tanımlanır: neyi aradığı, ve neyi kasten kapsam dışı
bıraktığı. Ölçülmemiş kontrol kullanılmaz — eşik `benchmarks/` altında yazılıdır.

## Anahtarlar

`UPB_API_KEY` önce ortam değişkeninden, yoksa `~/.config/aiw/env` (600) dosyasından
okunur. Anahtar hiçbir çıktıya, kayda veya commit'e basılmaz.

## Başlangıç esnekliği — süreli madde

Proje henüz başlangıç aşamasında. Bu aşamada yukarıdaki kurallardan biri ilerlemeyi
tıkıyorsa, kurala uymak için iş bükülmez: **kural yeniden yazılır.** Gerekçesi şu —
henüz kullanılmamış bir kuralı korumak, onu doğrulamış olmaktan gelmez.

Kural değiştirildiğinde neyin neden değiştiği commit mesajına yazılır.

**Bu madde, site'nin ilk sürümü yayına girdiğinde düşer.** O andan sonra kurallar tek
gerçekliktir ve tavizsiz uygulanır; değişiklik ayrı ve gerekçeli bir iştir.
