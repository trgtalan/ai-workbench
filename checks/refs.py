"""kontrol: kirik yerel referans.

NE ARAR
  Markdown dosyalarindaki yerel dosya/klasor referanslarinin diskte var olup
  olmadigi. Iki bicim taranir:
    - markdown link hedefi:  [ad](yol/dosya.md)
    - ters tirnak icindeki YOL:  `site/proje-envanteri.md`, `checks/`
      (ters tirnak icinde ayirici '/' YOKSA yol degil, dosya ADIdir -> kapsam disi)

NE ARAMAZ (kasten kapsam disi)
  - http/https/mailto adresleri            -> agdan dogrulama bu kontrolun isi degil
  - ```...``` kod bloklari                 -> agac semalari gercek yol degildir
  - ~ veya / ile baslayan mutlak yollar    -> depo disi, tasinabilir degil
  - semasiz alan adlari (wa.me/..., x.com/..) -> adres, dosya degil
  - `#bolum` sayfa ici cengelleri          -> baslik esleme ayri bir kontroldur
  - yolun icerigi                          -> yalnizca varlik denetlenir
  - ters tirnakta ayiricisiz ad (`BASLA.md`) -> duz yazida anma, referans degil
  - benchmarks/ altindaki ornek kume        -> kasten kirik, olcum verisi

Cikis: bulgu varsa 1, yoksa 0.
"""
import re
import sys
from pathlib import Path

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TIRNAK = re.compile(r"`([^`\n]+)`")
# yol gibi gorunen: en az bir / icerir ya da bilinen bir uzantiyla biter
YOL_GIBI = re.compile(r"(^|.*/)[^/\s]+\.(md|py|json|txt|toml|ya?ml|html|css|js|ts|tsx)$|/$|.+/.+")


def _kod_bloklari_disi(metin):
    """Fenced kod bloklarini bosluga cevirir, satir numaralari korunur."""
    cikti, icinde = [], False
    for satir in metin.splitlines():
        if satir.lstrip().startswith("```"):
            icinde = not icinde
            cikti.append("")
            continue
        cikti.append("" if icinde else satir)
    return cikti


ALAN_ADI = re.compile(r"^[a-z0-9-]+(\.[a-z0-9-]+)*\.(me|com|net|org|io|de|tr|co|dev|app|gov|edu)$", re.I)


def _aday_mi(ham):
    y = ham.strip()
    if not y or y.startswith(("http://", "https://", "mailto:", "#", "~", "/")):
        return False
    if any(c in y for c in " \t|"):
        return False
    if ALAN_ADI.match(y.split("/", 1)[0]):
        return False
    return bool(YOL_GIBI.match(y))


def dosyayi_tara(dosya: Path, kok: Path):
    bulgular = []
    for no, satir in enumerate(_kod_bloklari_disi(dosya.read_text(encoding="utf-8")), 1):
        adaylar = [(x, True) for x in LINK.findall(satir)]
        adaylar += [(x, False) for x in TIRNAK.findall(satir)]
        for ham, link_mi in adaylar:
            if not _aday_mi(ham):
                continue
            # ters tirnakta ayirici yoksa dosya adi anilmis demektir, referans degil
            if not link_mi and "/" not in ham:
                continue
            y = ham.split("#", 1)[0].rstrip("/")
            if not y:
                continue
            if (dosya.parent / y).exists() or (kok / y).exists():
                continue
            bulgular.append((dosya, no, ham.strip()))
    return bulgular


def kos(hedef: Path):
    hedef = hedef.resolve()
    kok = hedef if hedef.is_dir() else hedef.parent
    dosyalar = sorted(hedef.rglob("*.md")) if hedef.is_dir() else [hedef]
    bulgular = []
    for d in dosyalar:
        # haric tutma hedefe GORE degerlendirilir: kume dogrudan hedef gosterildiginde taranir
        gorece = d.relative_to(hedef) if hedef.is_dir() else Path(d.name)
        if any(p in gorece.parts for p in (".git", "node_modules", "runs", "benchmarks")):
            continue
        bulgular += dosyayi_tara(d, kok)
    return bulgular


if __name__ == "__main__":
    hedef = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    b = kos(hedef)
    for dosya, no, ref in b:
        print(f"{dosya}:{no}: kirik referans -> {ref}")
    print(f"\n{len(b)} bulgu")
    sys.exit(1 if b else 0)
