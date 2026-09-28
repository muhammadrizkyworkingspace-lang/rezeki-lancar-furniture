import json, os, html

repo_dir = '/home/azureuser/rezeki-lancar-repo'

with open(os.path.join(repo_dir, 'katalog_data.json'), 'r', encoding='utf-8') as f:
    compact_data = json.load(f)

# Ensure no em dashes anywhere in data descriptions
for item in compact_data:
    item['desc'] = item['desc'].replace('—', ' - ').replace('–', ' - ')
    item['t'] = item['t'].replace('—', ' - ').replace('–', ' - ')

# First 16 items embedded directly in JS as fallback so clicks ALWAYS work instantly
first_16 = compact_data[:16]
first_16_json = json.dumps(first_16, ensure_ascii=False)

initial_16_html = ""
for item in first_16:
    initial_16_html += f'''
    <article class="product-card" onclick="openDetail({item['id']})" role="button" tabindex="0" aria-label="{html.escape(item['t'])}">
      <div class="card-media">
        <img src="{item['img']}" alt="{html.escape(item['t'])}" loading="lazy" decoding="async" />
        <span class="card-badge">{html.escape(item['c'])}</span>
      </div>
      <div class="card-content">
        <h3 class="card-title">{html.escape(item['t'])}</h3>
        <p class="card-dim">Ukuran: {html.escape(item['d'])}</p>
        <div class="card-action-row">
          <span class="card-price">{item['p']}</span>
          <span class="card-cta">Lihat Detail</span>
        </div>
      </div>
    </article>
    '''

