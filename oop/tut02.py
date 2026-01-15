# Class Variables

class Instrument:

    notes = 12
    pitch = 440

    def __init__(self, instrument_name, instrument_type, octaves):
        self.instrument_name = instrument_name
        self.instrument_type = instrument_type
        self.octaves = octaves

    def totalNotes(self):
        return self.octaves * self.notes
    
    def increasePitch(self, pitchDifference):
        return Instrument.pitch + pitchDifference
    
    def decreasePitch(self, pitchDifference):
        return Instrument.pitch - pitchDifference
    
guitar = Instrument('Guitar', 'String-based Instrument', 4)
piano = Instrument('Piano', 'String-based Instrument', 7)

print(f"guitar.notes : {guitar.notes}")
print(f"piano.notes : {piano.notes}")
print(f"Instrument.notes : {Instrument.notes}")

print(guitar.__dict__)
print(piano.__dict__)
print(Instrument.__dict__)
