/**
 * IGNITE BIZ AI - INTERACTIVE JAVASCRIPT
 * Replica of https://ignitebizai.com/
 */

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initNavbar();
  initFaqAccordion();
  initContactForm();
  initModal();
  initCounters();
  initImageFallbacks();
  initNeuralCanvas();
  initBrainExplorer();
  initBrainwaveHarmonizer();
  initMiniBrainScan();
  initPublications();
});

/* ==========================================================================
   0. THEME SWITCHER (DARK & LIGHT MODE)
   ========================================================================== */
function initThemeToggle() {
  function getPreferredTheme() {
    const saved = localStorage.getItem('ignitebiz_theme');
    if (saved) return saved;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    if (document.body) document.body.setAttribute('data-theme', theme);
    try {
      localStorage.setItem('ignitebiz_theme', theme);
    } catch (e) {}
    
    const isDark = (theme === 'dark');
    document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
      btn.setAttribute('title', isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode');
      btn.setAttribute('aria-label', isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode');
    });

    window.dispatchEvent(new CustomEvent('themechanged', { detail: { theme } }));
  }

  window.toggleTheme = function() {
    const current = document.documentElement.getAttribute('data-theme') || 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    applyTheme(next);
  };

  // Add click listener as backup (if not already handled by inline onclick)
  document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
    if (!btn.getAttribute('onclick')) {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        window.toggleTheme();
      });
    }
  });

  // Ensure current theme matches state
  const initialTheme = document.documentElement.getAttribute('data-theme') || getPreferredTheme();
  applyTheme(initialTheme);

  // Listen to OS theme changes if user hasn't explicitly set preference
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('ignitebiz_theme')) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });
}

/* ==========================================================================
   1. NAVBAR & MOBILE DRAWER
   ========================================================================== */
function initNavbar() {
  const header = document.querySelector('.site-header');
  const hamburger = document.querySelector('.hamburger');
  const drawer = document.querySelector('.mobile-drawer');
  const overlay = document.querySelector('.drawer-overlay');
  const closeBtn = document.querySelector('.close-drawer');

  // Sticky header shadow on scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  });

  // Toggle drawer
  function openDrawer() {
    drawer?.classList.add('open');
    overlay?.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer?.classList.remove('open');
    overlay?.classList.remove('active');
    document.body.style.overflow = '';
  }

  hamburger?.addEventListener('click', openDrawer);
  closeBtn?.addEventListener('click', closeDrawer);
  overlay?.addEventListener('click', closeDrawer);

  // Mobile submenu accordion
  const submenuToggles = document.querySelectorAll('.mobile-submenu-toggle');
  submenuToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      const parent = toggle.closest('.mobile-nav-item');
      const submenu = parent?.querySelector('.mobile-submenu');
      const caret = toggle.querySelector('.caret-icon');
      
      if (submenu) {
        submenu.classList.toggle('show');
        if (caret) {
          caret.style.transform = submenu.classList.contains('show') ? 'rotate(180deg)' : 'rotate(0deg)';
        }
      }
    });
  });
}

/* ==========================================================================
   2. FAQ ACCORDION
   ========================================================================== */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    if (question && answer) {
      question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');

        // Close other items
        faqItems.forEach(otherItem => {
          if (otherItem !== item) {
            otherItem.classList.remove('active');
            const otherAnswer = otherItem.querySelector('.faq-answer');
            if (otherAnswer) otherAnswer.style.maxHeight = null;
          }
        });

        // Toggle current item
        if (!isActive) {
          item.classList.add('active');
          answer.style.maxHeight = answer.scrollHeight + 'px';
        } else {
          item.classList.remove('active');
          answer.style.maxHeight = null;
        }
      });
    }
  });

  // Open the first item by default if exists
  if (faqItems.length > 0) {
    const firstItem = faqItems[0];
    const firstAnswer = firstItem.querySelector('.faq-answer');
    firstItem.classList.add('active');
    if (firstAnswer) firstAnswer.style.maxHeight = firstAnswer.scrollHeight + 'px';
  }
}

/* ==========================================================================
   3. CONTACT FORM WITH TOAST NOTIFICATION
   ========================================================================== */
function initContactForm() {
  const forms = document.querySelectorAll('.contact-form-element');

  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = form.querySelector('[name="name"]')?.value || '';
      const email = form.querySelector('[name="email"]')?.value || '';
      const submitBtn = form.querySelector('button[type="submit"]');

      if (!name || !email) {
        showToast('Please fill in required fields (Name & Email).', 'error');
        return;
      }

      if (submitBtn) {
        submitBtn.disabled = true;
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = `<span>Submitting...</span>`;

        setTimeout(() => {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalText;
          form.reset();
          showToast('Thank you! Your inquiry has been submitted successfully. Our team will contact you soon.', 'success');
          
          // Close modal if open
          const modal = document.querySelector('.modal-overlay.open');
          if (modal) {
            modal.classList.remove('open');
          }
        }, 1200);
      }
    });
  });
}

function showToast(message, type = 'success') {
  let toast = document.querySelector('.toast-notice');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'toast-notice';
    document.body.appendChild(toast);
  }

  const icon = type === 'success' ? '✓ ' : '⚠ ';
  toast.innerHTML = `<span>${icon}${message}</span>`;
  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, 4500);
}

/* ==========================================================================
   4. MODAL POPUP (QUICK ASSESSMENT BOOKING)
   ========================================================================== */
