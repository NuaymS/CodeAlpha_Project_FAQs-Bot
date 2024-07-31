faq_data = {
    "What courses are offered at Kingston University?": "Kingston University offers a wide range of undergraduate and postgraduate courses. You can find the full list on the university's website.",
    "How do I apply to Kingston University?": "You can apply to Kingston University through the UCAS website for undergraduate courses and through the Kingston University website for postgraduate courses.",
    "What are the tuition fees?": "Tuition fees vary depending on the course and level of study. Please visit the Kingston University website for detailed information on fees.",
    "What if i feel lonely" : "You won't!",
}

import spacy

# Load SpaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Function to preprocess text
def preprocess(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

# Preprocess the FAQ questions
processed_faq = {preprocess(question): answer for question, answer in faq_data.items()}

def get_answer(user_question):
    processed_question = preprocess(user_question)
    best_match = None
    highest_similarity = 0
    
    for question in processed_faq:
        similarity = nlp(processed_question).similarity(nlp(question))
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = question
    
    if highest_similarity > 0.7:  # You can adjust the threshold
        return processed_faq[best_match]
    else:
        return "I'm sorry, I don't have an answer to that question. Please visit the Kingston University website or contact their support."

# Chatbot interaction
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    
    response = get_answer(user_input)
    print(f"Chatbot: {response}")

