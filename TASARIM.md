# Tasarım — ai-workbench

## İlkeler

1. **Tek yönlü bağımlılık.** Projeler altyapıyı çağırır; altyapı hiçbir projeyi bilmez.
   Bu yüzden altyapı ayrı bir depodur, proje klasörünün içinde durmaz.
2. **Çekirdek iş alanı bilmez.** Web, sosyal medya, mühendislik analizi dışarıdan eklenir.
3. **İddia sayısı kaynaksız yazılmaz.** *Kontrol referansın varlığını doğrular, sayının
   kaynakla uyumunu değil — bu sınır bilinerek kabul edilir.*
4. **Deterministik olan modele sorulmaz.**
5. **Model çıktısı yetkisizdir.** Doğrulayıcının değeri, doğrulananın ona
   dokunamamasından gelir. Ayrıntı: `CLAUDE.md` → Model katmanı.
6. **Kopya değil bağlantı.** Ortak kuralın kaynağı `CLAUDE.md`'dir; `aiw install` onu
   `~/.claude/CLAUDE.md` içindeki işaretli bloğa yazar. İkinci bir kaynak yoktur.
7. **Sürüm görünür.** Her çıktı `[ai-workbench <commit>]` ile damgalanır.
8. **Sezgisel kontrol ölçülmeden kullanılmaz.** Ölçülen, kodun doğruluğu değil, kuralın
   niyetiyle örtüşmesidir.

## Kapsam sınırı — altyapı ne kadar büyür

Altyapı yalnız gerçek bir işe hizmet ettiği kadar büyür. Bu, sıra kuralı değil **tavan**
kuralıdır: site kurulumu başlamadan önce yazılan altyapı, üç parçayla sınırlıdır —
geçit istemcisi, çağrı kaydı, ilk kontrol. Bunlar bitti; ötesi site çalışırken,
gerçek bir rahatsızlıktan doğarak eklenir.

Arkasındaki risk gerçek ve yürürlükte: 2026'nın baskın başarısızlığı yarım kalmış kod
değil, kullanıcısı olmayan bitmiş üründür. "Önce şu sistemi bitireyim" cümlesi bu
kalıbın kendisidir. Tavan bu yüzden var — sırayı değil, hacmi bağlar.

## Açılan ve açılmayan klasörler

Açıldı, çünkü bugün doldu: `aiw_lib/` · `checks/` · `benchmarks/` · `runs/` · `notlar/`.

Açılmadı: `core/` · `policies/` · `schemas/` · `templates/` · `adapters/` · `tests/` ·
`evaluations/` · rol ve ajan tanımları · koşullu kural dağıtımı · vektör veritabanı.

`adapters/` özellikle açılmadı: geçit OpenAI uyumlu ve tek istemci yetiyor. Sağlayıcı
başına adapter, ancak **OpenAI uyumlu olmayan ikinci bir sağlayıcı** fiilen geldiğinde
açılır. Tek sağlayıcı için adapter katmanı, kaçınmaya çalıştığımız erken yapının kendisi.

`tests/` ve `evaluations/` de açılmadı: kontrollerin doğruluğu `benchmarks/` altında,
altyapının kendi doğrulaması `aiw self-test` içinde ölçülüyor. Üçüncü bir yer yok.

## İlk kontrol — neden `refs`

Tahminle seçilmedi. 25 Ağustos 2026 oturumunda `ai-workbench` tasarım belgesi taşındı ve `BASLA.md`
içindeki iki referans sessizce kırıldı; elle grep'lenerek bulundu. Aynı gün ikinci kez
`CLAUDE.md`'ye yapılan referans kırık çıktı. İki kez tekrar eden, elle yakalanan,
deterministik olarak bulunabilen bir rahatsızlık — kontrolün tanımı bu.

Kapsamı ve kapsam dışı bıraktıkları `checks/refs.py` başlığında yazılı.

## Ölçüm

