from gabes.label import Label

class Wire(object):
    """The :class:`Wire` object holds two labels representing
    *True* and *False*.
    """
    def __init__(self):
        self.false_label = Label(False)
        self.true_label  = Label(True)

    def labels(self):
        for label in (self.false_label, self.true_label):
            yield label

    def get_label(self, representing):
        return self.true_label if representing else self.false_label