import os
import pathlib

try:
	from dotenv import load_dotenv
except ModuleNotFoundError:
	load_dotenv = None

# load the .env file variables
def _load_env_file(path: str):
	if load_dotenv:
		load_dotenv(path)
		return
	try:
		with open(path, "r", encoding="utf-8") as handle:
			for line in handle:
				line = line.strip()
				if not line or line.startswith("#") or "=" not in line:
					continue
				key, value = line.split("=", 1)
				os.environ.setdefault(key.strip(), value.strip())
	except FileNotFoundError:
		return


# load the .env file variables
_PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent


def _load_env():
	_load_env_file(str(_PROJECT_ROOT / ".env"))
	if not os.environ.get("CLIENT_ID"):
		_load_env_file(str(_PROJECT_ROOT / ".env.example"))


def get_credentials():
	_load_env()
	return os.environ.get("CLIENT_ID"), os.environ.get("CLIENT_SECRET")


# SOUNDCLOUD API credentials
client_id, client_secret = get_credentials()