function initModal() {
  let modal = document.querySelector('.modal-overlay');
  
  if (!modal) {
    modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
      <div class="modal-content">
        <button class="modal-close-btn" aria-label="Close modal">&times;</button>
        <span class="section-tag">Instant Booking</span>
        <h3 style="margin-bottom: 8px;">Register for Psychometric Assessment</h3>
        <p style="color: var(--gray-500); font-size: 0.92rem; margin-bottom: 20px;">
          Choose your test and enter your details to receive immediate portal access and your ₹70,000 bonus kit.
        </p>
        <form class="contact-form-element">
          <div class="form-group">
            <label class="form-label">Selected Assessment</label>
            <select name="test_interest" class="form-control">
              <option value="12-Dimension Psychometric Evaluation Test">12-Dimension Evaluation Test (₹990 / $15)</option>
              <option value="Eye 2 I Iris Analysis Test">Eye 2 I – Iris Analysis Test (₹5,555 / $59)</option>
              <option value="Both Tests Combo">Comprehensive Dual Assessment Combo</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">Full Name <span class="req">*</span></label>
            <input type="text" name="name" class="form-control" placeholder="Candidate Name" required>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label class="form-label">Email Address <span class="req">*</span></label>
              <input type="email" name="email" class="form-control" placeholder="name@email.com" required>
            </div>
            <div class="form-group">
              <label class="form-label">Mobile Number <span class="req">*</span></label>
              <input type="tel" name="phone" class="form-control" placeholder="+91 XXXXX XXXXX" required>
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">Category</label>
            <select name="category" class="form-control">
              <option value="Student">Student (High School / College)</option>
              <option value="Aspiring Founder">Aspiring Entrepreneur / Founder</option>
              <option value="Working Professional">Working Professional / Tech Specialist</option>
              <option value="Parent / Teacher">Parent or Educator</option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary btn-round" style="width: 100%; margin-top: 10px;">
            Proceed to Secure Portal &rarr;
          </button>
        </form>
      </div>
    `;
    document.body.appendChild(modal);
    
    // Bind form submission for newly created modal
    const newForm = modal.querySelector('.contact-form-element');
    if (newForm) {
      newForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const submitBtn = newForm.querySelector('button[type="submit"]');
        if (submitBtn) {
          submitBtn.disabled = true;
          const origText = submitBtn.innerHTML;
          submitBtn.innerHTML = '<span>Submitting...</span>';
          setTimeout(() => {
            submitBtn.disabled = false;
            submitBtn.innerHTML = origText;
            newForm.reset();
            showToast('Thank you! Your registration has been submitted. Our team will contact you shortly.', 'success');
            modal.classList.remove('open');
            document.body.style.overflow = '';
          }, 1200);
        }
      });
    }
  }

  const openButtons = document.querySelectorAll('[data-open-modal]');
  const closeBtn = modal.querySelector('.modal-close-btn');

  openButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const testName = btn.getAttribute('data-test-name') || '12-Dimension Psychometric Evaluation Test';
      const testSelect = modal.querySelector('[name="test_interest"]');
      if (testSelect) {
        testSelect.value = testName;
      }
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  function closeModal() {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  }

  closeBtn?.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });
}

/* ==========================================================================
   5. NUMBER COUNTERS ANIMATION
   ========================================================================== */
function initCounters() {
  const counters = document.querySelectorAll('.animate-counter');
  let hasAnimated = false;

  function runCounters() {
    counters.forEach(counter => {
      const target = parseInt(counter.getAttribute('data-target') || '0', 10);
      const prefix = counter.getAttribute('data-prefix') || '';
      const suffix = counter.getAttribute('data-suffix') || '';
      const duration = 2000;
      const stepTime = 30;
      const totalSteps = duration / stepTime;
      const increment = target / totalSteps;
      let current = 0;

      const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
          counter.textContent = prefix + target.toLocaleString() + suffix;
          clearInterval(timer);
        } else {
          counter.textContent = prefix + Math.floor(current).toLocaleString() + suffix;
        }
      }, stepTime);
    });
  }

  // Use Intersection Observer if available
  if ('IntersectionObserver' in window && counters.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !hasAnimated) {
          hasAnimated = true;
          runCounters();
        }
      });
    }, { threshold: 0.2 });

    const firstCounterParent = counters[0].closest('.section, .metrics-strip') || counters[0];
    observer.observe(firstCounterParent);
  } else {
    runCounters();
  }
}

/* ==========================================================================
   6. IMAGE ERROR FALLBACKS
   ========================================================================== */
function initImageFallbacks() {
  const images = document.querySelectorAll('img');
  images.forEach(img => {
    img.addEventListener('error', function() {
      // Fallback placeholder if local or remote asset is missing
      if (!this.getAttribute('data-fallback-applied')) {
        this.setAttribute('data-fallback-applied', 'true');
        this.src = 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80';
      }
    });
  });
}

/* ==========================================================================
   7. INTERACTIVE GLOBAL NEURAL SYNAPSE CANVAS (ALL WHITE BACKGROUNDS)
   ========================================================================== */
function initNeuralCanvas() {
  let canvas = document.getElementById('global-neural-canvas');
  if (!canvas) {
    canvas = document.createElement('canvas');
    canvas.id = 'global-neural-canvas';
    canvas.className = 'global-neural-canvas';
    document.body.prepend(canvas);
  } else { canvas.classList.add('global-neural-canvas'); }

  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  let mouse = {
    targetX: null,
    targetY: null,
    x: null,
    y: null,
    maxDist: 175,
    isOverDark: false,
    alpha: 0
  };

  let ripples = [];

  class Ripple {
    constructor(x, y) {
      this.x = x;
      this.y = y;
      this.radius = 4;
      this.maxRadius = 60;
      this.alpha = 0.45;
    }
    update() {
      this.radius += 2.2;
      this.alpha -= 0.018;
    }
    draw() {
      if (this.alpha <= 0) return;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.strokeStyle = `rgba(0, 188, 212, ${Math.max(0, this.alpha * 0.35)})`;
      ctx.lineWidth = 1.2;
      ctx.stroke();
    }
  }

  window.addEventListener('mousemove', (e) => {
    mouse.targetX = e.clientX;
    mouse.targetY = e.clientY;

    const el = document.elementFromPoint(e.clientX, e.clientY);
    const isDarkTheme = document.documentElement.getAttribute('data-theme') === 'dark';
    if (!isDarkTheme && el && el.closest('.section-dark, .brain-explorer-section, .site-footer')) {
      mouse.isOverDark = true;
    } else {
      mouse.isOverDark = false;
    }
  });

  window.addEventListener('mouseleave', () => {
    mouse.targetX = null;
    mouse.targetY = null;
    mouse.isOverDark = false;
  });

  window.addEventListener('click', (e) => {
    const el = document.elementFromPoint(e.clientX, e.clientY);
    const isDarkTheme = document.documentElement.getAttribute('data-theme') === 'dark';
    if (isDarkTheme || (!el || !el.closest('.section-dark, .brain-explorer-section, .site-footer'))) {
      ripples.push(new Ripple(e.clientX, e.clientY));
    }
  });

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    initParticles();
  });

  const particleCount = Math.min(95, Math.max(50, Math.floor((width * height) / 16000)));
  let particles = [];

  class Particle {
    constructor() {
      this.reset();
    }
    reset() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.vx = (Math.random() - 0.5) * 0.65;
      this.vy = (Math.random() - 0.5) * 0.65;
      this.radius = Math.random() * 1.5 + 1.2;
      this.baseAlpha = Math.random() * 0.3 + 0.45;
      this.pulse = Math.random() * Math.PI * 2;
      const rand = Math.random();
      this.colorType = rand > 0.72 ? 'orange' : (rand > 0.55 ? 'indigo' : 'cyan');
    }
    update() {
      this.x += this.vx;
      this.y += this.vy;
      this.pulse += 0.025;

      if (this.x < 0) this.x = width;
      if (this.x > width) this.x = 0;
      if (this.y < 0) this.y = height;
      if (this.y > height) this.y = 0;

      // Mouse gentle smooth attraction when over light background
      if (mouse.x !== null && mouse.y !== null && mouse.alpha > 0.05) {
        const dx = mouse.x - this.x;
        const dy = mouse.y - this.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < mouse.maxDist && dist > 1) {
          const force = ((mouse.maxDist - dist) / mouse.maxDist) * mouse.alpha;
          this.x += (dx / dist) * force * 0.45;
          this.y += (dy / dist) * force * 0.45;
        }
      }
    }
    draw() {
      const currentAlpha = this.baseAlpha + Math.sin(this.pulse) * 0.15;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);

      if (this.colorType === 'orange') {
        ctx.fillStyle = `rgba(255, 107, 53, ${Math.max(0.2, currentAlpha)})`;
        ctx.shadowColor = '#ff6b35';
      } else if (this.colorType === 'indigo') {
        ctx.fillStyle = `rgba(2, 86, 155, ${Math.max(0.2, currentAlpha)})`;
        ctx.shadowColor = '#0284c7';
      } else {
        ctx.fillStyle = `rgba(0, 188, 212, ${Math.max(0.2, currentAlpha)})`;
        ctx.shadowColor = '#00bcd4';
      }

      ctx.shadowBlur = 5;
      ctx.fill();
      ctx.shadowBlur = 0;
    }
  }

  function initParticles() {
    particles = [];
    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle());
    }
  }

  initParticles();

  function animate() {
    ctx.clearRect(0, 0, width, height);

    // Smooth lerp mouse position for silky momentum
    if (mouse.targetX !== null && mouse.targetY !== null) {
      if (mouse.x === null) {
        mouse.x = mouse.targetX;
        mouse.y = mouse.targetY;
      } else {
        mouse.x += (mouse.targetX - mouse.x) * 0.16;
        mouse.y += (mouse.targetY - mouse.y) * 0.16;
      }
      const targetAlpha = mouse.isOverDark ? 0 : 1;
      mouse.alpha += (targetAlpha - mouse.alpha) * 0.12;
    } else {
      mouse.alpha += (0 - mouse.alpha) * 0.12;
      if (mouse.alpha < 0.01) {
        mouse.x = null;
        mouse.y = null;
      }
    }

    // Draw ripples
    for (let r = ripples.length - 1; r >= 0; r--) {
      ripples[r].update();
      ripples[r].draw();
      if (ripples[r].alpha <= 0 || ripples[r].radius >= ripples[r].maxRadius) {
        ripples.splice(r, 1);
      }
    }

    // Draw synaptic filaments between particles
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 125) {
          const alpha = (1 - dist / 125) * 0.32;
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          const isDarkTheme = document.documentElement.getAttribute('data-theme') === 'dark';
          ctx.strokeStyle = isDarkTheme ? `rgba(56, 189, 248, ${alpha * 1.35})` : `rgba(2, 132, 199, ${alpha})`;
          ctx.lineWidth = 0.95;
          ctx.stroke();
        }
      }

      // Draw connection to mouse when over white background
      if (mouse.x !== null && mouse.y !== null && mouse.alpha > 0.02) {
        const dx = particles[i].x - mouse.x;
        const dy = particles[i].y - mouse.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < mouse.maxDist) {
          const alpha = (1 - dist / mouse.maxDist) * 0.75 * mouse.alpha;
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(mouse.x, mouse.y);
          ctx.strokeStyle = particles[i].colorType === 'orange'
            ? `rgba(255, 107, 53, ${alpha})`
            : `rgba(0, 188, 212, ${alpha})`;
          ctx.lineWidth = 1.3;
          ctx.stroke();
        }
      }

      particles[i].update();
      particles[i].draw();
    }

    // Draw smooth, soft ambient synaptic glow at cursor (NO circle-around-circle)
    if (mouse.x !== null && mouse.y !== null && mouse.alpha > 0.02) {
      const glowRadius = 22;
      const glow = ctx.createRadialGradient(
        mouse.x, mouse.y, 0,
        mouse.x, mouse.y, glowRadius
      );
      glow.addColorStop(0, `rgba(0, 212, 255, ${0.45 * mouse.alpha})`);
      glow.addColorStop(0.45, `rgba(0, 188, 212, ${0.15 * mouse.alpha})`);
      glow.addColorStop(1, 'rgba(0, 188, 212, 0)');

      ctx.beginPath();
      ctx.arc(mouse.x, mouse.y, glowRadius, 0, Math.PI * 2);
      ctx.fillStyle = glow;
      ctx.fill();

      // Delicate central glowing synaptic node (single smooth dot, no surrounding circle)
      ctx.beginPath();
      ctx.arc(mouse.x, mouse.y, 3, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(0, 229, 255, ${0.9 * mouse.alpha})`;
      ctx.shadowColor = '#00bcd4';
      ctx.shadowBlur = 8;
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    requestAnimationFrame(animate);
  }

  animate();
}

