# deploy_unified_navigation.py
import re, glob

def get_header_html(active_hub):
    h = active_hub
    def act(hub):
        return ' active' if h == hub else ''

    return f'''  <header class="site-header">
    <div class="container">
      <nav class="navbar">
        <a href="index.html" class="brand-logo" aria-label="IgniteBiz AI Home">
          <div class="brand-logo-img-wrapper">
            <img src="assets/images/logo.webp?v=5.1" alt="IgniteBiz AI Logo" onerror="this.src=\\'assets/images/logo-resolace.webp\\'">
          </div>
          <div class="brand-title">
            <span class="brand-name">IGNITEBIZ AI</span>
            <span class="brand-subtitle"><span class="neural-pulse-dot"></span>Venture Studio</span>
          </div>
        </a>

        <!-- Desktop Navigation Menu (10 Compact Outcome-Led Hubs) -->
        <ul class="nav-menu">
          <!-- 1. Home -->
          <li class="nav-item">
            <a href="index.html" class="nav-link{act('home')}">
              <span>Home</span>
              <svg class="caret" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="dropdown-menu">
              <a href="index.html#startup-journey" class="dropdown-item">
                <div class="dropdown-item-icon">🗺️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">12-Stage Startup Journey</span>
                    <span class="dropdown-tag">Core Roadmap</span>
                  </div>
                  <div class="dropdown-item-desc">Step-by-step milestone gates from first idea to IPO readiness</div>
                </div>
              </a>
              <a href="index.html#who-we-help" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">👥</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Who We Help (Cohorts)</span>
                  </div>
                  <div class="dropdown-item-desc">Students, aspiring founders, early startups, MSMEs &amp; institutions</div>
                </div>
              </a>
              <a href="index.html#what-you-get" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(40, 104, 232, 0.1); color: #2868e8;">📦</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">What You Get (Venture Hubs)</span>
                  </div>
                  <div class="dropdown-item-desc">Assessment, validation, pitch pack, legal launch, CXOs &amp; scale</div>
                </div>
              </a>
              <a href="index.html#impact" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(255, 107, 53, 0.1); color: #ff6b35;">📈</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Impact &amp; Case Studies</span>
                  </div>
                  <div class="dropdown-item-desc">Verified founder outcomes, milestones &amp; measurable traction</div>
                </div>
              </a>
              <a href="index.html#pricing" class="dropdown-item">
                <div class="dropdown-item-icon">💳</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Plans &amp; Transparent Terms</span>
                  </div>
                  <div class="dropdown-item-desc">Clear inclusions, verified deliverables, and zero hidden lock-ins</div>
                </div>
              </a>
              <a href="index.html#faq" class="dropdown-item">
                <div class="dropdown-item-icon">❓</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">FAQs &amp; Help Desk</span>
                  </div>
                  <div class="dropdown-item-desc">Answers on eligibility, stage gates, data privacy &amp; timelines</div>
                </div>
              </a>
            </div>
          </li>

          <!-- 2. About -->
          <li class="nav-item">
            <a href="about.html" class="nav-link{act('about')}">
              <span>About</span>
              <svg class="caret" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="dropdown-menu">
              <a href="about.html#vision" class="dropdown-item">
                <div class="dropdown-item-icon">🎯</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Mission &amp; Vision</span>
                  </div>
                  <div class="dropdown-item-desc">Empowering 100,000+ founders with AI-powered venture systems</div>
                </div>
              </a>
              <a href="about.html#model" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(40, 104, 232, 0.1); color: #2868e8;">🏛️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Venture Studio Model</span>
                  </div>
                  <div class="dropdown-item-desc">How our studio co-builds ventures with AI workflows &amp; human CXOs</div>
                </div>
              </a>
              <a href="about.html#leadership" class="dropdown-item">
                <div class="dropdown-item-icon">👔</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Leadership &amp; Mentors</span>
                  </div>
                  <div class="dropdown-item-desc">Verified founders, practicing CAs, CSs, and global advisors</div>
                </div>
              </a>
              <a href="about.html#books" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(255, 107, 53, 0.1); color: #ff6b35;">📚</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Books &amp; Publications</span>
                  </div>
                  <div class="dropdown-item-desc">6 definitive volumes on Business Yoga, Society 5.0 &amp; Startups</div>
                </div>
              </a>
              <a href="about.html#impact" class="dropdown-item">
                <div class="dropdown-item-icon">📊</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Ecosystem Impact</span>
                  </div>
                  <div class="dropdown-item-desc">Verified founder cohorts, campus drives &amp; venture incubation</div>
                </div>
              </a>
              <a href="about.html#governance" class="dropdown-item">
                <div class="dropdown-item-icon">🛡️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Trust &amp; Governance</span>
                  </div>
                  <div class="dropdown-item-desc">Data privacy, regulatory boundaries, and ethical standards</div>
                </div>
              </a>
            </div>
          </li>

          <!-- 3. Discover -->
          <li class="nav-item">
            <a href="psychometric-12d.html" class="nav-link{act('discover')}">
              <span>Discover</span>
              <svg class="caret" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="dropdown-menu">
              <a href="psychometric-12d.html" class="dropdown-item">
                <div class="dropdown-item-icon">🧠</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">12-Dimension Evaluation</span>
                    <span class="dropdown-tag">Flagship</span>
                  </div>
                  <div class="dropdown-item-desc">Cognitive, emotional &amp; execution readiness test (₹990)</div>
                </div>
              </a>
              <a href="psychometric-12d.html#sample-report" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(0, 188, 212, 0.12); color: #00bcd4;">📄</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Sample Diagnostic Report</span>
                    <span class="dropdown-tag cyan">Preview</span>
                  </div>
                  <div class="dropdown-item-desc">Illustrative 12-page breakdown of strengths &amp; execution style</div>
                </div>
              </a>
              <a href="psychometric-12d.html#readiness" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">⚡</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Founder Readiness Matrix</span>
                  </div>
                  <div class="dropdown-item-desc">Personalized insights, developmental areas &amp; role matching</div>
                </div>
              </a>
              <a href="psychometric-12d.html#skill-gap" class="dropdown-item">
                <div class="dropdown-item-icon">🧭</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Skill-Gap Action Plan</span>
                  </div>
                  <div class="dropdown-item-desc">Tailored learning sprint &amp; 1-on-1 mentor guidance pathway</div>
                </div>
              </a>
              <a href="iris-test.html" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(255, 107, 53, 0.1); color: #ff6b35;">👁️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Eye 2 I – Iris Analysis Test</span>
                    <span class="dropdown-tag orange">100B Neurons</span>
                  </div>
                  <div class="dropdown-item-desc">Optical nerve cognitive pattern analysis (₹5,555)</div>
                </div>
              </a>
              <a href="psychometric-12d.html#methodology" class="dropdown-item">
                <div class="dropdown-item-icon">⚖️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Methodology &amp; Privacy</span>
                  </div>
                  <div class="dropdown-item-desc">Developmental guidance standard with full user data consent</div>
                </div>
              </a>
            </div>
          </li>

          <!-- 4. Build -->
          <li class="nav-item">
            <a href="business-mastery.html" class="nav-link{act('build')}">
              <span>Build</span>
              <svg class="caret" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="dropdown-menu">
              <a href="business-mastery.html#ideation" class="dropdown-item">
                <div class="dropdown-item-icon">💡</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Find a Business Idea</span>
                  </div>
                  <div class="dropdown-item-desc">Founder-problem fit prompts &amp; market sector discovery</div>
                </div>
              </a>
              <a href="business-mastery.html#validation" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">🔍</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Customer &amp; Demand Validation</span>
                    <span class="dropdown-tag" style="background: rgba(16, 185, 129, 0.15); color: #10b981;">Evidence Gate</span>
                  </div>
                  <div class="dropdown-item-desc">Interview frameworks &amp; willingness-to-pay validation</div>
                </div>
              </a>
              <a href="business-mastery.html#business-model" class="dropdown-item">
                <div class="dropdown-item-icon">📐</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Business Model &amp; Financials</span>
                  </div>
                  <div class="dropdown-item-desc">Pricing strategy, unit economics, CAC/LTV &amp; cash burn model</div>
                </div>
              </a>
              <a href="business-mastery.html#mvp-roadmap" class="dropdown-item">
                <div class="dropdown-item-icon">🚀</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">MVP Roadmap &amp; Architecture</span>
                  </div>
                  <div class="dropdown-item-desc">Lean prototype milestones &amp; iterative launch sprints</div>
                </div>
              </a>
              <a href="business-mastery.html#pitch-deck" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(40, 104, 232, 0.1); color: #2868e8;">📊</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Master Pitch Deck Dossier</span>
                  </div>
                  <div class="dropdown-item-desc">Investor-ready 15-slide master deck &amp; executive teaser</div>
                </div>
              </a>
              <a href="awards.html" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(255, 107, 53, 0.1); color: #ff6b35;">🏆</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Competitions &amp; Grants</span>
                    <span class="dropdown-tag orange">$100k Prize</span>
                  </div>
                  <div class="dropdown-item-desc">Global innovation competitions, incubation &amp; seed awards</div>
                </div>
              </a>
            </div>
          </li>

          <!-- 5. Launch -->
          <li class="nav-item">
            <a href="launch-business.html" class="nav-link{act('launch')}">
              <span>Launch</span>
              <svg class="caret" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="dropdown-menu">
              <a href="launch-business.html#legal-structure" class="dropdown-item">
                <div class="dropdown-item-icon">⚖️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Choose Legal Structure</span>
                  </div>
                  <div class="dropdown-item-desc">Private Limited vs LLP vs OPC — liability &amp; investor readiness</div>
                </div>
              </a>
              <a href="launch-business.html#incorporation" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(40, 104, 232, 0.1); color: #2868e8;">🏢</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Company Incorporation (MCA)</span>
                    <span class="dropdown-tag">SPICe+</span>
                  </div>
                  <div class="dropdown-item-desc">Fast-track name approval, DIN, DSC, MoA/AoA &amp; PAN/TAN</div>
                </div>
              </a>
              <a href="launch-business.html#startup-india" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">🇮🇳</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Startup India / DPIIT</span>
                    <span class="dropdown-tag" style="background: rgba(16, 185, 129, 0.15); color: #10b981;">Tax Holiday</span>
                  </div>
                  <div class="dropdown-item-desc">DPIIT recognition, Section 80-IAC tax holiday &amp; IPR fee rebate</div>
                </div>
              </a>
              <a href="launch-business.html#ipr-patents" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(255, 107, 53, 0.1); color: #ff6b35;">📜</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">IPR, Patents &amp; Trademarks</span>
                  </div>
                  <div class="dropdown-item-desc">Prior-art patent search, trademark filing &amp; copyright security</div>
                </div>
              </a>
              <a href="launch-business.html#licences" class="dropdown-item">
                <div class="dropdown-item-icon">📋</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Licences &amp; Compliance Calendar</span>
                  </div>
                  <div class="dropdown-item-desc">GSTIN, MSME Udyam, annual MCA filings &amp; statutory audit</div>
                </div>
              </a>
              <a href="launch-business.html#banking" class="dropdown-item">
                <div class="dropdown-item-icon">🏦</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Banking &amp; Cloud Accounting</span>
                  </div>
                  <div class="dropdown-item-desc">Zero-balance founder accounts, payment gateways &amp; ERP</div>
                </div>
              </a>
              <a href="launch-business.html#launch-checklist" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(0, 188, 212, 0.12); color: #00bcd4;">✅</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Interactive Launch Checklist</span>
                    <span class="dropdown-tag cyan">Live Tracker</span>
                  </div>
                  <div class="dropdown-item-desc">Track status, documents, CS/CA review &amp; timeline gates</div>
                </div>
              </a>
            </div>
          </li>

          <!-- 6. Funding -->
          <li class="nav-item">
            <a href="investor-partners.html" class="nav-link{act('funding')}">
              <span>Funding</span>
              <svg class="caret" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="dropdown-menu">
              <a href="investor-partners.html#readiness" class="dropdown-item">
                <div class="dropdown-item-icon">📈</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Funding Readiness Diagnostic</span>
                    <span class="dropdown-tag">Fit Gate</span>
                  </div>
                  <div class="dropdown-item-desc">Traction scorecard, cap table review &amp; valuation benchmarks</div>
                </div>
              </a>
              <a href="investor-partners.html#grants" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">🏛️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Grants &amp; Govt Schemes</span>
                  </div>
                  <div class="dropdown-item-desc">SISFS, NIDHI-PRAYAS, BIRAC, MeitY &amp; state innovation funds</div>
                </div>
              </a>
              <a href="investor-partners.html#incubators" class="dropdown-item">
                <div class="dropdown-item-icon">🌱</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Incubators &amp; Accelerators</span>
                  </div>
                  <div class="dropdown-item-desc">Top Tier-1 &amp; Tier-2 incubator programs, dates &amp; application prep</div>
                </div>
              </a>
              <a href="investor-partners.html#investor-intel" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(40, 104, 232, 0.1); color: #2868e8;">🤝</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Investor Intelligence Network</span>
                  </div>
                  <div class="dropdown-item-desc">Verified angel syndicates, seed VCs, family offices &amp; CVCs</div>
                </div>
              </a>
              <a href="investor-partners.html#ai-matching" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(255, 107, 53, 0.1); color: #ff6b35;">🤖</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">AI Matching &amp; Introductions</span>
                  </div>
                  <div class="dropdown-item-desc">Thesis-aligned investor introductions with founder consent</div>
                </div>
              </a>
              <a href="investor-partners.html#data-room" class="dropdown-item">
                <div class="dropdown-item-icon">📁</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Due Diligence Data Room</span>
                  </div>
                  <div class="dropdown-item-desc">Financial models, contracts, MIS &amp; compliance data room</div>
                </div>
              </a>
            </div>
          </li>

          <!-- 7. CXO Services -->
          <li class="nav-item">
            <a href="c-suite.html" class="nav-link{act('cxo')}">
              <span>CXO</span>
              <svg class="caret" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="dropdown-menu">
              <a href="c-suite.html#fractional-cfo" class="dropdown-item">
                <div class="dropdown-item-icon">💰</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Fractional CFO</span>
                    <span class="dropdown-tag">Finance</span>
                  </div>
                  <div class="dropdown-item-desc">Cash flow modeling, burn rate, unit economics &amp; MIS</div>
                </div>
              </a>
              <a href="c-suite.html#fractional-cmo" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(255, 107, 53, 0.1); color: #ff6b35;">📢</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Fractional CMO</span>
                    <span class="dropdown-tag orange">Growth</span>
                  </div>
                  <div class="dropdown-item-desc">Brand positioning, customer acquisition funnel &amp; CAC control</div>
                </div>
              </a>
              <a href="c-suite.html#fractional-cto" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(0, 188, 212, 0.12); color: #00bcd4;">⚡</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Fractional CTO &amp; AI Architect</span>
                  </div>
                  <div class="dropdown-item-desc">Tech stack design, cloud infrastructure &amp; agentic AI workflows</div>
                </div>
              </a>
              <a href="c-suite.html#fractional-coo" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">⚙️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Fractional COO</span>
                  </div>
                  <div class="dropdown-item-desc">Operating cadence, supply chain, delivery SLAs &amp; team KPIs</div>
                </div>
              </a>
              <a href="c-suite.html#fractional-chro" class="dropdown-item">
                <div class="dropdown-item-icon">👥</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Fractional CHRO</span>
                  </div>
                  <div class="dropdown-item-desc">Core team hiring, ESOP pool architecture &amp; high-performance culture</div>
                </div>
              </a>
              <a href="c-suite.html#packages" class="dropdown-item">
                <div class="dropdown-item-icon">📦</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Service Packages &amp; SLAs</span>
                  </div>
                  <div class="dropdown-item-desc">Clear monthly scopes, decision rights, sprint cadences &amp; terms</div>
                </div>
              </a>
            </div>
          </li>

          <!-- 8. Global -->
          <li class="nav-item">
            <a href="global-expansion.html" class="nav-link{act('global')}">
              <span>Global</span>
              <svg class="caret" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="dropdown-menu">
              <a href="global-expansion.html#export-readiness" class="dropdown-item">
                <div class="dropdown-item-icon">🌐</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Export Readiness Diagnostic</span>
                    <span class="dropdown-tag">Audit</span>
                  </div>
                  <div class="dropdown-item-desc">Evaluate capacity, international certifications &amp; transfer pricing</div>
                </div>
              </a>
              <a href="global-expansion.html#country-scorecard" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(40, 104, 232, 0.1); color: #2868e8;">📊</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Country Selection Scorecard</span>
                  </div>
                  <div class="dropdown-item-desc">Target UAE, UK, US, Singapore &amp; EU market-demand benchmark</div>
                </div>
              </a>
              <a href="global-expansion.html#market-entry" class="dropdown-item">
                <div class="dropdown-item-icon">🚀</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Market Entry Strategy</span>
                  </div>
                  <div class="dropdown-item-desc">Wholly Owned Subsidiary vs Joint Venture vs Master Distribution</div>
                </div>
              </a>
              <a href="global-expansion.html#local-partners" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">🤝</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Local Partner Networks</span>
                  </div>
                  <div class="dropdown-item-desc">Vetted local distributors, advisory boards &amp; trade chambers</div>
                </div>
              </a>
              <a href="global-expansion.html#cross-border-compliance" class="dropdown-item">
                <div class="dropdown-item-icon">⚖️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Cross-Border Compliance</span>
                  </div>
                  <div class="dropdown-item-desc">FEMA/RBI compliance, ODI/FDI structuring &amp; international tax</div>
                </div>
              </a>
              <a href="global-expansion.html#operations" class="dropdown-item">
                <div class="dropdown-item-icon">💳</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Multi-Currency Treasury</span>
                  </div>
                  <div class="dropdown-item-desc">Global payment rails, multi-currency accounts &amp; trade logistics</div>
                </div>
              </a>
            </div>
          </li>

          <!-- 9. IPO -->
          <li class="nav-item">
            <a href="ipo-exits.html" class="nav-link{act('ipo')}">
              <span>IPO</span>
              <svg class="caret" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="dropdown-menu">
              <a href="ipo-exits.html#ipo-diagnostic" class="dropdown-item">
                <div class="dropdown-item-icon">🏛️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">IPO Readiness Diagnostic</span>
                    <span class="dropdown-tag">SEBI/BSE</span>
                  </div>
                  <div class="dropdown-item-desc">Eligibility screening across revenue, PAT, net worth &amp; track record</div>
                </div>
              </a>
              <a href="ipo-exits.html#governance" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">🛡️</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Board Governance &amp; Controls</span>
                  </div>
                  <div class="dropdown-item-desc">Independent directors, audit committees &amp; internal financial controls</div>
                </div>
              </a>
              <a href="ipo-exits.html#financial-readiness" class="dropdown-item">
                <div class="dropdown-item-icon">📜</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Financial &amp; Legal Audit Trail</span>
                  </div>
                  <div class="dropdown-item-desc">Restated Ind-AS accounts, peer-review audits &amp; clean diligence</div>
                </div>
              </a>
              <a href="ipo-exits.html#qualified-advisers" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(40, 104, 232, 0.1); color: #2868e8;">👔</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Merchant Banker Syndicate</span>
                  </div>
                  <div class="dropdown-item-desc">SEBI-registered merchant bankers, underwriters &amp; legal counsel</div>
                </div>
              </a>
              <a href="ipo-exits.html#strategic-exits" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(255, 107, 53, 0.1); color: #ff6b35;">🤝</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Strategic Exits &amp; M&amp;A</span>
                  </div>
                  <div class="dropdown-item-desc">Trade sale acquisitions, private equity buyouts &amp; secondaries</div>
                </div>
              </a>
              <a href="ipo-exits.html#ipo-roadmap" class="dropdown-item">
                <div class="dropdown-item-icon">📅</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">180-Day Listing Roadmap</span>
                  </div>
                  <div class="dropdown-item-desc">DRHP drafting, exchange in-principle approval to bell ringing</div>
                </div>
              </a>
            </div>
          </li>

          <!-- 10. Partners -->
          <li class="nav-item">
            <a href="institutional-partners.html" class="nav-link{act('institutional')}">
              <span>Partners</span>
              <svg class="caret" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="dropdown-menu">
              <a href="institutional-partners.html#universities" class="dropdown-item">
                <div class="dropdown-item-icon">🎓</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Universities &amp; Colleges</span>
                    <span class="dropdown-tag">Campus</span>
                  </div>
                  <div class="dropdown-item-desc">E-Cell acceleration, NIRF/NAAC innovation score &amp; student ventures</div>
                </div>
              </a>
              <a href="institutional-partners.html#coaching-institutes" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(255, 107, 53, 0.1); color: #ff6b35;">🎯</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Coaching &amp; EdTech</span>
                  </div>
                  <div class="dropdown-item-desc">Entrepreneurial mindset bootcamps &amp; psychometric diagnostic drives</div>
                </div>
              </a>
              <a href="institutional-partners.html#incubators-ecells" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">🏢</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Incubators &amp; Tech Parks</span>
                  </div>
                  <div class="dropdown-item-desc">Pre-seed founder pipeline, shared CXO desks &amp; cohort reporting</div>
                </div>
              </a>
              <a href="institutional-partners.html#associations" class="dropdown-item">
                <div class="dropdown-item-icon">🌐</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Industry Associations</span>
                  </div>
                  <div class="dropdown-item-desc">MSME modernization, export readiness drives &amp; trade challenges</div>
                </div>
              </a>
              <a href="institutional-partners.html#corporate-innovation" class="dropdown-item">
                <div class="dropdown-item-icon" style="background: rgba(40, 104, 232, 0.1); color: #2868e8;">🏭</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Corporate Innovation &amp; CSR</span>
                  </div>
                  <div class="dropdown-item-desc">Problem-statement challenges, proof-of-concept trials &amp; CSR grants</div>
                </div>
              </a>
              <a href="institutional-partners.html#mentor-onboard" class="dropdown-item">
                <div class="dropdown-item-icon">🤝</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">Mentor &amp; Provider Onboarding</span>
                  </div>
                  <div class="dropdown-item-desc">Credential verification, sector matching &amp; transparent standards</div>
                </div>
              </a>
              <a href="institutional-partners.html#cohort-calendar" class="dropdown-item">
                <div class="dropdown-item-icon">📅</div>
                <div class="dropdown-item-content">
                  <div class="dropdown-item-title-row">
                    <span class="dropdown-item-title">90-Day Cohort Calendar</span>
                  </div>
                  <div class="dropdown-item-desc">Canvassing &rarr; Validation &rarr; Prototype &rarr; Demo Day roadmap</div>
                </div>
              </a>
            </div>
          </li>
        </ul>

        <!-- Right Action Buttons (Slim & Modern) -->
        <div class="nav-actions">
          <button class="theme-toggle-btn" id="theme-toggle" onclick="toggleTheme()" aria-label="Toggle Light and Dark Mode" title="Toggle Light/Dark Theme">
            <svg class="sun-icon" viewBox="0 0 24 24"><path fill="currentColor" d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58a.996.996 0 00-1.41 0 .996.996 0 000 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41L5.99 4.58zm12.37 12.37a.996.996 0 00-1.41 0 .996.996 0 000 1.41l1.06 1.06c.39.39 1.03.39 1.41 0a.996.996 0 000-1.41l-1.06-1.06zm1.06-10.96a.996.996 0 00-1.41-1.41l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06zM7.05 18.36a.996.996 0 00-1.41-1.41l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06z"/></svg>
            <svg class="moon-icon" viewBox="0 0 24 24"><path fill="currentColor" d="M12.3 2a10 10 0 00-1.9.18 1 1 0 00-.79 1.15 1 1 0 001.09.82A8 8 0 0119.8 11.8a1 1 0 00.8 1.08 1 1 0 001.11-.75A10 10 0 0012.3 2zM9.27 4.49a1 1 0 00-.34.78 10 10 0 1010.6 10.6 1 1 0 00-.76-1.12 1 1 0 00-1.18.43A8 8 0 119.27 4.49z"/></svg>
          </button>
          <a href="https://pt.yotopper.co.in/app/" target="_blank" rel="noopener" class="btn-nav-login">Login</a>
          <button class="btn-nav-start" data-open-modal data-test-name="12-Dimension Psychometric Evaluation Test">
            <span>🚀 Start Journey</span>
          </button>
          <button class="hamburger" aria-label="Toggle mobile menu">
            <svg viewBox="0 0 24 24"><path fill="currentColor" d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
          </button>
        </div>
      </nav>
    </div>
  </header>'''

