
from PySide.QtGui import QKeySequence
from PySide.QtCore import Qt

from .menu import Menu, MenuEntry, MenuSeparator


class FileMenu(Menu):
    def __init__(self, main_window):
        super(FileMenu, self).__init__(main_window, "&File")

        self.entries.extend([
            MenuEntry('L&oad a new binary...', main_window.load_binary, shortcut=QKeySequence(Qt.CTRL + Qt.Key_O)),
            MenuSeparator(),
            MenuEntry('E&xit', main_window.quit),
        ])