const clearClassList = (locked = false) => {
    selected = document.querySelectorAll('.selected');
    marked = document.querySelectorAll('.marked');
    selected.forEach(element => {
        element.classList.remove('selected');
    });
    marked.forEach(element => {
        element.classList.remove('marked');
    })
    if (locked) {
        lock = document.querySelectorAll('.locked');
        lock.forEach(element => {
            element.classList.remove('locked');
        })
    }
}

const cellChanging = () => {

    const cells = document.querySelectorAll('.sudoku__cell');
    const number_tip = document.querySelector('.numbers-tool');
    const nr_btn = number_tip.children;

    cells.forEach(cell => {

        let cell_id = cell.id;
        let cell_y = cell_id[2];
        let cell_x = cell_id[5];
        if (cell_y == 2 || cell_y == 5) {
            cell.style.borderBottom = '5px solid #c7902e'
        }
        if (cell_x == 2 || cell_x == 5) {
            cell.style.borderRight = '5px solid #c7902e'
        }
        if (cell.innerText != '') {
            cell.classList.add('locked')
        }

        const markLines = (y, x) => {
            cells.forEach(element => {
                let el_y = element.id[2];
                let el_x = element.id[5];

                let rowBorder = Math.floor(y / 3);
                let colBorder = Math.floor(x / 3);

                for (let i = 3 * rowBorder; i < 3 * rowBorder + 3; i++) {
                    for (let j = 3 * colBorder; j < 3 * colBorder + 3; j++) {
                        if (el_y == i && el_x == j) {
                            element.classList.add('marked');
                        }
                    }
                }

                if (el_y == y || el_x == x) {
                    element.classList.add('marked');
                }
            });
        }

        cell.addEventListener('click', () => {
            clearClassList();
            if (!cell.contains(number_tip)) {
                cell.classList.add('selected');
                cell.append(number_tip);
                number_tip.style.display = 'flex';
                markLines(cell_y, cell_x);
            } else {
                cell.classList.remove('selected');
                cell.removeChild(number_tip);
            }
        });
    });

    Array.prototype.forEach.call(nr_btn, nr => {
        nr.addEventListener('click', function (e) {
            if (nr.innerText != 'Clear') {
                this.parentNode.parentNode.innerText = nr.innerText;
                this.parentNode.style.display = 'none';
            } else {
                this.parentNode.parentNode.innerText = '';
            }
        });
    });
};


const gameHandler = () => {
    let req = new XMLHttpRequest()
    const newGameBtn = document.querySelector('#sudoku_new_game');
    const checkCellBtn = document.querySelector('#sudoku_check_cell');
    const solveBtn = document.querySelector('#sudoku_solve');

    newGameBtn.addEventListener('click', () => {

        clearClassList(true);
        const game_difficulty = document.querySelector('#game_mode').value;
        const form = new FormData()
        form.append('difficulty', game_difficulty)

        req.open('POST', '/sudoku/new_game');
        req.send(form);
        req.onreadystatechange = () => {
            if (req.readyState == 4) {
                const board = JSON.parse(req.response);
                fillBoard(board.board);
            }
        }
    });

    checkCellBtn.addEventListener('click', () => {
        let cell = document.querySelector('.selected');
        const form = new FormData();
        form.append('cords', [cell.id[2], cell.id[5]]);
        form.append('value', cell.innerText[0]);

        req.open('POST', '/sudoku/check_cell');
        req.send(form);
        req.onreadystatechange = () => {
            if (req.readyState == 4) {
                const res = JSON.parse(req.response).valid;
                if (res) {
                    cell.style.backgroundColor = 'green';
                } else {
                    cell.style.backgroundColor = 'red';
                }
            }
        }
    });

    solveBtn.addEventListener('click', () => {
        req.open('POST', '/sudoku/solve');
        req.send();
        req.onreadystatechange = () => {
            if (req.readyState == 4) {
                let board = JSON.parse(req.response).board;
                fillBoard(board, false);
            }
        }
    });
}

const fillBoard = (boardValues, lock = true) => {
    const cells = document.querySelectorAll('.sudoku__cell');

    cells.forEach(cell => {
        let y = cell.id[2];
        let x = cell.id[5];
        cell.innerText = boardValues[y][x];
        if (cell.innerText != '') {
            if (lock) {
                cell.classList.add('locked')
            }
        }

    });
}


document.addEventListener('DOMContentLoaded', () => {
    cellChanging();
    gameHandler();
});