# needs:  pip install --upgrade pip enum34
from enum import Enum
import cairo
from renderers.chord import Chord

C = 'C'
C_SHARP = 'C#'
D = 'D'
D_SHARP = 'D#'
E = 'E'
F = 'F'
F_SHARP = 'F#'
G = 'G'
G_SHARP = 'G#'
A = 'A'
A_SHARP = 'A#'
B = 'B'



class Tones(Enum):
    C = 1
    D = 2
    E = 3
    F = 4
    G = 5
    A = 6
    B = 7

class Intervals(Enum):
    Tone = 2
    Semitone = 1

class ChordTypes(Enum):
    Major = 1
    Minor = 2



class Note:
    def __init__(self, note, sustained):
        self.note = note
        self.sustained = sustained


allNotesDefinitions = {
    C: Note(Tones.C, False),
    C_SHARP: Note(Tones.C, True),
    D: Note(Tones.D, False),
    D_SHARP: Note(Tones.D, True),
    E: Note(Tones.E, False),
    F: Note(Tones.F, False),
    F_SHARP: Note(Tones.F, True),
    G: Note(Tones.G, False),
    G_SHARP: Note(Tones.G, True),
    A: Note(Tones.A, False),
    A_SHARP: Note(Tones.A, True),
    B: Note(Tones.A, False),
}

allNotesSequence = [C, C_SHARP, D, D_SHARP, E, F, F_SHARP, G, G_SHARP, A, A_SHARP, B]


allChordTonalRelations = {
    ChordTypes.Major: [4, 3],
    ChordTypes.Minor : [3, 4]
}

tunings = {
    "Standard uke": [allNotesDefinitions[G], allNotesDefinitions[C], allNotesDefinitions[E], allNotesDefinitions[A]]
}


scales = {
    'Ionian' : [Intervals.Tone, Intervals.Tone, Intervals.Semitone, Intervals.Tone, Intervals.Tone, Intervals.Tone, Intervals.Semitone]
}


def getNotePositionInScale(note):
    """Calculates the note's position in semitones from the start of the scale
    
    """

    position = 0
    global allNotesSequence, Intervals


    for noteName in allNotesSequence:
        currentNote = allNotesDefinitions[noteName]
        if note == currentNote:
            break

        position = position + 1

    return position


def getNoteAtPosition(position):
    """Returns the note by it's tonal position
    
    """
    if position>=len(allNotesSequence):
        position = position % len(allNotesSequence)

    return allNotesDefinitions[allNotesSequence[position]]




def getNoteDistance(root, note):
    """Returns the tonal distance between two notes.
    
    """
    result = 0
    rootPosition = getNotePositionInScale(root)
    notePosition = getNotePositionInScale(note)
    result = notePosition - rootPosition
    if result < 0:
        result = result + len(allNotesSequence)

    if result > len(allNotesSequence):
        result = result - len(allNotesSequence)

    return result


def getNoteWithTonalDistanceFromNote(note, distance):
    """Returns the note that that has the defined distance from a root note
    
    """
    position = getNotePositionInScale(note)

    return getNoteAtPosition(position + distance)


def getChordNotes(note, chordType):
    result = []
    result.append(note)
    for chordNoteDistance in allChordTonalRelations[chordType]:
        note = getNoteWithTonalDistanceFromNote(note, chordNoteDistance)
        result.append(note)

    return result


def getChordDiagramData(note, chordType, scale = scales['Ionian'], tuning = tunings['Standard uke'], frets = 4):
    """Returns the data needed to draw a chord diagram
    """

    result = []
    chord = getChordNotes(note, chordType)
    for baseNote in tuning:
        lastDistance = frets
        distanceToAdd = None
        for chordNote in chord:
            distance = getNoteDistance(baseNote, chordNote)
            if distance < frets and distance < lastDistance:
                distanceToAdd = distance

            lastDistance = distance
            
        result.append(distanceToAdd)


    return result



#cChord = getChord(notes['C'])
#print(cChord)

def main():
    ps = cairo.SVGSurface("chord.svg", 200, 200)
    cr = cairo.Context(ps)

    chord = getChordDiagramData(allNotesDefinitions['C'], ChordTypes.Major)
    renderer = Chord(chord, cr)
    renderer.draw()

    #cr.set_source_rgb(0,0,0)
    #cr.select_font_face('Sans', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    #cr.set_font_size(40)

    #cr.move_to(10,50)
    #cr.show_text("TEST TXT")
    cr.show_page()

if __name__ == "__main__":
    main()
