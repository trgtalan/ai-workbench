"""kontrol: geri alinamaz yayina alma hatalari.

NEDEN BU KONTROL ONCEDEN YAZILDI
  Diger kontroller tekrar eden gercek bir rahatsizliktan dogar. Bu sinif ayri:
  sizan anahtar rotasyon ister, push edilen .env git gecmisinde kalir. Hatanin
  maliyeti kontrolun maliyetinden buyuk oldugu icin kural bilerek delindi.

NE ARAR
  1. Git'in izledigi .env dosyasi (ya da .gitignore'da olmayan .env)
  2. Kaynak dosyada gomulu sir: ANAHTAR = "<uzun deger>" bicimi
  3. Istemciye acilan onekte sir adi: NEXT_PUBLIC_*/VITE_* icinde KEY|SECRET|TOKEN|PASSWORD
  4. Git'in izledigi node_modules; package.json varken lock dosyasinin yoklugu
  5. Kaynak kodda sabit localhost / 127.0.0.1 adresi   kontrol:atla

NE ARAMAZ (kasten kapsam disi)
  - degisken ADInin anilmasi (`UPB_API_KEY` yazmak sir degildir) -> yalnizca DEGER taranir
  - .md/.txt icindeki localhost                                  -> belge, kod degil   kontrol:atla
  - .gitignore'lanmis, izlenmeyen yerel .env                     -> dogru kullanim
  - sirrin gecerli olup olmadigi                                 -> yalnizca bicim bakilir
  - deponun gecmisi                                              -> yalnizca calisma agaci
  - sonunda `kontrol:atla` yazan satir                           -> acik ve gorunur susturma

Cikis: bulgu varsa 1, yoksa 0.
"""
import re
import subprocess
import sys
from pathlib import Path

KAYNAK_UZANTI = {".js", ".jsx", ".ts", ".tsx", ".py", ".json", ".html", ".css",
                 ".mjs", ".cjs", ".sh", ".yml", ".yaml", ".toml", ".env"}
ATLA = {".git", "node_modules", "runs", "benchmarks", ".next", "dist", "build"}

# ANAHTAR = "deger": deger en az 16 karakter, bosluksuz, sir gibi
SIR = re.compile(
    r"""(?ix)
    \b (\w* (?: api[_-]?key | secret | token | password | passwd | private[_-]?key ) \w*)
    \s* [:=] \s*
    ['"]([A-Za-z0-9_\-\.\+/=]{16,})['"]
    """)
ONEK = re.compile(r"\b((?:NEXT_PUBLIC|VITE)_\w*(?:KEY|SECRET|TOKEN|PASSWORD)\w*)\b", re.I)
YEREL = re.compile(r"\b(?:localhost|127\.0\.0\.1)(?::\d+)?\b", re.I)  # kontrol:atla
# gercek sir degil, yer tutucu
YER_TUTUCU = re.compile(r"(?i)^(x{4,}|your[_-]|<.*>|placeholder|degistir|buraya|example|test)")


def _izlenen(kok: Path):
    try:
        c = subprocess.run(["git", "-C", str(kok), "ls-files"],
                           capture_output=True, text=True, timeout=10)
        return set(c.stdout.split()) if c.returncode == 0 else None
    except Exception:
        return None


def kos(hedef):
    hedef = Path(hedef).resolve()
    kok = hedef if hedef.is_dir() else hedef.parent
    bulgular = []
    izlenen = _izlenen(kok)

    # 1 + 4: git'in izledikleri
    if izlenen is not None:
        for y in sorted(izlenen):
            ad = Path(y).name
            if ad == ".env" or ad.startswith(".env."):
                bulgular.append((kok / y, 0, "git bu .env dosyasini izliyor"))
            if "node_modules" in Path(y).parts:
                bulgular.append((kok / y, 0, "git node_modules icerigini izliyor"))
                break
        if (kok / "package.json").exists():
            kilit = {"package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lockb"}
            if not any((kok / k).exists() for k in kilit):
                bulgular.append((kok / "package.json", 0, "lock dosyasi yok"))

    # 1b: gitignore'lanmamis yerel .env
    gi = (kok / ".gitignore")
    gi_metin = gi.read_text() if gi.exists() else ""
    for e in kok.rglob(".env*"):
        if e.is_file() and ".env" not in gi_metin:
            bulgular.append((e, 0, ".env var ama .gitignore'da degil"))
            break

    # 2 + 3 + 5: dosya icerigi
    for d in sorted(kok.rglob("*")):
        if not d.is_file() or d.suffix not in KAYNAK_UZANTI:
            continue
        if any(p in d.relative_to(kok).parts for p in ATLA):
            continue
        try:
            satirlar = d.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for no, s in enumerate(satirlar, 1):
            if "kontrol:atla" in s:
                continue
            for ad, deger in SIR.findall(s):
                if not YER_TUTUCU.match(deger):
                    bulgular.append((d, no, f"gomulu sir: {ad}"))
            for ad in ONEK.findall(s):
                bulgular.append((d, no, f"istemciye acik onekte sir adi: {ad}"))
            if YEREL.search(s):
                bulgular.append((d, no, "sabit localhost adresi"))  # kontrol:atla
    return bulgular


if __name__ == "__main__":
    b = kos(sys.argv[1] if len(sys.argv) > 1 else ".")
    for d, n, m in b:
        print(f"{d}:{n}: {m}")
    print(f"\n{len(b)} bulgu")
    sys.exit(1 if b else 0)
