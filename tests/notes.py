import sys
sys.path.insert(0,'..')

import unittest
from music.notes import Note, Tones, NoteError


class TestNotesClass(unittest.TestCase):

    def test_name(self):
        note = Note(Tones.C, False)
        self.assertEqual(note.name(), "C")

        note = Note(Tones.C, True)
        self.assertEqual(note.name(), "C#")

        note = Note(Tones.D, False)
        self.assertEqual(note.name(), "D")

        note = Note(Tones.D, True)
        self.assertEqual(note.name(), "D#")

        note = Note(Tones.E, False)
        self.assertEqual(note.name(), "E")

        with self.assertRaises(NoteError):
            note = Note(Tones.E, True)

        note = Note(Tones.F, False)
        self.assertEqual(note.name(), "F")

        note = Note(Tones.F, True)
        self.assertEqual(note.name(), "F#")

        note = Note(Tones.G, False)
        self.assertEqual(note.name(), "G")

        note = Note(Tones.G, True)
        self.assertEqual(note.name(), "G#")

        note = Note(Tones.A, False)
        self.assertEqual(note.name(), "A")

        note = Note(Tones.A, True)
        self.assertEqual(note.name(), "A#")

        note = Note(Tones.B,  False)
        self.assertEqual(note.name(), "B")

        with self.assertRaises(NoteError):
            note = Note(Tones.B, True)
