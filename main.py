import tkinter as tk
from tkinter import filedialog, ttk
import pytesseract
from PIL import Image
from evaluate_algorithm import cosine_similarity_score

class SubjectiveEvaluatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Subjective Evaluator")
        self.master.geometry("600x400")

        self.create_widgets()

        # Load the trained model
        self.cosine_similarity_models = self.load_cosine_similarity_models()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")  # You can change the theme if desired

        self.question_label = ttk.Label(self.master, text="Question Image:")
        self.question_label.pack(pady=10)

        self.corrected_answer_label = ttk.Label(self.master, text="Corrected Answer Image:")
        self.corrected_answer_label.pack(pady=10)

        self.student_answer_label = ttk.Label(self.master, text="Student Answer Image:")
        self.student_answer_label.pack(pady=10)

        browse_question_button = ttk.Button(self.master, text="Browse Question Image", command=self.browse_question_image)
        browse_question_button.pack(pady=10)

        browse_corrected_button = ttk.Button(self.master, text="Browse Corrected Answer Image", command=self.browse_corrected_image)
        browse_corrected_button.pack(pady=10)

        browse_student_button = ttk.Button(self.master, text="Browse Student Answer Image", command=self.browse_student_image)
        browse_student_button.pack(pady=10)

        mode_label = ttk.Label(self.master, text="Select Mode:")
        mode_label.pack(pady=10)

        self.mode_var = tk.StringVar()
        mode_combobox = ttk.Combobox(self.master, textvariable=self.mode_var, values=["Mode 1: Subjective Answers Theory"])
        mode_combobox.pack(pady=10)

        evaluate_button = ttk.Button(self.master, text="Evaluate", command=self.evaluate_subjective)
        evaluate_button.pack(pady=10)

    def browse_question_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            self.question_label.config(text=f"Question Image: {file_path}")
            self.question_image_path = file_path

    def browse_corrected_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            self.corrected_answer_label.config(text=f"Corrected Answer Image: {file_path}")
            self.corrected_image_path = file_path

    def browse_student_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            self.student_answer_label.config(text=f"Student Answer Image: {file_path}")
            self.student_image_path = file_path

    def evaluate_subjective(self):
        # Implement logic to extract question, corrected answer, and student answer
        question_text = self.extract_text_from_image(self.question_image_path)
        corrected_text = self.extract_text_from_image(self.corrected_image_path)
        student_text = self.extract_text_from_image(self.student_image_path)

        # Implement your evaluation algorithm
        similarity_score = cosine_similarity_score(corrected_text, student_text)

        # Display the results
        result_text = (
            f"Question: {question_text}\n"
            f"Corrected Answer: {corrected_text}\n"
            f"Student's Answer: {student_text}\n"
            f"Similarity Score: {similarity_score:.2f}%"
        )

        print(result_text)

    def extract_text_from_image(self, image_path):
        # Use Tesseract OCR for text extraction from the image
        # Replace 'eng' with the language code for your language (e.g., 'fra' for French)
        extracted_text = pytesseract.image_to_string(Image.open(image_path), lang='eng')
        return extracted_text

    def load_cosine_similarity_models(self):
        # Placeholder for loading cosine similarity models (replace with actual code)
        # This function should return a tuple of spaCy Doc objects or similar representations
        # representing the trained models for expected and user answers
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = SubjectiveEvaluatorApp(root)
    root.mainloop()
