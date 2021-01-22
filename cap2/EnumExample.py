GREEN=1
YELLOW=2
RED=4
#TRAFFIC_LIGHTS=(GREEN,YELLOW,RED)
#traffic_lights={'GREEN':1, 'YELLOW':2, 'RED':4}

from enum import Enum
class TrafficLights(Enum):
    GREEN=1
    YELLOW=2
    RED=4

print(TrafficLights.GREEN)
print(TrafficLights.GREEN.name)
print(TrafficLights.GREEN.value)

print(TrafficLights(1))
print(TrafficLights(1).value)
print(TrafficLights(4).value )