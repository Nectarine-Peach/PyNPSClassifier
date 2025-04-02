다른 프로젝트에서 현재의 패키징 및 엑셀 로딩 관련 내용을 반영하기 위한 요구사항을 정리해드리겠습니다:

## 1. 패키징 관련 요구사항

### 1.1 필수 패키지
```
PyQt5
xlwings
pandas
numpy
pytz
dateutil
six
pyinstaller
```

### 1.2 PyInstaller 설정 (spec 파일)
```python
# 필수 hiddenimports
hiddenimports=['xlwings', 'pandas', 'numpy', 'pytz', 'dateutil', 'six']

# 제외할 모듈 (불필요한 의존성 제거)
excludes=['matplotlib', 'scipy', 'PIL', 'tkinter', 'PySide2', 'PySide6', 'PyQt6', 'openpyxl', 'xlrd']

# 중요 설정
console=False  # 콘솔 창 숨김
upx=False     # UPX 압축 비활성화 (바이러스 백신 오탐지 방지)
cipher=None   # 암호화 비활성화
```

### 1.3 빌드 명령어
```
pyinstaller --clean --noconfirm excel_viewer.spec
```

## 2. 엑셀 로딩 관련 요구사항

### 2.1 xlwings 사용 방식
```python
# 올바른 엑셀 파일 로딩 방식
app = xw.App(visible=False)  # 백그라운드에서 실행
wb = app.books.open(file_path)
sheet = wb.sheets[0]

# 데이터 읽기
data = sheet.range('A1:E30').value  # 범위 지정 방식

# 리소스 정리
wb.close()  # 파일 닫기
```

### 2.2 CSV 파일 로딩 방식
```python
# pandas를 사용한 CSV 파일 로딩
df = pd.read_csv(
    file_path,
    sep=None,           # 구분자 자동 감지
    engine='python',    # Python 엔진 사용
    encoding='utf-8',   # UTF-8 인코딩
    on_bad_lines='skip', # 잘못된 라인 건너뛰기
    quoting=3,          # QUOTE_NONE
    dtype=str           # 모든 컬럼을 문자열로 처리
)

# 대체 방법 (pandas 실패 시)
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()[:30]  # 처음 30줄만 읽기
```

### 2.3 오류 처리
```python
# 모든 파일 작업은 try-except로 감싸기
try:
    # 파일 작업 코드
except Exception as e:
    # 오류 메시지 표시 (GUI에 표시)
    self.text_edit.setText(str(e))
```

### 2.4 리소스 관리
```python
# 프로그램 종료 시 리소스 정리
def closeEvent(self, event):
    if self.wb:
        self.wb.close()
    event.accept()
```

## 3. 바이러스 백신 오탐지 방지 요구사항

1. 실행 파일 이름은 영문으로 지정
2. 불필요한 모듈은 excludes에 추가하여 제외
3. UPX 압축 비활성화
4. 암호화(cipher) 비활성화
5. 디버그 정보 최소화
6. 오류 메시지 단순화 (스택 트레이스 제거)

## 4. 성능 최적화 요구사항

1. 필요한 데이터만 로드 (예: 처음 30줄만)
2. 불필요한 모듈 제외
3. 리소스 사용 후 즉시 해제

## 5. 사용자 경험 요구사항

1. 백그라운드에서 엑셀 실행 (visible=False)
2. 콘솔 창 숨김 (console=False)
3. 간결한 오류 메시지 표시
4. 파일 선택 후 자동 로드

이 요구사항들을 다른 프로젝트에 적용하면 현재 프로젝트와 동일한 방식으로 엑셀 파일을 처리하고 패키징할 수 있습니다.
