# AutoTyper

AutoTyper is a simple autotyping program made using Python. It simulates keyboard typing, which can be useful in various scenarios. The program is currently under development and works for Linux with X-server(Doesnt work on wayland). It hasn't been tested on Mac yet. 

## Features
 - Simple code so it is easily customizable
 - Uses command line arguments to pass input
 - Press `ESC` key to stop typing
 - Can use multiple typing speed:
    0: No delay
    1: fast type
    2: slow type

## Installation

Follow these steps to install and run the program:

1. Clone the repository: `git clone https://github.com/FluffyRudy/autotyper`
2. Go to the autotyper directory: `cd autotyper`
3. Run `pip install -r requirements.txt` 
   If this fails then:
   1. First create a virtual environment using `python3 -m venv env`
   2. Activate the environment using: `source ./env/bin/activate`
   3. Then rerun `pip install -r requirements.txt`
4. Run the program: `python3 main.py <existing filePath> <output name without extension> <speed: 0 or 1 or 2>`
5. Press enter once more after the program runs to start autotyping
