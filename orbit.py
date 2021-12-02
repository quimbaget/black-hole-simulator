import numpy as PI
import matplotlib.pyplot as plt

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
    fig, ax = plt.subplots()
    ax.plot(xPositions,yPositions)
    circle = plt.Circle((0, 0), .08, color='orange')
    ax.add_patch(circle)
    ax.set(title='An incomplete simulation',xlabel='X',ylabel='Y')
    left_x, right_x = ax.get_xlim()
    low_y, high_y = ax.get_ylim()
    ax.set_aspect(abs((right_x-left_x)/(low_y-high_y)))
    plt.show()

def main():
    # DEFNINIM LES VARIABLES INCICIALS
    # distanceFromHoleToStar = 1.49e+11 # Distància del forat negre a l'estrella en astronomical units
    # starPeriod = 3.1514e+7 # Període en segons de l'estrella al voltant del forat negre
    # blackHoleMass = 1.89928438e+14 # Massa en Kg del forat negre
    # blackHoleRadius = 0.235974 # Radi del forat negre en astronomical units

    blackHoleIsXTimesStar = 4 # Quantes vegades més gran es el forat negre respecte l'estrella

    starMassInBlackHoleRelation = 1 / blackHoleIsXTimesStar

    # Definim perheli
    perihelionX0 = 0.8982049
    perihelionY0 = 0

    # Perihelion velocities
    perihelionVX0 = 0
    perihelionVY0 = 30.29/1.496e+8*3.154e+7 # Velocitat en el eix Y al periheli de la obrita, quina V ha de ser?

    # Inicialitzem els vectors
    xPos = [perihelionX0]
    yPos = [perihelionY0]
    xvels = [perihelionVX0]
    yvels = [perihelionVY0]

    totalEnergy = euler_method(perihelionX0, perihelionY0, perihelionVX0, perihelionVY0, 1, starMassInBlackHoleRelation, xPos, yPos)
    print_plot(xPos, yPos)


if __name__ == "__main__":
    main()