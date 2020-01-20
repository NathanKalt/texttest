from flask import Flask
from textproc.app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

