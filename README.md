# Welcome to 3dPlot
A small lightweight CLI that functions to simply display bots

## Getting Started

### Clone Repo
Clone this repository with `git clone <url>

### Plot Figure
Run `cli.py` with the command `python cli.py` (python 3.5 or earlier) or `py cli.py` (python 3.6+)

Try out the following command:
`--plot3d plot:x+y=z`

### How to write your own command
* All commands start with `--plot3d plot:`
* No spaces in the expression that follows `--plot3d` for example: `--plot3d plot:3*x+y=z` is acceptable while `--plot3d plot:3 * x + y = z` is not
* Exponents must be written as `**` not `^`.

## Plotting
A certain file called `plot.py` should be generated when you run the `cli.py` file.

Run the file. 

A graph should be generated.

