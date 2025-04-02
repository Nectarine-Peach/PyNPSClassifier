import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # 스타일시트 설정
    app.setStyleSheet("""
        QMainWindow {
            background-color: #f5f6f7;
        }
        
        QWidget {
            font-family: 'Segoe UI', 'Malgun Gothic', sans-serif;
        }
        
        /* 헤더 스타일 */
        #headerWidget {
            background-color: white;
            border-bottom: 1px solid #e9ecef;
        }
        
        #headerTitle {
            font-size: 18px;
            font-weight: bold;
            color: #1a1a1a;
            margin-right: 20px;
        }
        
        #headerButton {
            padding: 6px 12px;
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            color: #212529;
            font-weight: 500;
            min-width: 80px;
        }
        
        #headerButton:hover {
            background-color: #e9ecef;
            border-color: #dee2e6;
        }
        
        /* 모델 선택 버튼 스타일 */
        #modelButton {
            padding: 6px 14px;
            background-color: #0d6efd;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: 500;
            min-width: 100px;
        }
        
        #modelButton:hover {
            background-color: #0b5ed7;
        }
        
        /* 왼쪽 섹션 스타일 */
        #leftSection {
            background-color: white;
            border: 1px solid #e9ecef;
            border-radius: 6px;
            padding: 16px;
        }
        
        #searchBox {
            padding: 8px 12px;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            margin-bottom: 12px;
        }
        
        #searchBox:focus {
            border-color: #0d6efd;
            outline: none;
        }
        
        #categoryTree {
            border: none;
            background-color: transparent;
            margin-top: 10px;
        }
        
        #categoryTree::item {
            padding: 8px 6px;
            border-radius: 4px;
            min-height: 30px;
        }
        
        #categoryTree::item:selected {
            background-color: #e7f1ff;
            color: #0d6efd;
        }
        
        #categoryTree::item:hover {
            background-color: #f8f9fa;
        }
        
        /* 오른쪽 섹션 스타일 */
        #uploadSection {
            background-color: white;
            border: 1px solid #e9ecef;
            border-radius: 6px;
            text-align: center;
        }
        
        #uploadButton {
            padding: 12px 24px;
            background-color: #0d6efd;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: 500;
            margin: 20px 0;
        }
        
        #uploadButton:hover {
            background-color: #0b5ed7;
        }
        
        #logSection {
            background-color: white;
            border: 1px solid #e9ecef;
            border-radius: 6px;
        }
        
        #logTitle {
            font-size: 16px;
            font-weight: 600;
            color: #1a1a1a;
        }
        
        #logFilterButton {
            padding: 4px 12px;
            background-color: transparent;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            color: #666;
            font-size: 12px;
        }
        
        #logFilterButton:hover {
            background-color: #f8f9fa;
        }
        
        #logText {
            border: none;
            background-color: #212529;
            color: #f8f9fa;
            font-family: 'Consolas', 'D2Coding', monospace;
            font-size: 12px;
            line-height: 1.4;
            padding: 12px;
        }
        
        /* 공통 스타일 */
        QComboBox {
            padding: 6px 12px;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            background-color: white;
            min-width: 150px;
        }
        
        QComboBox:hover {
            border-color: #0d6efd;
        }
        
        QComboBox::drop-down {
            border: none;
            width: 20px;
        }
        
        QComboBox::down-arrow {
            image: url(down_arrow.png);
            width: 12px;
            height: 12px;
        }
        
        #sectionTitle {
            font-size: 16px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 8px;
        }
        
        /* 카테고리 설정 다이얼로그 스타일 */
        QDialog {
            background-color: #f5f6f7;
        }
        
        #settingsHeader {
            background-color: white;
            border-bottom: 1px solid #e9ecef;
            padding: 16px 20px;
        }
        
        #categorySection {
            background-color: white;
            border: 1px solid #e9ecef;
            border-radius: 6px;
            padding: 20px;
            margin-top: 10px;
        }
        
        #settingsCategoryTree {
            border: none;
            background-color: transparent;
            outline: none;
        }
        
        #settingsCategoryTree::item {
            padding: 8px 6px;
            margin: 2px 0;
            border-radius: 4px;
            min-height: 30px;
        }
        
        #settingsCategoryTree::item:hover {
            background-color: #f8f9fa;
        }
        
        #settingsCategoryTree::item:selected {
            background-color: #e7f1ff;
        }
        
        #settingsCategoryTree QLineEdit {
            padding: 4px 8px;
            margin: 0;
            border: 1px solid transparent;
            border-radius: 4px;
            background-color: transparent;
            min-height: 24px;
            font-size: 13px;
        }
        
        #settingsCategoryTree QLineEdit:hover {
            background-color: #f8f9fa;
            border-color: #dee2e6;
        }
        
        #settingsCategoryTree QLineEdit:focus {
            background-color: white;
            border-color: #0d6efd;
        }
        
        #settingsCategoryTree QWidget {
            min-height: 32px;
        }
        
        #addButton {
            padding: 6px 12px;
            background-color: #0d6efd;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: 500;
            min-width: 100px;
        }
        
        #addButton:hover {
            background-color: #0b5ed7;
        }
        
        #deleteButton {
            background-color: transparent;
            color: #dc3545;
            border: 1px solid #dc3545;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            padding: 4px 10px;
        }
        
        #deleteButton:hover {
            background-color: #dc3545;
            color: white;
        }
        
        #primaryButton {
            padding: 6px 16px;
            background-color: #0d6efd;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: 500;
            min-width: 100px;
        }
        
        #primaryButton:hover {
            background-color: #0b5ed7;
        }
        
        #secondaryButton {
            padding: 6px 16px;
            background-color: #f8f9fa;
            color: #212529;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            font-weight: 500;
            min-width: 100px;
        }
        
        #secondaryButton:hover {
            background-color: #e9ecef;
            border-color: #dee2e6;
        }
        
        QLineEdit {
            padding: 6px 12px;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            background-color: white;
        }
        
        QLineEdit:focus {
            border-color: #0d6efd;
            outline: none;
        }
        
        QSpinBox {
            padding: 6px 12px;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            background-color: white;
        }
        
        QSpinBox:focus {
            border-color: #0d6efd;
            outline: none;
        }
        
        QCheckBox {
            spacing: 8px;
        }
        
        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            border: 1px solid #dee2e6;
            border-radius: 3px;
            background-color: white;
        }
        
        QCheckBox::indicator:checked {
            background-color: #0d6efd;
            border-color: #0d6efd;
            image: url(check.png);
        }
        
        QCheckBox::indicator:hover {
            border-color: #0d6efd;
        }
        
        /* 인라인 버튼 스타일 */
        #inlineAddButton, #inlineDeleteButton {
            background-color: transparent;
            border: 1px solid transparent;
            border-radius: 4px;
            font-size: 14px;
            font-weight: bold;
            padding: 2px;
            min-width: 30px;
            max-width: 30px;
            min-height: 30px;
            max-height: 30px;
            margin: 2px;
        }
        
        #inlineAddButton {
            color: #0d6efd;
        }
        
        #inlineAddButton:hover {
            background-color: #e7f1ff;
            border-color: #0d6efd;
        }
        
        #inlineDeleteButton {
            color: #dc3545;
        }
        
        #inlineDeleteButton:hover {
            background-color: #ffebee;
            border-color: #dc3545;
        }
    """)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 