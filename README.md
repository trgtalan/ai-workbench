# ai-workbench

Projelerden bağımsız, kişiye ait AI çalışma altyapısı. Bir proje açmak, denemek ve
silmek altyapıyı etkilemez; altyapı kişiye aittir, projeler tek kullanımlıktır.

## Kurulum

```
cd ~/Projects/ai-workbench
./aiw install      # ortak kuralı ~/.claude/CLAUDE.md'ye bağlar
./aiw self-test    # kontrol ölçümü + install idempotentliği + geçit erişimi
```

Anahtar: `UPB_API_KEY` ortam değişkeni, yoksa `~/.config/aiw/env` (600).

## Yapı

```
ai-workbench/
├── CLAUDE.md        # ortak kural — kaynak burasıdır, tavan 160 satır
├── TASARIM.md       # ilkeler, kararlar, bilinen takaslar
├── aiw              # komut satırı aracı
├── aiw_lib/         # geçit istemcisi ve çağrı kaydı
├── checks/          # deterministik kontroller
├── benchmarks/      # kontrollerin YP/YN ölçümü
├── runs/            # çağrı kayıtları (versiyonlanmaz)
└── notlar/          # arka plan, karar girdisi
```

## Durum

- Geçit doğrulandı: 71 model, `/v1/chat/completions` çalışıyor.
- Kontrol sayısı: 1 (`checks/refs.py`), ölçüldü — YP=0, YN=0, 12 vakalık `kume-v1`.
- İşçi model katmanı: çağrı ve kayıt hazır; ilk gerçek işçi görevi henüz koşulmadı.
