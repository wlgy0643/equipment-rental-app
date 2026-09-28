"""사내 비품 대여 관리 앱. 실행: python -m streamlit run app.py"""
from datetime import date, timedelta
import pandas as pd
import streamlit as st
from storage import load_rentals, save_rental

# 회사에 맞게 아래 목록을 수정하세요.
DEPARTMENTS = ["경영지원팀", "인사팀", "재무팀", "영업팀", "IT팀", "시설관리팀", "기타"]
ITEMS = ["노트북", "태블릿", "프로젝터", "회의용 스피커", "카메라", "공구 세트", "기타"]

st.set_page_config(page_title="사내 비품 대여 관리", page_icon="📋", layout="wide")
st.title("📋 사내 비품 대여 관리")
st.caption("대여 정보를 등록하고 직원별 비품 대여 현황을 확인하세요.")

with st.form("rental_form", clear_on_submit=False):
    st.subheader("대여 등록")
    employee = st.text_input("직원명", max_chars=50, placeholder="예: 홍길동")
    left, right = st.columns(2)
    department = left.selectbox("부서", DEPARTMENTS, index=None, placeholder="부서를 선택하세요")
    item = right.selectbox("대여 비품", ITEMS, index=None, placeholder="비품을 선택하세요")
    left, right = st.columns(2)
    rental_date = left.date_input("대여일", value=date.today(), format="YYYY/MM/DD")
    due_date = right.date_input("반납예정일", value=date.today() + timedelta(days=7), format="YYYY/MM/DD")
    submitted = st.form_submit_button("대여 등록", type="primary")
    if submitted:
        if not employee.strip():
            st.error("직원명을 입력해 주세요.")
        elif department is None or item is None:
            st.error("부서와 대여 비품을 모두 선택해 주세요.")
        elif due_date < rental_date:
            st.error("반납예정일은 대여일과 같거나 이후여야 합니다.")
        else:
            try:
                save_rental(employee.strip(), department, item, rental_date, due_date)
            except (OSError, ValueError) as exc:
                st.error(f"저장하지 못했습니다. CSV 파일과 폴더의 쓰기 권한을 확인해 주세요. ({exc})")
            else:
                st.success(f"{employee.strip()} 님의 대여가 등록되었습니다.")

st.divider()
st.subheader("등록된 대여 현황")
st.button("현황 새로고침")
try:
    records = load_rentals()
except (OSError, ValueError) as exc:
    st.error(f"대여 현황을 읽지 못했습니다. data/rentals.csv 파일을 확인해 주세요. ({exc})")
else:
    st.caption(f"총 {len(records)}건 · 최근 등록순")
    if records:
        st.dataframe(pd.DataFrame(list(reversed(records))), hide_index=True, use_container_width=True)
    else:
        st.info("아직 등록된 대여가 없습니다. 위 양식에서 첫 대여를 등록해 주세요.")
st.caption("저장 위치: 앱 폴더의 data/rentals.csv")
