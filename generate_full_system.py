import json, os, html

repo_dir = '/home/azureuser/rezeki-lancar-repo'
prod_dir = os.path.join(repo_dir, 'produk')
os.makedirs(prod_dir, exist_ok=True)

with open(os.path.join(repo_dir, 'katalog_500.json'), 'r', encoding='utf-8') as f:
    products = json.load(f)

base_url = 'https://muhammadrizkyworkingspace-lang.github.io/rezeki-lancar-furniture'

# 1. Generate clean, high-end, zero-bloat product pages for ALL 500 products
compact_index_data = []

for idx, p in enumerate(products):
    slug = ''.join(c if c.isalnum() else '-' for c in p['nama_produk'].lower()).strip('-')
    while '--' in slug: slug = slug.replace('--', '-')
    slug = f"{idx+1:03d}-{slug[:50]}"
    
    file_rel = f"produk/{slug}.html"
    page_url = f"{base_url}/{file_rel}"
    
    compact_index_data.append({
        'id': idx + 1,
        't': p['nama_produk'],
        'c': p['kategori'],
        'p': p['harga_pasar'],
        'd': p['dimensi'],
        'm': p['material'],
        'f': p['finishing'],
        'img': p['url_gambar'],
        'url': file_rel
    })
    
    # JSON-LD Schema
    price_clean = p['harga_pasar'].replace('Rp', '').replace('.', '').strip() if 'Rp' in p['harga_pasar'] else '0'
    schema = {
        '@context': 'https://schema.org/',
        '@type': 'Product',
        'name': p['nama_produk'],
        'image': [p['url_gambar']],
        'description': p.get('deskripsi') or f"Mebel solid {p['nama_produk']} kayu oven kiln-dried dari Rezeki Lancar Furniture Jepara. Dimensi {p['dimensi']}.",
        'brand': {'@type': 'Brand', 'name': 'Rezeki Lancar Furniture'},
        'category': p['kategori'],
        'offers': {
            '@type': 'Offer',
            'priceCurrency': 'IDR',
            'price': price_clean,
            'itemCondition': 'https://schema.org/NewCondition',
            'availability': 'https://schema.org/InStock',
            'seller': {'@type': 'Organization', 'name': 'Rezeki Lancar Furniture'}
        }
    }
    
    wa_msg = f"Halo Rezeki Lancar Furniture, saya tertarik dengan karya: {p['nama_produk']} ({p['dimensi']}). Mohon informasi opsi kayu, waktu produksi, dan penawaran RAB."
    wa_link = f"https://wa.me/6281234567890?text={html.escape(wa_msg)}"

    single_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(p['nama_produk'])} — Rezeki Lancar Furniture Jepara</title>
  <meta name="description" content="Detail spesifikasi {html.escape(p['nama_produk'])}. Ukuran {html.escape(p['dimensi'])}, bahan {html.escape(p['material'])}, finishing {html.escape(p['finishing'])}. Workshop Jepara." />
  <link rel="canonical" href="{page_url}" />
  <meta property="og:title" content="{html.escape(p['nama_produk'])} | Rezeki Lancar Furniture" />
  <meta property="og:description" content="Spesifikasi & penawaran {html.escape(p['nama_produk'])}. Dimensi: {html.escape(p['dimensi'])}." />
  <meta property="og:image" content="{p['url_gambar']}" />
  <meta property="og:url" content="{page_url}" />
  <script type="application/ld+json">
  {json.dumps(schema, ensure_ascii=False)}
  </script>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #f9f7f4;
      color: #1a1816;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.6;
      padding: 0 16px 60px;
    }}
    a {{ color: inherit; text-decoration: none; }}
    .wrap {{ max-width: 960px; margin: 0 auto; }}
    
    /* Header */
    .top-nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 0;
      border-bottom: 1px solid #e3ded8;
      margin-bottom: 32px;
      font-size: 13px;
    }}
    .back-link {{
      color: #78350f;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .brand-tag {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #78716c;
    }}
    
    /* Product Layout */
    .card-detail {{
      background: #ffffff;
      border: 1px solid #e3ded8;
      border-radius: 4px;
      overflow: hidden;
      display: grid;
      grid-template-columns: 1fr;
    }}
    @media(min-width: 768px) {{
      .card-detail {{ grid-template-columns: 1.1fr 1fr; }}
    }}
    .img-box {{
      background: #f0ece6;
      aspect-ratio: 1/1;
      width: 100%;
      overflow: hidden;
    }}
    .img-box img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .info-box {{
      padding: 32px 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .cat-badge {{
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: #78350f;
    }}
    .p-title {{
      font-family: "Iowan Old Style", "Apple Garamond", Baskerville, "Times New Roman", serif;
      font-size: 26px;
      font-weight: 600;
      line-height: 1.25;
      margin: 8px 0 12px;
    }}
    .p-price {{
      font-size: 20px;
      font-weight: 700;
      color: #78350f;
      margin-bottom: 24px;
    }}
    
    /* Specs Table */
    .spec-table {{
      width: 100%;
      border-top: 1px solid #f0ede9;
      border-bottom: 1px solid #f0ede9;
      padding: 16px 0;
      margin-bottom: 20px;
      font-size: 13px;
    }}
    .spec-row {{
      display: flex;
      justify-content: space-between;
      padding: 6px 0;
      border-bottom: 1px solid #faf8f5;
    }}
    .spec-row:last-child {{ border-bottom: none; }}
    .spec-k {{ color: #78716c; }}
    .spec-v {{ font-weight: 600; text-align: right; color: #1a1816; }}
    
    .p-desc {{
      font-size: 13px;
      color: #57534e;
      line-height: 1.7;
      margin-bottom: 28px;
    }}
    
    /* CTA */
    .btn-wa {{
      display: block;
      width: 100%;
      text-align: center;
      background: #1a1816;
      color: #ffffff;
      padding: 14px;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      border-radius: 2px;
      transition: background 0.2s;
    }}
    .btn-wa:hover {{ background: #78350f; }}
    .cta-sub {{
      font-size: 11px;
      color: #a8a29e;
      text-align: center;
      margin-top: 8px;
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="top-nav">
      <a href="../" class="back-link">← Kembali ke Katalog Utama</a>
      <span class="brand-tag">Rezeki Lancar • Jepara Woodworks</span>
    </div>

    <div class="card-detail">
      <div class="img-box">
        <img src="{p['url_gambar']}" alt="{html.escape(p['nama_produk'])}" />
      </div>
      <div class="info-box">
        <div>
          <span class="cat-badge">{html.escape(p['kategori'])}</span>
          <h1 class="p-title">{html.escape(p['nama_produk'])}</h1>
          <div class="p-price">{p['harga_pasar']}</div>

          <div class="spec-table">
            <div class="spec-row">
              <span class="spec-k">Dimensi (P×L×T)</span>
              <span class="spec-v">{html.escape(p['dimensi'])}</span>
            </div>
            <div class="spec-row">
              <span class="spec-k">Material Bahan</span>
              <span class="spec-v">{html.escape(p['material'])}</span>
            </div>
            <div class="spec-row">
              <span class="spec-k">Jenis Finishing</span>
              <span class="spec-v">{html.escape(p['finishing'])}</span>
            </div>
            <div class="spec-row">
              <span class="spec-k">Berat / Volume</span>
              <span class="spec-v">{html.escape(p.get('berat', '-'))}</span>
            </div>
            <div class="spec-row">
              <span class="spec-k">Konstruksi</span>
              <span class="spec-v">{html.escape(p.get('konstruksi', 'Mortise & Tenon'))}</span>
            </div>
            <div class="spec-row">
              <span class="spec-k">Asal Produksi</span>
              <span class="spec-v">Workshop Jepara, Jawa Tengah</span>
            </div>
          </div>

          <p class="p-desc">
            {html.escape(p.get('deskripsi') or 'Dibuat secara presisi oleh pengrajin berpengalaman di Jepara dengan sistem oven kayu terukur (MC < 12%) agar tidak retak atau susut saat dipasang pada ruangan ber-AC. Ukuran, warna, dan material dapat dikustomisasi sesuai gambar kerja arsitektur.')}
          </p>
        </div>

        <div>
          <a href="{wa_link}" target="_blank" class="btn-wa">Pesan / Diskusi Custom via WhatsApp →</a>
          <div class="cta-sub">Bisa custom ukuran & warna finishing • Estimasi RAB 1x24 jam</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>'''

    with open(os.path.join(prod_dir, f"{slug}.html"), 'w', encoding='utf-8') as f:
        f.write(single_html)

print(f"Generated {len(products)} individual detail pages in /produk/")

# 2. Build index.html containing the Authentic Company Profile + 500-Item Clickable Catalog
products_json_compact = json.dumps(compact_index_data, ensure_ascii=False)

index_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rezeki Lancar — Bengkel Mebel Kayu Solid & Mitra Produksi Interior Jepara</title>
  <meta name="description" content="Bengkel kayu keluarga di Jepara. Mitra eksekusi produksi mebel custom kayu solid kiln-dried untuk arsitek, desainer interior, dan proyek residensial mewah." />
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    :root {{
      --bg: #f9f7f4;
      --card-bg: #ffffff;
      --text: #1a1816;
      --text-muted: #6b6661;
      --border: #e3ded8;
      --accent: #78350f;
      --font-serif: "Iowan Old Style", "Apple Garamond", Baskerville, "Times New Roman", "Noto Serif", serif;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}

    body {{
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}

    a {{ color: inherit; text-decoration: none; }}
    button {{ font-family: inherit; cursor: pointer; border: none; background: none; }}

    .wrap {{ max-width: 1140px; margin: 0 auto; padding: 0 20px; }}

    /* Navigation */
    nav {{
      border-bottom: 1px solid var(--border);
      background: rgba(249, 247, 244, 0.96);
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .nav-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 68px;
    }}
    .brand-mark {{
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 700;
      letter-spacing: -0.5px;
      color: var(--text);
    }}
    .brand-sub {{
      font-size: 10px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-top: -2px;
    }}
    .nav-links {{
      display: flex;
      gap: 20px;
      align-items: center;
      font-size: 13px;
      font-weight: 500;
      color: var(--text-muted);
    }}
    .nav-links a:hover {{ color: var(--text); }}
    .btn-contact {{
      border: 1px solid var(--text);
      padding: 7px 14px;
      border-radius: 2px;
      color: var(--text) !important;
      font-size: 11px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      font-weight: 700;
      transition: all 0.2s ease;
    }}
    .btn-contact:hover {{
      background: var(--text);
      color: #fff !important;
    }}

    /* Hero / Company Statement */
    .hero {{
      padding: 64px 0 48px;
      border-bottom: 1px solid var(--border);
    }}
    .hero-label {{
      font-size: 11px;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 20px;
    }}
    .hero-title {{
      font-family: var(--font-serif);
      font-size: clamp(28px, 4.5vw, 48px);
      font-weight: 400;
      line-height: 1.2;
      letter-spacing: -0.8px;
      max-width: 860px;
      color: var(--text);
      margin-bottom: 20px;
    }}
    .hero-title em {{
      font-style: italic;
      font-family: var(--font-serif);
    }}
    .hero-lead {{
      font-size: 15px;
      line-height: 1.7;
      color: var(--text-muted);
      max-width: 640px;
    }}

    /* Specs Strip */
    .specs-strip {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      padding: 32px 0;
      border-bottom: 1px solid var(--border);
    }}
    @media(min-width: 768px) {{
      .specs-strip {{ grid-template-columns: repeat(4, 1fr); }}
    }}
    .spec-item {{
      border-left: 2px solid var(--text);
      padding-left: 14px;
    }}
    .spec-num {{
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 700;
      color: var(--text);
    }}
    .spec-label {{
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--text-muted);
      margin-top: 3px;
    }}

    /* About Section */
    .section-about {{
      padding: 64px 0;
      border-bottom: 1px solid var(--border);
    }}
    .about-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 40px;
    }}
    @media(min-width: 860px) {{
      .about-grid {{ grid-template-columns: 1fr 1fr; align-items: start; }}
    }}
    .about-h {{
      font-family: var(--font-serif);
      font-size: 26px;
      line-height: 1.3;
      margin-bottom: 16px;
    }}
    .about-body p {{
      margin-bottom: 14px;
      font-size: 14px;
      line-height: 1.8;
      color: var(--text-muted);
    }}
    .pillar-box {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: 24px;
      border-radius: 4px;
    }}
    .pillar-title {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      font-weight: 700;
      margin-bottom: 16px;
      color: var(--text);
    }}
    .pillar-list li {{
      list-style: none;
      font-size: 12px;
      padding: 10px 0;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      color: var(--text-muted);
    }}
    .pillar-list li:last-child {{ border-bottom: none; }}
    .pillar-list strong {{ color: var(--text); }}

    /* Full 500-Item Catalog Section */
    .section-catalog {{
      padding: 64px 0;
    }}
    .catalog-head {{
      margin-bottom: 28px;
    }}
    .catalog-title {{
      font-family: var(--font-serif);
      font-size: 30px;
      letter-spacing: -0.5px;
    }}
    .catalog-sub {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 4px;
    }}

    /* Search & Filter Controls */
    .search-input {{
      width: 100%;
      padding: 12px 16px;
      font-size: 14px;
      border: 1px solid var(--border);
      background: #ffffff;
      border-radius: 4px;
      outline: none;
      margin: 16px 0 12px;
    }}
    .search-input:focus {{ border-color: var(--text); }}
    
    .cat-bar {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 8px;
      white-space: nowrap;
      -webkit-overflow-scrolling: touch;
    }}
    .cat-btn {{
      font-size: 11px;
      font-weight: 600;
      padding: 6px 14px;
      border: 1px solid var(--border);
      background: #ffffff;
      border-radius: 20px;
      color: var(--text-muted);
    }}
    .cat-btn.active {{
      background: var(--text);
      color: #ffffff;
      border-color: var(--text);
    }}

    .meta-bar {{
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      color: var(--text-muted);
      margin: 18px 0;
    }}

    /* Product Grid */
    .product-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
    }}
    @media(min-width: 768px) {{
      .product-grid {{ grid-template-columns: repeat(3, 1fr); gap: 20px; }}
    }}
    @media(min-width: 1024px) {{
      .product-grid {{ grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    }}

    /* Clickable Card Link */
    .item-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      border-radius: 2px;
      transition: border-color 0.2s, transform 0.2s;
    }}
    .item-card:hover {{
      border-color: var(--text);
      transform: translateY(-2px);
    }}
    .item-img-box {{
      aspect-ratio: 1/1;
      background: #f0ece6;
      overflow: hidden;
    }}
    .item-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .item-body {{
      padding: 12px 14px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .item-cat {{
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--accent);
    }}
    .item-name {{
      font-family: var(--font-serif);
      font-size: 14px;
      font-weight: 600;
      line-height: 1.3;
      margin: 4px 0 6px;
      color: var(--text);
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    .item-dim {{
      font-size: 11px;
      color: var(--text-muted);
    }}
    .item-foot {{
      margin-top: 10px;
      padding-top: 8px;
      border-top: 1px solid #f4f0eb;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
    }}
    .item-price {{
      font-weight: 700;
      color: var(--text);
    }}
    .item-read {{
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--accent);
      font-weight: 700;
    }}

    /* Load More */
    .load-more-box {{
      text-align: center;
      margin: 36px 0;
    }}
    .btn-load {{
      background: var(--text);
      color: #ffffff;
      font-size: 12px;
      font-weight: 700;
      padding: 12px 28px;
      border-radius: 2px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    /* B2B Workflow */
    .section-flow {{
      background: #24201d;
      color: #ede8e3;
      padding: 64px 0;
      margin-top: 40px;
    }}
    .flow-head {{
      text-align: center;
      max-width: 640px;
      margin: 0 auto 40px;
    }}
    .flow-head h3 {{
      font-family: var(--font-serif);
      font-size: 28px;
      margin-bottom: 8px;
      color: #f7f4f0;
    }}
    .flow-steps {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
    }}
    @media(min-width: 768px) {{
      .flow-steps {{ grid-template-columns: repeat(4, 1fr); }}
    }}
    .step-card {{
      border: 1px solid rgba(255,255,255,0.1);
      padding: 20px;
      border-radius: 2px;
    }}
    .step-num {{
      font-family: var(--font-serif);
      font-size: 24px;
      font-weight: 700;
      color: #c4976c;
      margin-bottom: 8px;
    }}
    .step-name {{
      font-size: 13px;
      font-weight: 700;
      margin-bottom: 6px;
      color: #fff;
    }}
    .step-desc {{
      font-size: 11px;
      color: #a39c94;
      line-height: 1.6;
    }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--border);
      padding: 48px 0 32px;
      font-size: 12px;
      color: var(--text-muted);
    }}
    .foot-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 28px;
      margin-bottom: 32px;
    }}
    @media(min-width: 768px) {{
      .foot-grid {{ grid-template-columns: 2fr 1fr 1fr; }}
    }}
    .foot-h {{
      font-size: 10px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 10px;
    }}
  </style>
</head>
<body>

  <!-- Navigation -->
  <nav>
    <div class="wrap nav-bar">
      <div>
        <div class="brand-mark">Rezeki Lancar</div>
        <div class="brand-sub">Bengkel Mebel Kayu Jepara</div>
      </div>
      <div class="nav-links">
        <a href="#tentang">Tentang</a>
        <a href="#katalog">Katalog (500)</a>
        <a href="#kerjasama">Mitra Arsitek</a>
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

  <!-- Company Profile Section -->
  <section class="section-about wrap" id="tentang">
    <div class="about-grid">
      <div class="about-body">
        <div class="hero-label">Profil Perusahaan &amp; Etos Kerja</div>
        <h2 class="about-h">Bukan makelar retail. Kami bertumpu pada kayu yang benar dan tukang yang terlatih.</h2>
        <p>
          Banyak proyek interior kecewa dengan mebel asal Jepara akibat kayu basah yang melengkung setelah 3 bulan di ruang ber-AC, sambungan yang hanya dipaku tembak, serta komunikasi bengkel yang tidak disiplin membaca gambar kerja arsitektur.
        </p>
        <p>
          Rezeki Lancar didirikan untuk menjembatani kesenjangan tersebut. Kami mengawinkan keahlian tangan tradisional ukir & pasak kayu Jepara dengan disiplin kontrol mutu modern: kayu oven kering terukur, pelaporan progres bertahap, dan kepatuhan dimensi gambar kerja AutoCAD maupun 3D SketchUp.
        </p>
      </div>

      <div class="pillar-box">
        <div class="pillar-title">Spesifikasi Bengkel Kami</div>
        <ul class="pillar-list">
          <li><span>Material Baku</span> <strong>Kayu Jati Solid, Mindi, Mahoni, Rotan Asli</strong></li>
          <li><span>Perlakuan Kayu</span> <strong>Chemical Anti-Rayap &amp; Kiln-Dried Chamber</strong></li>
          <li><span>Standar Finishing</span> <strong>Polyurethane (PU), NC Matte, Natural Oil</strong></li>
          <li><span>Kapasitas Proyek</span> <strong>Loose Furniture Residensial, Cafe, Villa Bali</strong></li>
          <li><span>Pengiriman</span> <strong>Packing Palet Kayu Tertutup Seluruh Indonesia</strong></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Complete 500 Product Catalog Section -->
  <section class="section-catalog wrap" id="katalog">
    <div class="catalog-head">
      <div class="hero-label">Arsip Lengkap Koleksi</div>
      <h2 class="catalog-title">Katalog 500 Karya Mebel Kayu Solid</h2>
      <p class="catalog-sub">Klik pada produk mana saja untuk membaca spesifikasi detail, dimensi lengkap, dan formulir konsultasi pemesanan.</p>
    </div>

    <!-- Search Box -->
    <input type="text" id="searchInput" class="search-input" placeholder="Ketik kata kunci (contoh: meja kerja, kursi, bench, credenza, sofa)..." />

    <!-- Category Pills -->
    <div class="cat-bar" id="catBar">
      <button class="cat-btn active" onclick="setCat('Semua')">Semua (500)</button>
      <button class="cat-btn" onclick="setCat('Kursi & Sofa')">Kursi &amp; Sofa</button>
      <button class="cat-btn" onclick="setCat('Meja & Konsol')">Meja &amp; Konsol</button>
      <button class="cat-btn" onclick="setCat('Lemari & Storage')">Lemari &amp; Storage</button>
      <button class="cat-btn" onclick="setCat('Rak & Display')">Rak &amp; Display</button>
      <button class="cat-btn" onclick="setCat('Cermin & Dekorasi')">Cermin &amp; Dekorasi</button>
    </div>

    <!-- Meta Stats -->
    <div class="meta-bar">
      <div>Menampilkan <strong id="shownCount" style="color:var(--text);">20</strong> dari <span id="matchCount">500</span> karya</div>
      <div>*Setiap item bisa diklik untuk membaca detail</div>
    </div>

    <!-- Product Grid: Each item is a real link to its dedicated detail page -->
    <div class="product-grid" id="productGrid"></div>

    <!-- Load More -->
    <div class="load-more-box">
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
        <div class="brand-mark" style="font-size: 18px; margin-bottom: 6px;">Rezeki Lancar Furniture</div>
        <p style="max-width: 420px; line-height: 1.7;">
          Bengkel pengerjaan mebel kayu solid &amp; mitra manufaktur desainer interior. Berakar dari tradisi pertukangan kayu Jepara, Jawa Tengah.
        </p>
      </div>
      <div>
        <div class="foot-h">Workshop &amp; Studio</div>
        <p>Jepara, Jawa Tengah<br>Indonesia</p>
        <p style="margin-top: 8px;">Kunjungan workshop dengan perjanjian.</p>
      </div>
      <div>
        <div class="foot-h">Kontak Proyek</div>
        <p>WhatsApp: +62 812-3456-7890</p>
        <p>Email: proyek@rezekilancar.id</p>
      </div>
    </div>
    <div class="wrap" style="border-top: 1px solid var(--border); padding-top: 20px; text-align: center; font-size: 11px;">
      &copy; 2026 Rezeki Lancar Furniture. All rights reserved.
    </div>
  </footer>

  <!-- Catalog Engine (Instant Search + Direct Page Linking) -->
  <script>
    const allItems = {products_json_compact};
    let activeCategory = 'Semua';
    let searchQuery = '';
    let currentPage = 1;
    const pageSize = 20;
    let filteredItems = [];

    const grid = document.getElementById('productGrid');
    const shownCount = document.getElementById('shownCount');
    const matchCount = document.getElementById('matchCount');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const searchInput = document.getElementById('searchInput');

    function applyFilter() {{
      filteredItems = allItems.filter(item => {{
        const matchC = (activeCategory === 'Semua') || (item.c === activeCategory);
        const matchQ = (searchQuery === '') || 
                       item.t.toLowerCase().includes(searchQuery) || 
                       (item.d && item.d.toLowerCase().includes(searchQuery));
        return matchC && matchQ;
      }});
      currentPage = 1;
      renderGrid();
    }}

    function renderGrid() {{
      const limit = currentPage * pageSize;
      const visible = filteredItems.slice(0, limit);

      grid.innerHTML = '';
      visible.forEach(item => {{
        const card = document.createElement('a');
        card.href = './' + item.url;
        card.className = 'item-card';

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
      matchCount.innerText = filteredItems.length;

      if (limit >= filteredItems.length) {{
        loadMoreBtn.style.display = 'none';
      }} else {{
        loadMoreBtn.style.display = 'inline-block';
        loadMoreBtn.innerText = `Muat ${{Math.min(pageSize, filteredItems.length - limit)}} Karya Berikutnya ↓`;
      }}
    }}

    function loadMore() {{
      currentPage++;
      renderGrid();
    }}

    function setCat(cat) {{
      activeCategory = cat;
      document.querySelectorAll('.cat-btn').forEach(btn => {{
        btn.classList.toggle('active', btn.innerText.includes(cat));
      }});
      applyFilter();
    }}

    searchInput.addEventListener('input', e => {{
      searchQuery = e.target.value.toLowerCase().trim();
      applyFilter();
    }});

    // Init
    applyFilter();
  </script>
</body>
</html>'''

with open(os.path.join(repo_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Generated index.html and all 500 detail pages successfully!")
