import streamlit as st
from newsapi import NewsApiClient

def financial_news():
    st.title("📰 Financial News")

    newsapi = NewsApiClient(api_key='YOUR_NEWSAPI_KEY')  # Replace with your key
    
    try:
        news = newsapi.get_top_headlines(category='business', language='en', country='us')
        
        if news['totalResults'] > 0:
            for article in news['articles']:
                with st.expander(article['title']):
                    st.write(f"**Source**: {article['source']['name']}")
                    st.write(f"**Published**: {article['publishedAt'][:10]}")
                    st.write(article['description'])
                    st.markdown(f"[Read more]({article['url']})")
        else:
            st.warning("No financial news found.")
            
    except Exception as e:
        st.error(f"Error fetching news: {str(e)}")
