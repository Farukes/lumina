# 🛸 LUMINA GHOST & CLI — Premium AI Frontend Engine
> **In-Browser AI HUD & Reverse-Agent Teleport for AGY & Claude Code**
> *Linear · Apple · Vercel · Stripe · Raycast Standards for Terminal-First Developers*

---

## 🎯 Vizyon & Problem Tanımı

Bugün **Google Antigravity CLI (AGY)** veya **Claude Code** ile frontend geliştirirken karşılaşılan en büyük işkence **"Asimetrik Alt-Tab Döngüsü"** ve **"Görsel Körlük"**tür:
1. Terminalde ajana UI kodlatırsınız.
2. `Alt + Tab` ile tarayıcıya (`localhost:3000`) geçip bakarsınız.
3. Çirkin bir mor gradyan, orantısız padding veya mobilde taşan bir grid görürsünüz.
4. Tekrar terminale dönüp görsel kusurları kelimelerle tarif etmeye çalışırsınız.
5. Bu döngü 10 kez tekrarlanır ve geliştiriciyi tüketir.

**LUMINA GHOST**, geliştiriciyi hiçbir platforma hapsetmeden, yerel terminalinde ve git reposunda tutan; ancak **tarayıcıdaki `localhost` ile terminaldeki AGY/Claude Code arasına çift yönlü köprü kuran sıfır-kurulumlu bir araçtır.**

---

## 🛸 LUMINA GHOST: Nasıl Çalışır? (Tek Komutla)

```bash
# 1. Projenizin terminalinde çalıştırın:
npx lumina-ghost
# (veya: node bin/ghost.js)
```

Tarayıcınızda (`http://localhost:3000` veya `http://localhost:3939/demo`) gezinirken:
1. Çirkin ya da düzeltilmesi gereken herhangi bir elemana **`Alt + Tık`** (Mac: `Option + Click`) yapın.
2. Elemanın etrafında zümrüt renkli 1px metalik Apple/Linear chamfer çerçevesi parlar.
3. Yanında minik **"Lumina Ghost Kapsülü"** belirir:
   * **`[✨ Linear Polish]`**: Elemana anında 1px iç ışık (chamfer), koyu obsidian zemin ve yay fiziği (`active:scale-[0.98]`) basar.
   * **`[🍏 Apple Glass]`**: Elemanı anında `backdrop-blur-2xl` ve squircle lüks cam panel yapar.
   * **`[🧹 Purge AI Slop]`**: Mor gradyanı, untracked fontu ve çiğ kenarları tek tıkla süpürür.
   * **`[📱 Fix Mobile]`**: Ekrandan taşan veya mobilde kırılan CSS'i toparlar.
   * **Mikro-Prompt Kutusu**: *"Bu kartı Stripe fatura kartı gibi yap."*
4. Kapsüldeki butona bastığınız an:
   * Lumina Ghost yerel köprü üzerinden terminaldeki **AGY / Claude Code**'a hedef elemanın dosyasını, satırını ve hesaplanmış CSS'ini fırlatır (`.agents/tasks/ghost-intent.md`).
   * **/tokenjar** MCP sunucusu (`find_symbol_global` ve `read_file_smart`) devreye girerek tam o bileşeni sıfır token israfıyla bulur.
   * AGY kodu günceller, Vite HMR 30 milisaniyede tarayıcıyı yeniler ve Apple başarı sesi (chime) duyulur!

---

## 🏗️ 4 Katmanlı Ekosistem

```
┌─────────────────────────────────────────────────────────────┐
│  1. In-Browser AI HUD (Lumina Ghost)                        │
│     Alt + Click Inspector · Instant Polish · Web Chime      │
├─────────────────────────────────────────────────────────────┤
│  2. Local Teleport Bridge (:3939 & .agents/tasks/)          │
│     AGY & Claude Code Hot-Tasking · Tokenjar MCP Synergy    │
├─────────────────────────────────────────────────────────────┤
│  3. Living Design Constitution (Rules & DNA)                │
│     .agents/rules/frontend.md  ·  CLAUDE.md  ·  SKILL.md    │
├─────────────────────────────────────────────────────────────┤
│  4. AAA Component Registry & AI-Slop Code Auditor           │
│     Bento Grid · Command Palette · Score 0-100 Auto-Fix     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Hızlı Başlangıç (Quickstart)

### 1. Çalıştırma
Projeyi doğrudan terminalden veya Windows kısayolu ile çalıştırabilirsiniz:

```bash
# Windows Batch ile
.\bin\lumina.bat --help

