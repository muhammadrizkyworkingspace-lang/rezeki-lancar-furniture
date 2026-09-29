import json, os, html

repo_dir = '/home/azureuser/rezeki-lancar-repo'

with open(os.path.join(repo_dir, 'katalog_unggulan.json'), 'r', encoding='utf-8') as f:
    custom_works = json.load(f)

custom_works_json = json.dumps(custom_works, ensure_ascii=False)

# Pre-render cards for instant paint
cards_html = ""
for p in custom_works:
    cards_html += f'''
    <article class="showcase-card" onclick="openShowcaseDetail({p['id']})" role="button" tabindex="0" data-cat="{p['category']}">
      <div class="card-photo-box">
        <img src="./{p['img']}" alt="{html.escape(p['title'])}" loading="lazy" decoding="async" />
        <span class="card-series-tag">{html.escape(p['series'])}</span>
      </div>
      <div class="card-info-box">
        <div>
          <span class="card-space-tag">{html.escape(p['category'])}</span>
          <h3 class="card-item-title">{html.escape(p['title'])}</h3>
          <p class="card-dim-text">📐 {html.escape(p['dimensions'])}</p>
          <p class="card-mat-text">🪵 {html.escape(p['material'])}</p>
        </div>
        <div class="card-bottom-row">
          <div>
            <span class="price-label">Estimasi Biaya Produksi:</span>
            <div class="price-val">{html.escape(p['price_range'])}</div>
          </div>
          <span class="card-action-link">Detail &amp; Custom →</span>
        </div>
      </div>
    </article>
    '''

