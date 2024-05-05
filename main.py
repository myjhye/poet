from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

# 환경 변수 설정
load_dotenv()

# 챗 모델 초기화
chat_model = ChatOpenAI()

# 스트림릿 웹 앱 인터페이스 설정
st.title('Inspire a Poem with your word!')

# 사용자 입력을 받는 텍스트 필드
content = st.text_input('Please enter a topic for the poem', placeholder='e.g., Nature, Love, Adventure')

# 버튼 클릭 시 실행될 액션
if st.button('Request Poem'):
    if content:  # 입력된 텍스트가 있는지 확인
        with st.spinner('loading...'):  # 로딩 스피너 표시
            # 챗 모델을 통해 시 생성 요청
            result = chat_model.invoke(f"please write me a poem about {content}")
            # 결과 출력
            st.write(result.content)
    else:
        # 입력된 텍스트가 없을 경우 경고 메시지 출력
        st.error('Please enter a topic.')
