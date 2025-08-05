import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="YouTube Channel Analytics")

# --- TITLE ---
st.title("📊 YouTube Channel Analytics Dashboard")
st.markdown("""
Analyze and visualize your YouTube channel's performance using views, likes, dislikes, and comments.
Upload your dataset (CSV) with the following columns:
- `VideoID`, `Title`, `UploadDate`, `Views`, `Likes`, `Dislikes`, `Comments`
""")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Preprocess
    df['UploadDate'] = pd.to_datetime(df['UploadDate'])
    df = df.sort_values('UploadDate')

    # --- DATA OVERVIEW ---
    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head(10))

    # --- METRICS ---
    total_views = df['Views'].sum()
    total_likes = df['Likes'].sum()
    total_dislikes = df['Dislikes'].sum()
    total_comments = df['Comments'].sum()

    col1, col2 = st.columns(2)
    col1.metric("Total Views", f"{total_views:,}")
    col2.metric("Total Likes", f"{total_likes:,}")
    col1, col2 = st.columns(2)
    col1.metric("Total Dislikes", f"{total_dislikes:,}")
    col2.metric("Total Comments", f"{total_comments:,}")

    st.markdown("---")

    # --- LINE CHART: Views Over Time ---
    st.subheader("📈 Views Over Time")
    views_over_time = df.groupby('UploadDate')['Views'].sum()

    fig1, ax1 = plt.subplots()
    ax1.plot(views_over_time.index, views_over_time.values, color='blue', linewidth=2)
    ax1.set_title("Total Views Over Time")
    ax1.set_xlabel("Upload Date")
    ax1.set_ylabel("Views")
    ax1.grid(True)
    st.pyplot(fig1)

    st.markdown("---")

    # --- BAR CHART: Top 20 Videos by Views ---
    st.subheader("🏆 Top 20 Videos by Views")
    top_videos = df.sort_values('Views', ascending=False).head(20)

    fig2, ax2 = plt.subplots()
    ax2.barh(top_videos['Title'], top_videos['Views'], color='orange')
    ax2.set_title("Top 20 Videos")
    ax2.set_xlabel("Views")
    ax2.invert_yaxis()
    st.pyplot(fig2)

    st.markdown("---")

    # --- PIE CHART: Engagement Breakdown ---
    st.subheader("🥧 Engagement Distribution")
    engagement_labels = ['Likes', 'Dislikes', 'Comments']
    engagement_values = [total_likes, total_dislikes, total_comments]

    fig3, ax3 = plt.subplots()
    ax3.pie(engagement_values, labels=engagement_labels, autopct='%1.1f%%', startangle=140)
    ax3.axis('equal')
    st.pyplot(fig3)

    st.markdown("---")

    # --- SUMMARY ---
    st.subheader("📝 Summary")
    st.markdown(f"""
    - Your channel has received **{total_views:,} views** across all videos.
    - Highest engagement comes from **likes**, followed by **comments**.
    - Use the **top 20 videos** chart to identify successful content patterns.
    - Use the **views over time** chart to see content growth trends.
    """)
else:
    st.warning("👆 Please upload a valid YouTube analytics CSV file to begin.")


## streamlit run app.py - To run this app, save it as `app.py` and use the command