/* ==========================================================================
   8. INTERACTIVE BRAIN COGNITIVE EXPLORER
   ========================================================================== */
function initBrainExplorer() {
  const explorer = document.querySelector('.brain-explorer-section');
  if (!explorer) return;

  const LOBE_DATA = {
    frontal: {
      name: 'Prefrontal Cortex & Frontal Lobe',
      sanskrit: 'अन्तःकरण • Buddhi & Sankalpa',
      hz: '96.4 Hz',
      hzLabel: 'Hyper-Gamma Sync',
      desc: 'The biological command center for long-term vision, strategic risk-taking, hypothesis validation, and executive composure. High synaptic activity here directly correlates with qualification for the Entrepreneurship Track (≥60%).',
      dimensions: [
        'Problem-Solving & Decision Making',
        'Achievement Drive Analysis',
        'Risk Tolerance Assessment',
        'Business Acumen Measurement',
        'Entrepreneurial Mindset Analysis'
      ],
      fitRate: 94,
      fitLabel: '94% Entrepreneurship Track Affinity (Score ≥ 60%)',
      fitNote: 'Primary biological marker for venture founders, innovation architects, and C-Suite strategists.',
      opticalLink: 'Eye 2 I measures retinal nerve fiber thickness connecting to prefrontal dopamine pathways in <60 seconds with 90-100% accuracy.',
      testName: '12-Dimension Psychometric Evaluation Test',
      testBtnText: 'Take 12-Dimension Assessment (₹990)'
    },
    temporal: {
      name: 'Temporal Lobe & Amygdala Interface',
      sanskrit: 'हृदय • Manas & Emotional Resonance',
      hz: '64.8 Hz',
      hzLabel: 'High Beta / Harmonic Theta',
      desc: 'Dictates emotional intelligence (EQ), empathy, interpersonal communication, customer psychology, and cross-cultural syndicate leadership.',
      dimensions: [
        'Emotional Intelligence Assessment',
        'Interpersonal Skills',
        'Creative Expression Skills',
        'Learning Agility Test'
      ],
      fitRate: 88,
      fitLabel: '88% Leadership & Syndicate Harmonization',
      fitNote: 'Essential for co-founder compatibility, negotiation, and Indo-Arab global partnerships.',
      opticalLink: 'Pupillary dynamics and iris stroma density reveal autonomic nervous system balance and emotional resilience.',
      testName: '12-Dimension Psychometric Evaluation Test',
      testBtnText: 'Test Emotional Intelligence (₹990)'
    },
    parietal: {
      name: 'Parietal Lobe & Sensory Integration',
      sanskrit: 'धारणा • Dhyana & Precision',
      hz: '78.2 Hz',
      hzLabel: 'Coherent Beta Firing',
      desc: 'Processes complex spatial analytics, quantitative modeling, sensory integration, and operational rapid-learning loops. Core driver for mastery in high-income tech skills.',
      dimensions: [
        'Learning Agility Test',
        'Operational Skills Analysis',
        'Organizational Skills',
        'Financial Risk Assessment'
      ],
      fitRate: 91,
      fitLabel: '91% Skill Track Mastery (Industry 5.0)',
      fitNote: 'Ideal for AI/ML, Cloud Architecture, Cybersecurity, and Fractional CXO operations.',
      opticalLink: 'Scanned via the middle ciliary zone of the iris, reflecting neuro-muscular processing speed.',
      testName: '12-Dimension Psychometric Evaluation Test',
      testBtnText: 'Assess Operational Agility (₹990)'
    },
    occipital: {
      name: 'Occipital Lobe & Optical Nerve Conduit',
      sanskrit: 'नेत्र • Drishti & Prajna',
      hz: '104.5 Hz',
      hzLabel: 'Optical Nerve Bio-Resonance',
      desc: 'The only direct window from the exterior world into the brain. Because the optic nerve is brain tissue, Eye 2 I scans 100 Billion Neurons to reveal innate pre-natal talents.',
      dimensions: [
        'Pre-natal Unique Abilities',
        'Inherent Natural Talent',
        'Brain Lobe Strength & Polish Areas',
        'Cognitive Processing Speed'
      ],
      fitRate: 99,
      fitLabel: '99.4% Optical Iris Diagnostic Match',
      fitNote: 'Innovated by Dr. Sanjay Gautam, affiliated with American Research Institute of Dermis & Genetic Evaluation, USA.',
      opticalLink: 'The nerve directly connecting eyes with the cerebral cortex. Eye micro-movements are mandatory for every cognitive thought.',
      testName: 'Eye 2 I Iris Analysis Test',
      testBtnText: 'Book Eye 2 I Iris Scan (₹5,555)'
    },
    cerebellum: {
      name: 'Cerebellum & Motor Axis (Business Yoga)',
      sanskrit: 'योग • Karma & Sthiti (Equanimity)',
      hz: '52.0 Hz',
      hzLabel: 'Synchronized Alpha-Beta Wave',
      desc: 'The neuromuscular foundation of Business Yoga with AI. Transforms high-pressure decisions into fluid, intuitive execution habits and calm operational perseverance.',
      dimensions: [
        'Operational Resilience',
        'Organizational Execution',
        'Habit Automation & Focus',
        'Sustained Problem-Solving'
      ],
      fitRate: 90,
      fitLabel: '90% Fractional CXO Execution Power',
      fitNote: 'Prepares founders and executives to sustain high-growth execution without cognitive burnout.',
      opticalLink: 'Stabilized autonomic iris sphincter reflexes signify neurological parasympathetic mastery.',
      testName: '12-Dimension Psychometric Evaluation Test',
      testBtnText: 'Assess Executive Resilience (₹990)'
    }
  };

  const tabs = explorer.querySelectorAll('.lobe-tab-btn');
  const lobePaths = explorer.querySelectorAll('.brain-lobe-path');

  const titleEl = explorer.querySelector('.telemetry-title');
  const sanskritEl = explorer.querySelector('.telemetry-sanskrit-tag');
  const hzEl = explorer.querySelector('.hz-value');
  const hzLabelEl = explorer.querySelector('.hz-label');
  const descEl = explorer.querySelector('.telemetry-desc');
  const tagsContainer = explorer.querySelector('.telemetry-tags-list');
  const fitFill = explorer.querySelector('.track-fit-bar-fill');
  const fitLabel = explorer.querySelector('.track-fit-label');
  const fitNote = explorer.querySelector('.track-fit-note');
  const opticalNote = explorer.querySelector('.telemetry-optical-note');
  const actionBtn = explorer.querySelector('.telemetry-action-btn');

  function selectLobe(lobeKey) {
    const data = LOBE_DATA[lobeKey];
    if (!data) return;

    // Update active tab buttons
    tabs.forEach(tab => {
      tab.classList.toggle('active', tab.getAttribute('data-lobe') === lobeKey);
    });

    // Update active SVG lobe path
    lobePaths.forEach(path => {
      path.classList.toggle('active', path.getAttribute('data-lobe') === lobeKey);
    });

    // Animate details
    if (titleEl) titleEl.textContent = data.name;
    if (sanskritEl) sanskritEl.textContent = data.sanskrit;
    if (hzEl) hzEl.textContent = data.hz;
    if (hzLabelEl) hzLabelEl.textContent = data.hzLabel;
    if (descEl) descEl.textContent = data.desc;

    // Dimensions list
    if (tagsContainer) {
      tagsContainer.innerHTML = data.dimensions
        .map(dim => `<span class="dim-tag-pill"><span class="dot"></span>${dim}</span>`)
        .join('');
    }

    // Fit meter
    if (fitFill) fitFill.style.width = data.fitRate + '%';
    if (fitLabel) fitLabel.textContent = data.fitLabel;
    if (fitNote) fitNote.textContent = data.fitNote;
    if (opticalNote) opticalNote.textContent = data.opticalLink;

    if (actionBtn) {
      actionBtn.setAttribute('data-test-name', data.testName);
      actionBtn.innerHTML = `<span>${data.testBtnText}</span> &rarr;`;
    }
  }

  // Bind clicks
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const lobe = tab.getAttribute('data-lobe');
      if (lobe) selectLobe(lobe);
    });
  });

  lobePaths.forEach(path => {
    path.addEventListener('click', () => {
      const lobe = path.getAttribute('data-lobe');
      if (lobe) selectLobe(lobe);
    });
  });

  // Default select frontal
  selectLobe('frontal');
}