`benchmarks/refs/kume-v3` — 6 bulunması gereken, 4 bulunmaması gereken, 12 kasten
kapsam dışı vaka. Eşik ölçüm kümesinin `beklenen` dosyasında: YP≤0, YN≤0. Şu an geçiyor.

v1 → v3 nedeni ölçülmüş: kontrol ilk gerçek koşusunda 3 yanlış pozitif verdi — düz
yazıda anılan dosya adları, örnek kümenin kendisi, ve taşınmış bir dosyanın geçmişe
dönük anılması. Kapsam daraltıldı, daraltmanın kendisi kümeye vaka olarak yazıldı.
Ayrıca ölçüm, daraltma sırasında kontrole giren gerçek bir hatayı (küme klasörünün
kendi taramasından elenmesi) yakaladı — doğrulayıcının işini yaptığı yer burası.

v3'te sınır tek kurala oturdu: **ters tırnak içinde iç ayırıcı yoksa o bir addır, yol
değil.** `BASLA.md` ve `core/` anmadır; `checks/refs.py` ve `benchmarks/refs/` yoldur. Uzantısız
ve `/` ile bitmeyen (`next/image`) modül belirtecidir. Bu üç daraltmanın üçü de gerçek
kullanımda yanlış pozitif verdikten sonra yazıldı, tahminle değil.

Bilinen zayıflık: kümeyi ve kontrolü aynı kişi yazdı, küme küçük. Sayı, kontrolün
mutlak doğruluğunu değil, kural ile niyetin örtüştüğünü gösterir. Gerçek kullanımda
yanlış pozitif çıkarsa küme büyütülür ve sürümü artar.

## Satır tavanı — nereye uygulanır

160 satır tavanı **her oturuma yüklenen** dosyalar içindir (`CLAUDE.md`, 88 satır).
Bu belge gibi istendiğinde okunan başvuru belgeleri kapsam dışıdır; onları büyümekten
koruyan şey satır sayısı değil, bir başlığın bütün hakkında olmayı bırakmasıdır —
o an bölünür.

Ölçülen kalıp: dosya büyüdükçe uyum düşüyor, uyum düşünce daha çok kural ekleniyor.

## Geçit bağımlılığı

Şu an tanımlı **tek sağlayıcı** Paderborn geçidi ve geçit bir üniversite hizmeti. Kullanıcı
yakında iş ortamına geçecek; orada harici servise izin verilip verilmeyeceği bilinmiyor.

Bu yüzden katman **isteğe bağlı** yazıldı: geçit yoksa `aiw self-test` uyarı verir ve
sistem çalışmaya devam eder; iş Claude'da yapılır. Sessiz yedeğe geçiş yoktur — hangi
yolun kullanıldığı çıktıda görünür. Geçit tek yol olarak hiçbir yere yazılmadı; ikinci
bir sağlayıcı geldiğinde `aiw_lib/gateway.py` yanına ikinci istemci girer.

## İkinci kontrol — `sizinti`, ve kuralın bilerek delindiği yer

`refs` gerçek bir rahatsızlıktan doğdu. `sizinti` doğmadı — önden yazıldı ve bu,
"kullanımdan önce tasarım yapılmaz" ilkesinin bilinçli istisnasıdır.

Gerekçe tek cümle: bu sınıfta hata geri alınamaz. Sızan anahtar rotasyon ister,
push edilmiş `.env` git geçmişinde kalır, silmek yetmez. İstisnanın sınırı da dar —
yalnız geri alınamaz olan taranır. CORS, RLS, bellekte veri, arayüzde yetki gibi
maddeler bu projede karşılığı olmadığı için yazılmadı; hesaplayıcı geldiğinde
yeniden değerlendirilir.

Ölçüm ikiye bölündü: içerik taraması `benchmarks/sizinti/`, git'e bağlı maddeler
(`.env` izlenmesi, `node_modules`, lock dosyası) `aiw self-test` içinde geçici bir
depoda. İkincisi dosya tabanlı kümeye sığmıyordu.

Susturma açık ve görünür: satır sonunda `kontrol:atla`. Sessiz hariç tutma yok.

