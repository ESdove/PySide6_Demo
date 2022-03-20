import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-长度和只读限制")
window.resize(500, 500)
window.move(400, 250)

le_a = QLineEdit(window)
le_a.move(100, 100)
le_a.setMaxLength(5)  # 限制最大字符个数
# print(le_a.maxLength())

le_b = QLineEdit(window)
le_b.move(100, 150)
le_b.setText("muzing")
le_b.setReadOnly(True)  # 设置只读，可被选中，但不能修改

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())