def get_mobile_drawer_html():
    return '''  <!-- Mobile Drawer Menu (10 Hubs Accordion) -->
  <div class="drawer-overlay"></div>
  <aside class="mobile-drawer">
    <div class="mobile-drawer-header">
      <div class="brand-logo">
        <img src="assets/images/logo.webp?v=5.1" alt="IgniteBiz AI Logo" style="height: 36px;">
        <span style="font-weight: 800; font-size: 1.12rem; color: var(--primary);">IGNITEBIZ AI</span>
      </div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <button class="theme-toggle-btn mobile-theme-toggle" onclick="toggleTheme()" aria-label="Toggle Light and Dark Mode" title="Toggle Light/Dark Theme">
          <svg class="sun-icon" viewBox="0 0 24 24"><path fill="currentColor" d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58a.996.996 0 00-1.41 0 .996.996 0 000 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41L5.99 4.58zm12.37 12.37a.996.996 0 00-1.41 0 .996.996 0 000 1.41l1.06 1.06c.39.39 1.03.39 1.41 0a.996.996 0 000-1.41l-1.06-1.06zm1.06-10.96a.996.996 0 00-1.41-1.41l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06zM7.05 18.36a.996.996 0 00-1.41-1.41l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06z"/></svg>
          <svg class="moon-icon" viewBox="0 0 24 24"><path fill="currentColor" d="M12.3 2a10 10 0 00-1.9.18 1 1 0 00-.79 1.15 1 1 0 001.09.82A8 8 0 0119.8 11.8a1 1 0 00.8 1.08 1 1 0 001.11-.75A10 10 0 0012.3 2zM9.27 4.49a1 1 0 00-.34.78 10 10 0 1010.6 10.6 1 1 0 00-.76-1.12 1 1 0 00-1.18.43A8 8 0 119.27 4.49z"/></svg>
        </button>
        <button class="close-drawer" aria-label="Close menu">&times;</button>
      </div>
    </div>
    
    <div class="mobile-nav-list">
      <!-- 1. Home -->
      <div class="mobile-nav-item">
        <div class="mobile-nav-link mobile-submenu-toggle">
          <span>1. Home</span>
          <span class="caret-icon">&darr;</span>
        </div>
        <div class="mobile-submenu">
          <a href="index.html">Overview</a>
          <a href="index.html#startup-journey">12-Stage Startup Journey</a>
          <a href="index.html#who-we-help">Who We Help (Cohorts)</a>
          <a href="index.html#what-you-get">What You Get (Venture Hubs)</a>
          <a href="index.html#impact">Impact &amp; Stories</a>
          <a href="index.html#pricing">Plans &amp; Terms</a>
          <a href="index.html#faq">FAQs &amp; Help Desk</a>
        </div>
      </div>

      <!-- 2. About & Ecosystem -->
      <div class="mobile-nav-item">
        <div class="mobile-nav-link mobile-submenu-toggle">
          <span>2. About &amp; Ecosystem</span>
          <span class="caret-icon">&darr;</span>
        </div>
        <div class="mobile-submenu">
          <a href="about.html">About Overview</a>
          <a href="about.html#vision">Mission &amp; Vision</a>
          <a href="about.html#model">Venture Studio Model</a>
          <a href="about.html#leadership">Leadership &amp; Mentors</a>
          <a href="about.html#books">Books &amp; Publications</a>
          <a href="about.html#impact">Ecosystem Impact</a>
          <a href="about.html#governance">Trust &amp; Governance</a>
        </div>
      </div>

      <!-- 3. Discover Yourself -->
      <div class="mobile-nav-item">
        <div class="mobile-nav-link mobile-submenu-toggle">
          <span>3. Discover Yourself</span>
          <span class="caret-icon">&darr;</span>
        </div>
        <div class="mobile-submenu">
          <a href="psychometric-12d.html">12-Dimension Evaluation</a>
          <a href="psychometric-12d.html#sample-report">Sample Diagnostic Report</a>
          <a href="psychometric-12d.html#readiness">Founder Readiness Matrix</a>
          <a href="psychometric-12d.html#skill-gap">Skill-Gap Action Plan</a>
          <a href="iris-test.html">Eye 2 I – Iris Analysis Test</a>
          <a href="psychometric-12d.html#methodology">Methodology &amp; Privacy</a>
        </div>
      </div>

      <!-- 4. Build Your Startup -->
      <div class="mobile-nav-item">
        <div class="mobile-nav-link mobile-submenu-toggle">
          <span>4. Build Your Startup</span>
          <span class="caret-icon">&darr;</span>
        </div>
        <div class="mobile-submenu">
          <a href="business-mastery.html">Business Mastery with AI</a>
          <a href="business-mastery.html#ideation">Find a Business Idea</a>
          <a href="business-mastery.html#validation">Customer Validation</a>
          <a href="business-mastery.html#business-model">Business Model &amp; Financials</a>
          <a href="business-mastery.html#mvp-roadmap">MVP Roadmap</a>
          <a href="business-mastery.html#pitch-deck">Master Pitch Deck</a>
          <a href="awards.html">Global Innovation Awards</a>
        </div>
      </div>

      <!-- 5. Launch Your Business -->
      <div class="mobile-nav-item">
        <div class="mobile-nav-link mobile-submenu-toggle">
          <span>5. Launch Your Business</span>
          <span class="caret-icon">&darr;</span>
        </div>
        <div class="mobile-submenu">
          <a href="launch-business.html">Launch Hub Overview</a>
          <a href="launch-business.html#legal-structure">Choose Legal Structure</a>
          <a href="launch-business.html#incorporation">Company Incorporation (MCA)</a>
          <a href="launch-business.html#startup-india">Startup India / DPIIT</a>
          <a href="launch-business.html#ipr-patents">IPR, Patents &amp; Trademarks</a>
          <a href="launch-business.html#licences">Licences &amp; Compliance Calendar</a>
          <a href="launch-business.html#banking">Banking &amp; Accounting</a>
          <a href="launch-business.html#launch-checklist">Interactive Launch Checklist</a>
        </div>
      </div>

      <!-- 6. Funding & Investors -->
      <div class="mobile-nav-item">
        <div class="mobile-nav-link mobile-submenu-toggle">
          <span>6. Funding &amp; Investors</span>
          <span class="caret-icon">&darr;</span>
        </div>
        <div class="mobile-submenu">
          <a href="investor-partners.html">Funding Platform Overview</a>
          <a href="investor-partners.html#readiness">Funding Readiness Diagnostic</a>
          <a href="investor-partners.html#grants">Grants &amp; Govt Schemes</a>
          <a href="investor-partners.html#incubators">Incubators &amp; Accelerators</a>
          <a href="investor-partners.html#investor-intel">Investor Intelligence</a>
          <a href="investor-partners.html#ai-matching">AI Matching &amp; Introductions</a>
          <a href="investor-partners.html#data-room">Due Diligence Data Room</a>
        </div>
      </div>

      <!-- 7. Digital CXO Services -->
      <div class="mobile-nav-item">
        <div class="mobile-nav-link mobile-submenu-toggle">
          <span>7. Digital CXO Services</span>
          <span class="caret-icon">&darr;</span>
        </div>
        <div class="mobile-submenu">
          <a href="c-suite.html">C-Suite Services Overview</a>
          <a href="c-suite.html#fractional-cfo">Fractional CFO (Finance)</a>
          <a href="c-suite.html#fractional-cmo">Fractional CMO (Growth)</a>
          <a href="c-suite.html#fractional-cto">Fractional CTO &amp; AI Architect</a>
          <a href="c-suite.html#fractional-coo">Fractional COO (Operations)</a>
          <a href="c-suite.html#fractional-chro">Fractional CHRO (Talent)</a>
          <a href="c-suite.html#packages">Service Packages &amp; SLAs</a>
        </div>
      </div>

      <!-- 8. Global Expansion -->
      <div class="mobile-nav-item">
        <div class="mobile-nav-link mobile-submenu-toggle">
          <span>8. Global Expansion</span>
          <span class="caret-icon">&darr;</span>
        </div>
        <div class="mobile-submenu">
          <a href="global-expansion.html">Global Expansion Hub</a>
          <a href="global-expansion.html#export-readiness">Export Readiness Diagnostic</a>
          <a href="global-expansion.html#country-scorecard">Country Selection Scorecard</a>
          <a href="global-expansion.html#market-entry">Market Entry Strategy</a>
          <a href="global-expansion.html#local-partners">Local Partner Networks</a>
          <a href="global-expansion.html#cross-border-compliance">Cross-Border Compliance</a>
          <a href="global-expansion.html#operations">Multi-Currency Treasury</a>
        </div>
      </div>

      <!-- 9. IPO Readiness -->
      <div class="mobile-nav-item">
        <div class="mobile-nav-link mobile-submenu-toggle">
          <span>9. IPO Readiness</span>
          <span class="caret-icon">&darr;</span>
        </div>
        <div class="mobile-submenu">
          <a href="ipo-exits.html">IPO &amp; Exits Overview</a>
          <a href="ipo-exits.html#ipo-diagnostic">IPO Readiness Diagnostic</a>
          <a href="ipo-exits.html#governance">Board Governance &amp; Controls</a>
          <a href="ipo-exits.html#financial-readiness">Financial &amp; Legal Audit Trail</a>
          <a href="ipo-exits.html#qualified-advisers">Merchant Banker Syndicate</a>
          <a href="ipo-exits.html#strategic-exits">Strategic Exits &amp; M&amp;A</a>
          <a href="ipo-exits.html#ipo-roadmap">180-Day Listing Roadmap</a>
        </div>
      </div>

      <!-- 10. Institutional Partners -->
      <div class="mobile-nav-item">
        <div class="mobile-nav-link mobile-submenu-toggle">
          <span>10. Institutional Partners</span>
          <span class="caret-icon">&darr;</span>
        </div>
        <div class="mobile-submenu">
          <a href="institutional-partners.html">Partnerships Overview</a>
          <a href="institutional-partners.html#universities">Universities &amp; Colleges</a>
          <a href="institutional-partners.html#coaching-institutes">Coaching &amp; EdTech</a>
          <a href="institutional-partners.html#incubators-ecells">Incubators &amp; Tech Parks</a>
          <a href="institutional-partners.html#corporate-innovation">Corporate Innovation &amp; CSR</a>
          <a href="institutional-partners.html#mentor-onboard">Mentor Onboarding</a>
          <a href="institutional-partners.html#cohort-calendar">90-Day Cohort Calendar</a>
          <a href="institutional-partners.html#partner-enquiry">Partner Enquiry Form</a>
        </div>
      </div>

      <a href="contact.html" class="mobile-nav-link" style="font-weight: 700; color: var(--primary);">Contact Us</a>
    </div>

    <div style="margin-top: auto; padding-top: 24px; border-top: 1px solid var(--gray-200); display: flex; flex-direction: column; gap: 12px;">
      <a href="https://pt.yotopper.co.in/app/" target="_blank" rel="noopener" class="btn btn-outline" style="width: 100%;">Candidate Login</a>
      <button class="btn btn-primary" style="width: 100%;" data-open-modal data-test-name="12-Dimension Psychometric Evaluation Test">Start Your Journey</button>
    </div>
  </aside>'''

