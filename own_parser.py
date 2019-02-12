def main(input_text):

    # split the text using the colon
    primary_tokens = input_text.split(':')
    print("primary tokens: " + str(primary_tokens))

    # check if the first string in primary token is a plot command
    if (primary_tokens[0] != 'plot'):
        raise KeyError("Must call the keyword 'plot' ")



    # check if the equal sign is in the tokens
    if ("=" not in primary_tokens[1]):
        raise KeyError("entry must be an equation.")

    # split into two again
    sec_tokens = primary_tokens[1].split("=")
    print("secondary tokens: " + str(sec_tokens))

    # check if there is a z
    if ('z' not in sec_tokens[1]):
        raise KeyError('entry must contain a z variable')

    print(sec_tokens)

    # generate the expression to put into the function - replace the
    expr = sec_tokens[0].replace('^', '**')
    expr = expr.replace('sin(', 'np.sin(')
    expr = expr.replace('cos(', 'np.cos(')
    expr = expr.replace('e^', 'np.e')

    print("expr: " + str(expr))

    # make sure that you catch the sin, cos, e and other functions

    # generate the string
    main_str = """from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#set up the figure
fig = plt.figure()
ax = plt.axes(projection='3d')

#second plot
def f(x, y):
    return """ + expr + """

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_title(""" + "'f(" + expr + ")')" + """
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()"""

    # Generate PY file
    filename = "plot.py"
    with open(filename, 'w') as file:
        file.write(main_str)

    print("wrote to file")
    pass

if __name__ == "__main__":
    input_text = "plot: x^2 + y^2 = z"
    main(input_text)

