"""checks/sizinti.py icerik taramasinin YP/YN oranini olcer."""
import json
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent
sys.path.insert(0, str(KOK.parent.parent))
from checks import sizinti  # noqa: E402


def main():
    b = json.loads((KOK / "beklenen.json").read_text())
    kume = KOK / b["kume"]
    beklenen = set(b["beklenen_bulgular"])
    bulunan = {f"{d.relative_to(kume)}:{n}" for d, n, _ in sizinti.kos(kume) if n}
    yp, yn = sorted(bulunan - beklenen), sorted(beklenen - bulunan)
    print(f"kume: sizinti/{b['kume']} | beklenen {len(beklenen)} | bulunan {len(bulunan)}")
    for x in yp:
        print(f"  YANLIS POZITIF: {x}")
    for x in yn:
        print(f"  YANLIS NEGATIF: {x}")
    e = b["esik"]
    gecti = len(yp) <= e["yanlis_pozitif"] and len(yn) <= e["yanlis_negatif"]
    print(f"YP={len(yp)} YN={len(yn)} | {'GECTI' if gecti else 'KALDI'}")
    return 0 if gecti else 1


if __name__ == "__main__":
    sys.exit(main())
