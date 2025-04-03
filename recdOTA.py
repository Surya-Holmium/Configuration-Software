from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QListWidget, QGridLayout, QWidget, QListWidgetItem, 
    QLabel, QPushButton
)
from PyQt6.QtCore import Qt


class SearchableDropdown(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change Board Revision and Serial Number")
        self.setGeometry(100, 100, 400, 300)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Grid layout
        layout = QGridLayout(central_widget)

        # Serial Number
        self.serialLabel = QLabel("Serial Number")
        self.serialNumber = QLineEdit(self)
        self.serialNumber.setPlaceholderText("Search Serial Number...")
        layout.addWidget(self.serialLabel, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.serialNumber, 0, 1, 1, 2)
        self.dropdown_list_for_serialNumber = QListWidget(self)
        self.dropdown_list_for_serialNumber.setFixedHeight(0)
        layout.addWidget(self.dropdown_list_for_serialNumber, 1, 1, 1, 2)
        self.populate_serial_list()
        self.serialNumber.textChanged.connect(self.filter_serial_list)
        self.dropdown_list_for_serialNumber.itemClicked.connect(self.on_serialNumber_selected)

        # Board Revision
        self.boardRevisionLabel = QLabel("Board Revision")
        self.boardNumber = QLineEdit(self)
        self.boardNumber.setPlaceholderText("Search Board Revision...")
        layout.addWidget(self.boardRevisionLabel, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.boardNumber, 2, 1, 1, 2)
        self.dropdown_list_for_boardRevision = QListWidget(self)
        self.dropdown_list_for_boardRevision.setFixedHeight(0)
        layout.addWidget(self.dropdown_list_for_boardRevision, 3, 1, 1, 2)
        self.populate_board_revision_list()
        self.boardNumber.textChanged.connect(self.filter_board_revision_list)
        self.dropdown_list_for_boardRevision.itemClicked.connect(self.on_boardRevision_selected)

        # Button
        self.upload_button = QPushButton("Upload")
        self.upload_button.clicked.connect(self.upload_binfile)
        layout.addWidget(self.upload_button, 4, 1)

    def populate_serial_list(self):
        self.serial_numbers = [str(i) for i in range(1, 1001)]
        for item in self.serial_numbers:
            QListWidgetItem(item, self.dropdown_list_for_serialNumber)

    def populate_board_revision_list(self):
        self.board_revisions = [str(i) for i in range(1, 1001)]
        for item in self.board_revisions:
            QListWidgetItem(item, self.dropdown_list_for_boardRevision)

    def filter_serial_list(self, text):
        self.dropdown_list_for_serialNumber.clear()
        filtered_items = [item for item in self.serial_numbers if text in item]
        self.dropdown_list_for_serialNumber.addItems(filtered_items)
        if filtered_items:
            self.dropdown_list_for_serialNumber.setFixedHeight(150)
        else:
            self.dropdown_list_for_serialNumber.setFixedHeight(0)

    def filter_board_revision_list(self, text):
        self.dropdown_list_for_boardRevision.clear()
        filtered_items = [item for item in self.board_revisions if text in item]
        self.dropdown_list_for_boardRevision.addItems(filtered_items)
        if filtered_items:
            self.dropdown_list_for_boardRevision.setFixedHeight(150)
        else:
            self.dropdown_list_for_boardRevision.setFixedHeight(0)

    def on_serialNumber_selected(self, item):
        self.serialNumber.setText(item.text())
        self.dropdown_list_for_serialNumber.setFixedHeight(0) 

    def on_boardRevision_selected(self, item):
        self.boardNumber.setText(item.text())
        self.dropdown_list_for_boardRevision.setFixedHeight(0)

    def upload_binfile(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    window = SearchableDropdown()
    window.show()
    app.exec()
