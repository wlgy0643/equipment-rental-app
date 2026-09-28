# 사내 비품 대여 관리

Python과 Streamlit으로 만든 간단한 대여 등록·조회 앱입니다.

## Windows에서 처음 실행하기

1. Python이 없다면 https://www.python.org/downloads/ 에서 Python 3.12 이상을 설치하세요. 설치 화면에서 **Add python.exe to PATH**를 선택하세요.
2. 이 폴더의 **install.bat**를 더블클릭하세요. 최초 설치에는 인터넷 연결이 필요합니다. Installation complete가 나오면 창을 닫으세요.
3. **run.bat**를 더블클릭하세요.
4. 브라우저가 자동으로 열립니다. 열리지 않으면 주소창에 **http://localhost:8501** 을 입력하세요.
5. 직원명, 부서, 비품, 대여일, 반납예정일을 입력하고 **대여 등록**을 누르세요. 아래 표에 바로 표시됩니다.

다음부터는 run.bat만 실행하면 됩니다. 실행 중에는 검은 명령 창을 열어 두세요. 종료하려면 명령 창에서 Ctrl+C를 누르세요.

## 파일 안내

- app.py: 입력 화면과 대여 현황 표. DEPARTMENTS와 ITEMS 목록을 수정하면 선택 항목을 바꿀 수 있습니다.
- storage.py: CSV 읽기와 저장
- requirements.txt: 설치할 Python 패키지
- install.bat: 가상환경 생성 및 패키지 설치
- run.bat: 앱 실행
- data/rentals.csv: 대여 데이터. 처음에는 열 제목만 있습니다.

데이터는 앱 종료 후에도 유지됩니다. 한글을 읽을 수 있도록 UTF-8 BOM 형식으로 저장합니다. 백업하려면 앱 종료 후 data/rentals.csv를 복사하세요.
등록번호와 등록일시는 자동으로 추가됩니다. 직원명 누락, 미선택 항목, 잘못된 날짜 순서는 저장하지 않습니다.

## 직접 명령어로 실행하기

이 폴더에서 터미널을 열고 순서대로 실행하세요. 가상환경 활성화는 필요하지 않습니다.

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app.py --server.address localhost
```

## 문제가 생기면

- Python을 찾을 수 없음: Python을 설치하고 PATH 옵션을 선택한 뒤 다시 실행하세요.
- No module named streamlit: install.bat를 실행하여 설치를 완료하세요.
- 저장 실패: Excel에서 CSV를 열고 있다면 닫고, 폴더 쓰기 권한을 확인하세요.
- 포트 8501 사용 중: 이전 앱 창을 종료하거나 실행 명령 끝에 --server.port 8502를 추가하고 http://localhost:8502 에 접속하세요.
- 다른 창에서 등록한 내용이 안 보임: **현황 새로고침**을 누르세요.

## 사용 범위

이 버전은 로컬 PC에서 실행하며 로그인, 재고 수량 관리, 반납 처리 기능은 포함하지 않습니다.
동일 CSV를 여러 앱 프로세스나 여러 PC에서 동시에 수정하지 마세요. 여러 브라우저가 하나의 앱 프로세스에 접속하는 경우에는 저장 요청을 순서대로 처리합니다. OneDrive 동기화 폴더도 여러 PC에서 동시에 실행하는 용도로 사용하지 마세요.

Streamlit 공식 설치 안내: https://docs.streamlit.io/get-started/installation
