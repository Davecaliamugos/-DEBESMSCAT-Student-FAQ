import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="DEBESMSCAT FAQ Chatbot",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Outfit:wght@300;400;500;600;700&display=swap');

:root {
    --navy:    #0f2642;
    --navy2:   #1a3a5c;
    --gold:    #c9922a;
    --gold-lt: #f0c060;
    --cream:   #faf6ef;
    --white:   #ffffff;
    --text:    #1c1c2e;
    --muted:   #7a7a8c;
    --border:  #e8e0d0;
    --green:   #2d6a4f;
}

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
    background: var(--cream) !important;
    color: var(--text) !important;
}
footer { visibility: hidden; }

/* Responsive sidebar toggle */
button[data-testid="stSidebarToggle"] {
    visibility: visible !important;
    display: block !important;
    position: fixed !important;
    top: 0.5rem !important;
    left: 0.5rem !important;
    z-index: 999999 !important;
    background: var(--navy) !important;
    border: 1px solid var(--gold) !important;
    border-radius: 8px !important;
    padding: 0.3rem 0.5rem !important;
    color: var(--gold) !important;
    min-width: 40px !important;
    min-height: 40px !important;
    transition: all 0.2s ease !important;
}

button[data-testid="stSidebarToggle"]:hover {
    background: var(--gold) !important;
    color: var(--navy) !important;
    transform: scale(1.05) !important;
}

/* Responsive sidebar adjustments */
@media (max-width: 768px) {
    button[data-testid="stSidebarToggle"] {
        top: 0.3rem !important;
        left: 0.3rem !important;
        min-width: 35px !important;
        min-height: 35px !important;
        padding: 0.2rem 0.4rem !important;
    }
    
    section[data-testid="stSidebar"] {
        width: 280px !important;
        max-width: 80vw !important;
    }
}

@media (max-width: 480px) {
    button[data-testid="stSidebarToggle"] {
        top: 0.2rem !important;
        left: 0.2rem !important;
        min-width: 30px !important;
        min-height: 30px !important;
        padding: 0.15rem 0.3rem !important;
    }
    
    section[data-testid="stSidebar"] {
        width: 260px !important;
        max-width: 85vw !important;
    }
    
    .sidebar-header {
        padding: 1rem 0.8rem 0.8rem !important;
    }
    
    .sidebar-logo { font-size: 2rem !important; }
    .sidebar-school { font-size: 0.9rem !important; }
    .sidebar-tagline { font-size: 0.6rem !important; }
}

/* ── APP LAYOUT ── */
.stApp {
    margin-top: 0 !important;
    padding-top: 0 !important;
}

.main .block-container {
    padding-top: 0 !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    padding-bottom: 2rem !important;
    margin-top: 0 !important;
    max-width: 100% !important;
}

/* ── SIDEBAR BASE ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a1e35 0%, #0f2642 50%, #0d3320 100%) !important;
    box-shadow: 4px 0 24px rgba(0,0,0,0.35) !important;
    min-width: 260px !important;
    max-width: 300px !important;
    width: 300px !important;
    transition: all 0.3s ease !important;
}

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0 !important;
    overflow-x: hidden !important;
}

.sidebar-header {
    background: linear-gradient(135deg, rgba(201,146,42,0.18), rgba(201,146,42,0.04));
    border-bottom: 1px solid rgba(201,146,42,0.3);
    padding: 1.4rem 1.2rem 1rem;
    margin-bottom: 0.6rem;
    text-align: center;
}
.sidebar-logo { font-size: 2.5rem; line-height: 1; margin-bottom: 0.3rem; }
.sidebar-school {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1rem; font-weight: 700;
    color: var(--gold-lt) !important; line-height: 1.3;
}
.sidebar-tagline {
    font-size: 0.68rem;
    color: rgba(255,255,255,0.38) !important;
    margin-top: 4px; letter-spacing: 0.05em;
}

/* Sidebar text */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {
    color: rgba(255,255,255,0.75) !important;
    font-size: 0.82rem !important;
}

/* Selectbox / radio label header */
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stRadio label {
    color: rgba(201,146,42,0.85) !important;
    font-size: 0.7rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}

/* Radio options */
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    padding: 7px 11px !important;
    margin-bottom: 3px !important;
    color: rgba(255,255,255,0.78) !important;
    font-size: 0.78rem !important;
    font-weight: 400 !important;
    text-transform: none !important;
    letter-spacing: 0 !important;
    cursor: pointer;
    transition: all 0.15s ease;
    display: block;
    width: 100%;
}
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(201,146,42,0.18) !important;
    border-color: rgba(201,146,42,0.45) !important;
    color: var(--gold-lt) !important;
    transform: translateX(4px);
}

