"""The Storetoise CLI."""

from argparse import ArgumentParser
import requests

BASE_URL = "http://storetoise-lb-1365832025.eu-west-2.elb.amazonaws.com"


def load_storetoise_data(url: str) -> dict:
    """Loads the JSON data from the base URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")


def print_storage_ids(data: dict, number: int | None = None) -> None:
    """Prints the storage IDs listed for a user."""
    storage_ids = data["ids"]
    if number:
        limit = min(number, len(storage_ids))
        for id in sorted(storage_ids[:limit]):
            print(id)
    else:
        for id in sorted(storage_ids):
            print(id)


def valid_value(input_num: str) -> int:
    """Checks that the chosen number for messages display is a valid number."""
    if input_num.isdigit() and 0 <= int(input_num) <= 1000:
        return int(input_num)
    print("Number must be an integer between 0 and 1000.")


def valid_storage_id(input_storage_id: str) -> int:
    """Checks that the given storage ID is a valid number."""
    if input_storage_id.isdigit() and len(input_storage_id) == 3:
        return int(input_storage_id)
    print("Storage ID must be a three-digit integer.")
    sys.exit(1)


def valid_message(message: str) -> str:
    """Checks the provided message is in a valid format."""
    if len(message) > 140:
        print("Message must be 140 characters or fewer.")
        sys.exit(1)

    if not all(char.islower() or char.isspace() for char in message):
        print("Message must consist only of lowercase letters and spaces.")
        sys.exit(1)

    return message


def post_message(url: str, message: str) -> None:
    """Posts a message to the given URL."""
    try:
        response = requests.post(url, json={"message": message}, timeout=10)
        response.raise_for_status()  # Ensure we catch HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error posting message to {url}: {e}")
        sys.exit(1)


def command_line_interface_input():
    """
    Takes input from the user with the username.
    Can specify the number of messages to print.
    """
    parser = ArgumentParser()
    parser.add_argument("--username", "-u", required=True)
    parser.add_argument("--number", "-n", type=valid_value)
    parser.add_argument("--storage", "-s", type=valid_storage_id)
    parser.add_argument("--message", "-m", type=valid_message)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = command_line_interface_input()
    user_url = f"{BASE_URL}/storage/{args.username}"
    loaded_data = load_storetoise_data(user_url)
    print_storage_ids(loaded_data, args.number)

    if args.storage:
        storage_url = f"{user_url}/{args.storage}"
        storage_data = load_storetoise_data(storage_url)

        if args.message:
            messages = storage_data.get("messages", [])
            if len(messages) >= 10:
                print("Cannot add more than 10 messages to a storage ID.")
                sys.exit(1)  # Exit if the message limit is reached

            post_message(storage_url, args.message)
            print(f"Message added to Storage ID {args.storage} successfully.")