# veya Python ile doğrudan
python lumina/cli.py --help
```

### 2. Projenizi Premium Standartlara Hazırlayın
```bash
python lumina/cli.py init
```
Bu komut:
1. AGY için `.agents/rules/frontend-premium.md` kuralını oluşturur.
2. Claude Code için `CLAUDE.md` ve `.claude/skills/frontend-design/SKILL.md` skill'ini enjekte eder.
3. Seçtiğiniz temanın CSS değişkenlerini ve OKLCH tokenlarını `globals.css` içine yazar.

---

## 💻 CLI Komut Referansı

### `lumina theme [theme-id]`
5 Dünya Standardı Tasarım Arketipi arasında geçiş yapın:
* `linear-dark`: Obsidian lüks, 1px metalik chamfer, zümrüt/cyan aksanlar.
* `apple-clean`: Cupertino camı, `backdrop-blur-2xl`, squircle köşeler, yumuşak gölgeler.
* `vercel-mono`: Monolith minimalizm, Geist fontları, 0.5px razor keskin çizgiler.
* `stripe-saas`: Horizon mesh aurası, derin slate, yumuşak grafikler.
* `cyber-tactile`: Raycast terminalleri, kehribar fosfor, dot-matrix, mikro-sesler.

```bash
python lumina/cli.py theme linear-dark
```

---

### `lumina add <component-id>`
Yapay zekanın sıfırdan hayal etmekte zorlandığı AAA kalitesinde yaşayan blokları projenize ekler:

| Bileşen ID | Başlık | Açıklama |
| :--- | :--- | :--- |
| `bento-grid` | **Asymmetric Bento Grid** | Canlı telemetri sayacı, sparkline, interaktif switch ve chamferlar. |
| `command-bar` | **Tactile Command Bar (Cmd+K)** | Raycast tarzı klavye arama paleti ve ses efektleri. |
| `floating-dock` | **Dynamic Island Floating Dock** | iOS/macOS tarzı spring geçişli yüzen menü. |
| `glow-hero` | **Ambient Glow Hero** | Difüzyonlu mesh aurası ve metalik vitrin kartı. |
| `magnetic-button`| **Tactile Magnetic Button** | Dönen border-beam ışık huzmesi ve yay fiziği. |
| `stat-cards` | **High-Density Stat Cards** | Metrik göstergeleri, sparkline trendleri ve delta rozetleri. |
| `skeleton-shimmer`| **Ray Shimmer Skeleton** | Koyu gri yerine diagonal ışık huzmeli lüks yükleme iskeleti. |
| `empty-state` | **Tactile Empty State** | Kesik çizgili chamfer kart, interaktif buton ve kısayol rozeti. |

```bash
python lumina/cli.py add bento-grid
python lumina/cli.py add command-bar
```

---

### `lumina audit`
Projenizdeki tüm `.tsx`, `.jsx`, `.html` ve `.css` dosyalarını tarar:
* Yapay zeka klişelerini (AI slop) tespit eder.
* **0 - 100 arası "Tasarım Kalite Puanı"** ve Harf Notu (S, A, B, C, F) hesaplar.
* Otomatik olarak `.lumina/ai-fix-prompt.md` dosyasını üretir!

> **Kullanım:** Audit çalıştırdıktan sonra üretilen `.lumina/ai-fix-prompt.md` içeriğini doğrudan AGY veya Claude Code'a yapıştırın: *"Tüm AI-slop kusurlarını gider ve refactor et!"*

---

### `lumina prompt <feature>`
AGY ve Claude Code'a vermek üzere sıfır AI-slop içeren, token bazlı mimari promptlar üretir:
```bash
python lumina/cli.py prompt dashboard
python lumina/cli.py prompt landing-page
python lumina/cli.py prompt settings
python lumina/cli.py prompt pricing
```

---

### `lumina showcase`
Tüm temaları, yaşayan bento grid'i, Web Audio sentezleyicisini ve AI Audit simülatörünü tarayıcınızda canlı açar:
```bash
python lumina/cli.py showcase
```

---

## 🎨 Tasarım Anayasası (The Lumina Constitution)

Modele enjekte edilen `.agents/rules/frontend-premium.md` kuralı şu ilkeleri zorunlu kılar:
1. **1px Chamfer Highlight:** Her koyu kartta `border border-white/[0.08]` ve `shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]` uygulanır.
2. **Spring Micro-Physics:** `framer-motion` ile `stiffness: 350, damping: 25` yay eğrisi kullanılır.
3. **Typography Scale:** Başlıklarda `tracking-tight`, teknik etiketlerde `font-mono text-[11px] uppercase tracking-wider` zorunludur.
4. **Haptic & Tactile Polish:** Tüm butonlar tıklama anında `active:scale-[0.98]` ile yaylanır.

---

## 📦 Proje Yapısı

```
CLI Tasarım/
├── lumina/
│   ├── banner.py              # Zengin terminal karşılama paneli
│   ├── cli.py                 # Ana Click & Rich CLI motoru
│   └── core/
│       ├── auditor.py         # AI-slop tarayıcı ve puanlama motoru
│       ├── prompt_engine.py   # Hatasız UI prompt sentezleyici
│       ├── registry.py        # 8 adet AAA blok şablonu
│       ├── rules_generator.py # AGY & Claude Code kural enjektörü
│       └── themes.py          # 5 dünya standardı lüks tema
├── components/blocks/         # Hazır üretilen React/TypeScript blokları
├── showcase/
│   └── index.html             # Canlı interaktif vitrin (Web Audio + Temalar)
├── bin/
│   ├── lumina.bat             # Windows CMD çalıştırıcı
│   └── lumina.ps1             # PowerShell çalıştırıcı
├── pyproject.toml             # Python paket tanımı
└── README.md                  # Dokümantasyon
```

---

**Lumina CLI** — AI ile üretilen frontend'leri bir sanat eserine dönüştürün.