/* Selectbox styling */
section[data-testid="stSidebar"] .stSelectbox > div > div {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 8px !important;
    color: rgba(255,255,255,0.85) !important;
}

/* ── TOP NAV BAR ── */
.topbar {
    background: var(--navy);
    padding: 0.6rem 2rem;
    margin: 0 -1.5rem 0;
    display: flex; align-items: center; gap: 0.9rem;
    border-bottom: 3px solid var(--gold);
    margin-top: -1rem !important;
}
.topbar-logo { font-size: 1.3rem; }
.topbar-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.05rem; font-weight: 700;
    color: var(--gold-lt) !important;
}
.topbar-sub {
    font-size: 0.68rem;
    color: rgba(255,255,255,0.35) !important;
    margin-left: auto; letter-spacing: 0.07em; text-transform: uppercase;
}

/* ── HERO ── */
.hero {
    background: linear-gradient(130deg, var(--navy) 0%, #0d2a45 55%, #163a28 100%);
    border-radius: 20px; padding: 2.2rem 2.8rem;
    margin-bottom: 1.4rem; position: relative; overflow: hidden;
    border: 1px solid rgba(201,146,42,0.2);
}
.hero-orb1 {
    position: absolute; top:-50px; right:-30px;
    width:220px; height:220px; border-radius:50%;
    background: radial-gradient(circle, rgba(201,146,42,0.14) 0%, transparent 70%);
    pointer-events: none;
}
.hero-orb2 {
    position: absolute; bottom:-70px; left:10%;
    width:180px; height:180px; border-radius:50%;
    background: radial-gradient(circle, rgba(45,106,79,0.18) 0%, transparent 70%);
    pointer-events: none;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(201,146,42,0.16); border: 1px solid rgba(201,146,42,0.38);
    border-radius: 30px; padding: 4px 14px;
    font-size: 0.67rem; font-weight: 600;
    letter-spacing: 0.1em; text-transform: uppercase;
    color: var(--gold-lt) !important; margin-bottom: 0.9rem;
}
.hero h1 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.9rem, 3.5vw, 2.8rem) !important;
    font-weight: 700 !important; color: #ffffff !important;
    margin: 0 0 0.5rem !important; line-height: 1.15 !important;
}
.hero h1 em { font-style: normal; color: var(--gold-lt) !important; }
.hero-desc {
    color: rgba(255,255,255,0.56) !important;
    font-size: 0.87rem !important; margin: 0 !important;
    max-width: 500px; line-height: 1.65;
}
.hero-stats { display: flex; gap: 2.2rem; margin-top: 1.6rem; flex-wrap: wrap; }
.hero-stat-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.6rem; font-weight: 700;
    color: var(--gold-lt) !important; line-height: 1;
}
.hero-stat-label {
    font-size: 0.64rem; color: rgba(255,255,255,0.38) !important;
    text-transform: uppercase; letter-spacing: 0.07em; margin-top: 2px;
}

