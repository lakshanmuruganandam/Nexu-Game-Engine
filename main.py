import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import math

app = FastAPI(title="God Mode Tic-Tac-Toe")

class BoardState(BaseModel):
    board: list[str]  # 9 elements: 'X', 'O', or ''
    difficulty: str   # 'easy', 'medium', 'impossible'

# Winning combinations
WIN_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # cols
    [0, 4, 8], [2, 4, 6]             # diagonals
]

def check_winner(board, player):
    for line in WIN_LINES:
        if board[line[0]] == player and board[line[1]] == player and board[line[2]] == player:
            return True
    return False

def is_draw(board):
    return '' not in board

def evaluate(board):
    if check_winner(board, 'O'): return 10
    if check_winner(board, 'X'): return -10
    return 0

# Transposition Table
transposition_table = {}

def minimax(board, depth, is_maximizing, memo):
    board_tuple = tuple(board)
    if board_tuple in memo:
        return memo[board_tuple]

    score = evaluate(board)
    
    if score == 10: return score - depth
    if score == -10: return score + depth
    if is_draw(board): return 0
    
    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                best = max(best, minimax(board, depth + 1, False, memo))
                board[i] = ''
        memo[board_tuple] = best
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                best = min(best, minimax(board, depth + 1, True, memo))
                board[i] = ''
        memo[board_tuple] = best
        return best

def get_best_move(board, difficulty):
    import random
    
    # Empty board optimization
    empty_spots = [i for i, x in enumerate(board) if x == '']
    if len(empty_spots) == 9:
        return random.choice([0, 2, 4, 6, 8]) # Take corners or center first
        
    if difficulty == 'easy' and random.random() < 0.5:
        return random.choice(empty_spots)
    if difficulty == 'medium' and random.random() < 0.2:
        return random.choice(empty_spots)
        
    best_val = -math.inf
    best_move = -1
    memo = {} # Per-request transposition table to avoid depth collision
    
    for i in range(9):
        if board[i] == '':
            board[i] = 'O'
            move_val = minimax(board, 0, False, memo)
            board[i] = ''
            
            if move_val > best_val:
                best_move = i
                best_val = move_val
                
    return best_move

@app.post("/api/move")
async def play_move(state: BoardState):
    move = get_best_move(state.board, state.difficulty)
    return {"move": move}

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("index.html", "r") as f:
        return f.read()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
