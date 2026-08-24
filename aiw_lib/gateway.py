"""Paderborn AI Gateway istemcisi (OpenAI uyumlu). Yalnız stdlib.

Sözleşme:
- Her çağrı `runs/` altına kaydedilir: model, token sayısı, süre, sonuç.
- Sessiz yedeğe geçiş yoktur. Geçit cevap vermezse hata yükselir, çağıran karar verir.
"""
import hashlib
import json
import os
import ssl
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

BASE = "https://ai-gateway.uni-paderborn.de/v1"
ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"


class GatewayError(RuntimeError):
    pass


def _ssl_baglami():
    """macOS'ta python.org kurulumu kendi CA paketini kurmayabiliyor (cert.pem yok).
    Varsa certifi paketi kullanilir; yoksa sistem varsayilani. Dogrulama kapatilmaz."""
    try:
        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


_CTX = _ssl_baglami()


def anahtar():
    """Önce ortam değişkeni, sonra ~/.config/aiw/env. Anahtar hiçbir yere basılmaz."""
    k = os.environ.get("UPB_API_KEY")
    if k:
        return k.strip()
    p = Path.home() / ".config" / "aiw" / "env"
    if p.exists():
        for satir in p.read_text().splitlines():
            if satir.startswith("UPB_API_KEY="):
                return satir.split("=", 1)[1].strip()
    raise GatewayError(
        "UPB_API_KEY bulunamadi. Ortam degiskeni tanimla ya da ~/.config/aiw/env icine yaz."
    )


def _istek(yol, govde=None, zaman_asimi=180):
    url = f"{BASE}{yol}"
    veri = json.dumps(govde).encode() if govde is not None else None
    req = urllib.request.Request(url, data=veri, method="POST" if veri else "GET")
    req.add_header("Authorization", f"Bearer {anahtar()}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=zaman_asimi, context=_CTX) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        detay = e.read().decode()[:300]
        raise GatewayError(f"HTTP {e.code}: {detay}") from None
    except urllib.error.URLError as e:
        raise GatewayError(f"Gecide ulasilamadi: {e.reason}") from None


def modeller():
    return [m["id"] for m in _istek("/models")["data"]]


def _kaydet(kayit):
    klasor = RUNS / date.today().isoformat()
    klasor.mkdir(parents=True, exist_ok=True)
    ad = f"{datetime.now(timezone.utc).strftime('%H%M%S%f')}-{kayit['model'].replace('/', '_')}.json"
    (klasor / ad).write_text(json.dumps(kayit, ensure_ascii=False, indent=2))
    return klasor / ad


def sor(model, istem, sistem=None, azami_token=4000):
    """Tek turluk çağrı. Dönen: (metin, kayit). Kayit her hâlükârda diske yazılır."""
    mesajlar = ([{"role": "system", "content": sistem}] if sistem else []) + [
        {"role": "user", "content": istem}
    ]
    kayit = {
        "zaman": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "istem_ozeti": hashlib.sha256(istem.encode()).hexdigest()[:16],
        "istem_karakter": len(istem),
    }
    t0 = time.time()
    try:
        c = _istek(
            "/chat/completions",
            {"model": model, "messages": mesajlar, "max_completion_tokens": azami_token},
        )
    except GatewayError as e:
        kayit.update(sonuc="hata", hata=str(e)[:300], saniye=round(time.time() - t0, 2))
        _kaydet(kayit)
        raise
    kullanim = c.get("usage") or {}
    kayit.update(
        sonuc="tamam",
        saniye=round(time.time() - t0, 2),
        token_giris=kullanim.get("prompt_tokens"),
        token_cikis=kullanim.get("completion_tokens"),
    )
    _kaydet(kayit)
    return c["choices"][0]["message"]["content"], kayit
