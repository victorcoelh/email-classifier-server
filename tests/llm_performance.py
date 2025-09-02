import asyncio

from sklearn.metrics import accuracy_score, precision_score, recall_score

from src.services.classification import email_classification_service
from tests.load_testing_data import load_testing_data


def main() -> None:
    X, y = load_testing_data()
    print(f"Loaded data. Testing dataset size: {len(X)}")
    
    predictions = []
    for email in X:
        llm_label = asyncio.run(email_classification_service(email))[0]
        predictions.append(int(llm_label == "Productive"))  # Converts to Binary labels

    print_evaluation(y, predictions)
    print_errors(y, predictions, X)
        
def print_evaluation(y_true: list[int], y_pred: list[int]) -> None:
    print(f"Accuracy: {accuracy_score(y_true, y_pred)}")
    print(f"Precision: {precision_score(y_true, y_pred)}")
    print(f"Recall: {recall_score(y_true, y_pred)}")
    
def print_errors(y_true: list[int], y_pred: list[int], emails: list[str]) -> None:
    correct = [prediction == actual
               for prediction, actual in zip(y_pred, y_true)]

    errors = [emails[i] for i, is_correct in enumerate(correct)
              if not is_correct]
    
    print("\n\nThe LLM got the following files wrong:\n")
    
    for error in errors:
        print(error + "\n")


if __name__ == "__main__":
    main()
