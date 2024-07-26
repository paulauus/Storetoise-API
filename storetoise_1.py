"""The Storetoise CLI."""

from argparse import ArgumentParser
import requests

BASE_URL = "http://storetoise-lb-1365832025.eu-west-2.elb.amazonaws.com"


def load_storetoise_data(url: str) -> dict:
  """Loads the json data from the base url."""
  request = requests.get(url, timeout=10)
  request = request.json()
  return request


def print_storage_ids(data: dict, number:int | None=None) -> None:
  """Prints the storage IDs listed for a user."""
  storage_ids = data["ids"]
  if number:
    limit = min(number, len(storage_ids))
    for id in sorted(storage_ids[:limit]):
      print(id)
  if not number:
    for id in sorted(storage_ids):
      print(id)


def valid_value(input_num: str ) -> int:
    """Checks that the chosen number for messages display is a valid number."""
    if input_num:
      if input_num.isdigit() and 0 <= int(input_num) <= 1000:
        return int(input_num)
      print("Number must be an integer between 0 and 1000.")


def command_line_interface_input():
  """
  Takes an input from the user with the username.
  Can specify the number of messages to print.
  """
  parser = ArgumentParser()
  parser.add_argument("--username", "-u", required=True)
  parser.add_argument("--number", "-n", type=valid_value)
  args = parser.parse_args()
  return args

if __name__ == "__main__":
  args = command_line_interface_input()
  user_url = f"{BASE_URL}/storage/{args.username}"
  loaded_data = load_storetoise_data(user_url)
  print_storage_ids(loaded_data, args.number)
