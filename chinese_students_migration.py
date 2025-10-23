

import streamlit as st
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="Chinese Students Migrating to the U.S.", layout="wide")

# --- TITLE ---
st.title("Chinese Students Migrating to the U.S. for College")
st.caption("By Ava")

# --- INTRO ---
st.header("Type and Extent of Migration")
st.write("""
**Type:** Voluntary, international, educational migration  
**Scale:** Around **290,000 Chinese students** studied in the U.S. in **2022–2023**, 
making up about **30% of all international students**.
""")

# --- PIE CHART: INTERNATIONAL STUDENTS IN THE U.S. ---
labels = ['Chinese Students', 'Other International Students']
sizes = [30, 70]
colors = ['#FF4B4B', '#1F77B4']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.axis('equal')
st.pyplot(fig1)

# --- PUSH AND PULL FACTORS ---
st.header("Push and Pull Factors")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Push Factors (From China)")
    st.write("""
    - Intense **Gaokao** competition and limited top university spots  
    - Rigid education system with fewer research opportunities  
    - Desire for more **academic freedom**
    """)

with col2:
    st.subheader("Pull Factors (To the U.S.)")
    st.write("""
    - **World-class universities** and English-based education  
    - Flexible course structures and better **career prospects**  
    - Exposure to a **global learning environment**
    """)

# --- BAR CHART: PUSH VS PULL ---
factors = ['Competition', 'Education Flexibility', 'Research', 'Career Opportunities', 'Global Exposure']
china_push = [9, 3, 4, 2, 1]
us_pull = [1, 9, 8, 9, 8]

fig2, ax2 = plt.subplots()
bar_width = 0.35
x = range(len(factors))
ax2.bar(x, china_push, bar_width, label='Push (China)', color='#FF6F61')
ax2.bar([i + bar_width for i in x], us_pull, bar_width, label='Pull (U.S.)', color='#4B9CD3')
ax2.set_xticks([i + bar_width/2 for i in x])
ax2.set_xticklabels(factors, rotation=25)
ax2.set_ylabel('Influence Level (1–10)')
ax2.legend()
st.pyplot(fig2)

# --- EFFECTS ---
st.header("📈 Effects on Both Countries")

tab1, tab2 = st.tabs(["🇨🇳 Effects on China (Origin)", "🇺🇸 Effects on the U.S. (Destination)"])

with tab1:
    st.write("""
    - **Brain Drain:** Many top students stay abroad post-graduation.  
    - **Brain Gain:** Returnees ("**Sea Turtles**") bring global skills and innovation.  
    - **Cultural Impact:** Western learning influences Chinese schooling and parenting.  
    - **Economic Impact:** Families spend billions yearly on overseas education.  
    """)

with tab2:
    st.write("""
    - **Economic Boost:** Over **$10 billion** contributed yearly via tuition and living costs.  
    - **Campus Diversity:** Promotes cultural exchange and international awareness.  
    - **Research Contribution:** Chinese students strengthen U.S. **STEM and innovation sectors**.  
    """)

# --- SOURCES ---
st.header("Sources")
st.markdown("""
- [Council on Foreign Relations](https://www.cfr.org/blog/understanding-experiences-chinese-graduate-students-united-states)  
- [The Diplomat](https://thediplomat.com/2025/04/the-cost-of-china-us-rivalry-is-falling-on-students/)
""")