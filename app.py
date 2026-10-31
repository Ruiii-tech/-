import streamlit as st

st.set_page_config(page_title="询单通 | 外贸工作台", page_icon="S", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+SC:wght@400;500;600;700&display=swap');
:root{--ink:#202431;--muted:#7b8190;--line:#e9eaf0;--paper:#fff;--canvas:#f7f8fb;--violet:#7257e8;--green:#24866a;--amber:#c18126}
html,body,[class*="css"]{font-family:'DM Sans','Noto Sans SC',sans-serif;color:var(--ink)}.stApp{background:var(--canvas)}[data-testid="stHeader"]{background:transparent}[data-testid="stSidebar"]{display:none}.block-container{max-width:1600px;padding-top:1.5rem;padding-bottom:2rem}[data-testid="column"]{min-width:0}
.brand{display:flex;align-items:center;gap:9px;padding:8px 4px 24px;font-weight:700;font-size:16px;white-space:nowrap}.brand-mark{width:31px;height:31px;display:grid;place-items:center;border-radius:8px;color:white;background:#7257e8;font-size:17px}.nav-caption{color:#a0a4b0;font-size:10px;font-weight:700;letter-spacing:1px;padding:0 7px 9px}
[data-testid="stButton"]{width:100%}[data-testid="stButton"] button{width:100%;min-height:40px;justify-content:flex-start;border:0;border-radius:7px;background:transparent;color:#666d7c;font-size:12px;padding:0 7px;box-shadow:none}[data-testid="stButton"] button:hover{background:#efedf9;color:var(--violet);border:0}
.page-head{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:20px;gap:16px}.eyebrow,.head-note{color:var(--muted);font-size:12px}.eyebrow{margin-bottom:5px}.page-title{font-size:24px;font-weight:700}.head-note{padding-top:9px}
.stat-card,.panel,.ai-panel{background:var(--paper);border:1px solid var(--line);border-radius:8px;box-shadow:0 2px 8px #20243108}.stat-card{padding:15px 16px;min-height:102px}.stat-top{display:flex;justify-content:space-between;align-items:center}.stat-label{color:var(--muted);font-size:12px}.stat-icon{width:28px;height:28px;display:grid;place-items:center;border-radius:7px;background:#f1efff;color:var(--violet)}.stat-value{font-size:26px;font-weight:700;margin-top:9px}.stat-unit{color:var(--muted);font-size:12px;margin-left:4px}
.section-head{display:flex;justify-content:space-between;margin:25px 0 12px}.section-title,.panel-title{font-size:14px;font-weight:700}.section-hint{color:var(--muted);font-size:11px}.panel{padding:19px;height:100%}.panel-head{display:flex;justify-content:space-between;align-items:center;gap:10px;padding-bottom:14px;border-bottom:1px solid #f0f1f4}.tag{border-radius:5px;padding:4px 8px;color:#6650ce;background:#f0edff;font-size:10px;white-space:nowrap}.source-meta{display:flex;gap:8px;align-items:center;color:var(--muted);font-size:11px;margin:14px 0 10px}.avatar{width:25px;height:25px;display:grid;place-items:center;border-radius:50%;color:#246f75;background:#e4f3f1;font-weight:700}.email-box{border:1px solid #eceef3;border-radius:6px;padding:13px 14px;color:#4c5260;background:#fcfcfd;font-size:13px;line-height:1.8}.mail-subject{color:#303543;font-weight:600;margin-bottom:7px}
.extract{margin-top:15px;padding:13px 14px;border-left:3px solid var(--violet);background:#f8f7ff;border-radius:0 6px 6px 0}.extract-label{font-size:12px;font-weight:700;color:#5845b2;margin-bottom:8px}.extract-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.extract-item{color:var(--muted);font-size:11px}.extract-item strong{display:block;color:#303543;font-size:12px;margin-top:3px}
.timeline{padding-top:17px}.step{display:grid;grid-template-columns:25px 1fr;gap:10px;min-height:63px;position:relative}.step:not(:last-child):after{content:'';position:absolute;top:25px;left:11px;width:1px;height:38px;background:#e4e5eb}.step-icon{z-index:1;width:23px;height:23px;display:grid;place-items:center;border-radius:50%;font-size:10px;background:#e7f5ef;color:var(--green)}.step.current .step-icon{background:#fff3df;color:var(--amber)}.step.pending .step-icon{background:#f0f1f4;color:#989daa}.step-name{font-size:12px;font-weight:600;padding-top:2px}.step-state{color:var(--muted);font-size:10px;margin-top:4px}.step.current .step-name{color:#9a6418}.process-note{margin-top:5px;padding:10px;border-radius:6px;background:#fff9ef;color:#87632c;font-size:10px;line-height:1.6}
.ai-panel{padding:16px 19px;margin-top:18px}.ai-head{display:flex;align-items:center;gap:8px;font-size:13px;font-weight:700;margin-bottom:10px}.ai-spark{color:var(--violet)}[data-testid="stTextArea"] textarea{border:1px solid #e6e7ee;border-radius:6px;background:#fcfcfd;font-size:13px;line-height:1.6;min-height:90px}[data-testid="stTextArea"] label{display:none}.ai-footnote{color:var(--muted);font-size:10px;padding-top:8px}[data-testid="stFormSubmitButton"] button{min-height:42px;justify-content:center;color:#fff;background:#7257e8;border:1px solid #7257e8;border-radius:6px;font-size:13px;font-weight:600}[data-testid="stFormSubmitButton"] button:hover{color:#fff;background:#6045d0;border-color:#6045d0}.toast-result{padding:10px 12px;margin-top:10px;color:#315f50;background:#ecf7f2;border:1px solid #d6eee3;border-radius:6px;font-size:12px}
@media(max-width:760px){.block-container{padding:1rem .7rem}.brand{font-size:13px}[data-testid="stButton"] button{padding:0 3px;font-size:10px}.head-note{display:none}.page-title{font-size:21px}.panel{padding:14px}.extract-grid{grid-template-columns:1fr}}
</style>
""", unsafe_allow_html=True)

if "active_page" not in st.session_state:
    st.session_state.active_page = "工作台"

nav_col, main_col = st.columns([0.78, 5.22], gap="large")
with nav_col:
    st.markdown('<div class="brand"><span class="brand-mark">S</span><span>询单通</span></div><div class="nav-caption">WORKSPACE</div>', unsafe_allow_html=True)
    for icon, label in [("[ ]", "工作台"), ("<> ", "询盘管理"), ("[=]", "产品资料库"), ("[!]", "任务中心"), ("AI", "AI 翻译助手")]:
        if st.button(f"{icon}  {label}", key=f"nav_{label}"):
            st.session_state.active_page = label

with main_col:
    st.markdown('<div class="page-head"><div><div class="eyebrow">询盘协作 · 业务概览</div><div class="page-title">工作台</div></div><div class="head-note">欢迎回来，今天的询盘进展一览</div></div>', unsafe_allow_html=True)
    stats = [("今日询盘", "3", "条", "↗"), ("待确认任务", "1", "条", "✓"), ("待审批报价", "2", "份", "⇧"), ("待补充产品资料", "4", "项", "+")]
    for col, (label, value, unit, icon) in zip(st.columns(4, gap="small"), stats):
        with col:
            st.markdown(f'<div class="stat-card"><div class="stat-top"><span class="stat-label">{label}</span><span class="stat-icon">{icon}</span></div><div class="stat-value">{value}<span class="stat-unit">{unit}</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-head"><div class="section-title">询盘处理</div><div class="section-hint">从客户需求到正式报价，一处协同</div></div>', unsafe_allow_html=True)
    request_col, process_col = st.columns([1.55, 1], gap="medium")
    with request_col:
        st.markdown('''<div class="panel"><div class="panel-head"><span class="panel-title">客户原始需求</span><span class="tag">新询盘 · 待报价</span></div>
        <div class="source-meta"><span class="avatar">JM</span><span>James Miller</span><span>·</span><span>来自 Email</span><span>·</span><span>12 分钟前</span></div>
        <div class="email-box"><div class="mail-subject">Subject: Inquiry for 10 KV DC ceramic capacitors</div>Hello, we need 1,000 pcs of 10 KV DC ceramic capacitors for our upcoming project. Could you please share your best unit price and estimated lead time? We would also like to know the available shipping options. Looking forward to your reply.</div>
        <div class="extract"><div class="extract-label">AI 智能提取的关键需求</div><div class="extract-grid"><div class="extract-item">产品 / 数量<strong>10KV 直流陶瓷电容 · 1,000 件</strong></div><div class="extract-item">价格<strong>客户未提供目标价，需核算单价</strong></div><div class="extract-item">交期<strong>客户询问预计交期，待采购确认</strong></div></div></div></div>''', unsafe_allow_html=True)
    with process_col:
        st.markdown('''<div class="panel"><div class="panel-head"><span class="panel-title">从信息，到行动</span><span class="tag">处理进度 2 / 4</span></div><div class="timeline">
        <div class="step"><div class="step-icon">OK</div><div><div class="step-name">第一步：需求解析</div><div class="step-state">已完成 · 已识别数量、产品规格和报价问题</div></div></div>
        <div class="step"><div class="step-icon">OK</div><div><div class="step-name">第二步：匹配产品资料</div><div class="step-state">已完成 · 已匹配 10KV 陶瓷电容产品档案</div></div></div>
        <div class="step current"><div class="step-icon">...</div><div><div class="step-name">第三步：智能计算成本</div><div class="step-state">处理中... · 正在等待采购成本与交期</div></div></div>
        <div class="step pending"><div class="step-icon">4</div><div><div class="step-name">第四步：提交报价审批</div><div class="step-state">待处理 · 核算完成后生成报价草稿</div></div></div></div>
        <div class="process-note">当前待办：采购确认 1,000 件的可供数量、成本及预计交期。</div></div>''', unsafe_allow_html=True)
    st.markdown('<div class="ai-head"><span class="ai-spark">AI</span><span>AI 交互助手</span><span class="section-hint">· 当前询盘：James Miller</span></div>', unsafe_allow_html=True)
    with st.form("ai_request_form", clear_on_submit=False):
        prompt_col, action_col = st.columns([5, 1.2], gap="medium")
        with prompt_col:
            prompt = st.text_area("AI 处理指令", placeholder="对 AI 说：比如，帮我计算 10KV 陶瓷电容的出口报价，并按 FOB 条款发回复邮件给该客户", height=98, label_visibility="collapsed")
        with action_col:
            submitted = st.form_submit_button("AI 开始处理", use_container_width=True)
    st.markdown('<div class="ai-footnote">AI 生成的报价与邮件均为草稿，确认并完成审批后才会发送给客户。</div>', unsafe_allow_html=True)
    if submitted:
        if prompt.strip():
            st.markdown('<div class="toast-result">已收到指令。AI 将基于当前询盘生成处理草稿，报价发送前仍需人工确认与审批。</div>', unsafe_allow_html=True)
        else:
            st.warning("请先输入希望 AI 处理的事项。")
