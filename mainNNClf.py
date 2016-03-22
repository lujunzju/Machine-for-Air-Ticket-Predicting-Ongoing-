# system library
import numpy as np

# user-library
from ClassificationNN import ClassificationNN


def mainNN():
    nn = ClassificationNN()
    nn.evaluateOneRouteForMultipleTimes(nn.routes[7])

if __name__ == "__main__":
    mainNN()