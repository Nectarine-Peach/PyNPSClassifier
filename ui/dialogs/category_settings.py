from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QSpinBox, QTreeWidget, QTreeWidgetItem,
                             QPushButton, QLineEdit, QMessageBox, QToolButton)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon

class CategorySettingsDialog(QDialog):
    # 카테고리 변경 시그널
    categoriesChanged = pyqtSignal(list)
    
    def __init__(self, parent=None, categories=None):
        super().__init__(parent)
        self.setWindowTitle("Categories Settings")
        self.setMinimumSize(800, 600)
        
        # 현재 카테고리 데이터 저장
        self.categories = categories or []
        
        # UI 초기화
        self._init_ui()
        
        # 카테고리 데이터 로드
        self._load_categories()
    
    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        
        # 헤더 영역
        header = self._create_header()
        layout.addWidget(header)
        
        # 카테고리 관리 영역
        category_section = self._create_category_section()
        layout.addWidget(category_section)
        
        # 버튼 영역
        buttons = self._create_buttons()
        layout.addWidget(buttons)
    
    def _create_header(self):
        header = QWidget()
        header.setObjectName("settingsHeader")
        layout = QHBoxLayout(header)
        
        # 헤더 로우 설정
        header_row_label = QLabel("Header Row:")
        self.header_row_spin = QSpinBox()
        self.header_row_spin.setMinimum(1)
        self.header_row_spin.setValue(1)
        self.header_row_spin.setFixedWidth(80)
        
        layout.addWidget(header_row_label)
        layout.addWidget(self.header_row_spin)
        
        layout.addStretch()
        
        # 카테고리 추가 버튼
        add_btn = QPushButton("+ Add Category")
        add_btn.setObjectName("addButton")
        add_btn.clicked.connect(self._add_category)
        layout.addWidget(add_btn)
        
        return header
    
    def _create_category_section(self):
        section = QWidget()
        section.setObjectName("categorySection")
        layout = QVBoxLayout(section)
        
        # 카테고리 트리
        self.category_tree = QTreeWidget()
        self.category_tree.setHeaderLabels(["Categories"])
        self.category_tree.setColumnWidth(0, 700)
        self.category_tree.setObjectName("settingsCategoryTree")
        self.category_tree.setIndentation(20)
        
        layout.addWidget(self.category_tree)
        return section
    
    def _create_buttons(self):
        buttons = QWidget()
        layout = QHBoxLayout(buttons)
        layout.setContentsMargins(0, 0, 0, 0)
        
        layout.addStretch()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        
        save_btn = QPushButton("Save Changes")
        save_btn.setObjectName("primaryButton")
        save_btn.clicked.connect(self._save_changes)
        
        layout.addWidget(cancel_btn)
        layout.addWidget(save_btn)
        
        return buttons
    
    def _create_item_widget(self, item, is_category=True):
        """아이템별 액션 버튼 위젯 생성"""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(5, 2, 5, 2)
        layout.setSpacing(8)
        
        # 수정 가능한 이름 입력 필드
        name_edit = QLineEdit()
        # item.text(0)를 사용하지 않고 빈 텍스트로 시작
        name_edit.setStyleSheet("QLineEdit { border: none; background: transparent; padding: 2px; }")
        # textChanged 이벤트 핸들러 제거 - 더 이상 필요 없음
        
        # 버튼 컨테이너
        buttons = QWidget()
        button_layout = QHBoxLayout(buttons)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(4)
        
        if is_category:
            # 서브카테고리 추가 버튼
            add_sub_btn = QToolButton()
            add_sub_btn.setText("+")
            add_sub_btn.setToolTip("Add Subcategory")
            add_sub_btn.setObjectName("inlineAddButton")
            add_sub_btn.clicked.connect(lambda: self._add_subcategory(item))
            button_layout.addWidget(add_sub_btn)
        
        # 삭제 버튼
        delete_btn = QToolButton()
        delete_btn.setText("×")
        delete_btn.setToolTip("Delete")
        delete_btn.setObjectName("inlineDeleteButton")
        delete_btn.clicked.connect(lambda: self._delete_item(item))
        button_layout.addWidget(delete_btn)
        
        layout.addWidget(name_edit, 1)
        layout.addWidget(buttons, 0)
        return widget
    
    def _load_categories(self):
        """카테고리 데이터를 트리에 로드"""
        self.category_tree.clear()
        
        for category, subcategories in self.categories:
            # 트리 아이템 생성 시 빈 텍스트로 초기화
            item = QTreeWidgetItem(self.category_tree, [""])
            widget = self._create_item_widget(item)
            self.category_tree.setItemWidget(item, 0, widget)
            
            # 텍스트를 QLineEdit에 직접 설정
            name_edit = widget.layout().itemAt(0).widget()
            name_edit.setText(category)
            
            for sub in subcategories:
                # 서브카테고리도 빈 텍스트로 초기화
                sub_item = QTreeWidgetItem(item, [""])
                sub_widget = self._create_item_widget(sub_item, False)
                self.category_tree.setItemWidget(sub_item, 0, sub_widget)
                
                # 서브카테고리 텍스트를 QLineEdit에 직접 설정
                sub_name_edit = sub_widget.layout().itemAt(0).widget()
                sub_name_edit.setText(sub)
    
    def _add_category(self):
        """새 카테고리 추가"""
        # 빈 텍스트로 아이템 생성
        item = QTreeWidgetItem(self.category_tree, [""])
        widget = self._create_item_widget(item)
        self.category_tree.setItemWidget(item, 0, widget)
        
        # 직접 QLineEdit에 텍스트 설정
        name_edit = widget.layout().itemAt(0).widget()
        name_edit.setText("New Category")
        
        self.category_tree.scrollToItem(item)
    
    def _add_subcategory(self, parent_item):
        """서브카테고리 추가"""
        # 빈 텍스트로 아이템 생성
        item = QTreeWidgetItem(parent_item, [""])
        widget = self._create_item_widget(item, False)
        self.category_tree.setItemWidget(item, 0, widget)
        
        # 직접 QLineEdit에 텍스트 설정
        name_edit = widget.layout().itemAt(0).widget()
        name_edit.setText("New Subcategory")
        
        parent_item.setExpanded(True)
        self.category_tree.scrollToItem(item)
    
    def _delete_item(self, item):
        """아이템 삭제"""
        if item.parent():
            item.parent().removeChild(item)
        else:
            index = self.category_tree.indexOfTopLevelItem(item)
            self.category_tree.takeTopLevelItem(index)
    
    def _save_changes(self):
        """변경사항 저장"""
        categories = []
        root = self.category_tree.invisibleRootItem()
        
        for i in range(root.childCount()):
            category = root.child(i)
            name_edit = self.category_tree.itemWidget(category, 0).layout().itemAt(0).widget()
            subcategories = []
            
            for j in range(category.childCount()):
                sub_item = category.child(j)
                sub_name_edit = self.category_tree.itemWidget(sub_item, 0).layout().itemAt(0).widget()
                subcategories.append(sub_name_edit.text())
            
            categories.append((name_edit.text(), subcategories))
        
        self.categoriesChanged.emit(categories)
        self.accept() 