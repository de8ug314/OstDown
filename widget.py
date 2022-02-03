# This Python file uses the following encoding: utf-8
from asyncio.windows_events import NULL
from inspect import getfile
import os
from sqlite3 import connect
import widget
from pathlib import Path
import sys
import form
from PySide6.QtWidgets import QApplication, QWidget,QFileDialog,QMessageBox,QCheckBox,QVBoxLayout
import spider
import share_lib
def new_thread(func,name,args):
    t=threading.Thread(target=func,name=name,args=args)
    t.start()
class Widget(QWidget,form.Ui_Widget):
    url=None
    url_add=None
    format=None
    path_name=None
    spi=None
    def __init__(self):
        super(Widget, self).__init__()
        self.setupUi(self)
        self.btn_check.setEnabled(1)
        self.btn_file.setEnabled(0)
        self.check()
        
        
        
    def check(self):
        self.btn_check.clicked.connect(self.get_info)
        self.btn_file.clicked.connect(self.get_file(self.path_name))
        
        #i don't know why this doesn't work normally
    def get_info(self):
        self.url=self.ed_url.text().strip()
        self.format=self.ed_format.text().strip()
        self.btn_down.setEnabled(1)
        spi=spider.spider(self.url,self.format,self.path_name)
        try:
            spi.getUrls()
            spi.getName8Type()
            spi.Dnowload(spi.url_add)
        except:
            mes=QMessageBox.critical(self,'error',"i don't why,but...\nget errorrrrr")
        y=0
        rad_btn=None
        lay_V=QVBoxLayout(self.scrollArea)
        
        for i,name in enumerate(spi.song_name):
            rad_btn=QCheckBox(self.scrollArea)
            rad_btn.setText(name)
            lay_V.addWidget(rad_btn)
            
        
    def get_file(self,file_name):
        file_name=str(QFileDialog.getExistingDirectory(self))
if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.setWindowTitle('OstDown')
    widget.show()
    sys.exit(app.exec())