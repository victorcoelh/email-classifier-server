import os


def load_testing_data() -> tuple[list[str], list[int]]:
    data_path = "tests/mock_data/"

    file_names = [file for file in os.listdir(data_path)
                  if os.path.isfile(data_path + file)]

    mock_emails = [open(data_path + file, "r").read() for file in file_names]
    email_types = [file.split("_")[0].capitalize() for file in file_names]
    validate_labels(email_types)
    
    email_types_binary = [int(email_type == "Productive")
                          for email_type in email_types]

    return mock_emails, email_types_binary

def validate_labels(labels: list[str]) -> None:
    for label in labels:
        if label not in ["Productive", "Unproductive"]:
            raise ValueError(f"Invalid label: {label}")
