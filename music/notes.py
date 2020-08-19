from enum import Enum


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

class NoteError(Exception):
    """Exception for an invalid note."""

class Note:
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

    mappings = {
        Tones.C: {
            False: C,
            True: C_SHARP
        },
        Tones.D: {
            False: D,
            True: D_SHARP
        },
        Tones.E: {
            False: E
        },
        Tones.F: {
            False: F,
            True: F_SHARP
        },
        Tones.G: {
            False: G,
            True: G_SHARP
        },
        Tones.A: {
            False: A,
            True: A_SHARP
        },
        Tones.B: {
            False: B
        }
    }

    def __init__(self, note, sustained):
        
        if sustained not in self.mappings[note]:
            raise NoteError()

        self.note = note
        self.sustained = sustained


    def name(self):
        """ Returns the name of the note
        """
        return self.mappings[self.note][self.sustained]