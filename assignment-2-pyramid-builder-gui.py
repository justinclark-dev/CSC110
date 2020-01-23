from tkinter import *
import math

# https://stackoverflow.com/questions/54637795/how-to-make-a-tkinter-canvas-rectangle-transparent 

# https://www.youtube.com/watch?v=r5EQCSW_rLQ  pyramid math formulas TIME=3:55

class GridLines:
    
    def __init__(self, canvas, canvas_width, canvas_height, grid_space):
        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.grid_space = grid_space

    def __vertical_lines__(self):
        for i in range(0, self.canvas_height, self.grid_space):
            self.canvas.create_line(i, 0, i, self.canvas_height, fill='hotpink')

    def __horizontal_lines__(self):
        for i in range(0, self.canvas_width, self.grid_space):
            self.canvas.create_line(0, i, self.canvas_width, i, fill='cyan')

    def create_grid(self):
        self.__vertical_lines__()
        self.__horizontal_lines__()

root = Tk()

root.title('Pyramid Dimensions')
root.geometry("500x600+1100+200")

widthLabel = Label(root, text="Enter Width:")
widthLabel.grid(row=0, column=0)

widthText = Entry(root)
widthText.grid(row=0, column=1)

heightLabel = Label(root, text="Enter Height:")
heightLabel.grid(row=1, column=0)

heightText = Entry(root)
heightText.grid(row=1, column=1)

def clickFunction():

    # width = widthText.get()
    # height = heightText.get()
    width = 80
    height = 64

    responseText = 'Width entered: {}'.format(width) + '\n' + \
        'Height entered: {}'.format(height)

    responseLabel = Label(root, text=responseText)
    responseLabel.grid(row=3, column=0)

    createPyramid(width, height)


submitButton = Button(root, text="Submit", command=clickFunction)
submitButton.grid(row=2, column=0)

closeButton = Button(master=root, text='Close', command=root.destroy)
closeButton.grid(row=2, column=1)

print('GUI created and displayed')

def createPyramid(width, height):
    canvas_width = 400
    canvas_height = 400

    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.grid(row=5)
    canvas.configure(background='white')

    grid = GridLines(canvas, canvas_width, canvas_height, 20)
    GridLines.create_grid(grid)

    points = [[100,300],[300,300], [200, 100]]
    canvas.create_polygon(points, outline='black', fill='snow3', width=1)


    canvas.create_line(200, 200, 100, 300, fill='purple')
    canvas.create_line(200, 200, 200, 300, fill='blue')
    canvas.create_line(200, 300, 200, 100, fill='orange')

    canvas.create_line(300, 200, 200, 100, fill='green')
    canvas.create_line(300, 200, 200, 200, fill='green')
    
    canvas.create_line(150, 200, 200, 100, fill='red')

    canvas.create_line(300, 200, 300, 300, fill='magenta')


    # oval − Creates a circle or an ellipse at the given coordinates. 
    # It takes two pairs of coordinates; 
    # the top left and bottom right corners 
    # of the bounding rectangle for the oval.
    # canvas.create_oval([200-(25/2),100-25], [225-(25/2), 125-25], fill='yellow', outline='yellow')


    hypotenuse = math.sqrt(height**2+((width/2)**2))

    print(str(hypotenuse))

    """
        a=5^2   b=3^2
        Getting slant
        a^2 + b^2 = c^2
        5^2 + 3^2 = c^2
        25  + 9   = 34^
                c = sqrt(34)

        Getting surface area of each side
        A = 1/2 b(x) * h(x)
    """

# ===========================
clickFunction() # REMOVE
# ===============================

root.mainloop()
# https://www.youtube.com/watch?v=YXPyB4XeYLA  minute 25?
