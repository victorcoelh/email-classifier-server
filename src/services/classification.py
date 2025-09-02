from src.llm.prompts import CLASSIFICATION_PROMPT
from src.llm.client import send_message
from src.models import EmailType
from src.preprocessor import PreProcessor


async def email_classification_service(email: str) -> tuple[EmailType, float, str]:
    preprocessor = PreProcessor(email)
    email = preprocessor\
        .remove_punctuation()\
        .remove_digits()\
        .remove_stopwords()\
        .lemmatize()\
        .lowercase_all()\
        .get_processed_text()

    llm_answer = send_message(email, CLASSIFICATION_PROMPT)
    return parse_answer(await llm_answer)

def parse_answer(llm_response: str) -> tuple[EmailType, float, str]:
    label, confidence, answer = llm_response.splitlines()[:3]
    
    label = label.removeprefix("Label: ").strip()
    confidence = confidence.removeprefix("Confidence: ").strip()
    answer = answer.removeprefix("Suggested Answer: ").strip()
    
    if label not in ["Productive", "Unproductive"]:
        raise ValueError(f"Invalid label: {label}")

    return label, float(confidence), answer # type: ignore
