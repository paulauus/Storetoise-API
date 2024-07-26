"""The Storetoise CLI."""

from argparse import ArgumentParser
import requests

BASE_URL = "http://storetoise-lb-1365832025.eu-west-2.elb.amazonaws.com"

def load_storetoise_data(url: str) -> dict:
  ...

def command_line_input():
  parser = ArgumentParser()
  parser.add_argument("--username", "-u", required=True)
  args = parser.parse_args()
  return args
  ...

if __name__ == "__main__":

  pass
