class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return(self.width * self.height)

    def get_perimeter(self):
        return((2 * (self.width) + 2*(self.height)))

    def get_diagonal(self):
        return(((self.width**2) + (self.height**2))**.5)

    def get_picture(self):
        if self.width >50 or self.height> 50:
            return "Too big for picture."
        a = ("*" * self.width + "\n")*self.height
        return a
       
        
           
       
        
    def get_amount_inside(self, shape):
        A1 = self.width * self.height
        A2 = shape.width * shape.height
        return(A1//A2)

class Square(Rectangle):
    def __init__(self,side):
        self.width = side
        self.height= side
    def set_side(self, side):
      self.width= side
      self.height= side

    def set_width(self,side):
        self.width= side
        self.height= side

    def set_height(self,side):
        set.width= side
        set.height= side

    def __repr__(self):
        return f"Square(side={self.width})"