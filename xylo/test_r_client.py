
import r_client

from xylophone.client import XyloClient
from xylophone.xylo import XyloNote
import unittest


class TestNotes(unittest.TestCase):

    def setUp(self) -> None:
        self.scores = 'escala.txt'

    def test_xylo_read_scores(self):
        notes = [XyloNote("A4", 0, 90),
        XyloNote('Ab4', 1, 90),
        ]
        result = r_client.xylo_read_scores(self.scores)
        print(f"RESULT\n\n{result}")
        for i in range(len(notes)):
            self.assertEqual([notes[i].start_time,notes[i].value,notes[i].velocity], [result[i].start_time,result[i].value,result[i].velocity])

    
    def test_xylonotes(self):
        expected = []
        result = []
        with open(f'{self.scores}', 'r') as scr:
            for line in scr:
                line = line.split(' ')
                if line in r_client.ACCEPTED_NOTES:
                    expected.append(line)
            for line in scr:
                if r_client.xylonotes(line):
                    result.append(line)
        self.assertEqual(expected, result)

    def test_note_velocity(self):
        notes = [["A4", 0], ["Ab4", 1]]
        for i in notes:
            if i == notes[0]:
                r_client.note_velocity(i)
            else:
                r_client.note_velocity(i, 40)
        expected = [["A4", 0, 90], ["Ab4", 1, 40]]
        self.assertEqual(notes, expected)

    def test_xylo_object(self):
        notes = [["A4", 0, 90], ["Ab4", 1, 40]]
        result = []
        for i in range(len(notes)):
            result.append(r_client.xylo_object(notes[i]))
            self.assertTrue(isinstance(result[i], XyloNote))


    def tearDown(self) -> None:
        del self.scores

if __name__ == "__main__":
    unittest.main()