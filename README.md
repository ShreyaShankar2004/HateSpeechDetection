Automated Detection of Hate Speech/Offensive Language in Social Media Using a Transformer
Scope:- Introduction:
What is Hate Speech?
Hate speech or offensive language refers to content that attacks, threatens, or insults individuals or groups based on attributes like race, religion, ethnicity, gender, or sexual orientation. Commonly found on social media platforms like Twitter, Facebook, Reddit, etc.
What is Safe Speech?
Safe or neutral speech refers to social media content that does not contain offensive, abusive, or discriminatory language. It is informative, positive, or casual. For example, general conversation, news updates and greetings. Maintains a respectful tone and adheres to community guidelines.
Why Detect Hate Speech?
1)	Ensures safer online communities and reduces cyberbullying.
2)	Assists social media platforms in moderating content automatically.
3)	Supports research in NLP, AI ethics, and content moderation.
Motivation:
Why is this project important?
 
1)	Rise of Social Media Communication: Millions of users post daily on platforms like Twitter, Facebook, and Instagram, making moderation a challenge.
2)	Harmful Effects of Hate Speech: Hate/offensive posts can lead to psychological harm, cyberbullying, and social unrest.
3)	Automated Detection is Essential: Manual moderation is time-consuming and error-prone; NLP models help scale detection efficiently.
4)	Academic and Practical Relevance: Combines AI, NLP, and societal impact, suitable for real-world applications.
5)	High Accuracy is Possible: Using transformer-based models like RoBERTa, short text classification can achieve more than, providing reliable tools for content moderation.

Input and Output Interfaces:
Input: User-provided text or social media post (tweet/comment) entered via the Flask-based web dashboard.


Output: The system classifies the input as either “Hate/Offensive” or “Safe/Neutral” along with the
prediction probability.

 
Source of Text Corpus and Size:

•	Dataset: Hatexplain Dataset on HuggingFace
•	Size: 24,783 text samples divided into training, validation, and test sets.

Major Modules / Functionalities:

1.	Data Preprocessing Module: Cleans and tokenizes the dataset.
2.	Model Training Module: Fine-tunes the RoBERTa-base transformer model.
3.	Evaluation Module: Computes accuracy, confusion matrix, and visual metrics.
4.	Web Interface Module: Flask-based dashboard for real-time predictions.
5.	Deployment Module: Saves and loads fine-tuned model for user interaction.

Text Preprocessing Steps Applied:

•	Removal of URLs, special symbols, and emojis.
•	Lowercasing and trimming whitespace.
•	Tokenization using RoBERTa tokenizer with a maximum sequence length of 128.
•	Padding and truncation for uniform input shape.

Deep Learning Techniques Implemented:

•	Pre-trained RoBERTa-base Transformer model fine-tuned for binary text classification.
•	AdamW optimizer with learning rate 0.00002.
•	Cross-entropy loss function.
•	Training for 3 epochs with a batch size of 16.
•	Achieved 93.6% accuracy on validation data.

Working of Project:- Flow Diagram:
Flow:

•	Social Media Post / Tweet: The raw input text from platforms like Twitter or Facebook that will be analyzed.

•	Text Preprocessing (Tokenization, Cleaning, Padding): The text is cleaned, tokenized, and padded/truncated to a fixed length to prepare it for the model.
•	RoBERTa Model (Fine-tuned for Hate Speech Detection): A pre-trained transformer model fine- tuned on the Hatexplain dataset to classify the text.

•	Prediction (Hate/Offensive or Safe/Neutral): The model outputs probabilities and determines whether the text is offensive or neutral.

•	Output Display (Probability & Label on Dashboard): The result is displayed on the web dashboard, showing the predicted label and its probability.
 

 

Results and Discussions:
Test Accuracy: The model correctly predicted about 93.6% of all test samples overall showing strong general performance.

Performance Metrics


Confusion Matrix

Future Scope:
1)	Integrate multilingual support for hate speech detection in regional languages.
2)	Implement real-time monitoring of social media platforms.
3)	Deploy as a full web application with a database for storing flagged posts.
 
Conclusion:
-Implemented ROBERTa base Transformer model for offensive language detection.
-The model achieved high test accuracy (93.57).
-Models successfully differentiated between Offensive and Safe language.
-Natural Language Processing and Deep learning helped in understanding and classifying the texts.
