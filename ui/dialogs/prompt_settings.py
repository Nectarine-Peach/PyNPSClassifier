from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QPushButton, QTextEdit)
from PyQt5.QtCore import Qt, pyqtSignal

class PromptSettingsDialog(QDialog):
    # 프롬프트 변경 시그널
    promptChanged = pyqtSignal(str)
    
    def __init__(self, parent=None, current_prompt=None):
        super().__init__(parent)
        self.setWindowTitle("프롬프트 설정")
        self.setMinimumSize(800, 600)
        
        # 현재 프롬프트 데이터 저장
        self.current_prompt = current_prompt or ""
        
        # UI 초기화
        self._init_ui()
        
    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        
        # 헤더 영역
        header = self._create_header()
        layout.addWidget(header)
        
        # 프롬프트 편집 영역
        prompt_section = self._create_prompt_section()
        layout.addWidget(prompt_section)
        
        # 버튼 영역
        buttons = self._create_buttons()
        layout.addWidget(buttons)
    
    def _create_header(self):
        header = QWidget()
        header.setObjectName("settingsHeader")
        layout = QHBoxLayout(header)
        
        # 헤더 제목
        title = QLabel("AI 프롬프트 편집")
        title.setObjectName("settingsTitle")
        layout.addWidget(title)
        
        layout.addStretch()
        
        return header
    
    def _create_prompt_section(self):
        section = QWidget()
        section.setObjectName("promptSection")
        layout = QVBoxLayout(section)
        
        # 설명 레이블
        desc_label = QLabel("AI 모델이 NPS 데이터를 분류할 때 사용할 프롬프트를 입력하세요:")
        layout.addWidget(desc_label)
        
        # 프롬프트 편집 영역
        self.prompt_edit = QTextEdit()
        self.prompt_edit.setPlaceholderText("프롬프트를 입력하세요...")
        self.prompt_edit.setText(self.current_prompt)
        self.prompt_edit.setMinimumHeight(400)
        layout.addWidget(self.prompt_edit)
        
        # 가이드 레이블
        guide_label = QLabel("* {category}와 {feedback} 태그는 실제 데이터로 대체됩니다.")
        guide_label.setStyleSheet("color: #666; font-size: 12px;")
        layout.addWidget(guide_label)
        
        return section
    
    def _create_buttons(self):
        buttons = QWidget()
        layout = QHBoxLayout(buttons)
        layout.setContentsMargins(0, 0, 0, 0)
        
        layout.addStretch()
        
        cancel_btn = QPushButton("취소")
        cancel_btn.setObjectName("secondaryButton")
        cancel_btn.clicked.connect(self.reject)
        
        save_btn = QPushButton("저장")
        save_btn.setObjectName("primaryButton")
        save_btn.clicked.connect(self._save_changes)
        
        layout.addWidget(cancel_btn)
        layout.addWidget(save_btn)
        
        return buttons
    
    def _save_changes(self):
        """변경사항 저장"""
        prompt_text = self.prompt_edit.toPlainText()
        self.promptChanged.emit(prompt_text)
        self.accept() 