from PySide6.QtWidgets import QApplication, QWidget,QFileDialog

def get_file(self,file_name):
    file_name=str(QFileDialog.getExistingDirectory(self))
    print('this'+file_name)
    