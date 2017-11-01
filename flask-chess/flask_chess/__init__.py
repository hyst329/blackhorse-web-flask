"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
engine = None
import flask_chess.views