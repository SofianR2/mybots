class SENSOR:
  def __init__(self, linkName):
    self.linkName = linkName
    self.values = numpy.zeros(1000)
    print(self.values)
