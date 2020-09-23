# coding:utf-8
import os
from MyQR import myqr


class easyMake():
    Content = "https://www.baidu.com"
    filename: str
    targetPath: str

    def __init__(self, filename, targetname):
        self.filename = filename
        self.targetPath = targetname

    def easy_Mk(self):
        print(self.Content)
        version, level, qr_name = myqr.run(
            words=self.Content,
            version=1,
            level='H',
            picture=self.filename,
            colorized=True,
            contrast=2.0,
            brightness=1.5,
            save_name=self.targetPath,
            save_dir=os.getcwd()
        )


# easymm = easyMake('E:/Project/CompanyProject/mo.gif','E:/Project/CompanyProject/grd.gif')
# easymm.easy_Mk()