def get_footer_html():
    return '''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="brand-logo" style="margin-bottom: 12px;">
            <img src="assets/images/logo.webp?v=5.1" alt="IgniteBiz AI Logo" onerror="this.src=\\'assets/images/logo-resolace.webp\\'" style="height: 40px; filter: brightness(1.1);">
            <span style="font-weight: 800; font-size: 1.3rem; color: #ffffff;">IGNITEBIZ AI</span>
          </div>
          <p>World's largest AI-powered Digital Venture Studio initiative aimed at transforming potential from first idea to global IPO enterprise.</p>
        </div>
        <div class="footer-col">
          <h4>Venture Hubs</h4>
          <ul class="footer-links">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About &amp; Ecosystem</a></li>
            <li><a href="psychometric-12d.html">Discover Yourself</a></li>
            <li><a href="business-mastery.html">Build Your Startup</a></li>
            <li><a href="launch-business.html">Launch Your Business</a></li>
            <li><a href="contact.html">Contact Us</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Scale &amp; Capital</h4>
          <ul class="footer-links">
            <li><a href="investor-partners.html">Funding &amp; Investors</a></li>
            <li><a href="c-suite.html">Digital CXO Services</a></li>
            <li><a href="global-expansion.html">Global Expansion</a></li>
            <li><a href="ipo-exits.html">IPO &amp; Strategic Exits</a></li>
            <li><a href="institutional-partners.html">Institutional Partners</a></li>
            <li><a href="awards.html">Global Innovation Awards</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Headquarters</h4>
          <p style="font-size: 0.88rem; color: var(--gray-400); margin-bottom: 8px;">
            <strong>Corporate:</strong> 7, Nirav Park, Opp. ICICI Bank, Sevashram Road, Bharuch, Gujarat.
          </p>
          <p style="font-size: 0.88rem; color: var(--gray-400);">
            <strong>Registered:</strong> 1 Goswami Nivas, Opp. IIT Main Gate, Powai, Mumbai.
          </p>
          <p style="font-size: 0.88rem; color: var(--gray-400); margin-top: 8px;">
            <strong>Phone:</strong> +91 92241 85764 / +91 97373 11555
          </p>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="container">
          <div>Copyright &copy; 2026 Excellent Infrastructure Pvt. Ltd. All Rights Reserved.</div>
        </div>
      </div>
    </div>
  </footer>'''

