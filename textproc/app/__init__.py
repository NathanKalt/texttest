from flask import Flask
from textproc.config import Config

app = Flask(__name__)
app.config.from_object(Config)