/* ==========================================================================
   9. BRAIN WAVE FREQUENCY HARMONIZER
   ========================================================================== */
function initBrainwaveHarmonizer() {
  const canvas = document.getElementById('brainwave-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  const wrapper = canvas.parentElement;
  let width = (canvas.width = wrapper?.offsetWidth || 700);
  let height = (canvas.height = 140);

  window.addEventListener('resize', () => {
    if (wrapper) {
      width = canvas.width = wrapper.offsetWidth;
      height = canvas.height = wrapper.offsetHeight || 140;
    }
  });

  const MODES = {
    gamma: { freq: 0.08, speed: 0.12, amp: 26, label: 'Gamma (40 Hz) - Peak Synthesis & Venture Pitch', color: '#ff6b35' },
    beta: { freq: 0.045, speed: 0.08, amp: 22, label: 'Beta (20 Hz) - Analytical Focus & Execution', color: '#00bcd4' },
    alpha: { freq: 0.025, speed: 0.045, amp: 34, label: 'Alpha (10 Hz) - Business Yoga State & Mind-Machine Flow', color: '#38bdf8' },
    theta: { freq: 0.012, speed: 0.025, amp: 44, label: 'Theta (6 Hz) - Deep Intuition & Pre-natal Potential', color: '#a855f7' }
  };

  let currentMode = 'alpha';
  const overlay = document.querySelector('.brainwave-canvas-overlay');
  const tabs = document.querySelectorAll('.brainwave-tab');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const mode = tab.getAttribute('data-mode');
      if (mode && MODES[mode]) {
        currentMode = mode;
        if (overlay) overlay.textContent = MODES[mode].label;
      }
    });
  });

  let step = 0;
  function drawWave() {
    ctx.clearRect(0, 0, width, height);
    const cfg = MODES[currentMode] || MODES.alpha;
    step += cfg.speed;

    const centerY = height / 2;

    // Glowing main wave
    ctx.beginPath();
    ctx.lineWidth = 3;
    ctx.strokeStyle = cfg.color;
    ctx.shadowColor = cfg.color;
    ctx.shadowBlur = 12;

    for (let x = 0; x < width; x++) {
      const y = centerY + Math.sin(x * cfg.freq + step) * cfg.amp * Math.sin(x * 0.005 + step * 0.2);
      if (x === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Secondary subtle harmonic wave
    ctx.beginPath();
    ctx.lineWidth = 1.2;
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)';
    ctx.shadowBlur = 0;
    for (let x = 0; x < width; x += 2) {
      const y2 = centerY + Math.cos(x * cfg.freq * 1.5 - step * 0.8) * (cfg.amp * 0.45);
      if (x === 0) ctx.moveTo(x, y2);
      else ctx.lineTo(x, y2);
    }
    ctx.stroke();

    requestAnimationFrame(drawWave);
  }

  drawWave();
}

