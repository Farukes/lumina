# ⚡ LUMINA — Premium AI Frontend Engine & Style Polisher
> **Automated Design Linter, Style Polisher & MCP Server for AGY & Claude Code**
> *Linear · Apple · Vercel · Stripe · Raycast Standards for AI-Assisted Developers*

---

## 🎯 Vizyon: Neden Lumina?

Antigravity CLI (AGY) veya Claude Code gibi terminal tabanlı yapay zeka ajanları ile frontend geliştirirken en büyük sorun, modelin sürekli **"AI Slop" (Yapay Zeka Klişeleri)** üretmesidir:
* ❌ Standart mor/indigo gradyan butonlar (`from-purple-500 to-indigo-600`)
* ❌ 1px pah kırma (chamfer highlight) ve derinlik içermeyen düz koyu kartlar
* ❌ `tracking-tight` verilmemiş çiğ Inter fontları
* ❌ Dokunma hissi (spring physics, active scale) olmayan ölü butonlar

**Lumina**, karmaşık tarayıcı eklentileri veya hantal web kafesleri (v0, Lovable) yerine; geliştiricinin terminalinde **Prettier / ESLint sadeliğinde çalışan otomatik bir Tasarım Cilalayıcısı (Style Polisher)** ve AGY / Claude Code için **yerel bir MCP Tasarım Sunucusu** sunar.

---

## 🚀 1. Otomatik Tasarım Düzeltici: `lumina polish`

Yapay zekanın ne kadar kötü kod yazdığı fark etmez. Projenizde tek bir komut çalıştırırsınız:

```bash
# Değişiklikleri incelemek için (Dry-run):
npx lumina polish --dry-run

# Dosyaları doğrudan Linear/Apple standardına refactor etmek için:
npx lumina polish
# (veya: .\bin\lumina.bat polish)
```

### Neleri Otomatik Düzeltir?
1. **Mor/İndigo Gradyanları Temizler:** Butonları Apple/Linear tarzı beyaz hap butonlara (`bg-white shadow-[0_1px_2px_rgba(0,0,0,0.1),0_0_20px_rgba(255,255,255,0.15)] active:scale-[0.98]`) veya monokrom obsidian derinliğe dönüştürür.
2. **1px Metalik Pah Kırma (Chamfer) Ekler:** Düz kartlara `border-white/[0.08]` ve `shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]` ekleyerek metalik kenar yansıması kazandırır.
3. **Tipografiyi Sıkılaştırır:** Başlıklara otomatik olarak `tracking-tight` ekler.
4. **Butonlara Dokunma Hissi Verir:** Tıklama anında yaylanan `active:scale-[0.98]` yay fiziğini enjekte eder.

---

## 🧠 2. AGY & Claude Code MCP Sunucusu (Model Context Protocol)

Lumina, AGY ve Claude Code'a doğrudan bağlanabilen yerel bir **MCP Sunucusu** (`mcp/server.py`) barındırır.

### Kullanılabilir MCP Araçları:
* **`get_design_tokens`**: Linear, Apple, Vercel, Stripe ve Cyber temalarının OKLCH renklerini, chamfer gölgelerini ve yay parametrelerini döner.
* **`get_component_blueprint`**: Bento Grid, Command Bar (Cmd+K), Floating Dock ve Glow Hero gibi 8 adet AAA blok için hatasız üretim şablonu verir (modelin halüsinasyon görmesini engeller).
* **`audit_code_design`**: Üretilen kod parçasındaki AI-slop kusurlarını analiz edip puanlar.

### MCP Konfigürasyonu (Claude Code / AGY):
```json
{
  "mcpServers": {
    "lumina-design": {
      "command": "python",
      "args": ["C:/Users/omere/Desktop/CLI Tasarım/mcp/server.py"]
    }
  }
}
```

---

## 💻 3. CLI Komut Referansı

### `lumina init`
Projeye lüks tema değişkenlerini (`globals.css`), AGY kurallarını (`.agents/rules/frontend-premium.md`) ve Claude kurallarını (`CLAUDE.md`) tek komutla kurar.

### `lumina theme [theme-id]`
5 Dünya Standardı Tasarım Arketipi arasında geçiş yapın:
* `linear-dark`: Obsidian lüks, 1px metalik chamfer, zümrüt aksanlar.
* `apple-clean`: Cupertino camı, `backdrop-blur-2xl`, squircle köşeler.
* `vercel-mono`: Monolith minimalizm, Geist fontları, 0.5px razor hatlar.
* `stripe-saas`: Horizon mesh aurası, derin slate, yumuşak grafikler.
* `cyber-tactile`: Raycast terminalleri, kehribar fosfor, dot-matrix.

### `lumina add <component-id>`
AAA kalitesinde 8 yaşayan bloğu projeye kopyalar:
* `bento-grid`: Canlı telemetri sayacı, sparkline ve interaktif switch.
* `command-bar`: Raycast tarzı sesli klavye arama paleti (`Cmd+K`).
* `floating-dock`: iOS Dynamic Island / macOS tarzı yüzen menü.
* `glow-hero`: Difüzyonlu radial mesh ve metalik vitrin kartı.
* `magnetic-button`: Dönen border-beam ışık huzmeli buton.
* `stat-cards`: Metrik göstergeleri ve sparkline trendleri.
* `skeleton-shimmer`: Diagonal ışık huzmeli lüks yükleme iskeleti.
* `empty-state`: Kesik çizgili interaktif boş durum kartı.

### `lumina audit`
Projeyi tarar, 0-100 Tasarım Skoru hesaplar ve yapay zeka için otomatik `.lumina/ai-fix-prompt.md` üretir.

### `lumina showcase`
Tüm temaları, bento grid'i ve Web Audio mikro-ses efektlerini tarayıcınızda canlı açar.

---

## 📦 Proje Mimarisi

```
CLI Tasarım/
├── bin/
│   ├── cli.js                 # npx lumina çalıştırıcı
│   ├── lumina.bat             # Windows CMD çalıştırıcı
│   └── lumina.ps1             # PowerShell çalıştırıcı
├── lumina/
│   ├── cli.py                 # Click & Rich CLI motoru
│   └── core/
│       ├── auditor.py         # 12+ AI-slop kusurunu tarayan motor
│       ├── polisher.py        # Kodu otomatik refactor eden polisher motoru
│       ├── prompt_engine.py   # Sıfır AI-slop prompt sentezleyici
│       ├── registry.py        # 8 adet AAA blok şablonu
│       ├── rules_generator.py # AGY & Claude Code kural enjektörü
│       └── themes.py          # 5 dünya standardı lüks tema
├── mcp/
│   └── server.py              # AGY & Claude Code için stdio MCP sunucusu
├── components/blocks/         # Üretilen React/TypeScript blokları
├── showcase/
│   └── index.html             # Canlı interaktif vitrin
├── package.json               # npm / npx paketi
├── pyproject.toml             # Python paket tanımı
└── README.md                  # Dokümantasyon
```

---

**Lumina** — Karmaşa yok, kırılgan tarayıcı overlay'leri yok. Tek komutla kusursuz, yaşayan frontend mimarisi.
