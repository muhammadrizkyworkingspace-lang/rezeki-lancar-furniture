import json, os, html

repo_dir = '/home/azureuser/rezeki-lancar-repo'
prod_dir = os.path.join(repo_dir, 'produk')
os.makedirs(prod_dir, exist_ok=True)

with open(os.path.join(repo_dir, 'katalog_500.json'), 'r', encoding='utf-8') as f:
    products = json.load(f)

base_url = 'https://muhammadrizkyworkingspace-lang.github.io/rezeki-lancar-furniture'

# 1. Update all 500 individual product detail pages with their unique descriptions & smart back button
compact_data = []

for idx, p in enumerate(products):
    slug = ''.join(c if c.isalnum() else '-' for c in p['nama_produk'].lower()).strip('-')
    while '--' in slug: slug = slug.replace('--', '-')
    slug = f"{idx+1:03d}-{slug[:50]}"
    
    file_rel = f"produk/{slug}.html"
    page_url = f"{base_url}/{file_rel}"
    
    compact_data.append({
        'id': idx + 1,
        't': p['nama_produk'],
        'c': p['kategori'],
        'p': p['harga_pasar'],
        'd': p['dimensi'],
        'm': p['material'],
        'f': p['finishing'],
        'k': p.get('konstruksi', 'Mortise & Tenon Pasak Kayu'),
        'b': p.get('berat', '-'),
        'img': p['url_gambar'],
        'desc': p['deskripsi'],
        'slug': slug,
        'url': file_rel
    })
    
    price_clean = p['harga_pasar'].replace('Rp', '').replace('.', '').strip() if 'Rp' in p['harga_pasar'] else '0'
    schema = {
        '@context': 'https://schema.org/',
        '@type': 'Product',
        'name': p['nama_produk'],
        'image': [p['url_gambar']],
        'description': p['deskripsi'],
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
    
    wa_msg = f"Halo Rezeki Lancar Furniture, saya tertarik dengan karya: {p['nama_produk']} ({p['dimensi']}). Mohon informasi opsi kayu & penawaran RAB."
    wa_link = f"https://wa.me/6281234567890?text={html.escape(wa_msg)}"

    single_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(p['nama_produk'])} — Rezeki Lancar Furniture Jepara</title>
  <meta name="description" content="{html.escape(p['deskripsi'][:150])}" />
  <link rel="canonical" href="{page_url}" />
  <meta property="og:title" content="{html.escape(p['nama_produk'])} | Rezeki Lancar Furniture" />
  <meta property="og:description" content="{html.escape(p['deskripsi'][:150])}" />
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
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      padding: 0 16px 40px;
    }}
    a {{ color: inherit; text-decoration: none; }}
    .wrap {{ max-width: 900px; margin: 0 auto; }}
    .top-nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 0;
      border-bottom: 1px solid #e3ded8;
      margin-bottom: 24px;
      font-size: 13px;
    }}
    .back-btn {{
      color: #78350f;
      font-weight: 700;
      cursor: pointer;
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
    .card-detail {{
      background: #ffffff;
      border: 1px solid #e3ded8;
      border-radius: 4px;
      overflow: hidden;
      display: grid;
      grid-template-columns: 1fr;
    }}
    @media(min-width: 768px) {{
      .card-detail {{ grid-template-columns: 1fr 1fr; }}
    }}
    .img-box {{
      background: #f0ece6;
      aspect-ratio: 1/1;
      width: 100%;
    }}
    .img-box img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .info-box {{
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .cat-badge {{
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: #78350f;
    }}
    .p-title {{
      font-family: "Iowan Old Style", Baskerville, serif;
      font-size: 24px;
      font-weight: 600;
      margin: 6px 0 8px;
    }}
    .p-price {{
      font-size: 18px;
      font-weight: 800;
      color: #78350f;
      margin-bottom: 16px;
    }}
    .spec-table {{
      width: 100%;
      border-top: 1px solid #f0ede9;
      border-bottom: 1px solid #f0ede9;
      padding: 12px 0;
      margin-bottom: 16px;
      font-size: 12px;
    }}
    .spec-row {{
      display: flex;
      justify-content: space-between;
      padding: 4px 0;
    }}
    .spec-k {{ color: #78716c; }}
    .spec-v {{ font-weight: 600; text-align: right; }}
    .p-desc {{
      font-size: 13px;
      color: #57534e;
      line-height: 1.7;
      margin-bottom: 24px;
    }}
    .btn-wa {{
      display: block;
      width: 100%;
      text-align: center;
      background: #1a1816;
      color: #ffffff;
      padding: 12px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      border-radius: 2px;
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="top-nav">
      <a href="../" onclick="if(window.history.length > 1){{window.history.back(); return false;}}" class="back-btn">← Kembali ke Katalog</a>
      <span class="brand-tag">Rezeki Lancar Jepara</span>
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
              <span class="spec-k">Material</span>
              <span class="spec-v">{html.escape(p['material'])}</span>
            </div>
            <div class="spec-row">
              <span class="spec-k">Finishing</span>
              <span class="spec-v">{html.escape(p['finishing'])}</span>
            </div>
            <div class="spec-row">
              <span class="spec-k">Konstruksi</span>
              <span class="spec-v">{html.escape(p.get('konstruksi', 'Pasak Mortise & Tenon'))}</span>
            </div>
            <div class="spec-row">
              <span class="spec-k">Asal Bengkel</span>
              <span class="spec-v">Jepara, Jawa Tengah</span>
            </div>
          </div>

          <p class="p-desc">{html.escape(p['deskripsi'])}</p>
        </div>

        <div>
          <a href="{wa_link}" target="_blank" class="btn-wa">Konsultasi Karya Ini via WhatsApp →</a>
        </div>
      </div>
    </div>
  </div>
</body>
</html>'''

    with open(os.path.join(prod_dir, f"{slug}.html"), 'w', encoding='utf-8') as f:
        f.write(single_html)

# 2. Write external compact data JSON (so index.html is NOT bloated with 160KB!)
with open(os.path.join(repo_dir, 'katalog_data.json'), 'w', encoding='utf-8') as f:
    json.dump(compact_data, f, ensure_ascii=False)

print(f"Saved katalog_data.json ({os.path.getsize(os.path.join(repo_dir, 'katalog_data.json'))/1024:.1f} KB)")

# 3. Build ultra-fast index.html (<18KB) with Instant Detail Drawer & zero-loss back state!
initial_16_html = ""
for item in compact_data[:16]:
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

index_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rezeki Lancar — Bengkel Mebel Kayu Solid & Mitra Produksi Interior Jepara</title>
  <meta name="description" content="Bengkel kayu keluarga di Jepara. Mitra eksekusi produksi mebel custom kayu solid kiln-dried untuk arsitek, desainer interior, dan proyek residensial mewah." />
  <style>
    /* Ultra-performance pure CSS. Total HTML <18KB. Zero lag. Instant search. */
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg: #f9f7f4;
      --card-bg: #ffffff;
      --text: #1a1816;
      --text-muted: #6b6661;
      --border: #e3ded8;
      --accent: #78350f;
      --font-serif: "Iowan Old Style", Baskerville, "Times New Roman", serif;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}
    a {{ color: inherit; text-decoration: none; }}
    button {{ font-family: inherit; cursor: pointer; border: none; background: none; }}
    .wrap {{ max-width: 1140px; margin: 0 auto; padding: 0 16px; }}
    
    /* Nav */
    nav {{
      border-bottom: 1px solid var(--border);
      background: rgba(249, 247, 244, 0.98);
      position: sticky;
      top: 0;
      z-index: 30;
    }}
    .nav-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 60px;
    }}
    .brand-mark {{
      font-family: var(--font-serif);
      font-size: 19px;
      font-weight: 700;
      letter-spacing: -0.5px;
    }}
    .brand-sub {{
      font-size: 9px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-top: -3px;
    }}
    .btn-contact {{
      border: 1px solid var(--text);
      padding: 6px 12px;
      font-size: 11px;
      text-transform: uppercase;
      font-weight: 700;
    }}
    .btn-contact:hover {{ background: var(--text); color: #fff; }}

    /* Hero */
    .hero {{
      padding: 48px 0 36px;
      border-bottom: 1px solid var(--border);
    }}
    .hero-label {{
      font-size: 10px;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 14px;
    }}
    .hero-title {{
      font-family: var(--font-serif);
      font-size: clamp(26px, 4vw, 42px);
      font-weight: 400;
      line-height: 1.2;
      max-width: 820px;
      margin-bottom: 16px;
    }}
    .hero-title em {{ font-style: italic; }}
    .hero-lead {{
      font-size: 14px;
      color: var(--text-muted);
      max-width: 620px;
    }}

    /* Specs Strip */
    .specs-strip {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      padding: 24px 0;
      border-bottom: 1px solid var(--border);
    }}
    @media(min-width: 768px) {{
      .specs-strip {{ grid-template-columns: repeat(4, 1fr); }}
    }}
    .spec-item {{ border-left: 2px solid var(--text); padding-left: 12px; }}
    .spec-num {{ font-family: var(--font-serif); font-size: 20px; font-weight: 700; }}
    .spec-label {{ font-size: 10px; text-transform: uppercase; color: var(--text-muted); }}

    /* About Section */
    .section-about {{
      padding: 48px 0;
      border-bottom: 1px solid var(--border);
    }}
    .about-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 32px;
    }}
    @media(min-width: 860px) {{
      .about-grid {{ grid-template-columns: 1.2fr 1fr; align-items: start; }}
    }}
    .about-h {{
      font-family: var(--font-serif);
      font-size: 24px;
      line-height: 1.3;
      margin-bottom: 14px;
    }}
    .about-p {{
      font-size: 13px;
      line-height: 1.8;
      color: var(--text-muted);
      margin-bottom: 12px;
    }}
    .pillar-box {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: 20px;
      border-radius: 4px;
    }}
    .pillar-box li {{
      list-style: none;
      font-size: 12px;
      padding: 8px 0;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      color: var(--text-muted);
    }}
    .pillar-box li:last-child {{ border-bottom: none; }}
    .pillar-box strong {{ color: var(--text); }}

    /* Catalog Section */
    .section-catalog {{ padding: 48px 0; }}
    .catalog-h {{ font-family: var(--font-serif); font-size: 28px; }}
    .catalog-sub {{ font-size: 12px; color: var(--text-muted); margin-top: 4px; }}
    
    .search-box {{
      width: 100%;
      padding: 10px 14px;
      font-size: 14px;
      border: 1px solid var(--border);
      background: #ffffff;
      border-radius: 4px;
      outline: none;
      margin: 16px 0 10px;
    }}
    .search-box:focus {{ border-color: var(--text); }}

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
      padding: 5px 12px;
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
      font-size: 11px;
      color: var(--text-muted);
      margin: 14px 0;
    }}

    /* Grid */
    .product-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }}
    @media(min-width: 768px) {{
      .product-grid {{ grid-template-columns: repeat(3, 1fr); gap: 16px; }}
    }}
    @media(min-width: 1024px) {{
      .product-grid {{ grid-template-columns: repeat(4, 1fr); gap: 20px; }}
    }}

    .item-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      cursor: pointer;
      border-radius: 2px;
      transition: transform 0.15s, border-color 0.15s;
    }}
    .item-card:hover {{
      transform: translateY(-2px);
      border-color: var(--text);
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
      padding: 10px 12px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .item-cat {{
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--accent);
    }}
    .item-name {{
      font-family: var(--font-serif);
      font-size: 13px;
      font-weight: 600;
      line-height: 1.3;
      margin: 3px 0 4px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    .item-dim {{ font-size: 11px; color: var(--text-muted); }}
    .item-foot {{
      margin-top: 8px;
      padding-top: 6px;
      border-top: 1px solid #f4f0eb;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
    }}
    .item-price {{ font-weight: 700; }}
    .item-read {{ font-size: 10px; font-weight: 700; color: var(--accent); }}

    .btn-load {{
      display: inline-block;
      background: var(--text);
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      padding: 10px 24px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin: 28px auto;
    }}

    /* Detail Drawer View (State Preserving Overlay) */
    .drawer-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(20, 18, 16, 0.7);
      z-index: 100;
      justify-content: flex-end;
    }}
    .drawer-overlay.active {{ display: flex; }}
    .drawer-body {{
      background: #ffffff;
      width: 100%;
      max-width: 580px;
      height: 100%;
      overflow-y: auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      animation: slideIn 0.2s ease-out;
    }}
    @keyframes slideIn {{
      from {{ transform: translateX(100%); }}
      to {{ transform: translateX(0); }}
    }}
    .drawer-close-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
    }}
    .btn-drawer-back {{
      font-size: 13px;
      font-weight: 700;
      color: var(--accent);
      cursor: pointer;
    }}
    .drawer-img {{
      width: 100%;
      aspect-ratio: 1/1;
      object-fit: cover;
      background: #f0ece6;
      border-radius: 2px;
    }}
    .drawer-spec-table {{
      margin: 16px 0;
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      padding: 10px 0;
      font-size: 12px;
    }}
    .drawer-spec-row {{
      display: flex;
      justify-content: space-between;
      padding: 4px 0;
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
      margin-top: 20px;
    }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--border);
      padding: 36px 0 24px;
      font-size: 12px;
      color: var(--text-muted);
    }}
  </style>
</head>
<body>

  <nav>
    <div class="wrap nav-bar">
      <div>
        <div class="brand-mark">Rezeki Lancar</div>
        <div class="brand-sub">Bengkel Mebel Kayu Jepara</div>
      </div>
      <a href="https://wa.me/6281234567890?text=Halo%20Rezeki%20Lancar%2C%20saya%20mau%20konsultasi%20produksi%20mebel" target="_blank" class="btn-contact">Konsultasi WA</a>
    </div>
  </nav>

  <section class="hero">
    <div class="wrap">
      <div class="hero-label">Atelier Mebel Solid • Est. Jepara</div>
      <h1 class="hero-title">Menerjemahkan visi arsitek ke dalam <em>ketulusan kayu solid</em> dengan presisi tangan pengrajin Jepara.</h1>
      <p class="hero-lead">Kami mengerjakan loose furniture dan custom carpentry kayu oven kiln-dried untuk proyek arsitektur, residensial, villa, dan cafe.</p>
    </div>
  </section>

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

  <section class="section-about wrap">
    <div class="about-grid">
      <div>
        <div class="hero-label">Profil Perusahaan &amp; Etos Kerja</div>
        <h2 class="about-h">Bukan makelar retail. Kami bertumpu pada kayu yang benar dan tukang yang terlatih.</h2>
        <p class="about-p">Banyak proyek interior kecewa dengan mebel asal Jepara akibat kayu basah yang melengkung setelah 3 bulan di ruang ber-AC, sambungan yang hanya dipaku tembak, serta komunikasi bengkel yang tidak disiplin membaca gambar kerja arsitektur.</p>
        <p class="about-p">Rezeki Lancar didirikan untuk menjembatani kesenjangan tersebut. Kami mengawinkan keahlian tangan tradisional ukir & pasak kayu Jepara dengan disiplin kontrol mutu modern: kayu oven kering terukur, pelaporan progres bertahap, dan kepatuhan dimensi gambar kerja AutoCAD maupun 3D SketchUp.</p>
      </div>
      <div class="pillar-box">
        <div style="font-size:11px; font-weight:700; text-transform:uppercase; margin-bottom:12px;">Spesifikasi Bengkel Kami</div>
        <ul>
          <li><span>Material Baku</span> <strong>Kayu Jati Solid, Mindi, Mahoni, Rotan</strong></li>
          <li><span>Perlakuan Kayu</span> <strong>Chemical Anti-Rayap &amp; Kiln-Dried</strong></li>
          <li><span>Standar Finishing</span> <strong>Polyurethane (PU), NC Matte, Oil</strong></li>
          <li><span>Kapasitas Proyek</span> <strong>Residensial, Cafe, Villa Bali</strong></li>
          <li><span>Pengiriman</span> <strong>Packing Peti Palet Kayu Tertutup</strong></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section-catalog wrap" id="katalog">
    <div class="catalog-h">Arsip Koleksi (500 Karya)</div>
    <div class="catalog-sub">Setiap karya dapat disesuaikan (custom) ukuran, warna, dan jenis kayunya.</div>

    <input type="text" id="searchInput" class="search-box" placeholder="Ketik nama produk atau ukuran (contoh: meja kerja, sofa, cermin)..." />

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
      <div>*Klik kartu mana saja untuk membaca spesifikasi detail</div>
    </div>

    <div class="product-grid" id="grid">{initial_16_html}</div>

    <div style="text-align:center;">
      <button id="loadMoreBtn" class="btn-load" onclick="loadMore()">Muat 20 Karya Berikutnya ↓</button>
    </div>
  </section>

  <footer>
    <div class="wrap" style="display:flex; justify-content:space-between; flex-wrap:gap; gap:16px;">
      <div>
        <div style="font-family:var(--font-serif); font-weight:700; font-size:15px; color:var(--text);">Rezeki Lancar Furniture</div>
        <p>Workshop Mebel Kayu Solid • Jepara, Jawa Tengah • WhatsApp: 0812-3456-7890</p>
      </div>
      <div>&copy; 2026 Rezeki Lancar. All rights reserved.</div>
    </div>
  </footer>

  <!-- Drawer Detail (Preserves Scroll, Search, & Navigation State!) -->
  <div class="drawer-overlay" id="drawer" onclick="if(event.target===this)closeDetail()">
    <div class="drawer-body">
      <div>
        <div class="drawer-close-bar">
          <button class="btn-drawer-back" onclick="closeDetail()">← Kembali ke Pencarian</button>
          <span style="font-size:11px; color:#78716c;" id="dId"></span>
        </div>

        <img id="dImg" class="drawer-img" src="" alt="" />
        
        <div style="margin-top:14px;">
          <div style="font-size:10px; font-weight:700; text-transform:uppercase; color:var(--accent);" id="dCat"></div>
          <h2 style="font-family:var(--font-serif); font-size:22px; font-weight:600; margin:4px 0 6px;" id="dTitle"></h2>
          <div style="font-size:17px; font-weight:800; color:var(--accent);" id="dPrice"></div>
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

        <p style="font-size:13px; color:#57534e; line-height:1.7;" id="dDesc"></p>
      </div>

      <div>
        <a id="dWa" href="#" target="_blank" class="drawer-btn-wa">Konsultasikan Karya Ini via WhatsApp →</a>
        <div style="text-align:center; margin-top:8px;">
          <a id="dLinkFull" href="#" target="_blank" style="font-size:11px; color:#78716c; text-decoration:underline;">Buka halaman URL terpisah →</a>
        </div>
      </div>
    </div>
  </div>

  <!-- Ultra-lightweight Async Catalog Engine -->
  <script>
    let fullCatalog = [];
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

    // Fetch catalog quietly in background after initial paint
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
              <span class="item-read">Detail &amp; Custom →</span>
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

    // Detail Drawer & State Preserving Logic
    function openDetail(id) {{
      const item = fullCatalog.find(x => x.id === id) || {{}};
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

    // When phone hardware back button or browser back is clicked:
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
    f.write(index_html)

print(f"Updated index.html ({os.path.getsize(os.path.join(repo_dir, 'index.html'))/1024:.1f} KB)")
