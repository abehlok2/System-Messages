from SystemMessageGenerator import generate_system_message
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QLabel, QStatusBar
# Import the function from your script that takes the input prompt and returns the system message.
# from SystemMessageGenerator import your_function


def process_input():
    user_input = input_area.toPlainText()
    # Uncomment the line below once you import your function
    # output_message = your_function(user_input)
    output_message = generate_system_message(user_input)

    # output_message = f"Processed: {user_input}"  # Placeholder
    output_message = generate_system_message(user_input)
    output_area.setPlainText(output_message)
    status_bar.showMessage("System message generated successfully.")


def init_pyqt():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("System Message Generator - PyQt")
    window.resize(600, 400)

    layout = QVBoxLayout()

    global input_area, output_area, status_bar  # Make these global to access in `process_input`

    input_label = QLabel("Enter your request:")
    layout.addWidget(input_label)

    input_area = QTextEdit()
    layout.addWidget(input_area)

    submit_button = QPushButton("Generate System Message")
    submit_button.clicked.connect(process_input)  # Connect button to function
    layout.addWidget(submit_button)

    output_label = QLabel("System Message:")
    layout.addWidget(output_label)

    output_area = QTextEdit()
    layout.addWidget(output_area)

    status_bar = QStatusBar()
    layout.addWidget(status_bar)

    window.setLayout(layout)
    window.show()
    app.exec_()


if __name__ == "__main__":
    init_pyqt()