## Harcama sınırı — şimdi yok, tetiği yazılı

Ücretli uç noktaya harcama ve hız sınırı konmaması bilinen bir hata.

**Raporlama kuruldu.** Her çağrının USD tutarı `aiw ask` çıktısında ve `aiw maliyet`
özetinde görünüyor. Kaynak, geçit işletmecisinin kendi listesi: `Modelle_und_Preise.md`.

Elle tutulan ikinci bir tablo **yok** — 6. ilke gereği. İlk kurulumda bir `fiyatlar.json`
yazılmıştı, liste gelince silindi: aynı sayıyı iki yerde tutmak, ikisinin ayrışmasını
zaman meselesi yapar. Fiyat güncellendiğinde tek iş o dosyayı değiştirmektir.

USD, kayıt anında değil **rapor anında** hesaplanır; böylece liste güncellendiğinde
geçmiş çağrılar da doğru fiyatlanır.

**Ölçülen ayrım:** `gwdg.*` modellerinin tamamı $0.00, `openai.*` ücretli
($0.20–$30.00 giriş / 1M). İşçi katmanının maliyet gerekçesi bu satırda duruyor —
ucuz modele iş devretmek değil, ücretsiz modele devretmek söz konusu.
Hız sınırı da listede: gwdg 10 RPM / 500k TPM, openai 100 RPM / 2M TPM.

**Sınır mekanizması (durdurma/eşik) hâlâ yok.** Raporlama harcamayı görünür kılar,
engellemez. Eşik, gerçek bir ücret doğrulandığında yazılır.

## Anahtar köprüsü — şimdi yok, tetiği yazılı

`aiw` anahtarını macOS anahtar zincirinden okuyor. Ama Next.js zinciri bilmiyor,
yalnız `process.env`'e bakıyor — arada bir köprü gerekiyor.

**Köprü yazılmadı.** self-enerji-site'de tek bir sır yok; kullanılmayan altyapı
yazmak bu belgenin kaçındığı şeyin ta kendisi.

**Tetik:** site ilk sırrına ihtiyaç duyduğunda (büyük ihtimalle iletişim formu
e-posta göndermeye başladığında). O gün köprü yazılır ve aynı anahtar Vercel
paneline girilir — yerelde zincir, yayında panel. Düz metin dosya hiçbir yerde.

## Bilinen takas

`git pull` bütün projeleri aynı anda etkiler. Proje bazında sürüm sabitleme bilinçli
olarak eklenmiyor: her projeye "hangi altyapı sürümündeyim" kaydı koymak, altyapının
var olma sebebi olan proje-başına-kurulum maliyetini geri getirir. Çıktıya basılan
sürüm damgası, davranış değiştiğinde farkı açıklamaya yeter.

Tek makinede tek kişilik kullanım için geçerlidir. İkinci makine veya ikinci kullanıcı
girdiğinde yeniden değerlendirilir.

## Canlılık ölçütü

Altyapının yaşayıp yaşamadığı satır sayısıyla değil takvimle ölçülür: ayrı aylara
yayılan commit'ler config'in kullanıldığını, tek patlamada gelip donmuş bir geçmiş ise
yayınlanmış ama kullanılmayan bir config olduğunu gösteriyor.

## Hook politikası

Sıfır ya da bir, tek iş. Gerçekte kullanılan tek kalıp "düzenlemeden sonra
formatter/linter çalıştır". Başkası için kurulmaz. Şu an sıfır.

## Kayıt — ikinci görüş, 25 Ağustos 2026

Kural seti `openai.gpt-5.6-luna`'ya çelişki taraması için verildi (2998/2121 token,
21.8 sn). Tek bulgu: "tüm model erişimi geçide bağlı" ifadesi "geçit tek yol değildir"
ile çelişiyordu. Bulgu kabul edildi, ifade düzeltildi. İşçi çıktısı dosyaya doğrudan
yazılmadı; bulgu okundu, karar insan tarafında verildi.
