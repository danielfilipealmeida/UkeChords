# deprecated tests. 
# the code is being refactored and these tests should go on separetad files

import unittest
from main import getNotePositionInScale, allNotesDefinitions, getNoteAtPosition, getNoteDistance, getNoteDistance, getChordNotes, ChordTypes, getNoteWithTonalDistanceFromNote, getChordDiagramData

class TestAll(unittest.TestCase):

    def test_getNotePositionInScale(self):
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['C']), 0)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['C#']), 1)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['D']), 2)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['D#']), 3)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['E']), 4)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['F']), 5)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['F#']), 6)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['G']), 7)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['G#']), 8)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['A']), 9)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['A#']), 10)
        self.assertEqual(getNotePositionInScale(allNotesDefinitions['B']), 11)
       

    def test_getNoteAtPosition(self):
        self.assertEqual(getNoteAtPosition(0), allNotesDefinitions['C'])
        self.assertEqual(getNoteAtPosition(11), allNotesDefinitions['B'])
        self.assertEqual(getNoteAtPosition(12), allNotesDefinitions['C'])

    #def test_getChords(self):
    #    result = getChord(getNotePosition(allNotesDefinitions['C']))
    #    self.assertEqual(result, [0,0,0,1])


    def test_getNoteDistance(self):
        self.assertEqual(getNoteDistance(allNotesDefinitions['C'], allNotesDefinitions['C']), 0)
        self.assertEqual(getNoteDistance(allNotesDefinitions['C'], allNotesDefinitions['D']), 2)
        self.assertEqual(getNoteDistance(allNotesDefinitions['D'], allNotesDefinitions['C']), 10)


    def test_getChordNotes(self):
        chord = getChordNotes(allNotesDefinitions['C'], ChordTypes.Major)
        self.assertEqual(chord, [allNotesDefinitions['C'], allNotesDefinitions['E'], allNotesDefinitions['G']])

        chord = getChordNotes(allNotesDefinitions['C'], ChordTypes.Minor)
        self.assertEqual(chord, [allNotesDefinitions['C'], allNotesDefinitions['D#'], allNotesDefinitions['G']])



    def test_getNoteWithTonalDistanceFromNote(self):
        self.assertEqual(getNoteWithTonalDistanceFromNote(allNotesDefinitions['C'], 2), allNotesDefinitions['D'])
        self.assertEqual(getNoteWithTonalDistanceFromNote(allNotesDefinitions['D'], 2), allNotesDefinitions['E'])
        self.assertEqual(getNoteWithTonalDistanceFromNote(allNotesDefinitions['C'], 4), allNotesDefinitions['E'])
        self.assertEqual(getNoteWithTonalDistanceFromNote(allNotesDefinitions['C'], 3), allNotesDefinitions['D#'])
        self.assertEqual(getNoteWithTonalDistanceFromNote(allNotesDefinitions['B'], 1), allNotesDefinitions['C'])


    def test_getChordDiagramData(self):
        chordData = getChordDiagramData(allNotesDefinitions['C'], ChordTypes.Major)
        self.assertEqual(chordData, [0, 0, 0, 3])

        chordData = getChordDiagramData(allNotesDefinitions['D'], ChordTypes.Minor)
        self.assertEqual(chordData, [2, 2, 1, 0])



if __name__ == '__name__':
    unittest.main()