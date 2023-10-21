from SystemMessageGenerator import generate_system_message
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout
# Import the function from your script that takes the input prompt and returns the system message.
# from SystemMessageGenerator import your_function


def process_input():
    user_input = input_area.toPlainText()
    # Uncomment the line below once you import your function
    # output_message = your_function(user_input)
    output_message = generate_system_message(user_input)

    output_message = f"Processed: {user_input}"  # Placeholder
    output_area.setPlainText(output_message)


def init_pyqt():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("System Message Generator - PyQt")
    window.resize(600, 400)

    layout = QVBoxLayout()

    global input_area, output_area  # Make these global to access in `process_input`

    input_area = QTextEdit()
    layout.addWidget(input_area)

    submit_button = QPushButton("Submit")
    submit_button.clicked.connect(process_input)  # Connect button to function
    layout.addWidget(submit_button)

    output_area = QTextEdit()
    layout.addWidget(output_area)

    window.setLayout(layout)
    window.show()
    app.exec_()


if __name__ == "__main__":
    init_pyqt()
