# Minesweeper (in the terminal)

## Background

For some reason or other I found myself playing minesweeper to decompress the other day. As I played I began to think about and experiment with the logic of the game and before long, I had half a page of mental notes on how I would go about implementing "minesweeper". I could've done a browser game, and it most likely would have been simpler to do so, but I felt like a change of pace since I'd been working extensively on a near completely javascript based project. This simple terminal game, coded in Python(3), is my best attempt at recreating minesweeper from scratch, without looking at any of its original source code, or anyone else's implementation

## Setup

Obviously, the first thing you should do is clone the project onto your machine with :

```
git clone https://github.com/joshuasantore/minesweeper.git
```

The next thing I would personally do is create a new virtual environment for the project, as it does use termcolor a lot for gameplay and pytest for testing. : `python3 -m venv venv`

( p.s. It's recommended not to do this, but I keep my virtual environments in the root of the project for convenience sake )
And then activate it with : `source venv/bin/activate`

Once you've activated your venv, use :
`pip install -r requirements.txt` to install the projects dependencies.

## Bombs Away!

After you finish the setup you can run the tests with `pytest` to ensure everything is fully operational orrr you can skip all the systems checks and jump right into the fun by running :

```
python3 -m minesweeper
```

Enjoy the game and feel free to let me know if you come across any bugs.

## Disclaimer

Obviously, this isn't an original idea, nor do I think my implementation of it to be anythin to get excited about. It was just something I thought I'd enjoy making, that wouldn't take me too long to finish, and that's exactly what it was.

I would credit those who originally created the game, but I really don't know who it is, and I'm not particularly motivated to find out. So this will be my credit. Good job dudes and/or dudettes, I had a lot of fun playing and remaking your game.

## Still Reading?

What's wrong with you lol. I'd give you a cookie but it'd take too long to pull up the ascii art for one so you'll just have to settle for a verbal one. <3
