import streamlit as st
from rules import APPLIANCE_FAULTS

st.set_page_config(
    page_title="Home Appliance Fault Expert System",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Styling ----------
st.markdown("""
<style>
.main {background: #f7f8fc;}
.block-container {padding-top: 2rem; padding-bottom: 2rem; max-width: 1200px;}
.hero {
    padding: 1.5rem 1.8rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #182848, #4b6cb7);
    color: white;
    margin-bottom: 1.5rem;
}
.hero h1 {margin: 0.25rem 0 0.5rem 0; font-size: 2.2rem;}
.hero p {margin: 0; opacity: .92; font-size: 1.02rem;}
.badge {
    display:inline-block; padding:.35rem .7rem; border-radius:999px;
    background:rgba(255,255,255,.16); font-size:.78rem; font-weight:700;
    letter-spacing:.05em;
}
.section {
    padding: 1rem 1.2rem; border-radius: 15px; background: white;
    border: 1px solid #e5e7eb; margin-bottom: 1rem;
}
.result {
    padding: 1.2rem; border-radius: 15px; background: white;
    border: 1px solid #dfe4ea; margin-top: 1rem;
}
.rule {
    padding: .9rem 1rem; border-left: 4px solid #4b6cb7;
    background:#f1f5ff; border-radius: 8px; margin-top: .8rem;
}
.safe {
    padding:.8rem 1rem; border-radius:10px; background:#fff7ed;
    border:1px solid #fed7aa;
}
.footer {text-align:center; color:#6b7280; margin-top:2rem; font-size:.85rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <span class="badge">ARTIFICIAL INTELLIGENCE • RULE-BASED EXPERT SYSTEM</span>
  <h1>🔧 Home Appliance Fault Expert System</h1>
  <p>Select an appliance, select one of its actual faults, and the IF–THEN knowledge-base rule will produce the diagnosis and troubleshooting recommendation.</p>
</div>
""", unsafe_allow_html=True)

# ---------- Knowledge base ----------
appliances = list(APPLIANCE_FAULTS.keys())

# Keep selections stable and always derive faults from the selected appliance.
if "selected_appliance" not in st.session_state:
    st.session_state.selected_appliance = appliances[0]
if "selected_fault" not in st.session_state:
    st.session_state.selected_fault = None

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("1️⃣ Select Appliance")

appliance = st.selectbox(
    "Appliance",
    appliances,
    index=appliances.index(st.session_state.selected_appliance),
    key="appliance_select",
)
st.session_state.selected_appliance = appliance

faults = list(APPLIANCE_FAULTS[appliance].keys())

# Reset an old fault if the appliance changes.
if st.session_state.selected_fault not in faults:
    st.session_state.selected_fault = faults[0]

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("2️⃣ Select Related Fault")
st.caption(f"Showing {len(faults)} faults specifically available for **{appliance}**.")

fault = st.selectbox(
    "Fault / Symptom",
    faults,
    index=faults.index(st.session_state.selected_fault),
    key=f"fault_select_{appliance}",
)
st.session_state.selected_fault = fault
st.markdown("</div>", unsafe_allow_html=True)

# ---------- Rule inference ----------
rule = APPLIANCE_FAULTS[appliance][fault]

st.markdown('<div class="result">', unsafe_allow_html=True)
st.subheader("🤖 Expert System Result")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Appliance**")
    st.info(appliance)
with col2:
    st.markdown("**Selected Fault**")
    st.warning(fault)

st.markdown("### 🔎 Possible Fault")
st.success(rule["possible_fault"])

st.markdown("### 🔧 Recommended Troubleshooting")
st.write(rule["solution"])

st.markdown(
    f'<div class="rule"><b>IF–THEN RULE USED</b><br>{rule["rule"]}</div>',
    unsafe_allow_html=True,
)

if appliance == "Microwave":
    st.markdown(
        '<div class="safe"><b>⚠️ Safety:</b> Do not open or repair a microwave yourself. '
        'For electrical/heating faults, use a qualified technician.</div>',
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

with st.expander("📚 View Knowledge Base"):
    for a, fault_map in APPLIANCE_FAULTS.items():
        st.markdown(f"**{a}**")
        st.write(" • ".join(fault_map.keys()))

st.markdown(
    '<div class="footer">Educational rule-based AI application • '
    'USER INPUT → KNOWLEDGE BASE → INFERENCE → RESULT</div>',
    unsafe_allow_html=True,
)
