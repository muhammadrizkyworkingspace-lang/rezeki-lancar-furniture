import json, os, html

repo_dir = '/home/azureuser/rezeki-lancar-repo'

with open(os.path.join(repo_dir, 'katalog_data.json'), 'r', encoding='utf-8') as f:
    compact_data = json.load(f)

# First 16 items embedded directly in JS as fallback so clicks ALWAYS work instantly
first_16 = compact_data[:16]
first_16_json = json.dumps(first_16, ensure_ascii=False)

initial_16_html = ""
for item in first_16:
    initial_16_html += f'''
    <div class="item-card" onclick="openDetail({item['id']})">
      <div class="item-img-box">
        <img class="item-img" src="{item['img']}" alt="{html.escape(item['t'])}" loading="lazy" decoding="async" />
      </div>
      <div class="item-body">
        <div>
          <div class="item-cat">{html.escape(item['c'])}</div>
          <div class="item-name">{html.escape(item['t'])}</div>
          <div class="item-dim">📐 {html.escape(item['d'])}</div>
        </div>
        <div class="item-foot">
          <span class="item-price">{item['p']}</span>
          <span class="item-read">Detail &amp; Custom →</span>
        </div>
      </div>
    </div>
    '''

responsive_ultra_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover" />
  <title>Rezeki Lancar — Bengkel Mebel Kayu Solid & Mitra Produksi Interior Jepara</title>
  <meta name="description" content="Bengkel kayu keluarga di Jepara. Mitra eksekusi produksi mebel custom kayu solid kiln-dried untuk arsitek, desainer interior, dan proyek residensial mewah." />
  <style>
    /* Native App-Like Mobile Responsiveness. Zero Tap Lag. Zero Layout Shift. */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}
    
    :root {{
      --bg: #f9f7f4;
      --card-bg: #ffffff;
      --text: #1a1816;
      --text-muted: #6b6661;
      --border: #e3ded8;
      --accent: #78350f;
      --wood-dark: #24201d;
      --font-serif: "Iowan Old Style", "Apple Garamond", Baskerville, "Times New Roman", serif;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}

    html, body {{
      width: 100%;
      overflow-x: hidden;
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      touch-action: manipulation;
    }}

    a {{ color: inherit; text-decoration: none; }}
    button {{ font-family: inherit; cursor: pointer; border: none; background: none; touch-action: manipulation; }}
    img {{ max-width: 100%; height: auto; display: block; }}

    .wrap {{
      width: 100%;
      max-width: 1140px;
      margin: 0 auto;
      padding: 0 16px;
    }}
    @media (min-width: 640px) {{
      .wrap {{ padding: 0 24px; }}
    }}

    /* Top Announcement Bar */
    .topbar {{
      background: #361e0f;
      color: #fef3c7;
      font-size: 10px;
      font-weight: 500;
      text-align: center;
      padding: 6px 12px;
      letter-spacing: 0.3px;
      line-height: 1.35;
    }}
    @media (min-width: 640px) {{
      .topbar {{ font-size: 11px; padding: 7px 16px; }}
    }}

    /* Navigation */
    nav {{
      border-bottom: 1px solid var(--border);
      background: rgba(249, 247, 244, 0.98);
      position: sticky;
      top: 0;
      z-index: 40;
      width: 100%;
      backdrop-filter: blur(8px);
    }}
    .nav-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 52px;
    }}
    @media (min-width: 640px) {{
      .nav-bar {{ height: 64px; }}
    }}
    .brand-mark {{
      font-family: var(--font-serif);
      font-size: 17px;
      font-weight: 700;
      letter-spacing: -0.5px;
      color: var(--text);
      line-height: 1.1;
    }}
    @media (min-width: 640px) {{
      .brand-mark {{ font-size: 20px; }}
    }}
    .brand-sub {{
      font-size: 9px;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-top: 1px;
    }}
    .nav-links {{
      display: flex;
      gap: 12px;
      align-items: center;
    }}
    @media (min-width: 768px) {{
      .nav-links {{ gap: 20px; }}
    }}
    .nav-item-link {{
      display: none;
      font-size: 13px;
      font-weight: 500;
      color: var(--text-muted);
    }}
    @media (min-width: 768px) {{
      .nav-item-link {{ display: inline-block; }}
    }}
    .nav-item-link:hover {{ color: var(--text); }}

    .btn-contact {{
      border: 1px solid var(--text);
      padding: 6px 12px;
      border-radius: 2px;
      font-size: 10px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      font-weight: 700;
      white-space: nowrap;
      transition: all 0.15s ease;
    }}
    .btn-contact:active {{
      background: var(--text);
      color: #fff !important;
      transform: scale(0.96);
    }}
    @media (min-width: 640px) {{
      .btn-contact {{ padding: 7px 16px; font-size: 11px; }}
      .btn-contact:hover {{ background: var(--text); color: #fff !important; }}
    }}

    /* Hero */
    .hero {{
      padding: 28px 0 24px;
      border-bottom: 1px solid var(--border);
    }}
    @media (min-width: 640px) {{
      .hero {{ padding: 56px 0 40px; }}
    }}
    .hero-label {{
      font-size: 10px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 10px;
    }}
    .hero-title {{
      font-family: var(--font-serif);
      font-size: 23px;
      font-weight: 400;
      line-height: 1.25;
      letter-spacing: -0.4px;
      color: var(--text);
      margin-bottom: 12px;
    }}
    @media (min-width: 640px) {{
      .hero-title {{
        font-size: clamp(28px, 4vw, 44px);
        letter-spacing: -0.8px;
        margin-bottom: 16px;
      }}
    }}
    .hero-title em {{
      font-style: italic;
      font-family: var(--font-serif);
    }}
    .hero-lead {{
      font-size: 13px;
      line-height: 1.65;
      color: var(--text-muted);
    }}
    @media (min-width: 640px) {{
      .hero-lead {{ font-size: 15px; max-width: 660px; }}
    }}

    /* Workshop Standards Strip */
    .specs-strip {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      padding: 18px 0;
      border-bottom: 1px solid var(--border);
    }}
    @media (min-width: 768px) {{
      .specs-strip {{ grid-template-columns: repeat(4, 1fr); gap: 20px; padding: 28px 0; }}
    }}
    .spec-item {{
      border-left: 2px solid var(--text);
      padding-left: 10px;
    }}
    .spec-num {{
      font-family: var(--font-serif);
      font-size: 17px;
      font-weight: 700;
      color: var(--text);
      line-height: 1.1;
    }}
    @media (min-width: 640px) {{
      .spec-num {{ font-size: 22px; }}
    }}
    .spec-label {{
      font-size: 9px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      margin-top: 3px;
      line-height: 1.25;
    }}
    @media (min-width: 640px) {{
      .spec-label {{ font-size: 10px; letter-spacing: 0.8px; }}
    }}

    /* Company Profile & Philosophy (Mobile-Optimized Editorial Card) */
    .section-about {{
      padding: 24px 0 32px;
      border-bottom: 1px solid var(--border);
    }}
    @media (min-width: 640px) {{
      .section-about {{ padding: 48px 0 56px; }}
    }}
    .about-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 20px 16px;
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
    }}
    @media (min-width: 860px) {{
      .about-card {{
        grid-template-columns: 1.25fr 1fr;
        padding: 36px 32px;
        gap: 36px;
        align-items: start;
      }}
    }}
    .about-h {{
      font-family: var(--font-serif);
      font-size: 19px;
      line-height: 1.35;
      margin: 6px 0 12px;
      color: var(--text);
    }}
    @media (min-width: 640px) {{
      .about-h {{ font-size: 25px; margin: 8px 0 16px; }}
    }}
    .about-lead {{
      font-size: 13px;
      line-height: 1.7;
      color: var(--text-muted);
      margin-bottom: 10px;
    }}
    .about-sub {{
      font-size: 13px;
      line-height: 1.7;
      color: var(--text);
      margin-bottom: 16px;
    }}
    .about-points {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 14px;
      padding-top: 14px;
      border-top: 1px solid #f2ede8;
    }}
    .point-item {{
      display: flex;
      gap: 8px;
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    .point-icon {{
      color: #15803d;
      font-weight: 800;
      font-size: 13px;
      flex-shrink: 0;
    }}
    
    .pillar-box {{
      background: #faf8f5;
      border: 1px solid var(--border);
      padding: 16px;
      border-radius: 4px;
    }}
    @media (min-width: 640px) {{
      .pillar-box {{ padding: 22px; }}
    }}
    .pillar-title {{
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-weight: 700;
      margin-bottom: 12px;
      color: var(--text);
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
    }}
    .pillar-list {{
      list-style: none;
    }}
    .pillar-list li {{
      padding: 8px 0;
      border-bottom: 1px solid #eeebe6;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}
    @media (min-width: 480px) {{
      .pillar-list li {{
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
      }}
    }}
    .pillar-list li:last-child {{ border-bottom: none; }}
    .p-label {{
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      font-weight: 600;
    }}
    .p-val {{
      font-size: 12px;
      font-weight: 700;
      color: var(--text);
      line-height: 1.3;
    }}
    @media (min-width: 480px) {{
      .p-val {{ text-align: right; }}
    }}

    /* Full 500-Item Catalog Section */
    .section-catalog {{
      padding: 32px 0;
    }}
    @media (min-width: 640px) {{
      .section-catalog {{ padding: 56px 0; }}
    }}
    .catalog-head {{
      margin-bottom: 14px;
    }}
    .catalog-title {{
      font-family: var(--font-serif);
      font-size: 22px;
      letter-spacing: -0.5px;
    }}
    @media (min-width: 640px) {{
      .catalog-title {{ font-size: 28px; }}
    }}
    .catalog-sub {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 4px;
    }}

    .search-box {{
      width: 100%;
      padding: 10px 14px;
      font-size: 13px;
      border: 1px solid var(--border);
      background: #ffffff;
      border-radius: 4px;
      outline: none;
      margin: 12px 0 10px;
      -webkit-appearance: none;
    }}
    @media (min-width: 640px) {{
      .search-box {{ padding: 12px 16px; font-size: 14px; margin: 16px 0 12px; }}
    }}
    .search-box:focus {{ border-color: var(--text); }}

    .cat-bar {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 6px;
      white-space: nowrap;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }}
    .cat-bar::-webkit-scrollbar {{ display: none; }}

    .cat-btn {{
      font-size: 10px;
      font-weight: 600;
      padding: 6px 12px;
      border: 1px solid var(--border);
      background: #ffffff;
      border-radius: 20px;
      color: var(--text-muted);
      flex-shrink: 0;
    }}
    .cat-btn:active {{ transform: scale(0.95); }}
    @media (min-width: 640px) {{
      .cat-btn {{ font-size: 11px; padding: 6px 14px; }}
    }}
    .cat-btn.active {{
      background: var(--text);
      color: #ffffff;
      border-color: var(--text);
    }}

    .meta-bar {{
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      color: var(--text-muted);
      margin: 12px 0;
    }}

    /* Product Grid */
    .product-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }}
    @media (min-width: 640px) {{
      .product-grid {{ gap: 14px; }}
    }}
    @media (min-width: 768px) {{
      .product-grid {{ grid-template-columns: repeat(3, 1fr); gap: 18px; }}
    }}
    @media (min-width: 1024px) {{
      .product-grid {{ grid-template-columns: repeat(4, 1fr); gap: 20px; }}
    }}

    .item-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      cursor: pointer;
      border-radius: 2px;
      transition: transform 0.1s ease, border-color 0.15s;
    }}
    .item-card:active {{
      transform: scale(0.97);
    }}
    @media (hover: hover) {{
      .item-card:hover {{
        border-color: var(--text);
        transform: translateY(-2px);
      }}
    }}
    .item-img-box {{
      aspect-ratio: 1/1;
      background: #f0ece6;
      overflow: hidden;
      width: 100%;
    }}
    .item-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .item-body {{
      padding: 8px 10px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    @media (min-width: 640px) {{
      .item-body {{ padding: 12px 14px; }}
    }}
    .item-cat {{
      font-size: 8px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--accent);
    }}
    @media (min-width: 640px) {{
      .item-cat {{ font-size: 9px; letter-spacing: 0.8px; }}
    }}
    .item-name {{
      font-family: var(--font-serif);
      font-size: 12px;
      font-weight: 600;
      line-height: 1.25;
      margin: 3px 0 4px;
      color: var(--text);
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    @media (min-width: 640px) {{
      .item-name {{ font-size: 14px; line-height: 1.3; margin: 4px 0 6px; }}
    }}
    .item-dim {{
      font-size: 10px;
      color: var(--text-muted);
      line-height: 1.2;
    }}
    @media (min-width: 640px) {{
      .item-dim {{ font-size: 11px; }}
    }}
    .item-foot {{
      margin-top: 6px;
      padding-top: 6px;
      border-top: 1px solid #f4f0eb;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 10px;
    }}
    @media (min-width: 640px) {{
      .item-foot {{ margin-top: 10px; padding-top: 8px; font-size: 11px; }}
    }}
    .item-price {{
      font-weight: 700;
      color: var(--text);
      font-size: 10px;
    }}
    @media (min-width: 640px) {{
      .item-price {{ font-size: 11px; }}
    }}
    .item-read {{
      font-size: 9px;
      font-weight: 700;
      color: var(--accent);
      text-transform: uppercase;
    }}
    @media (min-width: 640px) {{
      .item-read {{ font-size: 10px; }}
    }}

    .btn-load {{
      display: inline-block;
      background: var(--text);
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      padding: 10px 20px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin: 20px auto 0;
    }}
    .btn-load:active {{ transform: scale(0.96); }}
    @media (min-width: 640px) {{
      .btn-load {{ padding: 12px 28px; margin: 28px auto 0; }}
    }}

    /* B2B Workflow for Architects */
    .section-flow {{
      background: var(--wood-dark);
      color: #ede8e3;
      padding: 40px 0;
      margin-top: 36px;
      width: 100%;
    }}
    @media (min-width: 640px) {{
      .section-flow {{ padding: 64px 0; margin-top: 56px; }}
    }}
    .flow-head {{
      text-align: center;
      max-width: 660px;
      margin: 0 auto 28px;
    }}
    .flow-head h3 {{
      font-family: var(--font-serif);
      font-size: 20px;
      margin-bottom: 6px;
      color: #f7f4f0;
    }}
    @media (min-width: 640px) {{
      .flow-head h3 {{ font-size: 28px; margin-bottom: 10px; }}
    }}
    .flow-head p {{ font-size: 12px; color: #a39c94; }}
    @media (min-width: 640px) {{
      .flow-head p {{ font-size: 13px; }}
    }}
    .flow-steps {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }}
    @media (min-width: 640px) {{
      .flow-steps {{ grid-template-columns: repeat(2, 1fr); gap: 16px; }}
    }}
    @media (min-width: 900px) {{
      .flow-steps {{ grid-template-columns: repeat(4, 1fr); gap: 20px; }}
    }}
    .step-card {{
      border: 1px solid rgba(255,255,255,0.1);
      padding: 16px;
      border-radius: 2px;
      background: rgba(255,255,255,0.02);
    }}
    .step-num {{
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 700;
      color: #c4976c;
      margin-bottom: 4px;
    }}
    .step-name {{
      font-size: 13px;
      font-weight: 700;
      margin-bottom: 4px;
      color: #fff;
    }}
    .step-desc {{
      font-size: 11px;
      color: #a39c94;
      line-height: 1.45;
    }}

    /* Detail Modal */
    .drawer-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(20, 18, 16, 0.75);
      z-index: 100;
      align-items: flex-end;
      justify-content: center;
      backdrop-filter: blur(4px);
    }}
    .drawer-overlay.active {{ display: flex; }}
    @media (min-width: 640px) {{
      .drawer-overlay {{ align-items: center; padding: 20px; }}
    }}
    .drawer-body {{
      background: #ffffff;
      width: 100%;
      max-height: 92vh;
      overflow-y: auto;
      padding: 16px;
      border-radius: 12px 12px 0 0;
      animation: slideUp 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}
    @media (min-width: 640px) {{
      .drawer-body {{
        max-width: 580px;
        border-radius: 4px;
        padding: 24px;
        animation: fadeIn 0.2s ease-out;
      }}
    }}
    @keyframes slideUp {{
      from {{ transform: translateY(100%); }}
      to {{ transform: translateY(0); }}
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: scale(0.98); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}
    .drawer-drag-bar {{
      width: 36px;
      height: 4px;
      background: #d6d3d1;
      border-radius: 2px;
      margin: 0 auto 12px;
    }}
    @media (min-width: 640px) {{
      .drawer-drag-bar {{ display: none; }}
    }}
    .drawer-close-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
    }}
    .btn-drawer-back {{
      font-size: 13px;
      font-weight: 700;
      color: var(--accent);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .drawer-img {{
      width: 100%;
      aspect-ratio: 1/1;
      object-fit: cover;
      background: #f0ece6;
      border-radius: 2px;
    }}
    .drawer-spec-table {{
      margin: 12px 0;
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      padding: 8px 0;
      font-size: 11px;
    }}
    @media (min-width: 640px) {{
      .drawer-spec-table {{ font-size: 12px; margin: 16px 0; padding: 12px 0; }}
    }}
    .drawer-spec-row {{
      display: flex;
      justify-content: space-between;
      padding: 3px 0;
    }}
    .drawer-btn-wa {{
      display: block;
      width: 100%;
      text-align: center;
      background: var(--text);
      color: #fff;
      padding: 13px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 14px;
      border-radius: 2px;
    }}
    .drawer-btn-wa:active {{ transform: scale(0.98); }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--border);
      padding: 32px 0 20px;
      font-size: 11px;
      color: var(--text-muted);
    }}
    @media (min-width: 640px) {{
      footer {{ padding: 48px 0 28px; font-size: 12px; }}
    }}
    .foot-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }}
    @media (min-width: 768px) {{
      .foot-grid {{ grid-template-columns: 2fr 1fr 1fr; gap: 32px; margin-bottom: 32px; }}
    }}
    .foot-h {{
      font-size: 10px;
      letter-spacing: 1px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 6px;
    }}
  </style>
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="topbar">
    JEPARA WOODWORKS • KAYU OVEN KILN-DRIED (MC &lt; 12%) • TERIMA GAMBAR KERJA CAD / 3D
  </div>

  <!-- Header -->
  <nav>
    <div class="wrap nav-bar">
      <div>
        <div class="brand-mark">Rezeki Lancar</div>
        <div class="brand-sub">Bengkel Mebel Kayu Jepara</div>
      </div>
      <div class="nav-links">
        <a href="#tentang" class="nav-item-link">Tentang Bengkel</a>
        <a href="#katalog" class="nav-item-link">Katalog (500)</a>
        <a href="#kerjasama" class="nav-item-link">Mitra Arsitek</a>
        <a href="https://wa.me/6281234567890?text=Halo%20Rezeki%20Lancar%2C%20saya%20mau%20konsultasi%20produksi%20mebel" target="_blank" class="btn-contact">Konsultasi WA</a>
      </div>
    </div>
  </nav>

  <!-- Hero Statement -->
  <section class="hero">
    <div class="wrap">
      <div class="hero-label">Atelier Mebel Solid • Est. Jepara</div>
      <h1 class="hero-title">
        Menerjemahkan visi arsitek ke dalam <em>ketulusan kayu solid</em> dengan presisi tangan pengrajin Jepara.
      </h1>
      <p class="hero-lead">
        Rezeki Lancar adalah bengkel mebel keluarga di Jepara. Kami mengerjakan loose furniture dan custom carpentry kayu oven kiln-dried untuk proyek arsitektur, residensial, villa, dan cafe.
      </p>
    </div>
  </section>

  <!-- Workshop Standards Strip -->
  <section class="wrap">
    <div class="specs-strip">
      <div class="spec-item">
        <div class="spec-num">&lt; 12% MC</div>
        <div class="spec-label">Kiln-Dried Oven Moisture</div>
      </div>
      <div class="spec-item">
        <div class="spec-num">Mortise &amp; Tenon</div>
        <div class="spec-label">Konstruksi Pasak Tradisional</div>
      </div>
      <div class="spec-item">
        <div class="spec-num">Jati &amp; Mindi</div>
        <div class="spec-label">Kayu Legal Perhutani Terkurasi</div>
      </div>
      <div class="spec-item">
        <div class="spec-num">1x24 Jam</div>
        <div class="spec-label">Estimasi RAB Gambar CAD / 3D</div>
      </div>
    </div>
  </section>

  <!-- Company Profile & Philosophy (Mobile-Optimized Editorial Card) -->
  <section class="section-about wrap" id="tentang">
    <div class="about-card">
      <div class="about-main">
        <span class="hero-label">Profil Perusahaan &amp; Etos Kerja</span>
        <h2 class="about-h">Bukan makelar retail. Kami bertumpu pada kayu yang benar dan tukang yang terlatih.</h2>
        
        <p class="about-lead">
          Banyak proyek interior kecewa dengan mebel asal Jepara akibat kayu basah yang melengkung setelah 3 bulan di ruang ber-AC, sambungan yang hanya dipaku tembak, serta komunikasi bengkel yang tidak disiplin membaca gambar kerja arsitektur.
        </p>

        <p class="about-sub">
          <strong>Rezeki Lancar</strong> didirikan untuk menjembatani kesenjangan tersebut. Kami mengawinkan keahlian tangan tradisional ukir &amp; pasak kayu Jepara dengan kontrol mutu modern: kayu oven kering terukur (MC &lt; 12%), pelaporan progres bertahap, dan kepatuhan dimensi gambar kerja AutoCAD maupun 3D SketchUp.
        </p>

        <div class="about-points">
          <div class="point-item">
            <span class="point-icon">✓</span>
            <div><strong>Kayu Oven Terukur:</strong> Standar oven kiln-dried garansi MC &lt; 12% anti-retak di ruang ber-AC.</div>
          </div>
          <div class="point-item">
            <span class="point-icon">✓</span>
            <div><strong>Konstruksi Pasak Tradisional:</strong> Sambungan purus (mortise &amp; tenon) kokoh tanpa paku tembak ringkih.</div>
          </div>
          <div class="point-item">
            <span class="point-icon">✓</span>
            <div><strong>Presisi Gambar Kerja:</strong> Dikerjakan patuh dimensi AutoCAD &amp; 3D SketchUp arsitek.</div>
          </div>
        </div>
      </div>

      <div class="pillar-box">
        <div class="pillar-title">Standar Spesifikasi Bengkel</div>
        <ul class="pillar-list">
          <li>
            <span class="p-label">Material Baku</span>
            <span class="p-val">Kayu Jati Solid, Mindi, Mahoni, Rotan</span>
          </li>
          <li>
            <span class="p-label">Perlakuan Kayu</span>
            <span class="p-val">Chemical Anti-Rayap &amp; Kiln-Dried</span>
          </li>
          <li>
            <span class="p-label">Standar Finishing</span>
            <span class="p-val">Polyurethane (PU), NC Matte, Oil</span>
          </li>
          <li>
            <span class="p-label">Kapasitas Proyek</span>
            <span class="p-val">Residensial, Cafe, Villa Bali</span>
          </li>
          <li>
            <span class="p-label">Proteksi Kargo</span>
            <span class="p-val">Packing Peti Palet Kayu Tertutup</span>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Complete 500 Product Catalog Section -->
  <section class="section-catalog wrap" id="katalog">
    <div class="catalog-head">
      <div class="hero-label">Arsip Lengkap Koleksi</div>
      <h2 class="catalog-title">Katalog 500 Karya Mebel Kayu Solid</h2>
      <p class="catalog-sub">Setiap karya memiliki deskripsi fungsional unik dan dapat dikustomisasi dimensi, jenis kayu, maupun warnanya.</p>
    </div>

    <!-- Search Box -->
    <input type="text" id="searchInput" class="search-box" placeholder="Ketik nama produk atau ukuran (contoh: meja kerja, sofa, bench, credenza, cermin)..." />

    <!-- Category Pills -->
    <div class="cat-bar">
      <button class="cat-btn active" onclick="filterCat('Semua')">Semua (500)</button>
      <button class="cat-btn" onclick="filterCat('Kursi & Sofa')">Kursi &amp; Sofa</button>
      <button class="cat-btn" onclick="filterCat('Meja & Konsol')">Meja &amp; Konsol</button>
      <button class="cat-btn" onclick="filterCat('Lemari & Storage')">Lemari &amp; Storage</button>
      <button class="cat-btn" onclick="filterCat('Rak & Display')">Rak &amp; Display</button>
      <button class="cat-btn" onclick="filterCat('Cermin & Dekorasi')">Cermin &amp; Dekorasi</button>
    </div>

    <div class="meta-bar">
      <div>Menampilkan <strong id="shownCount" style="color:var(--text);">16</strong> dari <span id="matchCount">500</span> karya</div>
      <div>*Tap kartu mana saja untuk membaca spesifikasi detail</div>
    </div>

    <div class="product-grid" id="grid">{initial_16_html}</div>

    <div style="text-align:center;">
      <button id="loadMoreBtn" class="btn-load" onclick="loadMore()">Muat 20 Karya Berikutnya ↓</button>
    </div>
  </section>

  <!-- B2B Workflow for Architects -->
  <section class="section-flow" id="kerjasama">
    <div class="wrap">
      <div class="flow-head">
        <div class="hero-label" style="color: #c4976c;">Alur Kerja Sama Mitra</div>
        <h3>Bagaimana Kami Bekerja Bersama Arsitek &amp; Desainer Interior</h3>
        <p>Sistematis, transparan, dan terukur agar proyek Anda selesai tepat waktu dengan kualitas yang disetujui klien Anda.</p>
      </div>

      <div class="flow-steps">
        <div class="step-card">
          <div class="step-num">01</div>
          <div class="step-name">Kirim Gambar Kerja</div>
          <div class="step-desc">Kirimkan file PDF, AutoCAD, atau 3D SketchUp denah furniture ruangan proyek Anda via WhatsApp atau email.</div>
        </div>

        <div class="step-card">
          <div class="step-num">02</div>
          <div class="step-name">RAB &amp; Sampel Kayu</div>
          <div class="step-desc">Kami hitung penawaran harga workshop tangan pertama dalam 1x24 jam dan siapkan sampel finishing jika dibutuhkan.</div>
        </div>

        <div class="step-card">
          <div class="step-num">03</div>
          <div class="step-name">Laporan Progres Fisik</div>
          <div class="step-desc">Kami kirimkan dokumentasi foto &amp; video di setiap fase: pemilihan kayu, assembling mentah, hingga proses finishing.</div>
        </div>

        <div class="step-card">
          <div class="step-num">04</div>
          <div class="step-name">QC &amp; Palet Kargo</div>
          <div class="step-desc">Pemeriksaan ketat kadar air dan kehalusan sebelum dibungkus kardus tebal dan peti palet kayu menuju lokasi proyek.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="wrap foot-grid">
      <div>
        <div class="brand-mark" style="font-size: 16px; margin-bottom: 4px;">Rezeki Lancar Furniture</div>
        <p style="line-height: 1.6;">
          Bengkel pengerjaan mebel kayu solid &amp; mitra manufaktur desainer interior. Berakar dari tradisi pertukangan kayu Jepara, Jawa Tengah.
        </p>
      </div>
      <div>
        <div class="foot-h">Workshop &amp; Studio</div>
        <p>Jepara, Jawa Tengah<br>Indonesia</p>
        <p style="margin-top: 6px;">Kunjungan workshop dengan perjanjian.</p>
      </div>
      <div>
        <div class="foot-h">Kontak Proyek</div>
        <p>WhatsApp: +62 812-3456-7890</p>
        <p>Email: proyek@rezekilancar.id</p>
      </div>
    </div>
    <div class="wrap" style="border-top: 1px solid var(--border); padding-top: 16px; text-align: center; font-size: 10px;">
      &copy; 2026 Rezeki Lancar Furniture. All rights reserved.
    </div>
  </footer>

  <!-- Detail Modal -->
  <div class="drawer-overlay" id="drawer" onclick="if(event.target===this)closeDetail()">
    <div class="drawer-body">
      <div class="drawer-drag-bar"></div>
      <div>
        <div class="drawer-close-bar">
          <button class="btn-drawer-back" onclick="closeDetail()">✕ Tutup Detail</button>
          <span style="font-size:10px; color:#78716c;" id="dId"></span>
        </div>

        <img id="dImg" class="drawer-img" src="" alt="" />
        
        <div style="margin-top:12px;">
          <div style="font-size:9px; font-weight:700; text-transform:uppercase; color:var(--accent);" id="dCat"></div>
          <h2 style="font-family:var(--font-serif); font-size:19px; font-weight:600; margin:3px 0 4px;" id="dTitle"></h2>
          <div style="font-size:16px; font-weight:800; color:var(--accent);" id="dPrice"></div>
        </div>

        <div class="drawer-spec-table">
          <div class="drawer-spec-row">
            <span style="color:#78716c;">Dimensi (P×L×T)</span>
            <span style="font-weight:600;" id="dDim"></span>
          </div>
          <div class="drawer-spec-row">
            <span style="color:#78716c;">Material Bahan</span>
            <span style="font-weight:600;" id="dMat"></span>
          </div>
          <div class="drawer-spec-row">
            <span style="color:#78716c;">Jenis Finishing</span>
            <span style="font-weight:600;" id="dFin"></span>
          </div>
          <div class="drawer-spec-row">
            <span style="color:#78716c;">Konstruksi Pasak</span>
            <span style="font-weight:600;" id="dKon"></span>
          </div>
        </div>

        <p style="font-size:12px; color:#57534e; line-height:1.65;" id="dDesc"></p>
      </div>

      <div>
        <a id="dWa" href="#" target="_blank" class="drawer-btn-wa">Konsultasikan Karya Ini via WhatsApp →</a>
        <div style="text-align:center; margin-top:8px;">
          <a id="dLinkFull" href="#" target="_blank" style="font-size:10px; color:#78716c; text-decoration:underline;">Buka link halaman terpisah →</a>
        </div>
      </div>
    </div>
  </div>

  <!-- Ultra-lightweight Async Catalog Engine -->
  <script>
    const initialItems = {first_16_json};
    let fullCatalog = initialItems;
    let currentCat = 'Semua';
    let searchQuery = '';
    let currentPage = 1;
    const pageSize = 20;
    let filteredList = [];

    const grid = document.getElementById('grid');
    const shownCount = document.getElementById('shownCount');
    const matchCount = document.getElementById('matchCount');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const searchInput = document.getElementById('searchInput');

    // Quietly fetch remaining catalog in background after page is visible
    fetch('./katalog_data.json')
      .then(res => res.json())
      .then(data => {{
        fullCatalog = data;
        checkUrlHash();
      }})
      .catch(err => console.log('Catalog load error', err));

    function applyFilter() {{
      if (fullCatalog.length === 0) return;
      filteredList = fullCatalog.filter(item => {{
        const matchC = (currentCat === 'Semua') || (item.c === currentCat);
        const matchQ = (searchQuery === '') || 
                       item.t.toLowerCase().includes(searchQuery) || 
                       (item.d && item.d.toLowerCase().includes(searchQuery));
        return matchC && matchQ;
      }});
      currentPage = 1;
      render();
    }}

    function render() {{
      const limit = currentPage * pageSize;
      const visible = filteredList.slice(0, limit);

      grid.innerHTML = '';
      visible.forEach(item => {{
        const card = document.createElement('div');
        card.className = 'item-card';
        card.onclick = () => openDetail(item.id);
        card.innerHTML = `
          <div class="item-img-box">
            <img class="item-img" src="${{item.img}}" alt="${{item.t}}" loading="lazy" decoding="async" />
          </div>
          <div class="item-body">
            <div>
              <div class="item-cat">${{item.c}}</div>
              <div class="item-name">${{item.t}}</div>
              <div class="item-dim">📐 ${{item.d}}</div>
            </div>
            <div class="item-foot">
              <span class="item-price">${{item.p}}</span>
              <span class="item-read">Detail →</span>
            </div>
          </div>
        `;
        grid.appendChild(card);
      }});

      shownCount.innerText = visible.length;
      matchCount.innerText = filteredList.length;

      if (limit >= filteredList.length) {{
        loadMoreBtn.style.display = 'none';
      }} else {{
        loadMoreBtn.style.display = 'inline-block';
        loadMoreBtn.innerText = `Muat ${{Math.min(pageSize, filteredList.length - limit)}} Karya Berikutnya ↓`;
      }}
    }}

    function loadMore() {{
      if (fullCatalog.length === 0) return;
      currentPage++;
      render();
    }}

    function filterCat(c) {{
      currentCat = c;
      document.querySelectorAll('.cat-btn').forEach(btn => {{
        btn.classList.toggle('active', btn.innerText.includes(c));
      }});
      applyFilter();
    }}

    searchInput.addEventListener('input', e => {{
      searchQuery = e.target.value.toLowerCase().trim();
      applyFilter();
    }});

    // Detail Modal Logic (Instant, Works on Millisecond 0)
    function openDetail(id) {{
      const item = fullCatalog.find(x => x.id === id) || initialItems.find(x => x.id === id) || {{}};
      if (!item.t) return;

      document.getElementById('dId').innerText = 'Koleksi #' + item.id;
      document.getElementById('dImg').src = item.img;
      document.getElementById('dCat').innerText = item.c;
      document.getElementById('dTitle').innerText = item.t;
      document.getElementById('dPrice').innerText = item.p;
      document.getElementById('dDim').innerText = item.d;
      document.getElementById('dMat').innerText = item.m;
      document.getElementById('dFin').innerText = item.f;
      document.getElementById('dKon').innerText = item.k || 'Mortise & Tenon Pasak Kayu';
      document.getElementById('dDesc').innerText = item.desc;
      
      const msg = encodeURIComponent(`Halo Rezeki Lancar Furniture, saya tertarik dengan karya ${{item.t}} (${{item.d}}). Mohon info penawaran harga & opsi kayu.`);
      document.getElementById('dWa').href = `https://wa.me/6281234567890?text=${{msg}}`;
      document.getElementById('dLinkFull').href = './' + item.url;

      document.getElementById('drawer').classList.add('active');
      window.history.pushState({{ id: item.id }}, '', '#item-' + item.id);
    }}

    function closeDetail() {{
      document.getElementById('drawer').classList.remove('active');
      if (window.location.hash.startsWith('#item-')) {{
        window.history.pushState('', '', window.location.pathname);
      }}
    }}

    window.addEventListener('popstate', (e) => {{
      if (document.getElementById('drawer').classList.contains('active')) {{
        document.getElementById('drawer').classList.remove('active');
      }}
    }});

    function checkUrlHash() {{
      const hash = window.location.hash;
      if (hash && hash.startsWith('#item-')) {{
        const id = parseInt(hash.replace('#item-', ''));
        if (id) openDetail(id);
      }}
    }}
  </script>
</body>
</html>'''

with open(os.path.join(repo_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(responsive_ultra_html)

print("Generated mobile-optimized index.html successfully!")
