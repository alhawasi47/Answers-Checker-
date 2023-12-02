import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def train_cosine_similarity_model(reference_text, user_text):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([reference_text, user_text])
    model = cosine_similarity(tfidf[0], tfidf[1])
    return model

def train_models(question_folder, corrected_folder):
    # Assuming the question and corrected answer images have similar names
    question_files = [f"{question_folder}/question_{i:03d}.jpg" for i in range(1, 14)]
    corrected_files = [f"{corrected_folder}/answer_{i:03d}.jpg" for i in range(1, 14)]

    # Training loop
    for q_file, c_file in zip(question_files, corrected_files):
        # Read the content of the files
        with open(c_file) as file:
            corrected_text = file.read()

        # Extract text from question image (you can replace this with your image processing logic)
        question_text = f"Question {q_file.split('_')[-1].split('.')[0]}"

        # Train the model
        trained_model = train_cosine_similarity_model(corrected_text, question_text)

        # Save the trained model to a file
        model_filename = f"cosine_similarity_model_{q_file.split('_')[-1].split('.')[0]}.joblib"
        joblib.dump(trained_model, model_filename)

    print("Training complete.")
