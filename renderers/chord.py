import cairo
import math

class Chord:
    LINE_WIDTH = 'lineWidth'
    NUMBER_OF_FRETS = 'numberOfFrets'
    MARGIN = 'margin'
    FRET_HEIGHT = 'fretHeight'
    ARM_WIDTH = 'armWidth'
    NUT_WIDTH = 'nutRatio'
    DOT_RADIUS = 'dotRadius'

    defaultSettings = {
        LINE_WIDTH: 1,
        NUMBER_OF_FRETS: 4,
        MARGIN: 10,
        FRET_HEIGHT: 10,
        ARM_WIDTH: 40,
        NUT_WIDTH: 2,
        DOT_RADIUS: 3
    }

    def __init__(self, chord, context):
        self.chord = chord
        self.context = context
        self.settings = self.defaultSettings
        print(self.settings)

    def draw(self, x = 0, y = 0):
        self.context.set_source_rgb(0,0,0)
        #self.context.select_font_face('Sans', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        
        self.drawFrets(x,y)
        self.drawNotes(x,y)
        self.writeChordName(x,y)
        
        
    def line(self, x1, y1, x2, y2):
        """Draws a line from point a to point b

        """
        self.context.move_to(x1,y1)
        self.context.line_to(x2,y2)
        self.context.stroke()

    def rectangle(self, x, y, width, height):
        """Draws a rectangle

        """
        self.context.rectangle(x, y, width, height)
        self.context.set_line_join(cairo.LINE_JOIN_MITER)
        self.context.stroke()


    def circle(self, x, y, radius):
        """Draws a circle
        """
        self.context.arc(x, y, radius, 0, 2*math.pi)
        self.context.fill()


    def write(self, x, y, text):
        """Writes text at x,y
        """
        self.context.move_to(x,y)
        self.context.show_text(text)


    def getStringSpace(self):
        """Returns the space between strings
        """
        return self.settings[self.ARM_WIDTH] /  (len(self.chord) -1)


    def drawFrets(self, x, y):
        """Draws the frets of the ukelele

        """
        
        # draw nut
        self.context.set_line_width(self.settings[self.LINE_WIDTH] * self.settings[self.NUT_WIDTH])
        currentX = self.settings[self.MARGIN] + x
        currentY = self.settings[self.MARGIN] + y 
        self.line(currentX, currentY, currentX + self.settings[self.ARM_WIDTH], currentY  )

        # draw frets
        self.context.set_line_width(self.settings[self.LINE_WIDTH])
        for fret in range(self.settings[self.NUMBER_OF_FRETS]):
            currentX = self.settings[self.MARGIN] + x
            currentY = self.settings[self.MARGIN] + y + (fret + 1) * self.settings[self.FRET_HEIGHT]
            
            self.line(currentX, currentY, currentX + self.settings[self.ARM_WIDTH], currentY  )
        
        # draw strings
        stringSpace = self.getStringSpace()
        for st in range(len(self.chord)):
            currentX = self.settings[self.MARGIN] + x + (st * stringSpace)
            currentY = self.settings[self.MARGIN] + y
            h =  self.settings[self.FRET_HEIGHT] * self.settings[self.NUMBER_OF_FRETS]
            self.line(currentX, currentY, currentX, currentY + h )



    def drawNotes(self, x, y):
        """Draws the notes
        """

        stringSpace = self.getStringSpace()
        for index in range(len(self.chord)):
            note = self.chord[index]
            currentX = self.settings[self.MARGIN] + x + (index * stringSpace)

            if note == -1:
                continue

            if note == 0:
                currentY = y + self.settings[self.MARGIN]
            else:
                currentY = y + self.settings[self.MARGIN] + note * (self.settings[self.FRET_HEIGHT])

            currentY = currentY - (self.settings[self.FRET_HEIGHT] / 2.0) 
            #cr.move_to(currentX,currentY)
            #cr.show_text("X")
            #self.write(currentX,currentY, "X")
            self.circle(currentX, currentY, self.settings[self.DOT_RADIUS])
                

    def writeChordName(self, x, y):
        """Writes the name of the chord underneath the diagram
        """
        currentY = y + self.settings[self.MARGIN] + (self.settings[self.FRET_HEIGHT] * (self.settings[self.NUMBER_OF_FRETS] + 1))
        currentX = x + self.settings[self.MARGIN] 
        self.write(currentX, currentY, "label")

