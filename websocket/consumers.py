import json
from channels.generic.websocket import WebsocketConsumer
import joblib
import nltk
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import os

# Ensure necessary NLTK resources are available
nltk.download('punkt')

try:
    nltk.data.find('corpora/wordnet')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('wordnet')
    nltk.download('stopwords')

# Load your machine learning model and vectorizer
model_path = 'D:/Sky/blog_assignment/assignment/sentiment_model.pkl'
vectorizer_path = 'D:/Sky/blog_assignment/assignment/vectorizer.pkl'

model, vectorizer = None, None
if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    try:
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        print("Model and vectorizer loaded successfully.")
    except Exception as e:
        print(f"Error loading model or vectorizer: {e}")
else:
    print("Model or vectorizer file does not exist at the specified path.")

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Get response from ML model
        response = self.get_response_from_ml_model(message)

        self.send(text_data=json.dumps({
            'message': response
        }))

    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'\W', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        lemmatizer = WordNetLemmatizer()
        words = text.split()
        filtered_words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')]
        return ' '.join(filtered_words)

    def get_response_from_ml_model(self, message):
        if model and vectorizer:
            # Rule-based response system
            if "hi" in message.lower():
                response = "Hello! How can I assist you today?"
            elif "bye" in message.lower():
                response = "Goodbye! Have a great day!"
            elif "help" in message.lower():
                response = "Sure, I'm here to help. Please tell me what you need assistance with."
            else:
                # Default response if no rule matches
                processed_text = self.preprocess_text(message)
                vectorized_text = vectorizer.transform([processed_text])
                prediction_proba = model.predict_proba(vectorized_text)
                prediction = prediction_proba.argmax(axis=1)
                confidence = prediction_proba.max(axis=1)[0]
                sentiment = "Positive" if prediction[0] == 1 else "Negative"
                response = f"The sentiment of your message is: {sentiment} with {confidence:.2f}% confidence"
            
            return response
        else:
            return "Error: Model not loaded"



# import json
# from channels.generic.websocket import WebsocketConsumer
# import tensorflow as tf
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import pickle

# # Load the trained model and tokenizer
# model = tf.keras.models.load_model('path/to/chatbot_model.h5')

# with open('path/to/tokenizer.pickle', 'rb') as handle:
#     tokenizer = pickle.load(handle)

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Get response from the custom trained model
#         response = self.get_response_from_model(message)

#         self.send(text_data=json.dumps({
#             'message': response
#         }))

#     def get_response_from_model(self, message):
#         # Preprocess the input message
#         sequence = tokenizer.texts_to_sequences([message])
#         sequence = pad_sequences(sequence, maxlen=model.input_shape[1], padding='post')
        
#         # Predict the response
#         prediction = model.predict(sequence)
#         predicted_sequence = prediction.argmax(axis=1)
        
#         # Convert the predicted sequence back to text
#         response = ' '.join(tokenizer.index_word[idx] for idx in predicted_sequence if idx > 0)
#         return response
