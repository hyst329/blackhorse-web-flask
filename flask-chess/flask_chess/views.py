"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify
from flask_chess import app, engine
import subprocess
import os
import chess
import chess.uci
from .settings import APP_STATIC

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/play')
def play():
    """Play chess inside the app."""
    global engine
    engine_path = os.path.join(APP_STATIC, "engine/Blackhorse.exe")
    engine = chess.uci.popen_engine(engine_path)
    engine.uci()
    return render_template(
        'chess.html',
        title="Play with " + engine.name,
        message=engine.author 
        )

@app.route('/move')
def move():
    """AJAX call to the engine"""
    global engine
    fen = request.args.get("fen", "", type=str)
    engine.position(chess.Board(fen))
    move = engine.go(movetime=10000)[0] # 10 seconds per move
    return jsonify(move=move.uci())