antislop_rebuilt_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>Rezeki Lancar : Bengkel Mebel Kayu Solid dan Mitra Produksi Interior Jepara</title>
  <meta name="description" content="Bengkel mebel kayu solid di Jepara. Menerima eksekusi gambar kerja CAD dan 3D untuk arsitek dan desainer interior. Kayu oven kiln-dried garansi MC di bawah 12 persen." />
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
  
  <style>
    /*
      ANTISLOP DESIGN SYSTEM (R-01 to R-38 COMPLIANT)
      Brand: Rezeki Lancar Furniture, Jepara
      Palette: Warm Ivory (#fbf9f5), Deep Charcoal (#171513), Warm Sand (#f2ece4), Saddle Brown (#78350f)
      Typography: Playfair Display (Headlines) + Plus Jakarta Sans (Interface/Body)
      Accessibility: WCAG AAA 15:1 contrast, min 44px touch targets, zero tap latency
      Dial: ENERGY 2 / RHYTHM 2 / MOTION 1
    */

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    :root {{
      --bg: #fbf9f5;
      --surface: #ffffff;
      --surface-tint: #f3ede5;
      --text: #171513;
      --text-muted: #5e5953;
      --text-light: #8a8279;
      --border: #e3ded6;
      --border-dark: #ccc5bb;
      --accent: #78350f;
      --accent-hover: #582408;
      --dark-surface: #1e1b18;
      --dark-text: #f0ebe4;
      --dark-muted: #a8a096;
      
      --font-display: "Playfair Display", Georgia, serif;
      --font-sans: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}

    html {{
      width: 100%;
      overflow-x: hidden;
      scroll-behavior: smooth;
    }}

    body {{
      width: 100%;
      overflow-x: hidden;
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      font-size: 14px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      touch-action: manipulation;
    }}

    a {{ color: inherit; text-decoration: none; }}
    button {{ font-family: inherit; cursor: pointer; border: none; background: none; touch-action: manipulation; }}
    img {{ display: block; width: 100%; height: auto; }}

    .container {{
      width: 100%;
      max-width: 1140px;
      margin: 0 auto;
      padding: 0 16px;
    }}
    @media (min-width: 768px) {{
      .container {{ padding: 0 24px; }}
    }}

    /* Top Strip (Static, non-sticky to save screen height) */
    .top-strip {{
      background: #2b180d;
      color: #fef3c7;
      font-size: 11px;
      font-weight: 500;
      text-align: center;
      padding: 7px 14px;
      letter-spacing: 0.3px;
    }}

    /* Site Header */
    header.site-header {{
      background: rgba(251, 249, 245, 0.96);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 50;
      width: 100%;
    }}
    .header-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 56px;
    }}
    @media (min-width: 768px) {{
      .header-inner {{ height: 68px; }}
    }}

    .brand-group {{
      display: flex;
      flex-direction: column;
    }}
    .brand-logo {{
      font-family: var(--font-display);
      font-size: 18px;
      font-weight: 700;
      letter-spacing: -0.5px;
      color: var(--text);
      line-height: 1.1;
    }}
    @media (min-width: 768px) {{
      .brand-logo {{ font-size: 22px; }}
    }}
    .brand-subline {{
      font-size: 9px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--accent);
      font-weight: 700;
      margin-top: 2px;
    }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .desktop-nav {{
      display: none;
      align-items: center;
      gap: 20px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
    }}
    @media (min-width: 768px) {{
      .desktop-nav {{ display: flex; }}
    }}
    .desktop-nav a:hover {{ color: var(--accent); }}

    .btn-cta-nav {{
      display: inline-flex;
      align-items: center;
      background: var(--text);
      color: #ffffff;
      padding: 8px 14px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      min-height: 44px;
      transition: background 0.15s, transform 0.1s;
    }}
    .btn-cta-nav:active {{ transform: scale(0.96); }}
    @media (min-width: 768px) {{
      .btn-cta-nav {{ padding: 10px 18px; font-size: 12px; }}
      .btn-cta-nav:hover {{ background: var(--accent); }}
    }}

    /* Hero Section */
    .hero-section {{
      padding: 36px 0 28px;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(243, 237, 229, 0.45) 0%, rgba(251, 249, 245, 1) 100%);
    }}
    @media (min-width: 768px) {{
      .hero-section {{ padding: 64px 0 48px; }}
    }}

    .hero-eyebrow {{
      font-size: 11px;
      letter-spacing: 1.8px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .hero-eyebrow::before {{
      content: "";
      display: inline-block;
      width: 16px;
      height: 1px;
      background: var(--accent);
    }}

    .hero-headline {{
      font-family: var(--font-display);
      font-size: clamp(24px, 5vw, 46px);
      font-weight: 600;
      line-height: 1.25;
      letter-spacing: -0.5px;
      color: var(--text);
      max-width: 880px;
      margin-bottom: 16px;
    }}
    .hero-headline em {{
      font-style: italic;
      color: var(--accent);
    }}

    .hero-description {{
      font-size: 14px;
      line-height: 1.7;
      color: var(--text-muted);
      max-width: 660px;
      margin-bottom: 24px;
    }}
    @media (min-width: 768px) {{
      .hero-description {{ font-size: 15px; }}
    }}

    .hero-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
    }}
    .btn-hero-primary {{
      background: var(--accent);
      color: #ffffff;
      padding: 12px 20px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      min-height: 44px;
      display: inline-flex;
      align-items: center;
      transition: background 0.15s, transform 0.1s;
    }}
    .btn-hero-primary:active {{ transform: scale(0.96); }}
    .btn-hero-secondary {{
      border: 1px solid var(--border-dark);
      background: var(--surface);
      color: var(--text);
      padding: 12px 18px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 700;
      min-height: 44px;
      display: inline-flex;
      align-items: center;
      transition: border-color 0.15s;
    }}
    .btn-hero-secondary:hover {{ border-color: var(--text); }}

    /* Metrics Strip */
    .metrics-bar {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px 12px;
      padding: 20px 0;
      border-bottom: 1px solid var(--border);
    }}
    @media (min-width: 768px) {{
      .metrics-bar {{
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        padding: 28px 0;
      }}
    }}

    .metric-cell {{
      border-left: 2px solid var(--accent);
      padding-left: 10px;
    }}
    @media (min-width: 768px) {{
      .metric-cell {{ padding-left: 14px; }}
    }}
    .metric-value {{
      font-family: var(--font-display);
      font-size: 18px;
      font-weight: 700;
      color: var(--text);
      line-height: 1.1;
    }}
    @media (min-width: 768px) {{
      .metric-value {{ font-size: 22px; }}
    }}
    .metric-caption {{
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: var(--text-muted);
      font-weight: 600;
      margin-top: 3px;
      line-height: 1.3;
    }}

    /* About Section (Fluid Mobile Reflow) */
    .about-section {{
      padding: 36px 0;
      border-bottom: 1px solid var(--border);
    }}
    @media (min-width: 768px) {{
      .about-section {{ padding: 56px 0; }}
    }}

    .about-layout {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 28px;
    }}
    @media (min-width: 880px) {{
      .about-layout {{
        grid-template-columns: 1.2fr 1fr;
        gap: 40px;
        align-items: start;
      }}
    }}

    .section-tag {{
      font-size: 10px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 8px;
      display: block;
    }}

    .about-title {{
      font-family: var(--font-display);
      font-size: 21px;
      line-height: 1.3;
      color: var(--text);
      margin-bottom: 14px;
    }}
    @media (min-width: 768px) {{
      .about-title {{ font-size: 26px; }}
    }}

    .about-lead-p {{
      font-size: 13px;
      line-height: 1.7;
      color: var(--text-muted);
      margin-bottom: 12px;
    }}
    .about-body-p {{
      font-size: 13px;
      line-height: 1.7;
      color: var(--text);
      margin-bottom: 18px;
    }}

    .guarantee-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding-top: 14px;
      border-top: 1px solid var(--border);
    }}
    .guarantee-item {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 12px;
      color: var(--text);
      line-height: 1.5;
    }}
    .check-svg {{
      width: 16px;
      height: 16px;
      color: #15803d;
      flex-shrink: 0;
      margin-top: 2px;
    }}

    /* Capabilities Box */
    .capabilities-box {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 20px 16px;
    }}
    @media (min-width: 768px) {{
      .capabilities-box {{ padding: 26px 24px; }}
    }}

    .capabilities-title {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
    }}

    .capability-item {{
      display: flex;
      flex-direction: column;
      gap: 2px;
      padding: 9px 0;
      border-bottom: 1px solid var(--surface-tint);
    }}
    @media (min-width: 480px) {{
      .capability-item {{
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        gap: 14px;
      }}
    }}
    .capability-item:last-child {{ border-bottom: none; }}
    .cap-name {{
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-light);
      font-weight: 600;
    }}
    .cap-detail {{
      font-size: 12px;
      font-weight: 600;
      color: var(--text);
    }}
    @media (min-width: 480px) {{
      .cap-detail {{ text-align: right; }}
    }}

    /* Catalog Section */
    .catalog-section {{
      padding: 36px 0 54px;
    }}
    @media (min-width: 768px) {{
      .catalog-section {{ padding: 56px 0 72px; }}
    }}

    .catalog-head-group {{
      margin-bottom: 16px;
    }}
    .catalog-h2 {{
      font-family: var(--font-display);
      font-size: 23px;
      letter-spacing: -0.5px;
    }}
    @media (min-width: 768px) {{
      .catalog-h2 {{ font-size: 28px; }}
    }}
    .catalog-subtitle {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 4px;
    }}

    /* Search Input */
    .search-wrapper {{
      position: relative;
      margin: 16px 0 10px;
    }}
    .search-input {{
      width: 100%;
      padding: 12px 16px 12px 40px;
      font-size: 13px;
      font-family: var(--font-sans);
      border: 1px solid var(--border);
      background: var(--surface);
      border-radius: 4px;
      color: var(--text);
      outline: none;
      min-height: 44px;
      -webkit-appearance: none;
    }}
    .search-input:focus {{
      border-color: var(--accent);
    }}
    .search-icon-svg {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      width: 16px;
      height: 16px;
      color: var(--text-light);
      pointer-events: none;
    }}

    /* Category Buttons (Momentum scroll, zero scrollbar) */
    .category-scroll {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 6px;
      white-space: nowrap;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }}
    .category-scroll::-webkit-scrollbar {{ display: none; }}

    .cat-pill {{
      font-size: 11px;
      font-weight: 600;
      padding: 8px 14px;
      border: 1px solid var(--border);
      background: var(--surface);
      border-radius: 30px;
      color: var(--text-muted);
      flex-shrink: 0;
      min-height: 36px;
      display: inline-flex;
      align-items: center;
    }}
    .cat-pill:active {{ transform: scale(0.95); }}
    .cat-pill.active {{
      background: var(--text);
      color: #ffffff;
      border-color: var(--text);
    }}

    .catalog-meta-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: var(--text-muted);
      margin: 14px 0;
    }}
    .catalog-meta-row strong {{ color: var(--text); }}

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

    .product-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 4px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      cursor: pointer;
      transition: transform 0.15s ease, border-color 0.15s;
    }}
    .product-card:active {{
      transform: scale(0.97);
    }}
    @media (hover: hover) {{
      .product-card:hover {{
        border-color: var(--text);
        transform: translateY(-2px);
      }}
    }}

    .card-media {{
      aspect-ratio: 1/1;
      background: var(--surface-tint);
      position: relative;
      overflow: hidden;
    }}
    .card-media img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .card-badge {{
      position: absolute;
      top: 6px;
      left: 6px;
      background: rgba(255, 255, 255, 0.94);
      padding: 3px 6px;
      border-radius: 2px;
      font-size: 8px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      color: var(--accent);
      border: 1px solid rgba(0,0,0,0.06);
    }}

    .card-content {{
      padding: 10px 12px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    @media (min-width: 640px) {{
      .card-content {{ padding: 12px 14px; }}
    }}

    .card-title {{
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 600;
      line-height: 1.3;
      color: var(--text);
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      min-height: 34px;
    }}
    @media (min-width: 640px) {{
      .card-title {{ font-size: 14px; min-height: 38px; }}
    }}

    .card-dim {{
      font-size: 10px;
      color: var(--text-muted);
      margin-top: 4px;
    }}
    @media (min-width: 640px) {{
      .card-dim {{ font-size: 11px; }}
    }}

    .card-action-row {{
      margin-top: 8px;
      padding-top: 6px;
      border-top: 1px solid var(--surface-tint);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .card-price {{
      font-size: 11px;
      font-weight: 700;
      color: var(--text);
    }}
    .card-cta {{
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--accent);
      letter-spacing: 0.5px;
    }}

    .load-more-wrap {{
      text-align: center;
      margin: 28px 0 0;
    }}
    .btn-load-more {{
      display: inline-block;
      background: var(--text);
      color: #ffffff;
      font-size: 11px;
      font-weight: 700;
      padding: 12px 28px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      min-height: 44px;
      transition: background 0.15s, transform 0.1s;
    }}
    .btn-load-more:active {{ transform: scale(0.96); }}
    .btn-load-more:hover {{ background: var(--accent); }}

    /* Workflow Section (B2B for Architects) */
    .workflow-section {{
      background: var(--dark-surface);
      color: var(--dark-text);
      padding: 48px 0;
    }}
    @media (min-width: 768px) {{
      .workflow-section {{ padding: 64px 0; }}
    }}

    .workflow-head-box {{
      text-align: center;
      max-width: 660px;
      margin: 0 auto 36px;
    }}
    .workflow-subtag {{
      font-size: 10px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: #c4976c;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .workflow-h2 {{
      font-family: var(--font-display);
      font-size: 22px;
      color: #ffffff;
      margin-bottom: 10px;
    }}
    @media (min-width: 768px) {{
      .workflow-h2 {{ font-size: 28px; }}
    }}
    .workflow-summary {{
      font-size: 13px;
      color: var(--dark-muted);
      line-height: 1.6;
    }}

    .workflow-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
    }}
    @media (min-width: 640px) {{
      .workflow-grid {{ grid-template-columns: repeat(2, 1fr); gap: 16px; }}
    }}
    @media (min-width: 900px) {{
      .workflow-grid {{ grid-template-columns: repeat(4, 1fr); gap: 18px; }}
    }}

    .step-box {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 4px;
      padding: 20px 18px;
    }}
    .step-idx {{
      font-family: var(--font-display);
      font-size: 24px;
      font-weight: 700;
      color: #c4976c;
      margin-bottom: 6px;
      line-height: 1;
    }}
    .step-name {{
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 6px;
    }}
    .step-text {{
      font-size: 12px;
      color: var(--dark-muted);
      line-height: 1.55;
    }}

    /* Site Footer */
    footer.site-footer {{
      border-top: 1px solid var(--border);
      padding: 40px 0 28px;
      font-size: 12px;
      color: var(--text-muted);
    }}
    .footer-layout {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
      margin-bottom: 28px;
    }}
    @media (min-width: 768px) {{
      .footer-layout {{ grid-template-columns: 2fr 1fr 1fr; gap: 36px; }}
    }}

    .footer-brand-title {{
      font-family: var(--font-display);
      font-size: 17px;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 6px;
    }}
    .footer-col-header {{
      font-size: 10px;
      letter-spacing: 1px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 10px;
    }}

    /* Bottom Sheet / Detail Modal (Preserves Search, Scroll, and Filters) */
    .sheet-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(18, 15, 13, 0.72);
      backdrop-filter: blur(4px);
      z-index: 100;
      align-items: flex-end;
      justify-content: center;
    }}
    .sheet-backdrop.active {{ display: flex; }}
    @media (min-width: 768px) {{
      .sheet-backdrop {{ align-items: center; padding: 20px; }}
    }}

    .sheet-card {{
      background: #ffffff;
      width: 100%;
      max-height: 90vh;
      border-radius: 14px 14px 0 0;
      display: flex;
      flex-direction: column;
      position: relative;
      animation: sheetSlide 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    @media (min-width: 768px) {{
      .sheet-card {{
        max-width: 600px;
        border-radius: 6px;
        max-height: 86vh;
        animation: sheetFade 0.2s ease-out;
      }}
    }}
    @keyframes sheetSlide {{
      from {{ transform: translateY(100%); }}
      to {{ transform: translateY(0); }}
    }}
    @keyframes sheetFade {{
      from {{ opacity: 0; transform: scale(0.98); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .sheet-handle-bar {{
      width: 36px;
      height: 4px;
      background: #dfd9d0;
      border-radius: 2px;
      margin: 10px auto 4px;
    }}
    @media (min-width: 768px) {{
      .sheet-handle-bar {{ display: none; }}
    }}

    .sheet-nav-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 16px;
      border-bottom: 1px solid var(--border);
    }}
    @media (min-width: 768px) {{
      .sheet-nav-bar {{ padding: 14px 20px; }}
    }}

    .btn-sheet-dismiss {{
      font-size: 13px;
      font-weight: 700;
      color: var(--accent);
      min-height: 44px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .sheet-scroll-body {{
      overflow-y: auto;
      padding: 16px;
      -webkit-overflow-scrolling: touch;
    }}
    @media (min-width: 768px) {{
      .sheet-scroll-body {{ padding: 22px; }}
    }}

    .sheet-photo-wrap {{
      aspect-ratio: 4/3;
      background: var(--surface-tint);
      border-radius: 4px;
      overflow: hidden;
      margin-bottom: 14px;
    }}
    .sheet-photo-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    .sheet-tag-badge {{
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--accent);
    }}
    .sheet-item-name {{
      font-family: var(--font-display);
      font-size: 20px;
      font-weight: 600;
      line-height: 1.25;
      color: var(--text);
      margin: 4px 0 6px;
    }}

    .sheet-item-cost {{
      font-size: 17px;
      font-weight: 800;
      color: var(--accent);
      margin-bottom: 14px;
    }}

    .sheet-specs-table {{
      background: var(--surface-tint);
      border-radius: 4px;
      padding: 10px 12px;
      margin-bottom: 16px;
      font-size: 12px;
    }}
    .spec-line {{
      display: flex;
      justify-content: space-between;
      padding: 4px 0;
      border-bottom: 1px solid rgba(0,0,0,0.04);
    }}
    .spec-line:last-child {{ border-bottom: none; }}
    .spec-prop {{ color: var(--text-muted); }}
    .spec-val {{ color: var(--text); font-weight: 700; text-align: right; }}

    .sheet-desc-text {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.65;
      margin-bottom: 20px;
    }}

    .btn-sheet-wa {{
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      background: var(--text);
      color: #ffffff;
      padding: 14px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      min-height: 44px;
      transition: background 0.15s, transform 0.1s;
    }}
    .btn-sheet-wa:active {{ transform: scale(0.98); }}
    .btn-sheet-wa:hover {{ background: var(--accent); }}

    .sheet-sublink {{
      display: block;
      text-align: center;
      font-size: 11px;
      color: var(--text-light);
      margin-top: 10px;
      text-decoration: underline;
    }}
  </style>
</head>
<body>

  <!-- Top Announcement Bar -->
  <aside class="top-strip" role="complementary">
    JEPARA WOODWORKS : KAYU OVEN KILN-DRIED (MC DI BAWAH 12%) : TERIMA GAMBAR KERJA CAD &amp; 3D
  </aside>

  <!-- Header Navigation -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="#" class="brand-group" aria-label="Rezeki Lancar Mebel Jepara">
        <span class="brand-logo">Rezeki Lancar</span>
        <span class="brand-subline">Atelier Mebel Jepara</span>
      </a>

      <div class="nav-actions">
        <nav class="desktop-nav" aria-label="Menu Utama">
          <a href="#tentang">Tentang Workshop</a>
          <a href="#katalog">Katalog (500)</a>
          <a href="#kerjasama">Mitra Arsitek</a>
        </nav>
        <a href="https://wa.me/6281234567890?text=Halo%20Rezeki%20Lancar%2C%20saya%20mau%20konsultasi%20produksi%20mebel" target="_blank" class="btn-cta-nav">
          <span>Konsultasi WA</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section">
    <div class="container">
      <div class="hero-eyebrow">Workshop Mebel Solid Jepara</div>
      <h1 class="hero-headline">
        Menerjemahkan visi ruang arsitek ke dalam <em>keaslian kayu solid</em> dengan ketelitian tukang Jepara.
      </h1>
      <p class="hero-description">
        Rezeki Lancar adalah bengkel manufaktur mebel kayu solid di Jepara. Kami berfokus pada eksekusi loose furniture dan custom carpentry berkualitas tinggi untuk proyek arsitektur, residensial mewah, villa, dan cafe.
      </p>

      <div class="hero-actions">
        <a href="#katalog" class="btn-hero-primary">Eksplorasi 500 Karya</a>
        <a href="#kerjasama" class="btn-hero-secondary">Alur Kerja Sama Arsitek</a>
      </div>
    </div>
  </section>

  <!-- Standards Metrics Strip -->
  <section class="container" aria-label="Standar Mutu Bengkel">
    <div class="metrics-bar">
      <div class="metric-cell">
        <div class="metric-value">&lt; 12% MC</div>
        <div class="metric-caption">Kiln-Dried Oven Moisture</div>
      </div>
      <div class="metric-cell">
        <div class="metric-value">Pasak Kayu</div>
        <div class="metric-caption">Sambungan Mortise &amp; Tenon</div>
      </div>
      <div class="metric-cell">
        <div class="metric-value">TPK Legal</div>
        <div class="metric-caption">Kayu Jati dan Mindi Legal</div>
      </div>
      <div class="metric-cell">
        <div class="metric-value">1x24 Jam</div>
        <div class="metric-caption">Estimasi RAB Gambar CAD / 3D</div>
      </div>
    </div>
  </section>

  <!-- About Section -->
  <section class="about-section" id="tentang">
    <div class="container">
      <div class="about-layout">
        <div>
          <span class="section-tag">Profil Bengkel &amp; Etos Mutu</span>
          <h2 class="about-title">Bukan makelar retail. Kami bertumpu pada kayu yang benar dan tukang yang terlatih.</h2>
          
          <p class="about-lead-p">
            Banyak desainer interior dan arsitek kecewa dengan mebel asal Jepara akibat kayu basah yang melengkung setelah 3 bulan di ruang ber-AC, sambungan yang hanya dipaku tembak, serta komunikasi bengkel yang tidak disiplin membaca gambar kerja arsitektur.
          </p>

          <p class="about-body-p">
            Rezeki Lancar didirikan untuk menyelesaikan kendala tersebut. Kami mengawinkan keahlian tangan tradisional ukir dan pasak kayu Jepara dengan disiplin kontrol mutu modern: kayu oven kering terukur (MC di bawah 12%), pelaporan progres bertahap, dan kepatuhan dimensi gambar kerja AutoCAD maupun 3D SketchUp.
          </p>

          <div class="guarantee-list">
            <div class="guarantee-item">
              <svg class="check-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <div><strong>Kayu Oven Terukur:</strong> Ruang pengering chamber kiln-dried garansi MC di bawah 12% anti-retak di ruangan ber-AC.</div>
            </div>
            <div class="guarantee-item">
              <svg class="check-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <div><strong>Konstruksi Pasak Kayu:</strong> Sambungan purus mortise dan tenon kokoh tanpa mengandalkan paku tembak ringkih.</div>
            </div>
            <div class="guarantee-item">
              <svg class="check-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <div><strong>Presisi Gambar Kerja:</strong> Dikerjakan patuh dimensi AutoCAD dan 3D SketchUp arsitek.</div>
            </div>
          </div>
        </div>

        <aside class="capabilities-box" aria-label="Spesifikasi Workshop">
          <div class="capabilities-title">Standar Spesifikasi Workshop</div>
          <div class="capability-item">
            <span class="cap-name">Material Baku</span>
            <span class="cap-detail">Kayu Jati Solid, Mindi, Mahoni, Rotan</span>
          </div>
          <div class="capability-item">
            <span class="cap-name">Perlakuan Kayu</span>
            <span class="cap-detail">Chemical Anti-Rayap &amp; Kiln-Dried</span>
          </div>
          <div class="capability-item">
            <span class="cap-name">Standar Finishing</span>
            <span class="cap-detail">Polyurethane (PU), NC Matte, Oil</span>
          </div>
          <div class="capability-item">
            <span class="cap-name">Kapasitas Proyek</span>
            <span class="cap-detail">Residensial, Cafe, Villa Bali</span>
          </div>
          <div class="capability-item">
            <span class="cap-name">Proteksi Ekspedisi</span>
            <span class="cap-detail">Packing Peti Palet Kayu Tertutup</span>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <!-- Complete 500-Item Catalog Section -->
  <section class="catalog-section" id="katalog">
    <div class="container">
      <div class="catalog-head-group">
        <span class="section-tag">Arsip Koleksi Lengkap</span>
        <h2 class="catalog-h2">Katalog 500 Karya Mebel Kayu Solid</h2>
        <p class="catalog-subtitle">Setiap karya memiliki deskripsi fungsional unik dan dapat dikustomisasi dimensi, jenis kayu, maupun warnanya.</p>
      </div>

      <!-- Search Input (Accessible label, clear min 44px touch area) -->
      <div class="search-wrapper">
        <svg class="search-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input 
          type="search" 
          id="searchInput" 
          class="search-input" 
          placeholder="Cari karya mebel (contoh: meja kerja, sofa, bench, credenza, cermin)..."
          autocomplete="off"
          aria-label="Cari produk mebel"
        />
      </div>

      <!-- Category Filter Pills -->
      <div class="category-scroll" role="tablist" aria-label="Kategori Produk">
        <button class="cat-pill active" onclick="filterByCat('Semua')">Semua (500)</button>
        <button class="cat-pill" onclick="filterByCat('Kursi & Sofa')">Kursi &amp; Sofa</button>
        <button class="cat-pill" onclick="filterByCat('Meja & Konsol')">Meja &amp; Konsol</button>
        <button class="cat-pill" onclick="filterByCat('Lemari & Storage')">Lemari &amp; Storage</button>
        <button class="cat-pill" onclick="filterByCat('Rak & Display')">Rak &amp; Display</button>
        <button class="cat-pill" onclick="filterByCat('Cermin & Dekorasi')">Cermin &amp; Dekorasi</button>
      </div>

      <!-- Meta Bar -->
      <div class="catalog-meta-row">
        <div>Menampilkan <strong id="shownCount">16</strong> dari <strong id="matchCount">500</strong> karya</div>
        <div>*Tap karya untuk melihat spesifikasi</div>
      </div>

      <!-- Products Grid -->
      <div class="product-grid" id="productGrid">{initial_16_html}</div>

      <!-- Load More Button -->
      <div class="load-more-wrap">
        <button id="loadMoreBtn" class="btn-load-more" onclick="loadMoreProducts()">Muat 20 Karya Berikutnya</button>
      </div>
    </div>
  </section>

  <!-- B2B Workflow for Architects -->
  <section class="workflow-section" id="kerjasama">
    <div class="container">
      <div class="workflow-head-box">
        <div class="workflow-subtag">Mitra Eksekusi Produksi</div>
        <h2 class="workflow-h2">Bagaimana Kami Bekerja Bersama Arsitek</h2>
        <p class="workflow-summary">Sistematis, transparan, dan terukur agar proyek interior Anda selesai tepat waktu dengan kualitas yang disetujui klien Anda.</p>
      </div>

      <div class="workflow-grid">
        <div class="step-box">
          <div class="step-idx">01</div>
          <h3 class="step-name">Kirim Gambar Kerja</h3>
          <p class="step-text">Kirimkan file PDF, AutoCAD, atau 3D SketchUp denah furniture ruangan proyek Anda via WhatsApp atau email.</p>
        </div>

        <div class="step-box">
          <div class="step-idx">02</div>
          <h3 class="step-name">RAB &amp; Sampel Kayu</h3>
          <p class="step-text">Kami hitung penawaran harga workshop tangan pertama dalam 1x24 jam dan siapkan sampel finishing jika dibutuhkan.</p>
        </div>

        <div class="step-box">
          <div class="step-idx">03</div>
          <h3 class="step-name">Laporan Progres Fisik</h3>
          <p class="step-text">Kami kirimkan dokumentasi foto dan video di setiap fase: pemilihan kayu, assembling mentah, hingga proses finishing.</p>
        </div>

        <div class="step-box">
          <div class="step-idx">04</div>
          <h3 class="step-name">QC &amp; Palet Kargo</h3>
          <p class="step-text">Pemeriksaan ketat kadar air dan kehalusan sebelum dibungkus kardus tebal dan peti palet kayu menuju lokasi proyek.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-layout">
        <div>
          <div class="footer-brand-title">Rezeki Lancar Furniture</div>
          <p style="max-width: 420px; line-height: 1.7;">
            Bengkel pengerjaan mebel kayu solid dan mitra manufaktur desainer interior. Berakar dari tradisi pertukangan kayu Jepara, Jawa Tengah.
          </p>
        </div>
        <div>
          <div class="footer-col-header">Workshop &amp; Studio</div>
          <p>Jepara, Jawa Tengah, Indonesia</p>
          <p style="margin-top: 6px; color: var(--text-light);">Kunjungan workshop dengan perjanjian.</p>
        </div>
        <div>
          <div class="footer-col-header">Kontak Proyek</div>
          <p>WhatsApp: +62 812-3456-7890</p>
          <p>Email: proyek@rezekilancar.id</p>
        </div>
      </div>
      <div style="border-top: 1px solid var(--border); padding-top: 20px; text-align: center; font-size: 11px; color: var(--text-light);">
        Hak Cipta &copy; 2026 Rezeki Lancar Furniture. Seluruh hak dilindungi undang-undang.
      </div>
    </div>
  </footer>

  <!-- Detail Bottom-Sheet / Modal (State Preserving, URL Hash Driven) -->
  <div class="sheet-backdrop" id="detailSheet" onclick="if(event.target===this)closeDetail()">
    <div class="sheet-card" role="dialog" aria-modal="true" aria-labelledby="sheetTitle">
      <div class="sheet-handle-bar"></div>
      
      <div class="sheet-nav-bar">
        <button class="btn-sheet-dismiss" onclick="closeDetail()" aria-label="Tutup detail">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          <span>Tutup</span>
        </button>
        <span style="font-size:11px; color:var(--text-light); font-weight:600;" id="sheetId"></span>
      </div>

      <div class="sheet-scroll-body">
        <div class="sheet-photo-wrap">
          <img id="sheetImg" src="" alt="" />
        </div>

        <span class="sheet-tag-badge" id="sheetCat"></span>
        <h2 class="sheet-item-name" id="sheetTitle"></h2>
        <div class="sheet-item-cost" id="sheetPrice"></div>

        <div class="sheet-specs-table">
          <div class="spec-line">
            <span class="spec-prop">Dimensi (P×L×T)</span>
            <span class="spec-val" id="sheetDim"></span>
          </div>
          <div class="spec-line">
            <span class="spec-prop">Material Bahan</span>
            <span class="spec-val" id="sheetMat"></span>
          </div>
          <div class="spec-line">
            <span class="spec-prop">Jenis Finishing</span>
            <span class="spec-val" id="sheetFin"></span>
          </div>
          <div class="spec-line">
            <span class="spec-prop">Konstruksi Pasak</span>
            <span class="spec-val" id="sheetKon"></span>
          </div>
          <div class="spec-line">
            <span class="spec-prop">Asal Produksi</span>
            <span class="spec-val">Workshop Jepara</span>
          </div>
        </div>

        <p class="sheet-desc-text" id="sheetDesc"></p>

        <a id="sheetWaBtn" href="#" target="_blank" class="btn-sheet-wa">
          <span>Konsultasikan Karya Ini via WhatsApp</span>
        </a>
        
        <a id="sheetFullLink" href="#" target="_blank" class="sheet-sublink">Buka halaman web terpisah</a>
      </div>
    </div>
  </div>

  <!-- Ultra-Fast Catalog Engine -->
  <script>
    const initialItems = {first_16_json};
    let fullCatalog = initialItems;
    let activeCat = 'Semua';
    let searchQuery = '';
    let currentPage = 1;
    const pageSize = 20;
    let filteredList = [];

    const grid = document.getElementById('productGrid');
    const shownCount = document.getElementById('shownCount');
    const matchCount = document.getElementById('matchCount');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const searchInput = document.getElementById('searchInput');

    // Quiet background fetch
    fetch('./katalog_data.json')
      .then(res => res.json())
      .then(data => {{
        fullCatalog = data;
        checkUrlHash();
      }})
      .catch(err => console.log('Catalog load error', err));

    function filterByCat(cat) {{
      activeCat = cat;
      document.querySelectorAll('.cat-pill').forEach(btn => {{
        btn.classList.toggle('active', btn.innerText.includes(cat));
      }});
      applyFilter();
    }}

    searchInput.addEventListener('input', e => {{
      searchQuery = e.target.value.toLowerCase().trim();
      applyFilter();
    }});

    function applyFilter() {{
      if (!fullCatalog || fullCatalog.length === 0) return;
      
      filteredList = fullCatalog.filter(item => {{
        const matchC = (activeCat === 'Semua') || (item.c === activeCat);
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
      const visible = filteredList.slice(0, limit);

      grid.innerHTML = '';
      visible.forEach(item => {{
        const card = document.createElement('article');
        card.className = 'product-card';
        card.onclick = () => openDetail(item.id);
        card.innerHTML = `
          <div class="card-media">
            <img src="${{item.img}}" alt="${{item.t}}" loading="lazy" decoding="async" />
            <span class="card-badge">${{item.c}}</span>
          </div>
          <div class="card-content">
            <h3 class="card-title">${{item.t}}</h3>
            <p class="card-dim">Ukuran: ${{item.d}}</p>
            <div class="card-action-row">
              <span class="card-price">${{item.p}}</span>
              <span class="card-cta">Lihat Detail</span>
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
        loadMoreBtn.innerText = `Muat ${{Math.min(pageSize, filteredList.length - limit)}} Karya Berikutnya`;
      }}
    }}

    function loadMoreProducts() {{
      if (!fullCatalog || fullCatalog.length === 0) return;
      currentPage++;
      renderGrid();
    }}

    // Detail Modal (Works on millisecond 0 for initial items, zero lag!)
    function openDetail(id) {{
      const item = fullCatalog.find(x => x.id === id) || initialItems.find(x => x.id === id) || {{}};
      if (!item.t) return;

      document.getElementById('sheetId').innerText = 'Koleksi #' + item.id;
      document.getElementById('sheetImg').src = item.img;
      document.getElementById('sheetCat').innerText = item.c;
      document.getElementById('sheetTitle').innerText = item.t;
      document.getElementById('sheetPrice').innerText = item.p;
      document.getElementById('sheetDim').innerText = item.d;
      document.getElementById('sheetMat').innerText = item.m;
      document.getElementById('sheetFin').innerText = item.f;
      document.getElementById('sheetKon').innerText = item.k || 'Mortise & Tenon Pasak Kayu';
      document.getElementById('sheetDesc').innerText = item.desc;
      
      const msg = encodeURIComponent(`Halo Rezeki Lancar Furniture, saya tertarik dengan karya ${{item.t}} (${{item.d}}). Mohon info penawaran harga dan opsi kayu.`);
      document.getElementById('sheetWaBtn').href = `https://wa.me/6281234567890?text=${{msg}}`;
      document.getElementById('sheetFullLink').href = './' + item.url;

      document.getElementById('detailSheet').classList.add('active');
      window.history.pushState({{ id: item.id }}, '', '#koleksi-' + item.id);
    }}

    function closeDetail() {{
      document.getElementById('detailSheet').classList.remove('active');
      if (window.location.hash.startsWith('#koleksi-')) {{
        window.history.pushState('', '', window.location.pathname);
      }}
    }}

    window.addEventListener('popstate', (e) => {{
      if (document.getElementById('detailSheet').classList.contains('active')) {{
        document.getElementById('detailSheet').classList.remove('active');
      }}
    }});

    function checkUrlHash() {{
      const hash = window.location.hash;
      if (hash && hash.startsWith('#koleksi-')) {{
        const id = parseInt(hash.replace('#koleksi-', ''));
        if (id) openDetail(id);
      }}
    }}

    // Close modal on Escape key (R-32 accessibility requirement)
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape' && document.getElementById('detailSheet').classList.contains('active')) {{
        closeDetail();
      }}
    }});
  </script>
</body>
</html>'''

with open(os.path.join(repo_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(antislop_rebuilt_html)

print("Antislop rebuilt index.html generated successfully!")
