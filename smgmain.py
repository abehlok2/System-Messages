from SystemMessageGenerator import generate_system_message
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QLabel, QStatusBar, QSpacerItem, QSizePolicy

def process_input():
    user_input = input_area.toPlainText()
    output_message = generate_system_message(user_input)
    output_area.setPlainText(output_message)
    status_bar.showMessage("System message generated successfully.")

def clear_fields():
    input_area.clear()
    output_area.clear()
    status_bar.clearMessage()

def init_pyqt():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("System Message Generator")
    window.resize(800, 600)

    layout = QVBoxLayout()

    global input_area, output_area, status_bar  # Make these global to access in `process_input`

    input_label = QLabel("Enter your request:")
    layout.addWidget(input_label)

    input_area = QTextEdit()
    input_area.setPlaceholderText("Enter your request here...")
    layout.addWidget(input_area)

    submit_button = QPushButton("Generate System Message")
    submit_button.clicked.connect(process_input)  # Connect button to function
    layout.addWidget(submit_button)

    clear_button = QPushButton("Clear Fields")
    clear_button.clicked.connect(clear_fields)
    layout.addWidget(clear_button)

    output_label = QLabel("System Message:")
    layout.addWidget(output_label)

    output_area = QTextEdit()
    output_area.setPlaceholderText("Generated system message will appear here...")
    layout.addWidget(output_area)

    status_bar = QStatusBar()
    layout.addWidget(status_bar)

    spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    layout.addItem(spacer)

    window.setLayout(layout)
    window.show()
    app.exec_()

if __name__ == "__main__":
    init_pyqt()
