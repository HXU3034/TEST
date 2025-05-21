
import streamlit as st

st.set_page_config(layout="centered")
st.title("🎉 Happy Birthday!")

# 圖片順序
pages = ['images/page1.png', 'images/page2.png', 'images/page3.png', 'images/page4.png', 'images/page5.png', 'images/page6.png', 'images/page7.png']

# 狀態追蹤
if "page_index" not in st.session_state:
    st.session_state.page_index = 0

# 顯示當前頁面
st.image(pages[st.session_state.page_index])

# 下一頁按鈕
if st.session_state.page_index < len(pages) - 1:
    if st.button("Next"):
        st.session_state.page_index += 1
else:
    st.success("🎈 You've reached the end of the birthday surprises!")
