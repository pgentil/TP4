
import notes



class Notes():
    def __init__ (self, param: list):
        self._start = float(param[0])
        self._note = param[1]
        self._duration = float(param[2])
        self._freq = None

        for i in notes.notes_mapping:
            if i[0] == self._note:
                self._freq = i[1]
                
        if self._freq == None:
            raise ValueError("Check that the music sheet has valid notes.")

    @property
    def freq(self):
        """Getter method of the frequency of the note. Returns frequency of the note."""
        return self._freq

    @property
    def start(self):
        """Getter method of the start time of the note. Returns start time of the note."""
        return self._start

    @property
    def duration(self):
        """Getter method of the duration of the note. Returns duration of the note."""
        return self._duration


    def __eq__(self, other: 'Notes'):
        return self.start == other. start

    def __lt__(self, other: 'Notes'):
        return self.start < other.start

    def __str__(self):
        return f"{self._note}"

    def __repr__(self):
        return f"Notes([{self.start}, {self._note}, {self.duration}])"



if __name__ == "__main__":
    param = ['0', 'C8', '0.5']
    param2 = ['0', 'R4', '0.5']
    note1 = Notes(param)
    # note2 = Notes(param2)
    print(note1.freq)