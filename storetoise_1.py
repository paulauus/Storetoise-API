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
  if 

  for id in sorted(storage_ids):
    print(id)

def valid_value(input_num: str) -> int:
  """Checks that the chosen number for messages display is a valid number."""
  if not input_num.isdigit():
    raise AssertionError("Number must be an integer between 0 and 1000.")
  if 0 <= int(input_num) <= 1000:
    return int(input_num)
  else:
    raise AssertionError("Number must be an integer between 0 and 1000.")

def command_line_interface_input():
  """
  Takes an input from the user with the username.
  """
  parser = ArgumentParser()
  parser.add_argument("--username", "-u", required=True)
  parser.add_argument("--number", "-n", type=valid_value)
  args = parser.parse_args()
  return args

if __name__ == "__main__":

  pass
