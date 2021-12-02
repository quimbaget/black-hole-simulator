import numpy as PI
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import plotly.graph_objects as go

G = 4 * PI.pi**2

def euler_method(x0, y0, vx0, vy0, relativeHoleMass, relativeStarMass, xPositions, yPositions):
    orbitEnergy = PI.array([])
    dt = .001
    # Initialize velocities
    vx = vx0
    vy = vy0

    # Initialize positions
    x = x0
    y = y0

    for i in PI.linspace(0,1,3001): # Itera 100 vegades
        r = PI.sqrt(x**2+y**2)
        ax = -G*relativeHoleMass*x/r**3
        ay = -G*relativeHoleMass*y/r**3
        #calc next position and next vel
        x = x + vx*dt
        y = y + vy*dt
        vx = vx + ax*dt
        vy = vy + ay*dt
        xPositions.append(x)
        yPositions.append(y)
        orbitEnergy = PI.append(orbitEnergy,.5*relativeStarMass*(vx**2+vy**2)-G*relativeStarMass*relativeHoleMass/r)
    return orbitEnergy

def print_plot(xPositions, yPositions):
    figure = plt.figure()
    axes1 = figure.add_axes([0,0,1,1])
    axes1.plot(xPositions,yPositions)
    axes1.set(title='An incomplete simulation',xlabel='X',ylabel='Y')
    axes1.axis('equal')
    circle1 = plt.Circle((0, 0), .08, color='orange')
    axes1.add_artist(circle1)
    plt.show()

def main():
    # DEFNINIM LES VARIABLES INCICIALS
    distanceFromHoleToStar = 970 # Distància del forat negre a l'estrella en astronomical units
    starPeriod = 5.06e+8 # Període en segons de l'estrella al voltant del forat negre
    blackHoleMass = 7.956e+36 # Massa en Kg del forat negre
    blackHoleRadius = 0.1470588235 # Radi del forat negre en astronomical units

    blackHoleIsXTimesStar = 4.51339 # Quantes vegades més gran es el forat negre respecte l'estrella

    starMassInBlackHoleRelation = 205128.2051

    # Definim perheli
    perihelionX0 = 122.6153815
    perihelionY0 = 0

    # Perihelion velocities
    perihelionVX0 = 0
    perihelionVY0 = 0.0000481283422 # Velocitat en el eix Y al periheli de la obrita, quina V ha de ser?

    # Inicialitzem els vectors
    xPos = [perihelionX0]
    yPos = [perihelionY0]
    xvels = [perihelionVX0]
    yvels = [perihelionVY0]

    totalEnergy = euler_method(perihelionX0, perihelionY0, perihelionVX0, perihelionVY0, 1, starMassInBlackHoleRelation, xPos, yPos)
    print_plot(xPos, yPos)


if __name__ == "__main__":
    main()
