
import mimetypes
import urllib.parse
import json
import logging
import socket
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from datetime import datetime



parse_dict = {"key1": "value1", "key2": "value2"}
with open('storage/data.json', 'a', encoding='utf-8') as file:
            # existing_data = json.load(file)
            # existing_data.update(parse_dict)
            json.dump(parse_dict, file, ensure_ascii=False, indent=4)