from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QPushButton, QTreeWidget, QTreeWidgetItem,
                             QFileDialog, QTextEdit, QFrame, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NPS Data Classifier")
        self.setMinimumSize(1200, 800)
        
        # 메인 위젯 설정
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 헤더 영역
        header = self._create_header()
        main_layout.addWidget(header)
        
        # 메인 컨텐츠 영역
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        
        # 왼쪽 섹션 (카테고리 트리)
        left_section = self._create_left_section()
        content_layout.addWidget(left_section, 1)
        
        # 오른쪽 섹션 (파일 선택 및 로그)
        right_section = self._create_right_section()
        content_layout.addWidget(right_section, 2)
        
        main_layout.addWidget(content_widget)
        
    def _create_header(self):
        header = QWidget()
        header.setObjectName("headerWidget")
        layout = QHBoxLayout(header)
        layout.setContentsMargins(20, 12, 20, 12)
        
        # 앱 타이틀과 모델 선택 영역
        left_header = QHBoxLayout()
        
        title = QLabel("NPS Data Classifier")
        title.setObjectName("headerTitle")
        left_header.addWidget(title)
        
        model_label = QLabel("LLM Model:")
        model_label.setStyleSheet("color: #666;")
        left_header.addWidget(model_label)
        
        model_combo = QComboBox()
        model_combo.addItems(["gemma:4b", "GPT-4", "GPT-3.5", "Claude"])
        model_combo.setMinimumWidth(150)
        left_header.addWidget(model_combo)
        
        left_header.addStretch()
        layout.addLayout(left_header, stretch=2)
        
        # 버튼 영역
        button_layout = QHBoxLayout()
        button_layout.setSpacing(8)
        
        buttons = [
            ("설정 저장", "save"),
            ("설정 내보내기", "export"),
            ("AI 설정", "ai"),
            ("카테고리 설정", "category")
        ]
        
        for text, icon_name in buttons:
            btn = QPushButton(text)
            btn.setObjectName("headerButton")
            button_layout.addWidget(btn)
            btn.clicked.connect(lambda checked, b=text: self._show_popup(b))
        
        layout.addLayout(button_layout)
        return header
    
    def _create_left_section(self):
        section = QWidget()
        section.setObjectName("leftSection")
        layout = QVBoxLayout(section)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # 섹션 헤더
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        title = QLabel("분류 카테고리")
        title.setObjectName("sectionTitle")
        count = QLabel("(총 0개)")
        count.setStyleSheet("color: #666;")
        
        header_layout.addWidget(title)
        header_layout.addWidget(count)
        header_layout.addStretch()
        
        # 카테고리 검색
        search_box = QLineEdit()
        search_box.setPlaceholderText("카테고리 검색...")
        search_box.setObjectName("searchBox")
        
        # 카테고리 트리
        tree = QTreeWidget()
        tree.setHeaderLabels(["카테고리", "갯수"])
        tree.setColumnWidth(0, 250)
        tree.setAlternatingRowColors(True)
        tree.setObjectName("categoryTree")
        
        # 샘플 카테고리 데이터
        categories = [
            ("UI & Visual Design", [
                "레이아웃 구조 관련",
                "디자인 품질/일관성 관련",
                "가독성 관련",
                "이미지/미디어 품질 관련"
            ]),
            ("Content & Information", [
                "제품 정보 관련",
                "콘텐츠 관련",
                "번역/용어 관련",
                "정보 과다/과부족"
            ])
        ]
        
        for category, subcategories in categories:
            item = QTreeWidgetItem(tree, [category, "0"])
            for sub in subcategories:
                QTreeWidgetItem(item, [sub, "0"])
        
        layout.addWidget(header)
        layout.addWidget(search_box)
        layout.addWidget(tree)
        return section
    
    def _create_right_section(self):
        section = QWidget()
        section.setObjectName("rightSection")
        layout = QVBoxLayout(section)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        
        # 파일 업로드 영역
        upload_section = QWidget()
        upload_section.setObjectName("uploadSection")
        upload_layout = QVBoxLayout(upload_section)
        upload_layout.setContentsMargins(20, 20, 20, 20)
        
        upload_title = QLabel("NPS 데이터 파일 업로드")
        upload_title.setObjectName("sectionTitle")
        upload_layout.addWidget(upload_title)
        
        upload_desc = QLabel("또는 드래그 앤 드롭으로 파일을 업로드하세요")
        upload_desc.setStyleSheet("color: #666;")
        upload_layout.addWidget(upload_desc)
        
        file_btn = QPushButton("파일 선택하기")
        file_btn.setObjectName("uploadButton")
        file_btn.clicked.connect(self._select_file)
        upload_layout.addWidget(file_btn, alignment=Qt.AlignCenter)
        
        file_type = QLabel("CSV, Excel 파일 지원 (.csv, .xlsx, .xls)")
        file_type.setStyleSheet("color: #666; font-size: 12px;")
        upload_layout.addWidget(file_type, alignment=Qt.AlignCenter)
        
        layout.addWidget(upload_section)
        
        # 로그 영역
        log_section = QWidget()
        log_section.setObjectName("logSection")
        log_layout = QVBoxLayout(log_section)
        log_layout.setContentsMargins(0, 0, 0, 0)
        
        log_header = QWidget()
        log_header_layout = QHBoxLayout(log_header)
        log_header_layout.setContentsMargins(12, 12, 12, 0)
        
        log_title = QLabel("Processing Logs")
        log_title.setObjectName("logTitle")
        log_header_layout.addWidget(log_title)
        
        # 로그 필터 버튼들
        filter_buttons = ["전체", "에러", "성공", "정보"]
        for text in filter_buttons:
            btn = QPushButton(text)
            btn.setObjectName("logFilterButton")
            log_header_layout.addWidget(btn)
        
        log_layout.addWidget(log_header)
        
        log_text = QTextEdit()
        log_text.setReadOnly(True)
        log_text.setObjectName("logText")
        log_layout.addWidget(log_text)
        
        layout.addWidget(log_section)
        return section
    
    def _select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "파일 선택",
            "",
            "Excel Files (*.xlsx *.xls);;CSV Files (*.csv)"
        )
        if file_name:
            # 파일 선택 후 처리 로직은 나중에 구현
            pass
    
    def _show_popup(self, button_text):
        # 팝업 표시 로직은 나중에 구현
        pass 