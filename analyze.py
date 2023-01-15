import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
print(backLegSensorValues)

frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
print(frontLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()