/* ==========================================================================
   10. 60-SECOND COGNITIVE MINI-SCAN
   ========================================================================== */
function initMiniBrainScan() {
  const card = document.querySelector('.cognitive-miniscan-card');
  if (!card) return;

  const steps = card.querySelectorAll('.miniscan-step');
  const optionBtns = card.querySelectorAll('.miniscan-option-btn');
  const scoreResult = card.querySelector('.miniscan-score-display');
  const trackResult = card.querySelector('.miniscan-track-display');
  const lobeResult = card.querySelector('.miniscan-lobe-display');
  const restartBtn = card.querySelector('.miniscan-restart-btn');

  let currentStep = 1;
  let entrepreneurPoints = 0;
  let skillPoints = 0;

  function showStep(stepNum) {
    steps.forEach(s => s.classList.remove('active'));
    const target = card.querySelector(`.miniscan-step[data-step="${stepNum}"]`);
    if (target) target.classList.add('active');
  }

  optionBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const type = btn.getAttribute('data-type');
      if (type === 'entrepreneur') {
        entrepreneurPoints += 30;
      } else {
        skillPoints += 30;
      }

      currentStep++;
      if (currentStep <= 3) {
        showStep(currentStep);
      } else {
        // Compute outcome
        const total = entrepreneurPoints + skillPoints || 1;
        const scorePercent = Math.min(95, Math.max(55, Math.round((entrepreneurPoints / total) * 100)));

        if (scoreResult) scoreResult.textContent = `${scorePercent}%`;

        if (scorePercent >= 60) {
          if (trackResult) {
            trackResult.innerHTML = `<span style="color: #ff9d76; font-weight: 700;">🚀 Entrepreneurship Track (≥60%)</span>`;
          }
          if (lobeResult) {
            lobeResult.textContent = 'Dominant: Prefrontal Cortex (Executive Strategy & Venture Architecture)';
          }
        } else {
          if (trackResult) {
            trackResult.innerHTML = `<span style="color: #38bdf8; font-weight: 700;">⚙ Skill Development Track (<60%)</span>`;
          }
          if (lobeResult) {
            lobeResult.textContent = 'Dominant: Parietal Sensory & Analytical Cortex (High-Income Future Tech)';
          }
        }

        showStep('result');
      }
    });
  });

  restartBtn?.addEventListener('click', () => {
    currentStep = 1;
    entrepreneurPoints = 0;
    skillPoints = 0;
    showStep(1);
  });
}


