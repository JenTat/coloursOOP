
class Colour:

    def __init__(self, r, g, b):

##        self._red = r
##        self._green = g
##        self._blue = b
        
        self._red = max(min(r, 255), 0)
        self._green = max(min(g, 255), 0)
        self._blue = max(min(b, 255), 0)


    def red(self):
        
        return self._red
    

    def green(self):
        
        return self._green
    

    def blue(self):
        
        return self._blue
    
    
    def __str__(self):

        return f'({self._red}, {self._green}, {self._blue})'


    def __repr__(self):

        return f'Colour(r={self._red}, g={self._green}, b={self._blue})'
    

    def __add__(self, other):
        
        new_r = min(self._red + other.red(), 255)
        new_g = min(self._green + other.green(), 255)
        new_b = min(self._blue + other.blue(), 255)

        new_colour = Colour(new_r, new_g, new_b)
        return new_colour
        
    def __sub__(self, other):

        new_r = max(self._red - other.red(), 0)
        new_g = max(self._green - other.green(), 0)
        new_b = max(self._blue - other.blue(), 0)

        new_colour = Colour(new_r, new_g, new_b)
        return new_colour



    def __eq__(self, other):
        
        return self._red == other.red() and self._green == other.green() and self._blue == other.blue()

##        is_equal = False
##
##        if self._red == other.red() and self._blue == other.blue() and self._green == other.green():
##            is_equal = True
##
##        return is_equal
##        red_equal = False
##        blue_equal = False
##        green_equal = False
##        is_equal = False
##
##        if self._red == other.red():
##            red_equal = True
##
##        if self._blue == other.blue():
##            blue_equal = True
##
##        if self._green == other.green():
##            green_equal = True
##
##        if red_equal == True and blue_equal == True and green_equal == True:
##            is_equal = True
##
##        return is_equal

    def hex(self):
        
        return f'#{self._red:02X}{self._green:02X}{self._blue:02X}'

    
    def luminosity(self):

        maxrgb = max(self._red, self._green, self._blue)
        minrgb = min(self._red, self._green, self._blue)

        luminosity = 0.5 * ((maxrgb/255) + (minrgb/255))

        luminosity = max(min(luminosity, 1.0), 0.0)
        return luminosity
        
         

    def saturation(self):

        maxrgb = max(self._red, self._green, self._blue)
        minrgb = min(self._red, self._green, self._blue)

        if maxrgb == minrgb:
            
            saturation = 0.0

        elif self.luminosity() <= 0.5:

            saturation = ((maxrgb/255) - (minrgb/255)) / ((maxrgb/255) + (minrgb/255))

        elif self.luminosity() > 0.5:
            
            saturation = ((maxrgb/255) - (minrgb/255)) / (2 - (maxrgb/255) - (minrgb/255))
            
        saturation = max(min(saturation, 1.0), 0.0)
        return saturation


    def __lt__(self, other):
        
        return self.saturation() < other.saturation()


    def __gt__(self, other):
        
        return self.saturation() > other.saturation()


    def __le__(self, other):
        
        return self.saturation() <= other.saturation()


    def __ge__(self, other):
        
        return self.saturation() >= other.saturation()
    

c = Colour (0, 0, 1)
d = Colour(125, 34, 77)
print(repr(d))
##print(d.hex(), d.luminosity(), c.saturation())

colour1 = Colour(125,34,77)
colour2 = Colour(10,10,10)
colour3 = Colour(205,1,506)
colour4 = Colour(355,256,-2)
colour5 = Colour(502,278,0)

print('testing restrictions: ' + str(colour3.blue()) + ' ' + str(colour4.blue()))

print('colour 1 hex, should be #7D224D: ' + colour1.hex())
print('colour 1 luminosity, should be 0.33176470588235294: ' + str(colour1.luminosity()))
print('colour 1 saturation, should be 0.5723270440251571: ' + str(colour1.saturation()))

print('testing add func, should be (255,35,255): ' + str(colour1 + colour3))
print('testing sub func, should be (245,245,0): ' + str(colour4 - colour2))

print('testing hex func, should be #0A0A0A: ' + colour2.hex())

print('colour 2 luminosity, should be 0.039: ' + str(colour2.luminosity()))
print('colour 2 saturation, should be 0: ' + str(colour2.saturation()))

print('testing boolean stuff')
print('lt should be false: ' + str(colour1 < colour2))
print('gt should be false: ' + str(colour3 > colour4))
print('le should be true: ' + str(colour5 <= colour4))
print('ge should be true: ' + str(colour3 >= colour5))
