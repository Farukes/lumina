# ⚡ LUMINA — World-Class Generative Frontend Engine

> **Minimalist, Autonomous & Zero-Trace Design System for AI-Assisted Developers (Antigravity & Claude Code)**
> *Linear · Apple · Vercel · Stripe · Teenage Engineering Grade Standards*

---

## ⚡ Hızlı Kurulum (GitHub Üzerinden Tek Satırda)

Lumina'yı bilgisayarınıza **tek satırla** kurabilir ve her terminalden doğrudan `lumina` yazarak kullanabilirsiniz:

### Windows (PowerShell):
```powershell
irm https://raw.githubusercontent.com/Farukes/lumina/main/install.ps1 | iex
```

### Python İle (Windows / macOS / Linux):
```bash
python -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/Farukes/lumina/main/install.py').read())"
```
*(Veya repoyu indirip doğrudan `python install.py` çalıştırabilirsiniz).*

---

## 🗑️ İz Bırakmadan Kaldırma (Zero-Trace Uninstall)

Lumina sisteminize bağımlılık veya arka plan hizmeti yüklemez, Windows Registry'e yazmaz. Bilgisayarınızdan tamamen silmek istediğinizde:

```bash
lumina uninstall
```
> **Sonuç:** `~/.lumina` klasörü, PATH değişkeni, geçici raporlar ve tüm proje kuralları anında silinir. Sisteminizde 0 bayt artık kalır.

---

## 🎮 Sadeleştirilmiş Temel Komutlar

Lumina'da kafa karıştırıcı onlarca alt komut yerine **4 temel komut** bulunur:

| Komut | Açıklama |
| :--- | :--- |
| **`lumina`** | İnteraktif kontrol panelini açar (ok tuşlarıyla seçim yapın). |
| **`lumina on`** | Projenize lüks tasarım kurallarını ve CSS değişkenlerini enjekte eder. |
| **`lumina fix`** | Kodunuzdaki tüm AI-slop (mor gradyan, eksik pah vb.) hatalarını otomatik düzeltir. |
| **`lumina check`** | Kod tabanını tarar, 0-100 arası tasarım kalitesi puanı verir. |
| **`lumina off`** | Lumina'yı mevcut projeden iz bırakmadan temizler. |

### Hızlı Yardımcılar:
* **`lumina theme`**: 9 lüks arketip arasında geçiş yapın (`obsidian-craft`, `industrial-machina`, `liquid-spatial`, `parchment-editorial`, `stark-monolith`, `fintech-horizon`, `amber-terminal`, `pure-cupertino`, `refined-brutalism`).
* **`lumina view`**: İnteraktif tasarım vitrinini tarayıcınızda açar.
* **`lumina add <blok>`**: AAA kalitesinde hazır blok kopyalar (`bento-grid`, `command-bar`, `floating-dock`, `glow-hero` vb.).
* **`lumina mcp`**: Antigravity veya Claude Code için stdio Model Context Protocol sunucusunu başlatır.

---

## 🧠 Model Context Protocol (MCP) Kurulumu

Antigravity CLI veya Claude Code ayarlarınıza (`agy.json` veya `claude_desktop_config.json`) ekleyin:

```json
{
  "mcpServers": {
    "lumina": {
      "command": "lumina",
      "args": ["mcp"]
    }
  }
}
```

---

## 📦 Proje Yapısı

```
lumina/
├── install.py             # Global Python kurulum betiği
├── install.ps1            # Windows tek satır PowerShell kurucu
├── lumina/
│   ├── cli.py             # Click & Rich CLI motoru
│   └── core/
│       ├── installer.py   # Global kurulum ve iz bırakmayan kaldırma motoru
│       ├── auditor.py     # AI-slop tarayıcı ve puanlayıcı
│       ├── polisher.py    # Otomatik kod parlatıcı ve dönüştürücü
│       ├── themes.py      # 9 adet özgün lüks tasarım arketipi
│       ├── registry.py    # AAA bileşen şablonları
│       └── rules_generator.py # AGY & Claude kural enjektörü
├── mcp/
│   └── server.py          # Model Context Protocol stdio sunucusu
├── components/blocks/     # Hazır UI bileşenleri
└── showcase/              # Canlı interaktif tasarım vitrini
```

---

**Lumina** — Karmaşa yok, arka plan süreci yok. Saf hız, sıfır iz ve dünya zirvesinde tasarım kalitesi.