/* ==========================================================================
   11. PUBLICATIONS & BOOKS INTERACTIVE MODULE
   ========================================================================== */
function initPublications() {
  const filterBtns = document.querySelectorAll('.pub-filter-btn');
  const bookCards = document.querySelectorAll('.book-card-rich');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const category = btn.getAttribute('data-filter');
      
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      bookCards.forEach(card => {
        const cardCat = card.getAttribute('data-category') || '';
        if (category === 'all' || cardCat.includes(category)) {
          card.style.display = 'flex';
          card.style.opacity = '0';
          card.style.transform = 'translateY(8px)';
          setTimeout(() => {
            card.style.transition = 'all 0.3s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 30);
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Modal Preview Handlers
  const previewBtns = document.querySelectorAll('[data-open-book-modal]');
  const bookModal = document.getElementById('book-preview-modal');
  const bookModalClose = bookModal?.querySelector('.book-modal-close');

  const bookData = {
    'ai-ml': {
      title: 'Anybody Can Use AI / ML',
      author: 'Pritish Mahajan',
      vol: 'VOL. 01',
      cover: 'assets/images/books/book1_anybody_ai.png',
      category: '🤖 AI & Tech Democratization',
      rating: '★★★★★ 4.9 (520+ Reviews on Amazon)',
      badge: 'Amazon Top-10 Bestseller',
      synopsis: 'A comprehensive, plain-English roadmap designed to break through the mathematical intimidation of artificial intelligence. Empowers non-technical founders, students, and professionals to build agentic workflows, harness generative models, and automate operations in under 48 hours.',
      chapters: [
        'Demystifying Machine Learning: Core Models Without Calculus',
        'Generative AI & Agentic Prompt Architectures',
        'Hands-On Industry Case Studies: Retail, Health, Supply Chain & Fintech',
        'Ethical AI Governance & The Society 5.0 Vision'
      ],
      idealFor: 'Entrepreneurs, Domain Specialists, Students, and Corporate Leaders seeking practical AI fluency.'
    },
    'business-yoga': {
      title: 'Business Yoga with AI',
      author: 'Pritish Mahajan & Ashok Jadhav',
      vol: 'VOL. 02',
      cover: 'assets/images/books/book4_business_yoga.png',
      category: '🧘 Venture Philosophy & Studio Model',
      rating: '★★★★★ 5.0 (680+ Reviews across Platforms)',
      badge: 'Flagship Venture Masterwork',
      synopsis: 'The philosophical and operational cornerstone of IgniteBiz AI. Unites ancient Vedic yogic equanimity, breathwork, and mental stamina with hyper-scalable autonomous AI agent architecture to build thriving, sustainable 10x ventures.',
      chapters: [
        'The Business Yoga Philosophy: Sustaining Inner Equanimity at Scale',
        'The Autonomous Venture Studio Architecture: 10x Velocity',
        'Synthesizing Technological Efficiency with Human-Centric Values',
        'Holistic Governance: Building Companies for Society 5.0'
      ],
      idealFor: 'Founders, Venture Builders, CXOs, and Mindful Innovators navigating hyper-growth.'
    },
    'society-5': {
      title: 'Society 5.0 – Vision for Crafting the Future',
      author: 'Ashok Jadhav & Pritish Mahajan',
      vol: 'VOL. 03',
      cover: 'assets/images/books/book3_society_50.png',
      category: '🌏 Future Foresight & Global Macro',
      rating: '★★★★★ 4.9 (410+ Academic Reviews)',
      badge: 'Academic Library Selection',
      synopsis: "A forward-looking strategic manifesto mapping humanity's transition from the Information Age (4.0) into Society 5.0. Demonstrates how cyber-physical systems and ethical artificial intelligence can solve systemic scarcity, enhance human longevity, and democratize wealth creation.",
      chapters: [
        'The Evolution of Human Civilization: From Hunting to Super-Smart Society',
        'Integrating Cyber & Physical Spaces: Real-Time Society Orchestration',
        'Aligning Venture Innovation with the United Nations Sustainable Development Goals',
        'Architecting High-Trust, High-Equity Societal Frameworks'
      ],
      idealFor: 'Policy Makers, Economists, Strategists, and Future-Oriented Founders.'
    },
    '1200-ideas': {
      title: 'Golden Success Skills: 1200+ Ideas Playbook',
      author: 'Priya Sawant, Ashok Jadhav & Pritish Mahajan',
      vol: 'VOL. 04',
      cover: 'assets/images/books/book2_golden_success.png',
      category: '💡 Entrepreneurship & Opportunity Mapping',
      rating: '★★★★★ 5.0 (890+ Founder Endorsements)',
      badge: "Founder's Favorite Toolkit",
      synopsis: 'The definitive encyclopedia of pre-validated business opportunities in the AI era. Categorized across 24 high-growth sectors, this playbook provides unit economics models, addressable market sizing, and a 48-hour MVP execution framework for each concept.',
      chapters: [
        'Micro-SaaS & Specialized Autonomous Agent Opportunities',
        'HealthTech, AgriTech & Clean Energy Frontier Niches',
        'Tier-2 and Tier-3 Regional Arbitrage Opportunities in Emerging Markets',
        'The 48-Hour Rapid MVP Launch and Validation Methodology'
      ],
      idealFor: 'Aspiring Entrepreneurs, Incubator Cohorts, and Corporate Intrapreneurs.'
    },
    'hq-mind': {
      title: 'The Mentoring Playbook & Holistic Mind Mastery',
      author: 'Ashok Jadhav',
      vol: 'VOL. 05',
      cover: 'assets/images/books/book5_mentoring.png',
      category: '🧠 Neuroscience & Cognitive Resilience',
      rating: '★★★★★ 4.9 (340+ Executive Reviews)',
      badge: 'Executive Performance Standard',
      synopsis: 'A cutting-edge neuroscience manual translating the 12-Dimension Cognitive Matrix into actionable daily rituals. Guides leaders in inverting acute stress into kinetic energy, regulating autonomic nervous system tone, and sustaining peak alpha-theta brainwave states.',
      chapters: [
        'Neuroplasticity and the 12-Dimension Holistic Quotient Framework',
        'Stress Inversion: Converting Cortisol Surges into Laser Focus',
        'Biometric Self-Regulation: Heart-Rate Variability & Vagal Nerve Toning',
        'The Daily 15-Minute Neuro-Yogic Cognitive Reset'
      ],
      idealFor: 'High-Stakes Executives, Athletes, Traders, and Founders under continuous cognitive load.'
    },
    'sequa': {
      title: 'Business Idea Validation Framework (SEQUA)',
      author: 'Ashok Jadhav',
      vol: 'VOL. 06',
      cover: 'assets/images/books/book6_business_ideas.png',
      category: '📐 Venture Architecture & Studio Methodology',
      rating: '★★★★★ 4.8 (280+ Studio Evaluations)',
      badge: 'Proprietary Studio Framework',
      synopsis: 'The institutional de-risking methodology engineered by IgniteBiz AI Venture Studio. Implements a 5-gate scientific gating mechanism to mathematically validate customer willingness-to-pay and unit economics before committing venture capital.',
      chapters: [
        'The 5 Gates of SEQUA: Strategic, Economic, Quality, Utility, & Alignment',
        'Quantitative Demand Friction Testing Without Software Development',
        'Pricing Elasticity & Contribution Margin Stress-Testing',
        'Preparing Institutional-Grade Diligence Packages for Tier-1 Investors'
      ],
      idealFor: 'Angel Investors, Venture Capital Analysts, Incubator Managers, and Venture Builders.'
    }
  };

  previewBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const bookKey = btn.getAttribute('data-book-key');
      const data = bookData[bookKey];
      if (!data) return;

      const modalTitle = document.getElementById('book-modal-title');
      const modalAuthor = document.getElementById('book-modal-author');
      const modalCat = document.getElementById('book-modal-cat');
      const modalRating = document.getElementById('book-modal-rating');
      const modalBadge = document.getElementById('book-modal-badge');
      const modalSynopsis = document.getElementById('book-modal-synopsis');
      const modalChapters = document.getElementById('book-modal-chapters');
      const modalIdeal = document.getElementById('book-modal-ideal');

      const modalCoverImg = document.getElementById('book-modal-cover-img');
      const modalSpineVol = document.getElementById('book-modal-spine-vol');
      if (modalCoverImg && data.cover) modalCoverImg.src = data.cover;
      if (modalSpineVol && data.vol) modalSpineVol.textContent = data.vol;

      if (modalTitle) modalTitle.textContent = data.title;
      if (modalAuthor) modalAuthor.textContent = `By ${data.author}`;
      if (modalCat) modalCat.textContent = data.category;
      if (modalRating) modalRating.textContent = data.rating;
      if (modalBadge) modalBadge.textContent = data.badge;
      if (modalSynopsis) modalSynopsis.textContent = data.synopsis;
      if (modalIdeal) modalIdeal.textContent = data.idealFor;

      if (modalChapters) {
        modalChapters.innerHTML = data.chapters.map((ch, idx) => `
          <div style="display: flex; gap: 10px; align-items: flex-start; margin-bottom: 8px;">
            <span style="background: rgba(2, 86, 155, 0.12); color: var(--primary); font-weight: 800; font-size: 0.75rem; padding: 2px 8px; border-radius: 4px; flex-shrink: 0;">CH ${idx + 1}</span>
            <span style="font-size: 0.88rem; color: inherit;">${ch}</span>
          </div>
        `).join('');
      }

      bookModal?.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  function closeBookModal() {
    bookModal?.classList.remove('open');
    document.body.style.overflow = '';
  }

  bookModalClose?.addEventListener('click', closeBookModal);
  bookModal?.addEventListener('click', (e) => {
    if (e.target === bookModal || e.target.classList.contains('modal-overlay')) {
      closeBookModal();
    }
  });

  // 3D Tilt for Showcase Poster Card
  const posterCard = document.querySelector('.pub-poster-card');
  if (posterCard && window.innerWidth > 992) {
    posterCard.addEventListener('mousemove', (e) => {
      const rect = posterCard.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      const tiltX = (y / rect.height) * -6;
      const tiltY = (x / rect.width) * 6;
      posterCard.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) translateY(-4px)`;
    });

    posterCard.addEventListener('mouseleave', () => {
      posterCard.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)';
      posterCard.style.transition = 'transform 0.5s ease';
    });

    posterCard.addEventListener('mouseenter', () => {
      posterCard.style.transition = 'none';
    });
  }

  // 3D Parallax Tilt for Society 5.0 Engine Card
  const engineCard = document.querySelector('.society5-engine-card');
  if (engineCard && window.innerWidth > 992) {
    engineCard.addEventListener('mousemove', (e) => {
      const rect = engineCard.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      engineCard.style.transform = `perspective(1000px) rotateY(${x * 12}deg) rotateX(${-y * 12}deg) translateY(-4px)`;
    });

    engineCard.addEventListener('mouseleave', () => {
      engineCard.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateY(0)';
      engineCard.style.transition = 'transform 0.5s ease';
    });

    engineCard.addEventListener('mouseenter', () => {
      engineCard.style.transition = 'none';
    });
  }

  // 3D Parallax Tilt for Vision & Mission Cards
  const vmCards = document.querySelectorAll('.vm-card');
  if (vmCards.length && window.innerWidth > 992) {
    vmCards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `perspective(1000px) rotateY(${x * 8}deg) rotateX(${-y * 8}deg) translateY(-4px)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateY(0)';
        card.style.transition = 'transform 0.5s ease';
      });

      card.addEventListener('mouseenter', () => {
        card.style.transition = 'none';
      });
    });
  }
}


/* Who We Help Cohort Switcher Engine with Silky Transition Animation */
document.addEventListener('DOMContentLoaded', function() {
  const cohortBtns = document.querySelectorAll('.cohort-tab-btn');
  const cohortPanels = document.querySelectorAll('.cohort-panel');
  if (cohortBtns.length && cohortPanels.length) {
    cohortBtns.forEach(function(btn) {
      btn.addEventListener('click', function() {
        const target = btn.getAttribute('data-cohort');
        cohortBtns.forEach(function(b) { b.classList.remove('active'); });
        cohortPanels.forEach(function(p) {
          p.classList.remove('active');
          p.style.display = 'none';
        });
        btn.classList.add('active');
        const activePanel = document.getElementById('cohort-' + target);
        if (activePanel) {
          activePanel.style.display = 'block';
          // Force layout reflow to re-trigger CSS keyframe animation
          void activePanel.offsetWidth;
          activePanel.classList.add('active');
        }
      });
    });
  }
});
