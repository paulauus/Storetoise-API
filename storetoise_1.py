"""The Storetoise CLI."""

from argparse import ArgumentParser
import requests

BASE_URL = "http://storetoise-lb-1365832025.eu-west-2.elb.amazonaws.com"

def load_storetoise_data(url: str) -> dict:
  request = requests.get(url, timeout=10)
  request = request.json()
  return request

def print_storage_ids(data: dict, number:int) -> None:
  ...

def command_line_interface_input():
  parser = ArgumentParser()
  parser.add_argument("--username", "-u", required=True)
  args = parser.parse_args()
  return args
  ...

if __name__ == "__main__":

  pass
