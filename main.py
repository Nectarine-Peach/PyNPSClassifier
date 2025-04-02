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
        }
        
        #categoryTree::item {
            padding: 6px 4px;
            border-radius: 4px;
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
    """)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 