showcase_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>Rezeki Lancar : Showcase Karya Mebel Custom Kayu Solid Jepara</title>
  <meta name="description" content="Showcase 24 karya mebel custom kayu solid unggulan untuk villa, cafe, dan residensial mewah. Spesialis mitra produksi arsitek dan desainer interior di Jepara." />
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
  
  <style>
    /*
      REZEKI LANCAR ATELIER SHOWCASE 2026
      Bespoke Furniture Portfolio for Architects & Interior Designers
      Clean, Pure CSS, 60fps Mobile Fluidity, Zero AI Slop
    */

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    :root {{
      --bg: #faf8f5;
      --surface: #ffffff;
      --surface-tint: #f3ece4;
      --text: #171513;
      --text-muted: #5e5953;
      --text-light: #8e867d;
      --border: #e3ded6;
      --border-dark: #cfc7bc;
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
      max-width: 1180px;
      margin: 0 auto;
      padding: 0 16px;
    }}
    @media (min-width: 768px) {{
      .container {{ padding: 0 28px; }}
    }}

    /* Top Strip */
    .top-strip {{
      background: #2b180d;
      color: #fef3c7;
      font-size: 11px;
      font-weight: 500;
      text-align: center;
      padding: 7px 14px;
      letter-spacing: 0.3px;
    }}

    /* Header Nav */
    header.site-header {{
      background: rgba(250, 248, 245, 0.96);
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
      .header-inner {{ height: 70px; }}
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

    .desktop-nav {{
      display: none;
      align-items: center;
      gap: 22px;
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
      min-height: 40px;
      transition: background 0.15s, transform 0.1s;
    }}
    .btn-cta-nav:active {{ transform: scale(0.96); }}
    @media (min-width: 768px) {{
      .btn-cta-nav {{ padding: 10px 18px; font-size: 12px; min-height: 44px; }}
      .btn-cta-nav:hover {{ background: var(--accent); }}
    }}

    /* Hero Section */
    .hero-section {{
      padding: 40px 0 32px;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(243, 236, 228, 0.45) 0%, rgba(250, 248, 245, 1) 100%);
    }}
    @media (min-width: 768px) {{
      .hero-section {{ padding: 68px 0 52px; }}
    }}

    .hero-eyebrow {{
      font-size: 11px;
      letter-spacing: 2px;
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
      font-size: clamp(24px, 5.2vw, 48px);
      font-weight: 600;
      line-height: 1.25;
      letter-spacing: -0.5px;
      color: var(--text);
      max-width: 900px;
      margin-bottom: 16px;
    }}
    .hero-headline em {{
      font-style: italic;
      color: var(--accent);
    }}

    .hero-description {{
      font-size: 14px;
      line-height: 1.75;
      color: var(--text-muted);
      max-width: 680px;
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
      padding: 12px 22px;
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
      padding: 12px 20px;
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
        gap: 24px;
        padding: 28px 0;
      }}
    }}

    .metric-cell {{
      border-left: 2px solid var(--accent);
      padding-left: 12px;
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

    /* About Section */
    .about-section {{
      padding: 40px 0;
      border-bottom: 1px solid var(--border);
    }}
    @media (min-width: 768px) {{
      .about-section {{ padding: 60px 0; }}
    }}

    .about-layout {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 28px;
    }}
    @media (min-width: 880px) {{
      .about-layout {{
        grid-template-columns: 1.25fr 1fr;
        gap: 44px;
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
      padding: 22px 18px;
    }}
    @media (min-width: 768px) {{
      .capabilities-box {{ padding: 28px 24px; }}
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

    /* ==========================================================================
       FLAGSHIP CUSTOM SHOWCASE SECTION (THE NEW ARCHITECTURAL EXHIBITION)
       ========================================================================== */
    .showcase-section {{
      padding: 44px 0 64px;
    }}
    @media (min-width: 768px) {{
      .showcase-section {{ padding: 68px 0 88px; }}
    }}

    .showcase-header {{
      margin-bottom: 24px;
    }}
    .showcase-title {{
      font-family: var(--font-display);
      font-size: 24px;
      letter-spacing: -0.5px;
      color: var(--text);
    }}
    @media (min-width: 768px) {{
      .showcase-title {{ font-size: 32px; }}
    }}
    .showcase-subtitle {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 6px;
      max-width: 720px;
    }}

    /* Space Filters (Pills) */
    .filter-scroll-bar {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 8px;
      white-space: nowrap;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
      margin: 18px 0 24px;
    }}
    .filter-scroll-bar::-webkit-scrollbar {{ display: none; }}

    .filter-pill {{
      font-size: 12px;
      font-weight: 600;
      padding: 9px 18px;
      border: 1px solid var(--border);
      background: var(--surface);
      border-radius: 30px;
      color: var(--text-muted);
      flex-shrink: 0;
      min-height: 40px;
      display: inline-flex;
      align-items: center;
      transition: all 0.15s ease;
    }}
    .filter-pill:active {{ transform: scale(0.96); }}
    .filter-pill.active {{
      background: var(--text);
      color: #ffffff;
      border-color: var(--text);
    }}

    /* Showcase Grid (Large Editorial Cards) */
    .showcase-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
    }}
    @media (min-width: 640px) {{
      .showcase-grid {{ grid-template-columns: repeat(2, 1fr); gap: 24px; }}
    }}
    @media (min-width: 1024px) {{
      .showcase-grid {{ grid-template-columns: repeat(3, 1fr); gap: 28px; }}
    }}

    .showcase-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      cursor: pointer;
      transition: transform 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s, box-shadow 0.15s;
    }}
    .showcase-card:active {{
      transform: scale(0.98);
    }}
    @media (hover: hover) {{
      .showcase-card:hover {{
        border-color: var(--border-dark);
        transform: translateY(-3px);
        box-shadow: 0 10px 24px rgba(0, 0, 0, 0.05);
      }}
    }}

    .card-photo-box {{
      aspect-ratio: 4/3;
      background: var(--surface-tint);
      position: relative;
      overflow: hidden;
    }}
    .card-photo-box img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }}
    @media (hover: hover) {{
      .showcase-card:hover .card-photo-box img {{
        transform: scale(1.04);
      }}
    }}

    .card-series-tag {{
      position: absolute;
      top: 10px;
      left: 10px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(4px);
      padding: 4px 10px;
      border-radius: 3px;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      color: var(--accent);
      border: 1px solid rgba(0,0,0,0.06);
    }}

    .card-info-box {{
      padding: 16px 18px 18px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .card-space-tag {{
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--text-light);
    }}

    .card-item-title {{
      font-family: var(--font-display);
      font-size: 16px;
      font-weight: 600;
      line-height: 1.35;
      color: var(--text);
      margin: 4px 0 8px;
    }}
    @media (min-width: 640px) {{
      .card-item-title {{ font-size: 17px; min-height: 46px; }}
    }}

    .card-dim-text {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.4;
      margin-bottom: 2px;
    }}
    .card-mat-text {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.4;
      margin-bottom: 12px;
    }}

    .card-bottom-row {{
      margin-top: 8px;
      padding-top: 10px;
      border-top: 1px solid var(--surface-tint);
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}
    .price-label {{
      font-size: 9px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-light);
      display: block;
      margin-bottom: 2px;
    }}
    .price-val {{
      font-size: 12px;
      font-weight: 700;
      color: var(--accent);
    }}
    .card-action-link {{
      font-size: 11px;
      font-weight: 700;
      color: var(--text);
      letter-spacing: 0.3px;
    }}

    /* Workflow Section */
    .workflow-section {{
      background: var(--dark-surface);
      color: var(--dark-text);
      padding: 56px 0;
    }}
    @media (min-width: 768px) {{
      .workflow-section {{ padding: 76px 0; }}
    }}

    .workflow-head-box {{
      text-align: center;
      max-width: 680px;
      margin: 0 auto 40px;
    }}
    .workflow-subtag {{
      font-size: 11px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #c4976c;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .workflow-h2 {{
      font-family: var(--font-display);
      font-size: 24px;
      color: #ffffff;
      margin-bottom: 12px;
    }}
    @media (min-width: 768px) {{
      .workflow-h2 {{ font-size: 32px; }}
    }}
    .workflow-summary {{
      font-size: 13px;
      color: var(--dark-muted);
      line-height: 1.6;
    }}

    .workflow-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
    }}
    @media (min-width: 640px) {{
      .workflow-grid {{ grid-template-columns: repeat(2, 1fr); gap: 20px; }}
    }}
    @media (min-width: 900px) {{
      .workflow-grid {{ grid-template-columns: repeat(4, 1fr); gap: 22px; }}
    }}

    .step-box {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 4px;
      padding: 22px 20px;
    }}
    .step-idx {{
      font-family: var(--font-display);
      font-size: 26px;
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
      padding: 44px 0 32px;
      font-size: 12px;
      color: var(--text-muted);
    }}
    .footer-layout {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 28px;
      margin-bottom: 32px;
    }}
    @media (min-width: 768px) {{
      .footer-layout {{ grid-template-columns: 2fr 1fr 1fr; gap: 40px; }}
    }}

    .footer-brand-title {{
      font-family: var(--font-display);
      font-size: 18px;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 6px;
    }}
    .footer-col-header {{
      font-size: 11px;
      letter-spacing: 1px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 10px;
    }}

    /* Detail Modal (Preserves Scroll & State) */
    .sheet-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(18, 15, 13, 0.75);
      backdrop-filter: blur(5px);
      z-index: 100;
      align-items: flex-end;
      justify-content: center;
    }}
    .sheet-backdrop.active {{ display: flex; }}
    @media (min-width: 768px) {{
      .sheet-backdrop {{ align-items: center; padding: 24px; }}
    }}

    .sheet-card {{
      background: #ffffff;
      width: 100%;
      max-height: 92vh;
      border-radius: 14px 14px 0 0;
      display: flex;
      flex-direction: column;
      position: relative;
      animation: sheetSlide 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    @media (min-width: 768px) {{
      .sheet-card {{
        max-width: 640px;
        border-radius: 6px;
        max-height: 88vh;
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
      padding: 12px 18px;
      border-bottom: 1px solid var(--border);
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
      padding: 18px;
      -webkit-overflow-scrolling: touch;
    }}
    @media (min-width: 768px) {{
      .sheet-scroll-body {{ padding: 24px; }}
    }}

    .sheet-photo-wrap {{
      aspect-ratio: 4/3;
      background: var(--surface-tint);
      border-radius: 4px;
      overflow: hidden;
      margin-bottom: 16px;
    }}
    .sheet-photo-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    .sheet-tag-badge {{
      font-size: 10px;
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
    @media (min-width: 768px) {{
      .sheet-item-name {{ font-size: 24px; }}
    }}

    .sheet-item-cost {{
      font-size: 18px;
      font-weight: 800;
      color: var(--accent);
      margin-bottom: 16px;
    }}

    .sheet-specs-table {{
      background: var(--surface-tint);
      border-radius: 4px;
      padding: 12px 14px;
      margin-bottom: 18px;
      font-size: 12px;
    }}
    .spec-line {{
      display: flex;
      justify-content: space-between;
      padding: 5px 0;
      border-bottom: 1px solid rgba(0,0,0,0.04);
    }}
    .spec-line:last-child {{ border-bottom: none; }}
    .spec-prop {{ color: var(--text-muted); }}
    .spec-val {{ color: var(--text); font-weight: 700; text-align: right; }}

    .sheet-desc-text {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.7;
      margin-bottom: 24px;
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
  </style>
</head>
<body>

  <!-- Top Announcement Bar -->
  <aside class="top-strip" role="complementary">
    JEPARA WOODWORKS : MITRA MANUFAKTUR CUSTOM FURNITURE RESIDENSIAL &amp; VILLA BALI
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
          <a href="#karya-custom">Karya Unggulan (24)</a>
          <a href="#kerjasama">Mitra Arsitek</a>
        </nav>
        <a href="https://wa.me/6281234567890?text=Halo%20Rezeki%20Lancar%2C%20saya%20arsitek%2Fdesainer%20interior%20mau%20konsultasi%20produksi%20custom" target="_blank" class="btn-cta-nav">
          <span>Konsultasi Proyek</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section">
    <div class="container">
      <div class="hero-eyebrow">Workshop Mebel Solid Jepara</div>
      <h1 class="hero-headline">
        Menerjemahkan gambar kerja arsitektur ke dalam <em>keaslian kayu solid</em> dengan presisi tukang Jepara.
      </h1>
      <p class="hero-description">
        Rezeki Lancar adalah bengkel manufaktur mebel kayu solid di Jepara. Kami berfokus pada eksekusi loose furniture custom bermutu tinggi untuk proyek arsitektur, villa Bali, cafe estetik, dan residensial mewah.
      </p>

      <div class="hero-actions">
        <a href="#karya-custom" class="btn-hero-primary">Lihat 24 Karya Unggulan</a>
        <a href="#kerjasama" class="btn-hero-secondary">Alur Gambar Kerja CAD</a>
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
        <div class="metric-value">Jati &amp; Mindi</div>
        <div class="metric-caption">Kayu Legal Perhutani Terkurasi</div>
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
            <span class="cap-detail">Kayu Jati Solid, Mindi, Mahoni, Rotan Alami</span>
          </div>
          <div class="capability-item">
            <span class="cap-name">Perlakuan Kayu</span>
            <span class="cap-detail">Chemical Anti-Rayap &amp; Kiln-Dried Chamber</span>
          </div>
          <div class="capability-item">
            <span class="cap-name">Standar Finishing</span>
            <span class="cap-detail">Polyurethane (PU), NC Matte, Natural Oil</span>
          </div>
          <div class="capability-item">
            <span class="cap-name">Kapasitas Proyek</span>
            <span class="cap-detail">Residensial Mewah, Cafe, Villa Bali</span>
          </div>
          <div class="capability-item">
            <span class="cap-name">Proteksi Ekspedisi</span>
            <span class="cap-detail">Packing Peti Palet Kayu Tertutup Seluruh Indonesia</span>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SHOWCASE KARYA CUSTOM UNGGULAN (LOOKBOOK 2026)
       ========================================================================== -->
  <section class="showcase-section" id="karya-custom">
    <div class="container">
      <div class="showcase-header">
        <span class="section-tag">Lookbook &amp; Portofolio Workshop</span>
        <h2 class="showcase-title">24 Karya Mebel Custom Unggulan</h2>
        <p class="showcase-subtitle">
          Koleksi kurasi desain loose furniture yang siap diadaptasi ukuran, pilihan kayu, dan warnanya sesuai gambar kerja proyek interior Anda.
        </p>
      </div>

      <!-- Space Filter Tabs -->
      <div class="filter-scroll-bar" role="tablist" aria-label="Filter Ruangan">
        <button class="filter-pill active" onclick="filterSpace('Semua')">Semua Karya (24)</button>
        <button class="filter-pill" onclick="filterSpace('Dining & Cafe')">Ruang Makan &amp; Cafe (6)</button>
        <button class="filter-pill" onclick="filterSpace('Living & Lounge')">Living Room &amp; Villa (6)</button>
        <button class="filter-pill" onclick="filterSpace('Kamar Tidur')">Kamar Tidur Residensial (6)</button>
        <button class="filter-pill" onclick="filterSpace('Ruang Kerja')">Ruang Kerja &amp; Storage (6)</button>
      </div>

      <!-- Exhibition Grid -->
      <div class="showcase-grid" id="showcaseGrid">
        {cards_html}
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

  <!-- Detail Bottom-Sheet / Modal (State Preserving) -->
  <div class="sheet-backdrop" id="showcaseModal" onclick="if(event.target===this)closeShowcaseDetail()">
    <div class="sheet-card" role="dialog" aria-modal="true" aria-labelledby="mTitle">
      <div class="sheet-handle-bar"></div>
      
      <div class="sheet-nav-bar">
        <button class="btn-sheet-dismiss" onclick="closeShowcaseDetail()" aria-label="Tutup detail karya">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          <span>Tutup</span>
        </button>
        <span style="font-size:11px; color:var(--text-light); font-weight:600;" id="mSeries"></span>
      </div>

      <div class="sheet-scroll-body">
        <div class="sheet-photo-wrap">
          <img id="mImg" src="" alt="" />
        </div>

        <span class="sheet-tag-badge" id="mCategory"></span>
        <h2 class="sheet-item-name" id="mTitle"></h2>
        <div class="sheet-item-cost" id="mPrice"></div>

        <div class="sheet-specs-table">
          <div class="spec-line">
            <span class="spec-prop">Dimensi Standar</span>
            <span class="spec-val" id="mDim"></span>
          </div>
          <div class="spec-line">
            <span class="spec-prop">Material Kayu</span>
            <span class="spec-val" id="mMat"></span>
          </div>
          <div class="spec-line">
            <span class="spec-prop">Standar Finishing</span>
            <span class="spec-val" id="mFin"></span>
          </div>
          <div class="spec-line">
            <span class="spec-prop">Konstruksi</span>
            <span class="spec-val" id="mKon"></span>
          </div>
          <div class="spec-line">
            <span class="spec-prop">Waktu Produksi</span>
            <span class="spec-val" id="mTime"></span>
          </div>
        </div>

        <p class="sheet-desc-text" id="mDesc"></p>

        <a id="mWaBtn" href="#" target="_blank" class="btn-sheet-wa">
          <span>Konsultasi &amp; Penawaran RAB Karya Ini via WhatsApp</span>
        </a>
      </div>
    </div>
  </div>

  <!-- Showcase Engine -->
  <script>
    const flagshipData = {custom_works_json};
    let activeSpace = 'Semua';

    function filterSpace(space) {{
      activeSpace = space;
      document.querySelectorAll('.filter-pill').forEach(btn => {{
        btn.classList.toggle('active', btn.innerText.includes(space));
      }});

      document.querySelectorAll('.showcase-card').forEach(card => {{
        const cardCat = card.getAttribute('data-cat');
        if (space === 'Semua' || cardCat === space) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    function openShowcaseDetail(id) {{
      const item = flagshipData.find(x => x.id === id);
      if (!item) return;

      document.getElementById('mSeries').innerText = item.series;
      document.getElementById('mImg').src = './' + item.img;
      document.getElementById('mCategory').innerText = item.category;
      document.getElementById('mTitle').innerText = item.title;
      document.getElementById('mPrice').innerText = 'Estimasi: ' + item.price_range;
      document.getElementById('mDim').innerText = item.dimensions;
      document.getElementById('mMat').innerText = item.material;
      document.getElementById('mFin').innerText = item.finishing;
      document.getElementById('mKon').innerText = item.construction;
      document.getElementById('mTime').innerText = item.lead_time;
      document.getElementById('mDesc').innerText = item.description;

      const waText = encodeURIComponent(`Halo Rezeki Lancar Furniture, saya tertarik dengan karya custom: ${{item.title}} (${{item.dimensions}}). Mohon rincian RAB workshop & opsi kayu untuk proyek kami.`);
      document.getElementById('mWaBtn').href = `https://wa.me/6281234567890?text=${{waText}}`;

      document.getElementById('showcaseModal').classList.add('active');
      window.history.pushState({{ id: item.id }}, '', '#karya-' + item.id);
    }}

    function closeShowcaseDetail() {{
      document.getElementById('showcaseModal').classList.remove('active');
      if (window.location.hash.startsWith('#karya-')) {{
        window.history.pushState('', '', window.location.pathname);
      }}
    }}

    window.addEventListener('popstate', () => {{
      if (document.getElementById('showcaseModal').classList.contains('active')) {{
        document.getElementById('showcaseModal').classList.remove('active');
      }}
    }});

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape' && document.getElementById('showcaseModal').classList.contains('active')) {{
        closeShowcaseDetail();
      }}
    }});

    // Check hash on load
    if (window.location.hash && window.location.hash.startsWith('#karya-')) {{
      const hId = parseInt(window.location.hash.replace('#karya-', ''));
      if (hId) openShowcaseDetail(hId);
    }}
  </script>
</body>
</html>'''

with open(os.path.join(repo_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(showcase_html)

print("Generated self-hosted flagship showcase index.html successfully!")
