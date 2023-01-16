import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
print(backLegSensorValues)

frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
print(frontLegSensorValues)

targetAngles = numpy.load('data/targetAngles.npy')

matplotlib.pyplot.plot(backLegSensorValues, linewidth=5, label='Back Leg')
matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg')
matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
