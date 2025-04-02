from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QPushButton, QTreeWidget, QTreeWidgetItem,
                             QFileDialog, QTextEdit, QFrame, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from .dialogs.category_settings import CategorySettingsDialog
from .dialogs.prompt_settings import PromptSettingsDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NPS Data Classifier")
        self.setMinimumSize(1200, 800)
        
        # 카테고리 데이터 초기화
        self.categories = [
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
        
        # 기본 프롬프트 설정
        self.current_prompt = """다음 사용자 피드백 내용을 분석하여 가장 적합한 카테고리로 분류해주세요:
피드백: {feedback}

카테고리:
{category}

결과는 카테고리 이름만 반환하세요."""
        
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
        self.left_section = self._create_left_section()
        content_layout.addWidget(self.left_section, 1)
        
        # 오른쪽 섹션 (파일 선택 및 로그)
        right_section = self._create_right_section()
        content_layout.addWidget(right_section, 2)
        
        main_layout.addWidget(content_widget)
        
        # 카테고리 데이터 로드
        self._load_categories()
    
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
            ("프롬프트 설정", "ai"),
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
        self.category_count = QLabel("(총 0개)")
        self.category_count.setStyleSheet("color: #666;")
        
        header_layout.addWidget(title)
        header_layout.addWidget(self.category_count)
        header_layout.addStretch()
        
        # 카테고리 검색
        search_box = QLineEdit()
        search_box.setPlaceholderText("카테고리 검색...")
        search_box.setObjectName("searchBox")
        
        # 카테고리 트리
        self.category_tree = QTreeWidget()
        self.category_tree.setHeaderLabels(["카테고리", "갯수"])
        self.category_tree.setColumnWidth(0, 250)
        self.category_tree.setAlternatingRowColors(True)
        self.category_tree.setObjectName("categoryTree")
        
        layout.addWidget(header)
        layout.addWidget(search_box)
        layout.addWidget(self.category_tree)
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
        if button_text == "카테고리 설정":
            dialog = CategorySettingsDialog(self, self.categories)
            dialog.categoriesChanged.connect(self._update_categories)
            dialog.exec_()
        elif button_text == "프롬프트 설정":
            dialog = PromptSettingsDialog(self, self.current_prompt)
            dialog.promptChanged.connect(self._update_prompt)
            dialog.exec_()
    
    def _load_categories(self):
        """카테고리 데이터를 트리에 로드"""
        self.category_tree.clear()
        total_count = 0
        
        for category, subcategories in self.categories:
            item = QTreeWidgetItem(self.category_tree, [category, "0"])
            category_count = 0
            
            for sub in subcategories:
                sub_item = QTreeWidgetItem(item, [sub, "0"])
                category_count += 0  # 실제 데이터에서는 해당 카테고리의 항목 수를 더함
            
            item.setText(1, str(category_count))
            total_count += category_count
        
        self.category_count.setText(f"(총 {total_count}개)")
        self.category_tree.expandAll()
    
    def _update_categories(self, categories):
        """카테고리 설정이 변경되었을 때 호출"""
        self.categories = categories
        self._load_categories()
    
    def _update_prompt(self, prompt):
        """프롬프트 설정이 변경되었을 때 호출"""
        self.current_prompt = prompt 