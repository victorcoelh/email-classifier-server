from src.llm.prompts import CLASSIFICATION_PROMPT
from src.llm.client import openai_client
from src.models import EmailType
from src.preprocessor import PreProcessor


def email_classification_service(email: str) -> tuple[EmailType, float, str]:
    preprocessor = PreProcessor(email)
    email = preprocessor\
        .remove_punctuation()\
        .remove_digits()\
        .remove_stopwords()\
        .lemmatize()\
        .lowercase_all()\
        .get_processed_text()
   
    response = openai_client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": CLASSIFICATION_PROMPT},
            {"role": "user", "content": email}
        ]
    ).choices[0].message.content
    
    if not response:
        raise ValueError("No response from OpenAI")

    return parse_answer(response)

def parse_answer(llm_response: str) -> tuple[EmailType, float, str]:
    label, confidence, answer = llm_response.splitlines()[:3]
    
    label = label.removeprefix("Label: ").strip()
    confidence = confidence.removeprefix("Confidence: ").strip()
    answer = answer.removeprefix("Suggested Answer: ").strip()
    
    if label not in ["Productive", "Unproductive"]:
        raise ValueError(f"Invalid label: {label}")

    return label, float(confidence), answer # type: ignore
