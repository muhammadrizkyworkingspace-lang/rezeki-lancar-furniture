import json, os, html

with open('/home/azureuser/rezeki-lancar-repo/katalog_500.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Compact products for index.html (only keep what is needed for card rendering)
compact_products = []
for idx, p in enumerate(products):
    compact_products.append({
        'id': idx + 1,
        't': p['nama_produk'],
        'c': p['kategori'],
        'p': p['harga_pasar'],
        'd': p['dimensi'],
        'm': p['material'],
        'f': p['finishing'],
        'img': p['url_gambar'],
        'desc': (p.get('deskripsi') or '')[:180]
    })

products_json = json.dumps(compact_products, ensure_ascii=False)

html_code = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rezeki Lancar Furniture — Jepara Woodworks & Interior Partner</title>
  <meta name="description" content="Workshop mebel kayu solid Jepara. Spesialis custom furniture & mitra produksi arsitek dan desainer interior." />
  <style>
    /* Ultra-lightweight native CSS (<3KB). Zero external frameworks. Instant render. */
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: #faf9f6;
      color: #1c1917;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }}
    a {{ color: inherit; text-decoration: none; }}
    button {{ font-family: inherit; cursor: pointer; border: none; background: none; }}
    
    .container {{ max-width: 1100px; margin: 0 auto; padding: 0 16px; }}
    
    /* Top Bar */
    .topbar {{
      background: #3c1e08;
      color: #fef3c7;
      font-size: 11px;
      font-weight: 500;
      text-align: center;
      padding: 6px 12px;
      letter-spacing: 0.5px;
    }}
    
    /* Nav */
    header {{
      background: #ffffff;
      border-bottom: 1px solid #e7e5e4;
      position: sticky;
      top: 0;
      z-index: 30;
    }}
    .nav-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 56px;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .brand-logo {{
      width: 32px;
      height: 32px;
      background: #78350f;
      color: #fff;
      font-weight: 700;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
    }}
    .brand-name {{ font-size: 15px; font-weight: 700; color: #1c1917; line-height: 1.1; }}
    .brand-sub {{ font-size: 10px; color: #78350f; font-weight: 600; text-transform: uppercase; }}
    .btn-wa-header {{
      background: #78350f;
      color: #ffffff;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 6px;
    }}
    
    /* Hero */
    .hero {{
      padding: 32px 0 24px;
      text-align: center;
      background: #f4f1ec;
      border-bottom: 1px solid #e7e5e4;
    }}
    .hero-badge {{
      display: inline-block;
      background: #fef3c7;
      color: #92400e;
      font-size: 10px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 12px;
      margin-bottom: 10px;
      text-transform: uppercase;
    }}
    .hero-title {{
      font-size: 24px;
      font-weight: 800;
      letter-spacing: -0.5px;
      color: #1c1917;
      max-width: 680px;
      margin: 0 auto;
      line-height: 1.25;
    }}
    .hero-desc {{
      font-size: 13px;
      color: #57534e;
      max-width: 540px;
      margin: 8px auto 0;
    }}
    
    /* Controls */
    .controls {{
      margin: 18px auto 0;
      max-width: 480px;
    }}
    .search-box {{
      width: 100%;
      padding: 10px 14px;
      font-size: 13px;
      border: 1px solid #d6d3d1;
      border-radius: 8px;
      background: #ffffff;
      outline: none;
    }}
    .search-box:focus {{ border-color: #78350f; }}
    
    .cat-bar {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding: 12px 0 4px;
      white-space: nowrap;
      justify-content: flex-start;
      -webkit-overflow-scrolling: touch;
    }}
    @media(min-width: 640px) {{
      .cat-bar {{ justify-content: center; }}
      .hero-title {{ font-size: 32px; }}
    }}
    .cat-pill {{
      font-size: 11px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 20px;
      background: #ffffff;
      border: 1px solid #d6d3d1;
      color: #44403c;
    }}
    .cat-pill.active {{
      background: #78350f;
      color: #ffffff;
      border-color: #78350f;
    }}
    
    /* Stats Bar */
    .meta-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 0 8px;
      font-size: 12px;
      color: #78716c;
      border-bottom: 1px solid #f0ede9;
    }}
    
    /* Grid */
    .catalog-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: 14px;
    }}
    @media(min-width: 768px) {{
      .catalog-grid {{ grid-template-columns: repeat(3, 1fr); gap: 16px; }}
    }}
    @media(min-width: 1024px) {{
      .catalog-grid {{ grid-template-columns: repeat(4, 1fr); gap: 18px; }}
    }}
    
    /* Card */
    .card {{
      background: #ffffff;
      border: 1px solid #e7e5e4;
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      cursor: pointer;
    }}
    .card-img-wrap {{
      position: relative;
      aspect-ratio: 1/1;
      background: #f5f5f4;
      overflow: hidden;
    }}
    .card-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .card-body {{
      padding: 10px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .card-cat {{
      font-size: 9px;
      font-weight: 700;
      color: #78350f;
      text-transform: uppercase;
    }}
    .card-title {{
      font-size: 12px;
      font-weight: 700;
      color: #1c1917;
      margin-top: 2px;
      line-height: 1.25;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    .card-dim {{
      font-size: 11px;
      color: #78716c;
      margin-top: 4px;
    }}
    .card-footer {{
      margin-top: 8px;
      padding-top: 6px;
      border-top: 1px solid #f5f5f4;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .card-price {{
      font-size: 11px;
      font-weight: 800;
      color: #78350f;
    }}
    .card-btn {{
      font-size: 10px;
      font-weight: 600;
      background: #fef3c7;
      color: #92400e;
      padding: 3px 6px;
      border-radius: 4px;
    }}
    
    /* Load More Button */
    .load-more-wrap {{
      text-align: center;
      margin: 28px 0 40px;
    }}
    .btn-load-more {{
      background: #1c1917;
      color: #ffffff;
      font-size: 12px;
      font-weight: 600;
      padding: 10px 20px;
      border-radius: 6px;
      display: inline-block;
    }}
    
    /* B2B Section */
    .b2b-banner {{
      background: #1c1917;
      color: #ffffff;
      padding: 32px 16px;
      border-radius: 10px;
      text-align: center;
      margin: 32px auto;
    }}
    .b2b-sub {{ font-size: 10px; font-weight: 700; color: #f59e0b; text-transform: uppercase; letter-spacing: 0.8px; }}
    .b2b-h {{ font-size: 20px; font-weight: 800; margin: 6px 0; }}
    .b2b-p {{ font-size: 12px; color: #a8a29e; max-width: 540px; margin: 0 auto 16px; }}
    .b2b-btn {{
      display: inline-block;
      background: #d97706;
      color: #ffffff;
      font-weight: 700;
      font-size: 12px;
      padding: 9px 18px;
      border-radius: 6px;
    }}
    
    /* Modal */
    .modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.6);
      z-index: 50;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }}
    .modal-overlay.open {{ display: flex; }}
    .modal-card {{
      background: #ffffff;
      border-radius: 12px;
      max-width: 520px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 18px;
      position: relative;
    }}
    .modal-close {{
      position: absolute;
      top: 10px;
      right: 10px;
      font-size: 20px;
      color: #78716c;
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .modal-img {{
      width: 100%;
      aspect-ratio: 1/1;
      object-fit: cover;
      border-radius: 6px;
      background: #f5f5f4;
    }}
    .modal-specs {{
      margin: 12px 0;
      font-size: 12px;
      border-top: 1px solid #f0ede9;
      border-bottom: 1px solid #f0ede9;
      padding: 8px 0;
    }}
    .modal-specs div {{ margin-bottom: 3px; }}
    .modal-btn {{
      display: block;
      width: 100%;
      text-align: center;
      background: #78350f;
      color: #fff;
      font-size: 12px;
      font-weight: 700;
      padding: 11px;
      border-radius: 6px;
    }}
  </style>
</head>
<body>

  <div class="topbar">
    JEPARA WOODWORKS • KAYU OVEN KILN-DRIED (MC &lt; 12%) • TERIMA GAMBAR KERJA CAD / 3D
  </div>

  <header>
    <div class="container nav-inner">
      <div class="brand">
        <div class="brand-logo">RL</div>
        <div>
          <div class="brand-name">Rezeki Lancar</div>
          <div class="brand-sub">Furniture Jepara</div>
        </div>
      </div>
      <a href="https://wa.me/6281234567890?text=Halo%20Rezeki%20Lancar%20Furniture%2C%20saya%20mau%20konsultasi%20custom%20mebel" target="_blank" class="btn-wa-header">
        Konsultasi WA
      </a>
    </div>
  </header>

  <section class="hero">
    <div class="container">
      <span class="hero-badge">Workshop Jepara — Handcrafted</span>
      <h1 class="hero-title">Kejujuran Kayu & Presisi Tukang Jepara</h1>
      <p class="hero-desc">
        Katalog produk mebel solid & mitra eksekusi produksi gambar kerja interior di Jakarta, Bali, dan kota lainnya.
      </p>

      <div class="controls">
        <input type="text" id="searchInput" class="search-box" placeholder="Ketik untuk mencari produk (contoh: meja, sofa, rak)..." />
        <div class="cat-bar" id="catBar">
          <button class="cat-pill active" onclick="setCategory('Semua')">Semua (500)</button>
          <button class="cat-pill" onclick="setCategory('Kursi & Sofa')">Kursi & Sofa</button>
          <button class="cat-pill" onclick="setCategory('Meja & Konsol')">Meja & Konsol</button>
          <button class="cat-pill" onclick="setCategory('Lemari & Storage')">Lemari & Storage</button>
          <button class="cat-pill" onclick="setCategory('Rak & Display')">Rak & Display</button>
          <button class="cat-pill" onclick="setCategory('Cermin & Dekorasi')">Cermin & Dekorasi</button>
        </div>
      </div>
    </div>
  </section>

  <main class="container">
    <div class="meta-bar">
      <div>Menampilkan <span id="countText" style="font-weight:700; color:#1c1917;">16</span> dari <span id="totalMatchText">500</span> produk</div>
      <div>Klik foto untuk spesifikasi detail</div>
    </div>

    <div class="catalog-grid" id="grid"></div>

    <div class="load-more-wrap">
      <button id="loadMoreBtn" class="btn-load-more" onclick="loadMore()">Muat 16 Produk Lainnya ↓</button>
    </div>

    <!-- B2B Section for Architects -->
    <div class="b2b-banner">
      <div class="b2b-sub">Mitra Produksi Arsitek & Desainer Interior</div>
      <div class="b2b-h">Punya Gambar Kerja Sendiri? Kami Buatkan Estimasi RAB</div>
      <div class="b2b-p">Kirim file 3D SketchUp, PDF, atau CAD Anda. Kami hitung estimasi biaya produksi kayu solid langsung dari tangan pertama pengrajin Jepara.</div>
      <a href="https://wa.me/6281234567890?text=Halo%20Rezeki%20Lancar%2C%20saya%20arsitek%2Fdesainer%20interior%20mau%20kirim%20gambar%20kerja%20untuk%20RAB" target="_blank" class="b2b-btn">Kirim Gambar Kerja via WhatsApp →</a>
    </div>
  </main>

  <footer style="text-align:center; padding:20px 16px; font-size:11px; color:#78716c; border-top:1px solid #e7e5e4;">
    &copy; 2026 Rezeki Lancar Furniture • Workshop Mebel Jepara, Jawa Tengah.
  </footer>

  <!-- Modal -->
  <div class="modal-overlay" id="modal" onclick="if(event.target===this)closeModal()">
    <div class="modal-card">
      <button class="modal-close" onclick="closeModal()">&times;</button>
      <img id="mImg" class="modal-img" src="" alt="" />
      <div style="margin-top:10px;">
        <span id="mCat" style="font-size:10px; font-weight:700; color:#78350f; text-transform:uppercase;"></span>
        <h3 id="mTitle" style="font-size:15px; font-weight:800; margin-top:2px;"></h3>
        <div id="mPrice" style="font-size:13px; font-weight:800; color:#78350f; margin-top:2px;"></div>
      </div>
      <div class="modal-specs">
        <div><strong>Dimensi:</strong> <span id="mDim"></span></div>
        <div><strong>Material:</strong> <span id="mMat"></span></div>
        <div><strong>Finishing:</strong> <span id="mFin"></span></div>
      </div>
      <p id="mDesc" style="font-size:11px; color:#57534e; margin-bottom:14px;"></p>
      <a id="mWa" href="#" target="_blank" class="modal-btn">Pesan / Diskusi Produk via WhatsApp</a>
    </div>
  </div>

  <script>
    const data = {products_json};
    let activeCat = 'Semua';
    let query = '';
    let page = 1;
    const pageSize = 16;
    let filteredList = [];

    const grid = document.getElementById('grid');
    const countText = document.getElementById('countText');
    const totalMatchText = document.getElementById('totalMatchText');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const searchInput = document.getElementById('searchInput');

    function filterData() {{
      filteredList = data.filter(item => {{
        const matchCat = (activeCat === 'Semua') || (item.c === activeCat);
        const matchQ = query === '' || item.t.toLowerCase().includes(query) || (item.d && item.d.toLowerCase().includes(query));
        return matchCat && matchQ;
      }});
      page = 1;
      render();
    }}

    function render() {{
      const limit = page * pageSize;
      const visible = filteredList.slice(0, limit);
      
      grid.innerHTML = '';
      visible.forEach(p => {{
        const card = document.createElement('div');
        card.className = 'card';
        card.onclick = () => openModal(p);
        
        card.innerHTML = `
          <div class="card-img-wrap">
            <img class="card-img" src="${{p.img}}" alt="${{p.t}}" loading="lazy" decoding="async" onerror="this.src='https://placehold.co/300x300/f5f5f4/a8a29e?text=Mebel+Jepara'" />
          </div>
          <div class="card-body">
            <div>
              <div class="card-cat">${{p.c}}</div>
              <div class="card-title">${{p.t}}</div>
              <div class="card-dim">📐 ${{p.d}}</div>
            </div>
            <div class="card-footer">
              <div class="card-price">${{p.p}}</div>
              <span class="card-btn">Detail →</span>
            </div>
          </div>
        `;
        grid.appendChild(card);
      }});

      countText.innerText = visible.length;
      totalMatchText.innerText = filteredList.length;

      if (limit >= filteredList.length) {{
        loadMoreBtn.style.display = 'none';
      }} else {{
        loadMoreBtn.style.display = 'inline-block';
        loadMoreBtn.innerText = `Muat ${{Math.min(pageSize, filteredList.length - limit)}} Lainnya ↓`;
      }}
    }}

    function loadMore() {{
      page++;
      render();
    }}

    function setCategory(cat) {{
      activeCat = cat;
      document.querySelectorAll('.cat-pill').forEach(btn => {{
        btn.classList.toggle('active', btn.innerText.includes(cat));
      }});
      filterData();
    }}

    searchInput.addEventListener('input', e => {{
      query = e.target.value.toLowerCase().trim();
      filterData();
    }});

    function openModal(p) {{
      document.getElementById('mImg').src = p.img;
      document.getElementById('mCat').innerText = p.c;
      document.getElementById('mTitle').innerText = p.t;
      document.getElementById('mPrice').innerText = p.p;
      document.getElementById('mDim').innerText = p.d;
      document.getElementById('mMat').innerText = p.m;
      document.getElementById('mFin').innerText = p.f;
      document.getElementById('mDesc').innerText = p.desc || 'Kayu solid pilihan diproduksi dengan sambungan presisi dan kontrol oven (MC < 12%) di workshop Jepara.';
      
      const msg = encodeURIComponent(`Halo Rezeki Lancar Furniture, saya tertarik dengan ${{p.t}} (${{p.d}}). Mohon info penawaran harga & estimasi pengerjaan.`);
      document.getElementById('mWa').href = `https://wa.me/6281234567890?text=${{msg}}`;
      document.getElementById('modal').classList.add('open');
    }}

    function closeModal() {{
      document.getElementById('modal').classList.remove('open');
    }}

    filterData();
  </script>
</body>
</html>'''

with open('/home/azureuser/rezeki-lancar-repo/index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("Generated super-fast index.html successfully!")
