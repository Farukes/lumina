<div align="center">

# ⚡ LUMINA
### The Generative Frontend Engine & Automated MCP for AI Developers
**Linear · Apple · Vercel · Stripe · Teenage Engineering Tier Standards**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-cyan.svg?style=flat-square)](https://python.org)
[![MCP Compatible](https://img.shields.io/badge/MCP-Model_Context_Protocol-purple.svg?style=flat-square)](https://modelcontextprotocol.io)
[![Zero Trace](https://img.shields.io/badge/Zero--Trace-Uninstaller-emerald.svg?style=flat-square)](#-iz-bırakmadan-kaldırma-zero-trace)
[![Design Standard](https://img.shields.io/badge/Standard-Tier_S_Luxury-orange.svg?style=flat-square)](#-9-lüks-tasarım-arketipi)

<br/>

> **Lumina**, Antigravity (AGY) ve Claude Code ile kod yazarken yapay zekanın ürettiği bayat şablonları (**mor gradyanlar, düz karanlık kartlar, çiğ fontlar**) yok eden; projenize **Linear, Apple ve Stripe kalitesinde yaşayan tasarım DNA'sı** kazandıran otonom tasarım motorudur.

---

</div>

## ⚡ Hızlı Kurulum (Global)

Lumina'yı bilgisayarınıza **tek satırla** kurun. Kurulum motoru; global CLI komutunu, PATH ortam değişkenini ve **Antigravity / Claude MCP sunucusunu otomatik olarak yapılandırır.**

### 🪟 Windows (PowerShell - Önerilen)
```powershell
irm https://raw.githubusercontent.com/Farukes/lumina/main/install.ps1 | iex
```

### 🐍 Python İle (Windows / macOS / Linux)
```bash
python -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/Farukes/lumina/main/install.py').read())"
```

### 📦 Alternatif: Repodan Doğrudan Kurulum
```bash
git clone https://github.com/Farukes/lumina.git
cd lumina
python install.py
```

> **Kurulum Ne Yapar?**
> 1. Motoru `~/.lumina/engine` dizinine yerleştirir.
> 2. `lumina` komutunu sistem PATH'ine ekler (artık her terminalde `lumina` yazabilirsiniz).
> 3. Antigravity (`~/.gemini/config/mcp_config.json`) ve Claude ayarlarına **Lumina MCP sunucusunu otomatik tanıtır** (sizdeki `tokenjar` veya diğer MCP'lere asla dokunulmaz).

---

## 🎮 Temel Komutlar (Sade & Sezgisel)

Lumina, kafa karıştırıcı parametreler yerine geliştirici odaklı **4 temel eylem** sunar:

| Komut | Eylem | Açıklama |
| :--- | :---: | :--- |
| **`lumina`** | 🎮 | **İnteraktif Kontrol Paneli**: Ok tuşlarıyla tüm işlemleri terminalden görsel olarak yönetin. |
| **`lumina on`** | 🚀 | **Projeye Enjekte Et**: Lüks tasarım anayasasını (`GEMINI.md`, `.agents/rules`) ve CSS tokenlarını enjekte eder. |
| **`lumina fix`** | ✨ | **Kodu Parlat**: Kod tabanındaki tüm mor gradyan, eksik pah ve kötü font hatalarını otomatik refactor eder. |
| **`lumina check`** | 🔍 | **Kalite Skoru**: Kod tabanınızı tarar ve 0-100 arası lüks tasarım skoru hesaplar. |
| **`lumina off`** | 🧹 | **Projeden Çıkart**: Lumina kurallarını ve tokenlarını mevcut projeden iz bırakmadan temizler. |

### 🛠️ Hızlı Yardımcılar
* `lumina theme` $\rightarrow$ 9 özgün lüks arketip arasında geçiş yapın.
* `lumina view` $\rightarrow$ Canlı interaktif vitrini (showcase) tarayıcınızda açın.
* `lumina add <blok>` $\rightarrow$ AAA kalitede yaşayan blok ekleyin (`bento-grid`, `command-bar`, `floating-dock`, `glow-hero` vb.).
* `lumina mcp` $\rightarrow$ Model Context Protocol stdio sunucusunu başlatır (veya `lumina mcp -i` ile yeniden kaydeder).

---

## 🧠 Akıllı Asistan Tespiti (Sıfır Çöp Dosya)

Lumina, geliştiricinin bilgisayarındaki araçları otomatik olarak tarar:
* **Yalnızca Antigravity (AGY) kuruluysa:** Sadece `GEMINI.md` ve `.agents/rules` dosyaları oluşturulur. Bilgisayarınızda bulunmayan Claude Code için **`CLAUDE.md` veya `.claude/` gibi gereksiz çöp dosyalar ASLA açılmaz.**
* **Claude Code kuruluysa:** Claude Code uyumlu direktifler eklenir.
* Manuel seçim yapmak isterseniz:
  ```bash
  lumina on --ai agy      # Sadece Antigravity için
  lumina on --ai claude   # Sadece Claude Code için
  lumina on --ai both     # Her ikisi için
  ```

---

## 🎨 9 Lüks Tasarım Arketipi

Lumina, telif haklarından arındırılmış 9 özgün tasarım arketipi ile yapay zekanın halüsinasyon görmesini engeller:

1. **`obsidian-craft` (Linear Standartı):** Derin obsidyen zemin (`#09090b`), 1px iç metalik pah yansıması (`border-white/[0.08]`), zümrüt aksanlar.
2. **`industrial-machina` (Teenage Engineering):** Mat gri gövde (`#18181b`), dot-matrix telemetri, mekanik Safety Orange (`#ff4400`) tetikleyiciler.
3. **`liquid-spatial` (visionOS):** Çok katmanlı cam difüzyonu (`backdrop-blur-2xl`), üst kenar ışık kırılması (`border-t-white/40`), akışkan yay fiziği.
4. **`parchment-editorial` (Stripe Press):** Sıcak ham kağıt dokusu (`#fbf9f5`), Newsreader editoryal serif tipografi, 0.5px razor çizgiler.
5. **`stark-monolith` (Vercel Minimalizmi):** Keskin monokrom disiplini, Geist font eşleşmesi, 0.5px ultra-ince çerçeveler.
6. **`fintech-horizon` (Stripe SaaS):** Lacivert derinlik, mesh aurora ışıması, yumuşak izometrik derinlik.
7. **`amber-terminal` (Raycast Cyber):** Kehribar fosfor ışıması (`#f59e0b`), monospace telemetri, klavye-öncelikli kontrol.
8. **`pure-cupertino` (Apple Clean):** Pürüzsüz squircle köşeler, ferah negatif boşluk, multi-tier cam morfolojisi.
9. **`refined-brutalism`:** 2px net mürekkep kenarlıklar, 3px sıfır-bulanıklık sert gölgeler, asit yeşil aksanlar.

---

## 🤖 Model Context Protocol (MCP) Yetenekleri

Lumina, LLM'in yaratıcılığını robotlaştırmadan ona ilham veren 5 zeki MCP aracına sahiptir:

* **`synthesize_design_tokens`**: Seçilen arketipe ve yoğunluğa göre dinamik OKLCH renkleri, pah gölgeleri ve yay fizikleri üretir.
* **`get_composition_grammar`**: Kopyala-yapıştır kod vermek yerine yapay zekaya görsel hiyerarşi, asimetri kuralları ve ASCII wireframe rehberliği sunar.
* **`get_visual_primitive`**: Border Beam, Spotlight Follow, 3D Tilt ve Text Scramble gibi saf matematiksel efektleri döner.
* **`get_component_blueprint`**: Canlı telemetrili Bento Grid ve Raycast Cmd+K gibi 8 adet AAA blok sağlar.
* **`critique_ui_design`**: Yazılan kodu Baş Tasarımcı gözüyle denetler ve puanlar.

---

## 🗑️ İz Bırakmadan Kaldırma (Zero-Trace)

Lumina sisteminize asla kalıcı bağımlılıklar yüklemez, Windows Registry'e yazmaz ve arka planda çalışan daemon barındırmaz.

Kaldırmak istediğinizde tek komut yeterlidir:
```bash
lumina uninstall
```

**Temizlik Garantisi:**
* `~/.lumina` dizini tamamen silinir.
* Windows / Unix `PATH` ortam değişkeninden `lumina` çıkarılır.
* `mcp_config.json` dosyasından yalnızca `"lumina"` silinir (**diğer tüm MCP'leriniz aynen korunur**).
* Sisteminizde **0 bayt ve 0 iz** bırakır.

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında açık kaynak olarak geliştirilmektedir. Ticari ve kişisel projelerde özgürce kullanılabilir.
