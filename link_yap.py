# Panel linki üretir. Kullanım: python link_yap.py
import json, zlib, base64

ADRES = "https://KULLANICIADIN.github.io/panel/"  # <-- kendi adresini yaz

def link(veri):
    ham = json.dumps(veri, ensure_ascii=False).encode("utf-8")
    c = zlib.compressobj(9, zlib.DEFLATED, -15)
    sik = c.compress(ham) + c.flush()
    return ADRES + "#k=" + base64.urlsafe_b64encode(sik).decode().rstrip("=")

if __name__ == "__main__":
    ornek = {
        "ad": "Semih",
        "gorevler": [{"m": "Instagram için 3 görsel hazırla", "b": False}],
        "notlar": [{"m": "Müşteri logoyu pazartesi bekliyor", "t": "22.11"}],
        "projeler": [{"ad": "Instagram sayfası", "durum": "içerik planı", "yuzde": 30}],
        "para": [{"m": "Logo işi", "k": 1500, "t": "21.11"}],
    }
    print(link(ornek))