/* ── CHIPS ── */
.chips-wrap { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 1.4rem; }
.chip {
    background: var(--white); border: 1.5px solid var(--border);
    border-radius: 30px; padding: 6px 16px;
    font-size: 0.75rem; font-weight: 500;
    color: var(--navy2) !important; white-space: nowrap;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

/* ── INPUT CARD ── */
.input-card {
    background: var(--white); border: 1.5px solid var(--border);
    border-radius: 16px; padding: 1.2rem 1.4rem 1rem;
    margin-bottom: 1rem; box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}
.input-label {
    font-size: 0.72rem; font-weight: 600;
    letter-spacing: 0.08em; text-transform: uppercase;
    color: var(--muted) !important; margin-bottom: 0.6rem;
}
div[data-testid="stTextInput"] input {
    background: var(--cream) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 10px !important; padding: 0.7rem 1rem !important;
    font-size: 0.92rem !important; color: var(--text) !important;
    font-family: 'Outfit', sans-serif !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: var(--navy2) !important;
    box-shadow: 0 0 0 3px rgba(15,38,66,0.1) !important;
    background: var(--white) !important; outline: none !important;
}

/* ── MAIN BUTTONS ── */
div[data-testid="stMain"] .stButton button {
    background: linear-gradient(135deg, var(--navy) 0%, var(--navy2) 100%) !important;
    color: #fff !important; border: none !important;
    border-radius: 10px !important; padding: 0.7rem 1.4rem !important;
    font-weight: 600 !important; font-size: 0.88rem !important;
    letter-spacing: 0.03em !important;
    transition: all 0.2s ease !important; width: 100% !important;
    box-shadow: 0 3px 10px rgba(15,38,66,0.25) !important;
}
div[data-testid="stMain"] .stButton button:hover {
    background: linear-gradient(135deg, var(--gold) 0%, #a87820 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 18px rgba(201,146,42,0.35) !important;
}

/* ── CHAT BUBBLES ── */
.chat-area { display: flex; flex-direction: column; gap: 14px; padding: 0.5rem 0; }
.msg-row { display: flex; align-items: flex-end; gap: 10px; }
.msg-row.you { flex-direction: row-reverse; }

.avatar {
    width: 34px; height: 34px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.9rem; flex-shrink: 0;
}
.avatar.bot-av {
    background: linear-gradient(135deg, var(--navy), var(--navy2));
    border: 2px solid var(--gold);
}
.avatar.you-av {
    background: linear-gradient(135deg, var(--green), #1e5235);
    border: 2px solid rgba(255,255,255,0.2);
}
.bubble {
    max-width: 75%; padding: 12px 16px;
    border-radius: 16px; font-size: 0.88rem; line-height: 1.62;
}
.bubble.bot {
    background: var(--white); color: var(--text) !important;
    border-bottom-left-radius: 4px; border-left: 3px solid var(--gold);
    box-shadow: 0 2px 10px rgba(0,0,0,0.07);
}
.bubble.you {
    background: linear-gradient(135deg, var(--navy), var(--navy2));
    color: rgba(255,255,255,0.9) !important;
    border-bottom-right-radius: 4px;
    box-shadow: 0 2px 10px rgba(15,38,66,0.22);
}
.bubble-name {
    font-size: 0.62rem; font-weight: 700;
    letter-spacing: 0.08em; text-transform: uppercase;
    margin-bottom: 4px; opacity: 0.5;
}
.bubble.bot .bubble-name { color: var(--gold) !important; }
.bubble.you .bubble-name { color: rgba(255,255,255,0.65) !important; }

.empty-state {
    background: var(--white); border: 1.5px dashed var(--border);
    border-radius: 16px; padding: 3.5rem 2rem; text-align: center;
}
.empty-icon { font-size: 2.8rem; margin-bottom: 0.7rem; }
.empty-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.2rem; font-weight: 700;
    color: var(--navy) !important; margin-bottom: 0.4rem;
}
.empty-sub { font-size: 0.82rem; color: var(--muted) !important; }

hr { border-color: var(--border) !important; margin: 1rem 0 !important; }

@media (max-width: 768px) {
    /* Main container adjustments */
    .main .block-container {
        padding: 0 0.8rem 2rem !important;
        margin-top: 0 !important;
    }
    
    /* Simple mobile sidebar - WORKING APPROACH */
    section[data-testid="stSidebar"] {
        width: 280px !important;
        min-width: 280px !important;
        max-width: 85vw !important;
        transition: all 0.3s ease !important;
    }
    
    /* Ensure sidebar is always accessible */
    section[data-testid="stSidebar"] > div:first-child {
        overflow-x: hidden !important;
        overflow-y: auto !important;
    }
    
    /* Enhanced sidebar header for mobile */
    .sidebar-header {
        padding: 1rem 0.8rem 0.8rem !important;
    }
    .sidebar-logo { font-size: 2rem !important; }
    .sidebar-school { 
        font-size: 0.9rem !important;
        line-height: 1.2 !important;
    }
    .sidebar-tagline { 
        font-size: 0.6rem !important;
        margin-top: 2px !important;
    }
    
    /* Radio button improvements for mobile */
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        gap: 6px !important;
        display: flex !important;
        flex-direction: column !important;
    }
    
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
        padding: 8px 10px !important;
        font-size: 0.7rem !important;
        line-height: 1.3 !important;
        margin-bottom: 2px !important;
    }
    
    /* Selectbox improvements for mobile */
    section[data-testid="stSidebar"] .stSelectbox > div > div {
        font-size: 0.75rem !important;
        padding: 8px !important;
    }
    
    /* Chips improvements for mobile */
    .chips-wrap {
        gap: 6px !important;
        margin-bottom: 1rem !important;
    }
    
    .chip {
        font-size: 0.65rem !important;
        padding: 4px 8px !important;
    }
    
    /* Input card improvements for mobile */
    .input-card {
        padding: 0.8rem !important;
        margin-bottom: 0.8rem !important;
    }
    
    .input-label {
        font-size: 0.68rem !important;
    }
    
    div[data-testid="stTextInput"] input {
        font-size: 0.85rem !important;
        padding: 0.6rem 0.8rem !important;
    }
    
    /* Chat improvements for mobile */
    .chat-area {
        gap: 10px !important;
        padding: 0.3rem 0 !important;
    }
    
    .bubble {
        max-width: 95% !important;
        font-size: 0.8rem !important;
        padding: 10px 12px !important;
    }
    
    .avatar {
        width: 30px !important;
        height: 30px !important;
        font-size: 0.8rem !important;
    }
    
    .bubble-name {
        font-size: 0.55rem !important;
        margin-bottom: 3px !important;
    }
    
    /* Button improvements for mobile */
    div[data-testid="stMain"] .stButton button {
        padding: 0.6rem 1rem !important;
        font-size: 0.8rem !important;
    }
    
    /* Toggle button mobile positioning */
    button[data-testid="stSidebarToggle"] {
        top: 0.5rem !important;
        left: 0.5rem !important;
        min-width: 36px !important;
        min-height: 36px !important;
        padding: 0.25rem 0.4rem !important;
    }
}