file_hub_map = {
    'index.html': 'home',
    'about.html': 'about',
    'psychometric-12d.html': 'discover',
    'iris-test.html': 'discover',
    'business-mastery.html': 'build',
    'awards.html': 'build',
    'venture-architect.html': 'build',
    'focus-domain.html': 'build',
    'ai-life-manager.html': 'build',
    'ai-general-workshop.html': 'build',
    'launch-business.html': 'launch',
    'investor-partners.html': 'funding',
    'c-suite.html': 'cxo',
    'global-expansion.html': 'global',
    'ipo-exits.html': 'ipo',
    'institutional-partners.html': 'institutional',
    'contact.html': 'none',
}

files = sorted(glob.glob('*.html'))
for fn in files:
    hub = file_hub_map.get(fn, 'none')
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    header_html = get_header_html(hub)
    drawer_html = get_mobile_drawer_html()
    footer_html = get_footer_html()

    c = re.sub(r'<header class="site-header"[^>]*>.*?</header>', header_html, c, flags=re.DOTALL)
    c = re.sub(r'<div class="drawer-overlay"></div>\s*<aside class="mobile-drawer"[^>]*>.*?</aside>', drawer_html, c, flags=re.DOTALL)
    c = re.sub(r'<footer class="site-footer"[^>]*>.*?</footer>', footer_html, c, flags=re.DOTALL)
    c = re.sub(r'\?v=\d+\.\d+', '?v=5.1', c)

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f'Compacted header in {fn:28} (Active: {hub})')

print('All 17 HTML files successfully compressed and upgraded!')
