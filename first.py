import streamlit as st
st.set_page_config(page_title='音乐播放器', page_icon='🎵')
st.header("🎶简易音乐播放器")
music = [
    {
        'url': 'https://music.163.com/song/media/outer/url?id=2078077516.mp3',
        'parm': '坏女孩',
        'photo':'https://p1.music.126.net/kZb9DO4vykqiYEx0HHx86w==/109951163065542645.jpg?param=230y230',
        'author':'歌手:徐良'
        
    },
    {
          'url': 'https://music.163.com/song/media/outer/url?id=455535252.mp3',
          'parm': '泡沫',
          'photo':'https://p1.music.126.net/oJorrgJ3IotZUAbZkBMuFw==/109951167771736533.jpg?param=230y230',
          'author':'歌手:邓紫棋'
     },
    {
         'url': 'https://music.163.com/song/media/outer/url?id=464534706.mp3',
         'parm': '演员',
         'photo':'https://p1.music.126.net/jj_Ke8S0q8lpDtohy9seDw==/109951168719781607.jpg?param=230y230',
         'author':'歌手:薛之谦'
     }

]





if 'ind' not in st.session_state:
   st.session_state['ind'] = 0


def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music)

def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(music)

a1, a2 = st.columns([1, 2])

with a1:
    st.image(music[st.session_state['ind']]['photo'])

with a2:
    st.title(music[st.session_state['ind']]['parm'])
    st.text(music[st.session_state['ind']]['author'])
    st.audio(music[st.session_state['ind']]['url'],autoplay=True)
    
c1,c2 = st.columns(2)

    
with c1:
    st.button('上一首', on_click=prevImg, use_container_width=True)

with c2:
    st.button('下一首', on_click=nextImg,use_container_width=True)

st.header("音乐列表")
st.text("1.坏女孩")
st.text("2.泡沫")
st.text("3.演员")

