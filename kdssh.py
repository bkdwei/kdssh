# coding: utf-8

import os
import sys
import pexpect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.uic import loadUi
from kdconfig import sshconfig


class kdssh(QMainWindow):
    def __init__(self):
        super(kdssh, self).__init__()
        loadUi("kdssh.ui", self)
        self.sshconfig = sshconfig()
        self.confs = self.sshconfig.confs
        self.sshconfig.lw_confs = self.lw_confs
        if self.confs:
            for conf in self.confs:
                self.lw_confs.addItem(conf["solution"])

    @pyqtSlot()
    def on_pb_addconfig_clicked(self):
        self.sshconfig.show()
        self.sshconfig.new_item_flag = True

    @pyqtSlot()
    def on_pb_editconf_clicked(self):
        self.sshconfig.show()
        self.sshconfig.new_item_flag = False
        item = self.lw_confs.currentItem()
        print(item.text())
        self.sshconfig.edit_conf(item.text())

    @pyqtSlot()
    def on_pb_delconf_clicked(self):
        item = self.lw_confs.currentItem()
        print(item.text())
        self.sshconfig.del_conf(item.text())
        self.lw_confs.removeItemWidget(
            self.lw_confs.takeItem(self.lw_confs.currentRow())
        )

    @pyqtSlot()
    def on_pb_connect_clicked(self):
        item = self.lw_confs.currentItem()
        print(item.text())
        for conf in self.confs:
            if conf["solution"] == item.text():
                self.ssh_connect(conf)

    def ssh_connect(self, conf):
        self.hide()
        cmd = "x-terminal-emulator -e /home/bkd/dev/pyqt/kdssh/create_session.sh {} {} {} {}".format(
            conf["host"], int(conf["port"]), conf["name"], conf["password"]
        )
        print(cmd)
        os.system(cmd)
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = kdssh()
    win.show()
    sys.exit(app.exec_())