@media (max-width: 480px) {
    /* Extra small mobile optimizations */
    .sidebar-header {
        padding: 0.8rem 0.6rem 0.6rem !important;
    }
    
    .sidebar-logo { font-size: 1.8rem !important; }
    .sidebar-school { 
        font-size: 0.8rem !important;
    }
    .sidebar-tagline { 
        font-size: 0.55rem !important;
    }
    
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
        font-size: 0.65rem !important;
        padding: 6px 8px !important;
    }
    
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] div[data-testid="stRadio"] {
        padding: 6px 8px !important;
        margin-bottom: 3px !important;
    }
    
    .input-card {
        padding: 0.6rem !important;
    }
    
    div[data-testid="stTextInput"] input {
        font-size: 0.8rem !important;
        padding: 0.5rem 0.6rem !important;
    }
    
    .chat-area {
        gap: 8px !important;
    }
    
    .bubble {
        max-width: 98% !important;
        font-size: 0.75rem !important;
        padding: 8px 10px !important;
    }
    
    .avatar {
        width: 28px !important;
        height: 28px !important;
        font-size: 0.75rem !important;
    }
    
    div[data-testid="stMain"] .stButton button {
        padding: 0.5rem 0.8rem !important;
        font-size: 0.75rem !important;
    }
    
    .topbar {
        padding: 0.3rem 0.8rem !important;
        margin: 0 -0.8rem 0.8rem !important;
    }
    
    .chips-wrap {
        margin-bottom: 0.8rem !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  SESSION STATE
# ═══════════════════════════════════════════════════════════════
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "prefill" not in st.session_state:
    st.session_state.prefill = ""
if "sidebar_selected" not in st.session_state:
    st.session_state.sidebar_selected = False

# ═══════════════════════════════════════════════════════════════
#  SIDEBAR — uses selectbox per category (reliable native widget)
# ═══════════════════════════════════════════════════════════════

# Maps display label → exact FAQS.py key
categories = {
    "🧠 Trivia & Culture": [
        ("📅 Founding Year",        "what is debesmscat's founding year"),
        ("🎨 School Colors",        "what are the school colors"),
        ("🏅 Named After",          "who is the school named after"),
        ("📜 School Motto",         "what is the school motto"),
        ("🎯 Mission",              "mission"),
        ("🔭 Vision",               "vision"),
        ("🎵 School Hymn",          "hymn"),
        ("🤠 Rodeo Team",           "rodeo"),
    ],
    "📖 Handbook & Conduct": [
        ("🪪 No ID No Entry",       "id"),
        ("👔 Uniform Schedule",     "uniform"),
        ("👗 Dress Code",           "dress code"),
        ("🤝 Expected Behavior",    "behavior"),
        ("🚭 Smoking Policy",       "smoking"),
        ("🍺 Alcohol Policy",       "alcohol"),
        ("✂️ Haircut Policy",       "haircut"),
    ],
    "📍 Locations & Landmarks": [
        ("🏔️ Mandaon Campus",       "mandaon"),
        ("🏫 Cawayan Campus",       "cawayan campus"),
        ("🏙️ Masbate City Campus",  "masbate city campus"),
        ("📚 Library",              "library"),
        ("🍽️ Cafeteria",            "cafeteria"),
        ("🏀 Gymnasium",            "gym"),
        ("🏥 School Clinic",        "clinic"),
        ("🔒 Security Office",      "security"),
    ],
    "🏛️ Institutes & Colleges": [
        ("💻 CCIT",                 "ccit"),
        ("🖥️ IT Program",           "it"),
        ("🌾 Institute of Agriculture", "agri"),
        ("📖 Institute of Education",   "educ"),
        ("⚙️ Engineering",          "engineering"),
    ],
    "📚 Academics & Admissions": [
        ("📝 Enrollment",           "enrollment"),
        ("🌐 Student Portal",       "portal"),
        ("🗂️ Registrar",            "registrar"),
        ("📊 Final Grades",         "grades"),
        ("✅ Clearance",            "clearance"),
        ("💰 Scholarships",         "scholarship"),
        ("🏢 OSAS",                 "osas"),
        ("🗳️ Student Council (SSC)","ssc"),
        ("👥 Student Orgs",         "orgs"),
        ("📶 Free WiFi",            "wifi"),
    ],
    "🌿 Campus Life & Environment": [
        ("😌 Peaceful Campus",      "peaceful"),
        ("♻️ Eco-Friendly Campus",  "environment"),
        ("🌲 Nature & Land",        "nature"),
        ("🚨 Emergency",            "emergency"),
    ],
}

with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <div class="sidebar-logo">🏛️</div>
        <div class="sidebar-school">DEBESMSCAT</div>
        <div class="sidebar-tagline">Student FAQ Assistant</div>
    </div>
    """, unsafe_allow_html=True)

    # Category picker
    cat_choice = st.selectbox(
        "📂 Browse Category",
        options=list(categories.keys()),
        index=0,
        label_visibility="visible"
    )

    # Questions for the chosen category
    options_for_cat = categories[cat_choice]
    labels = [label for label, _ in options_for_cat]

    selected_label = st.radio(
        "💡 Pick a question:",
        options=labels,
        index=None,           
        label_visibility="visible",
        key="sidebar_radio"  
    )

    # When a radio option is picked, automatically add to chat (only if not already selected)
    if selected_label and not st.session_state.sidebar_selected:
        faq_key = dict(options_for_cat)[selected_label]
        response = get_response(faq_key)
        if response:
            st.session_state.chat_history.append(("You", faq_key))
            st.session_state.chat_history.append(("Bot", response))
            st.session_state.sidebar_selected = True  # Mark as selected
            st.session_state.prefill = ""  # Clear prefill after using
            st.rerun()
    elif not selected_label:
        # Reset flag when no selection
        st.session_state.sidebar_selected = False

    st.markdown("---")
    st.markdown("""
    <div style='font-size:0.68rem; color:rgba(255,255,255,0.28); text-align:center; padding:0.2rem 0 0.8rem; line-height:1.8;'>
        Dr. Emilio B. Espinosa Sr.<br>Memorial State College of<br>Agriculture & Technology<br>
        <span style='color:rgba(201,146,42,0.45)'>🌿 Masbate, Philippines</span>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
#  MAIN CONTENT
# ═══════════════════════════════════════════════════════════════

st.markdown("""
<div class="chips-wrap">
    <span class="chip">🧠 Trivia</span>
    <span class="chip">📖 Rules &amp; Conduct</span>
    <span class="chip">📍 Locations</span>
    <span class="chip">🏛️ Institutes</span>
    <span class="chip">📚 Academics</span>
    <span class="chip">🌿 Campus Life</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="input-card"><div class="input-label">💬 Your Question</div>', unsafe_allow_html=True)
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input(
        "question",
        value=st.session_state.prefill,
        placeholder="e.g. How many colleges does DEBESMSCAT have?",
        label_visibility="collapsed",
        key="question_input"
    )
with col2:
    ask_clicked = st.button("Ask ➤", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.prefill:
    st.session_state.prefill = ""

if ask_clicked and user_input.strip():
    response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))
    st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

if not st.session_state.chat_history:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">💬</div>
        <div class="empty-title">No conversation yet</div>
        <div class="empty-sub">Type a question above or pick a suggestion from the sidebar to get started.</div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="chat-area">', unsafe_allow_html=True)
    for sender, message in st.session_state.chat_history:
        if sender == "You":
            st.markdown(f"""
            <div class="msg-row you">
                <div class="avatar you-av">🙋</div>
                <div class="bubble you">
                    <div class="bubble-name">You</div>
                    {message}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="msg-row bot">
                <div class="avatar bot-av">🎓</div>
                <div class="bubble bot">
                    <div class="bubble-name">DEBESMSCAT Bot</div>
                    {message}
                </div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🗑️ Clear Conversation"):
        st.session_state.chat_history = []
        st.rerun()