from flask import Blueprint, render_template, jsonify, request, session
from app.apps.sudoku.engine import Sudoku



sudoku = Blueprint('sudoku', __name__)

@sudoku.route('/')
def index():
    sudoku = Sudoku()
    if session.get('board', False):
        board = session['board']['generated_board']
    else:
        board = sudoku.playable_board('easy')

    return render_template('sudoku.html', board=board)



@sudoku.route('/new_game', methods=['POST'])
def generate_board():
    difficulty = request.form.get('difficulty')
    sudoku = Sudoku()
    board = sudoku.playable_board(difficulty)
    session['board'] = sudoku.__dict__
    return jsonify(board=board)

@sudoku.route('/solve', methods=['POST'])
def solve_board():
    if session['board']:
        res = session['board']['board']
        return jsonify(board=res)

@sudoku.route('/check_cell', methods=['POST'])
def check_cell():
    if session['board']:
        y,x = [int(z) for z in request.form['cords'].split(',')]
        value = int(request.form['value'])
        fillBoard = session['board']['board']
        res = True if fillBoard[y][x] == value else False
        return jsonify(valid=res)