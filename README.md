# Tic Tac Toe Wars!
#### Video Demo:  <https://youtu.be/9kLFGqUk3CM>
#### Description: An enhanced version of tic tac toe played in a 6x6 grid inside the console
## How to Play:
### Rules
* Offense makes the first move
* The first move may be placed anywhere on the board
* Offense may take 2 turns at the start, Defense only takes 1
* Defense may put marks anywhere, Offense must place it in adjacent squares next to other offensive marked squares
* If the Offense is blocked from a square, Defense automatically wins the square
* Players may score diagonally, horizontally, vertically, four-corners, and illuminati
* Both Offense and Defense can score points

### Scoring
* 4 in a row = 1 Point
* 5 in a row = 2 Points
* 6 in a row = 5 Points
* Illuminati(Complete Triangle Around Opponent’s Square) = 3 Points
* 4 Corners = 1 Point

### Usage
* Run the project.py file in the terminal
* Names must be 1 letter, uppercase and lowercase are both fine, just don't use the same letter
* To place moves, type in the console in "letternumber" format EX: "a6" or "B2"
* Uses a chess grid system, where rows start at A and go up alphabetically and columns start at 1 and go up numerically
* Will show the state of the board and each person's score after each person's move
* Will automatically stop running and report the score when the game finishes

## project.py

<p>The main file to be run</p>

### Player
<p>Created to store the score and the mark of each player</p>

### main()

<p>Will deal with the flow of the game and automate all of the checking, prompting, and drawing of the board along with ending the game when needed. Has a game loop of max length 17 as there are only 36 moves in total in the longest theoretical game, and each loop has each player play once. The other 2 moves are the extra move for offense at the beginning, which means they also get an extra move at the end</p>

### create_board()

<p>Will generate an empty board of width and height LENGTH, which has been defined to be 6. Does this by making a list with LENGTH number of elements, where each list has LENGTH number of elements. Each element has been defaulted as ' '</p>

### get_name()

<p>Deals with forcing the user to input a valid name, which is a single alphabet character in this case<p>

### print_board()

<p>Will print out the state of the board using ASCII Art by taking each element of the board and putting it inside of a little box. After printing the board it will print out the scores of each player once check_score() is run</p>

### check_possible()

<p>Will run before the play_move() function is called for offense because if the offense runs out of legal moves, then the game should end. Does the check by checking every offensive square and seeing if there is an empty space next to it, in which it ends the check and returns True. Otherwise it will return False to initiate the ending of the game</p>

### check_legal()

<p>Called during the check for offense's moves if they are legal. This is because they can only place adjacent to another square they control, so this function checks if that square has an offensive mark next to it</p>

### play_move()

<p>Will prompt for a move, which using Regex only allows moves in the format letternumber, in which it will keep reprompting until a legal move is given. If the player moving is offense, then it will also call the check_legal() function to make sure the move is legal. Otherwise, it checks if the move is on an empty square</p>

### check_score()

<p>Combines the horizontal_check(), vertical_check(), diagonal_check_1(), diagonal_check_2(), four_corners_check(), and illuminati_check() function all into one to check for every type of way to score. Is called every time a move is made, so it automatically resets the player's score to 0 and adds up the new score again. Chose to split up each check to make it easier to organize</p>

### horizontal_check()

<p>To minimize the amount of squares checked, it checks the middle 2 squares of each row first because it's impossible to score without those squares. If both are the player's square, then it will set a variable length to 2. Then, for each square on each end of the line that is found consecutively, it adds 1 to length. When it's done checking the line, it checks the value of length and depending on the length, adds score to the player's score. Does this for each line</p>

### vertical_check()

<p>Same idea as the horizontal check, just implemented vertically</p>

### diagonal_check_1()

<p>Decided to split up the top-left to bottom-right and the top-right to bottom-left checks to minimize the amount of extra square checking. This has the same concept as the horizontal and vertical checks, except it first makes sure that the square it's checking exists to avoid an IndexError, as each diagonal is not the same length. This one is for top-left to bottom-right diagonals</p>

### diagonal_check_2()

<p>Same thing as above, just for the top-right to bottom-left diagonals instead</p>

### four_corners_check()

<p>Just checks the four corners and if all four are equal to the player's mark, then it will award a point to the player's score</p>

### illuminati_check()

<p>For this, I divided the board into 4 sections: top-left, top-right, bottom-left, bottom-right. This is because for each section, if the vertex of a right triangle was in any of these sections, then the triangle can only face one possible way, which is the opposite direction of the section of the grid the vertex is in. Thus, I checked every square, checking which section each square was in, and based on that, ran the triangle check for that section. This avoids checking for theoretically impossible triangles and reduces the amount of checks required. If a triangle is found around the opposing player's mark, then it will award 3 points</p>

### end_game()

<p>Runs the check_score() function for each player and then print_board() to get the final state of the game. Once it has done this it will call sys.exit() to end the program</p>

## test_project.py

<p>Runs tests to ensure that the Player class is working, then the create_board(), get_name(), check_possible(), check_legal(), test_play_move(), test_check_score() functions as well</p>
* The print_board() function is not tested because it has no return value and simply prints to the console, in which it's much easier and efficient to just look at the console instead of trying to copy and paste the ASCII Art into code
* It also does not do each individual score check because I gave the test_check_score() a case where each scoring method is used, with all of them except the four corners being used at least twice
* end_game() is not tested because it just calls the other functions and ends the program, which is easy to just see
