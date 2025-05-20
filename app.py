import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Kamaleashwar Portfolio",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state['page'] = 'Home'

def back_home():
    st.session_state['page'] = 'Home'

def change():
    st.session_state['page'] = 'Explanation'

st.markdown("""
    <style>
    body {
        background-color: #F7FAFC;
        color: #1A202C;
    }
    .stButton>button {
        background-color: #2C7A7B;
        color: white;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #285E61;
        color: white;
    }
    h1, h2, h3 {
        color: #2C7A7B;
    }
    .css-1v0mbdj p {
        color: #4A5568;
    }
    </style>
""", unsafe_allow_html=True)

if st.session_state['page'] == 'Home':
    #-------------------------------------------------------------------------------------------------------------------
    #Banner section
    #------------------------------------------------------------------------------------------------------------------
    banner = st.container()
    with banner:
        st.image("assets\banner.png",use_container_width=True)

    left, middle, right = st.columns([0.2,0.4,0.2],gap="small",vertical_alignment="top",border=False)

    left.image("assets\profile-pic (4).png",width=150)
    with middle:
        st.title("Kamaleashwar G")
        st.subheader("Data Analyst")
        st.markdown("""
        [![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=linkedin)](www.linkedin.com/in/g-kamaleashwar-28a2802ba)
        [![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat&logo=github)](https://github.com/G-Kamalesh)
        [![Resume](https://img.shields.io/badge/-Resume-green?style=flat)](https://drive.google.com/file/d/1KpnOup_dz0xvF6JxVkURUrEjn6RC35ez/view?usp=sharing)
        """)

    st.divider()    
    #-------------------------------------------------------------------------------------------------------------------
    #About section
    #-------------------------------------------------------------------------------------------------------------------
    st.markdown("<h2 style='text-align: center;'>About Me</h2>", unsafe_allow_html=True)
    st.markdown(""" 
    **Hello! I'm Kamalesh, a Data Analyst with a background in Mechanical Engineering and a passion for uncovering insights through data.**

My interest in data sparked unexpectedly during my CAT exam preparation, when a New York Times article titled **"How Companies Learn Your Secrets"** revealed how predictive analytics could identify life-changing events—like a teenage girl’s pregnancy—based on buying behavior. That eye-opening moment made me realize the hidden power of data and how it can be used to drive meaningful outcomes.

Although I initially set out to pursue an MBA in Business Analytics, I took a different path when I couldn’t crack the entrance exam. Instead of giving up, I dove into hands-on learning through a Data Science program at Guvi, where I built a strong foundation in Python, SQL, Power BI and machine learning.

Previously at TAFE, I worked in Quality Assurance, where I led process improvements that resulted in a 100% reduction in export complaints—an experience that taught me the real-world value of data-driven decisions. Currently, I’m interning at Abhyaz, where I focus on CRM and attendance analytics, translating data into actionable insights for internal teams.

I’m now seeking a full-time role where I can continue growing as a Data Analyst and contribute to solving real-world business problems with data. 
                
Let’s connect and explore how data can tell better stories and drive smarter decisions—together.
    """)

    st.divider()
    #--------------------------------------------------------------------------------------------------------------------
    #Skills Section
    #--------------------------------------------------------------------------------------------------------------------
    st.markdown("<h2 style='text-align: center;'>Skills</h2>", unsafe_allow_html=True)
    cat1, icon1,icon2,icon3,icon4,icon5= st.columns([2,1,1,1,1,1],gap="small",vertical_alignment="top")
    cat1.subheader("Languages")
    icon1.image("assets\python.png",caption="Python")
    icon2.image("assets\sql.png",caption="SQL")

    cat2,icon6,icon7,icon8,icon9,icon10 = st.columns([2,1,1,1,1,1],gap="small",vertical_alignment="top")
    cat2.subheader("Tools")
    icon6.image("assets\power_bi.png",caption="Power BI")
    icon7.image("assets\tableau.png",caption="Tableau")
    icon8.image("assets\excel.png",caption="Excel")
    icon9.image("assets\streamlit.png",caption="Streamlit")

    cat3, icon11,icon12,icon13,icon14,icon15 = st.columns([2,1,1,1,1,1],gap="small",vertical_alignment="top")
    cat3.subheader("Libraries")
    icon11.image("assets\matplotlib.png",caption="Matplotlib")
    icon12.image("assets\pandas.png",caption="Pandas")
    icon13.image("assets\plotly.png",caption="Plotly")
    icon14.image("assets\numpy.png",caption="Numpy")

    cat4, icon16,icon17,icon18,icon19,icon20 = st.columns([2,1,1,1,1,1],gap="small",vertical_alignment="top")
    cat4.subheader("Databases")
    icon16.image("assets\mongodb.png",caption="MongoDB")
    icon17.image("assets\mysql.png",caption="MySql")

    st.divider()
    #---------------------------------------------------------------------------------------------------------------------
    #Project section
    #---------------------------------------------------------------------------------------------------------------------
    st.markdown("<h2 style='text-align: center;'>Projects</h2>", unsafe_allow_html=True)
    side1,side2,side3 = st.columns([2,2,2],gap="small",vertical_alignment="top")

    
    with side1.container(border=True):
        st.image("assets\dashboard_snapshot.JPG",width=400)
        s1,s2,s3 = st.columns([1,0.5,1],gap="small",vertical_alignment="top")
        s1.badge("Zoho Analytics",color="red")
        s2.badge("SQL",color="gray")
        s3.badge("Internship Project",color='violet')
        st.markdown("""
            <h5 style='letter-spacing: 4px; text-transform: uppercase; font-weight: 600; font-family: sans-serif;'>
                Interns Attendance Dashboard
            </h5>""", unsafe_allow_html=True)
        st.write("  Build an attendance dashboard using Zoho Analytics to track and analyze workforce performance, improving operational insights.")
        st.button("Know More",on_click=change)

    with side2.container(border=False):
        st.info(body="Check my Github Account for my other projects on ML and Data visualization. Link is at the end of the page.Thank You")

    st.divider()
    #-------------------------------------------------------------------------------------------------------------------
    #EXPERIENCE SECTION
    #-------------------------------------------------------------------------------------------------------------------
    st.markdown("<h2 style='text-align: center;'>Experience</h2>", unsafe_allow_html=True)
    e1, e2 = st.columns([0.5,0.5],gap='small',vertical_alignment='top')
    with e1.container(border=True):
        st.subheader("Data Analyst Intern – Abhyaz")
        st.caption("Feb 2025 - Present")
        st.markdown("""
                       - 🔄 **Developed a Weekly ETL Pipeline:** Built and automated an ETL pipeline to extract intern data from integrated CRM and attendance sources, preprocess it, and refresh dashboard insights weekly.

                       - 📚 **Integrated Multiple Data Sources:** Combined data from CRM tools and attendance systems to create a unified dataset for analysis and reporting.

                       - 📊 **Designed Interactive Dashboards:** Built visually intuitive dashboards to track attendance trends, intern engagement, and performance metrics.

                       - 📈 **Delivered Actionable Insights:** Generated weekly reports that helped stakeholders make informed decisions to improve participation and operational efficiency.


                    """)
    with e2.container(border=True):
        st.subheader("Quality Assurance – TAFE")
        st.caption("Jul 2020 - Dec 2021")
        st.markdown("""
                    - 🔍 **Led Quality Control for Inbound and Assembly Operations:** Conducted sample quality checks on GRINs (Goods Received Inward) for components like gearboxes, control valves and various other tractor parts to ensure assembly readiness and minimize rework.

                    - ⚙️ **Managed Urgent Material Dispatch (IMO):** Oversaw immediate material outflows for high-priority orders, ensuring 24-hour delivery turnaround without compromising on quality.

                    - 🔹 **Achieved 100% Reduction in Export Complaints:** Led quality inspections and optimized packing standards for exports to countries including Sri Lanka, Bangladesh, Mexico, and South Africa, ensuring compliance with international requirements and eliminating export complaints within two months.

                    - 📦 **Oversaw Export Operations for AGCO Corporation:** Ensured product quality and proper packaging for exports to AGCO, aligning deliverables with specific client specifications for maximum customer satisfaction.


                    """)

    st.divider()
    #------------------------------------------------------------------------------------------------------------------
    #Education & Certification
    #------------------------------------------------------------------------------------------------------------------
    st.markdown("<h2 style='text-align: center;'>Certification & Education</h2>", unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns([1,1,1,1],gap='small',vertical_alignment='top',border=True)
    c1.markdown("""  **Master Data Science**  
                    *Guvi*""")
    c2.markdown("""  **Advanced Data Visualization (Power BI)**  
                    *Guvi*""")
    c3.markdown("""  **Machine Learning with TensorFlow**  
                    *freeCodeCamp*""")
    c4.markdown(""" **B.E. Mechanical Engineering**  
                    *St. Peter College (2015 – 2019)*""")

    
    st.divider()
    #------------------------------------------------------------------------------------------------------------------
    #Contacts
    #------------------------------------------------------------------------------------------------------------------
    sec1, sec2, sec3, sec4, sec5 = st.columns([0.75, 0.23, 0.2, 0.2, 0.9], gap='small',vertical_alignment='bottom')

    with sec2:
        st.container(height=60,border=False)
        with st.container(border=True):
            st.markdown("""
            <a href="https://www.linkedin.com/in/g-kamaleashwar-28a2802ba" target="_blank" style="text-decoration: none;">
                <div style="text-align: center;">
                    <img src="https://img.icons8.com/?size=100&id=13930&format=png&color=000000" alt="LinkedIn" width="40" style="margin-bottom: 5px;"/>
                    <p style="margin: 0; font-weight: bold; color: #0e76a8;">LinkedIn</p>
                </div>
            </a>
            """, unsafe_allow_html=True)

    with sec3:
        st.container(height=60,border=False)
        with st.container(border=True):
            st.markdown("""
            <a href="https://github.com/G-Kamalesh" target="_blank" style="text-decoration: none;">
                <div style="text-align: center;">
                    <img src="https://img.icons8.com/?size=100&id=16318&format=png&color=000000" alt="GitHub" width="40" style="margin-bottom: 5px;"/>
                    <p style="margin: 0; font-weight: bold; color: #333;">GitHub</p>
                </div>
            </a>
            """, unsafe_allow_html=True)
    with sec4:
        st.container(height=60,border=False)
        with st.container(border=True):
           st.markdown("""
            <a href="https://mail.google.com/mail/?view=cm&fs=1&to=gkamaleash@gmail.com" target="_blank" style="text-decoration: none;">
                <div style="text-align: center;">
                    <img src="https://img.icons8.com/?size=100&id=P7UIlhbpWzZm&format=png&color=000000" alt="Gmail" width="40" style="margin-bottom: 5px;"/>
                    <p style="margin: 0; font-weight: bold; color: #D44638;">Gmail</p>
                </div>
            </a>
            """, unsafe_allow_html=True)






if st.session_state['page'] == 'Explanation':
    back, heading= st.columns([0.1,0.8],gap="small")
    heading.markdown("""
    <h5 style='letter-spacing: 5px; text-transform: uppercase; font-weight: 600; font-family: sans-serif;'>
        Interns Attendance Dashboard
    </h5>""", unsafe_allow_html=True)
    back.button("Back",on_click=back_home)
    with heading:
        cat1, s1,s2,s3,s4,s5 = st.columns([0.15,0.18,0.21,0.18,0.2,0.44],gap='small',vertical_alignment='top')
        cat1.badge("Tools Used",color='red')
        s1.badge("Zoho Analytics",color='orange')
        s2.badge("Excel - Power Query",color='orange')
        s3.badge("Zoho Workdrive",color="orange")
        s4.badge("SQL",color="orange")

        cat2,s1,s2,s3,s4 = st.columns([0.16,0.35,0.3,0.4,0.28],gap='small',vertical_alignment='top')#,border=True)
        cat2.badge("Skills", color='red')
        s1.badge("Data Cleaning & Preparation",color='primary')
        s2.badge("Storytelling with Data",color='primary')
        s3.badge("Interactive Dashboard Design",color='primary')
        s1.badge("Employee Engagement Analytics",color='primary')
        s2.badge("Performance Monitoring",color='primary') 
        s1.badge("KPI Tracking & Trend Analysis",color='primary')
        s2.badge("ETL Pipeline Development",color='primary')
        s3.badge("Automated Data Refresh & Sync",color='primary')
        s3.badge("Data Integration & Transformation",color='primary')
        s1.badge("SQL Queries",color='primary')

        cat3, s1,s2,s3,s4,s5 = st.columns([0.15,0.2,0.21,0.18,0.2,0.44],gap='small',vertical_alignment='top')
        cat3.badge("Type",color='red')
        s1.badge("Internship Project",color='violet')

        st.divider()
        st.header("Project Background")
        st.markdown("""As the internship program expanded across multiple department, it became increasingly challenging 
                    to keep track of intern engagement. Manual tracking methods like spreadsheets were error-prone, 
                    time-consuming, and lacked the clarity needed to make timely decisions. Managers struggled to spot 
                    disengaged interns, track newcomers, or identify trends in attendance. There was a clear need for a 
                    smarter, more insightful solution. That’s when the idea of building a real-time **Intern Attendance 
                    Dashboard was born**—one that would bring clarity, accountability, and control to the entire 
                    attendance tracking process. """)

        st.header("Executive Summary")
        st.markdown(""" This dashboard is more than just a collection of charts—it’s a dynamic lens into the heartbeat 
                    of the internship program. Spanning **data from September 2024 to April 2025**, it captures every 
                    session, every intern’s journey, and every fluctuation in attendance. Build in **Zoho Analytics**, 
                    the dashboard pulls data through an automated pipeline, processes it, and presents it in a format 
                    that’s intuitive, insightful, and action-ready.
                    \nFrom overall attendance trends to individual engagement levels, it allows teams to not just monitor, 
                    but **understand and improve** intern participation. Whether you're an HR leader or a team mentor, this 
                    dashboard puts the right information at your fingertips""")
        st.image("assets\d2.png",caption="Interns Attendance Dashboard")
        
                # Insights Deep Dive
        st.header("Insights Deep Dive")

        st.subheader("1️⃣ Current Month Performance Analysis")
        st.markdown("""
        - As of **April 2025**, **87 interns** are actively engaged — reflecting **steady month-over-month growth**.
        - **1,011 total attendance records** have been logged this month.
        - **Present rate stands at 76.1%** (763), showing **strong participation** across the board.
        - **Minimal late entries (6)** and **excused absences (1)** suggest punctuality isn’t the problem — but **consistency is**.
        - However, **24.4% absenteeism (247)** is a growing concern, with a **6.9% increase in April**. This calls for deeper investigation into possible **workload, motivation, or scheduling issues**.
        """)

        st.subheader("2️⃣ Engagement is Steady — But Inconsistency Persists")
        st.markdown("🧭 *Punctuality isn’t the problem — maintaining rhythm is.*")
        st.markdown("""
        - Most interns fall in the **60–80% attendance** bracket — a sign of **inconsistent participation**, not disengagement.
        - This could stem from **external commitments**, **poor time management**, or **lack of accountability**.
        - There's an opportunity to provide **structure and nudges** to reinforce regularity.
        """)

        st.subheader("3️⃣ Leading By Example: The Top Performers")
        st.markdown("🌟 *High performers set the tone — let’s spotlight them.*")
        st.markdown("""
        - The **Top 10 Interns by Attendance** are highly reliable and consistent.
        - These individuals can be **positioned as role models**, mentors, or even **ambassadors** of good practices.
        - Recognizing and leveraging them builds a **positive, peer-driven culture**.
        """)

        st.subheader("4️⃣ Absenteeism Is Localized — Not Universal")
        st.markdown("🚩 *Few are falling behind — target them.*")
        st.markdown("""
        - The **Top 10 Interns with Maximum Absences** highlight a **concentrated issue**.
        - This isn’t a widespread problem — but an opportunity for **targeted, compassionate intervention**.
        - Tailored mentoring or check-ins can **re-engage these interns** effectively.
        """)

        st.subheader("5️⃣ Intern Onboarding Drives Attendance Spikes")
        st.markdown("📈 *Attendance is cyclical — not linear.*")
        st.markdown("""
        - Attendance **spikes align with onboarding waves**, but drop shortly after.
        - These drop-offs are prime opportunities for **timely motivation, team bonding**, or **goal-setting sessions**.
        - A structured post-onboarding engagement plan can help **sustain early momentum**.
        """)

        st.subheader("6️⃣ Absenteeism Peaks Near Long Weekends")
        st.markdown("📅 *Fridays, Mondays, and Thursdays see the most no-shows.*")
        st.markdown("""
        - Interns are likely **extending weekends or disengaging midweek**.
        - Use this insight to **plan lighter activities**, **engagement sessions**, or **fun incentives** on those days.
        """)

        st.subheader("7️⃣ New Joiners: Fragile Start, Early Drop-off Risk")
        st.markdown("🔍 *Low attendance often maps to new joiners.*")
        st.markdown("""
        - Some interns with **very low attendance** joined recently.
        - Differentiating between **onboarding lag vs. disengagement** can help guide **personalized check-ins or support**.
        """)

        st.subheader("8️⃣ Standardize Leave Reporting")
        st.markdown("📝 *Emails are messy — structured forms lead to better data.*")
        st.markdown("""
        - Leave intimation via email causes **tracking issues** and **data loss**.
        - Implement a **centralized digital leave form** with predefined fields like:
            - 📆 Date of Leave
            - 🗂️ Reason Category (Health, Personal, Academic, etc.)
            - ⏳ Duration
        - This ensures **data consistency** and **better absenteeism forecasting**.
        """)

        # Recommendations
        st.header("Recommendations")

        st.markdown("""
        - 🚨 **Trigger early interventions**: Interns with **<50% attendance in their first month** often remain low-engagement. **Intervene within the first 2 weeks**.
        - 🏆 **Recognize top performers monthly**: This will motivate interns in the **60–80% bracket** to push toward higher consistency.
        - 🔔 **Enable smart alerts**: Set up alerts for interns with **>15% absences** to prompt **1:1 engagement or mentoring**.
        - 📆 **Leverage attendance patterns**: Assign **important sessions or projects** on high-attendance days (e.g., Tuesdays & Wednesdays).
        - 📝 **Adopt a standardized leave form**: Replace emails with a **central leave submission tool** for accurate, structured, and analyzable data.
        """)

        st.header("Assumptions")
        st.markdown(""" 
                    - Student IDs are unique and persist through the reporting period.

                    \n- Absence data is accurately logged with no manual overrides.

                    \n- New interns are defined as individuals who do not appear in the previous month’s dataset.

                    \n- All sessions have equal weight and are mandatory unless otherwise stated.
                    \n-  The **first recorded attendance entry** for each intern is assumed to represent their **official date of joining** the internship.
                    """)
        st.subheader("🎯 Key Questions for Senior Partners")

        st.markdown("""
        To better understand your needs and improve the attendance dashboard, please consider the following questions:


        1. **What time interval should we use to measure attendance trends?**  
        (e.g., daily, weekly, monthly)

        2. **What actions do you want the dashboard users to take based on the attendance insights?**  
        (e.g., follow-up with absentees, adjust schedules)

        3. **Should the dashboard highlight any attendance anomalies or patterns?**  
        (e.g., repeated absences, unusual attendance drops)

        4. **What level of detail do you want available?**  
        (e.g., overall summary vs. individual intern attendance records)

        5. **Do you want the ability to filter attendance data by date range/relevant period or intern attributes?**  
        (e.g., filter by month, team, or location)

        6. **Are there any existing attendance tracking systems we need to integrate with or consider?**

        7. **How do you want missing or inconsistent attendance data handled?**  
        (e.g., mark as unknown, exclude)

        8. **What frequency do you prefer for dashboard updates?**  
        (e.g., real-time, daily batch updates)

        9. **Are there privacy or data security considerations we should be aware of?**

""")
