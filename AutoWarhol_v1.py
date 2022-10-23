from turtle import *
from random import randint

######################################################################
###### Zone de définition des fonctions utiles #######################
######################################################################
ciel_color = "#173877"


def make_tree_segment(size, top_position, x_position):
    segments = Turtle()
    segments.speed(0)
    segments.hideturtle()
    segments.color("green")
    segments.penup()
    segments.begin_fill()
    segments.setposition(x_position, top_position)
    segments.pendown()
    segments.setposition(x_position + size, top_position - size)
    segments.setposition(x_position - size, top_position - size)
    segments.setposition(x_position, top_position)
    segments.end_fill()


def make_tree(taille, position):
    start_segments = -50

    # Tronc
    tronc = Turtle()
    tronc.hideturtle()
    tronc.speed(0)
    tronc.color("brown")
    tronc.penup()
    tronc.setposition(position, start_segments)
    tronc.right(90)
    tronc.pensize(5)
    tronc.penup()
    tronc.forward(45)
    tronc.pendown()
    tronc.forward(10)

    color((15, 83, 12))
    tree_segments = ((int(0.6 * taille), start_segments), (int(0.8 * taille), start_segments - 10),
                     (int(0.9 * taille), start_segments - 20), (taille, start_segments - 30))
    for size, top_position in tree_segments:
        make_tree_segment(size, top_position, position)


def draw_moon():
    bgcolor(ciel_color)
    up()
    goto(180, 200)
    color('orange')
    begin_fill()
    circle(50)
    end_fill()
    up()
    goto(195, 200)
    color(ciel_color)
    begin_fill()
    circle(50)
    end_fill()


def maison(cote):
    """ Doit dessiner une maison simple (carré + triangle par dessus)

    :param cote: longueur des côtés du carré et du triangle
    """
    # Compléter la fonction ici
    setheading(0)

    # Bloc maison
    color(new_color())
    # color('black')
    x = xcor()
    y = ycor()
    begin_fill()
    pendown()

    for i in range(0, 4):
        forward(cote)
        right(90)
    setheading(90)

    end_fill()

    # Toit
    color(new_color())
    # color('grey')
    begin_fill()

    right(30)
    forward(cote)
    right(120)
    forward(cote)

    end_fill()
    penup()


def new_color():
    x = (randint(0, 255), randint(0, 255), randint(0, 255))
    return x


def rue(nb_maisons):
    """ Doit dessiner une rue de maisons aléatoires, espacées aléatoirement dans la fenêtre

    :param nb_maisons: le nombre de maisons à dessiner à la suite
    """
    # Compléter la fonction ici

    position_depart_x = -300
    position_depart_y = -200

    # Taille de la place max pour la maison
    max_place = int(600 / nb_maisons)

    # Taille max de coté de la maison
    max_cote = randint(int(0.7 * max_place), int(0.90 * max_place))

    for i in range(0, nb_maisons):
        cote = randint(int(0.75 * max_cote), int(1 * max_cote))
        place_restante = max_place - cote
        if place_restante <= 10:
            max_rand = 1
        else:
            max_rand = place_restante - 10
        position_x = randint(1, max_rand)
        position_y = randint(0, 90)
        bool_value = randint(0, 1)
        if bool_value == 0:
            position_y = -position_y
        setpos(position_depart_x + position_x, position_depart_y + cote + position_y)
        maison(cote)
        position_depart_x = position_depart_x + max_place


def etoile(diametre, rotation, nombre_branches):  # étoile à 5 branches
    """ Doit dessiner une étoile à 5 branches de diamètre donné, en partant avec un angle donné

    :param diamètre: diamètre de l'étoile (longueur des segments)
    :param rotation: angle de départ du crayon
    """
    # Compléter la fonction ici

    pendown()
    color('yellow', 'yellow')
    nbr = int(nombre_branches / 2)
    angle = nbr * 360 / nombre_branches  # Angle de rotation par branche
    begin_fill()
    left(rotation)  # Déplacement de la rotation initiale
    for i in range(0, nombre_branches):
        forward(diametre)
        left(angle)
    end_fill()
    penup()


def ciel_etoile(nb_etoiles):
    """ Doit produire un ciel étoilé au dessus de la maison en utilisant la fonction etoile

    :param nb_etoiles: nombre d'étoiles à dessiner
    """
    # Compléter la fonction ici

    for i in range(0, nb_etoiles):
        taille = randint(20, 40)
        angle = randint(0, 360)
        x = randint(-290, 290)
        y = randint(150, 290)
        nombre_branches = 2 * randint(2, 4) + 1
        setpos(x, y)
        etoile(taille, angle, nombre_branches)

    # etoile(0,0)


############################################################################
##### Zone du programme qui dessine votre nuit étoilée #######
############################################################################

taille_gazon = 200


def gazon():
    # color('green')
    green_color = "#20781d"
    color(green_color)
    fillcolor(green_color)
    penup()
    setpos(-300, taille_gazon - 300)
    begin_fill()
    pendown()
    setpos(300, taille_gazon - 300)
    setpos(300, -300)
    setpos(-300, -300)
    end_fill()
    penup()


def ciel():
    fillcolor(ciel_color)
    penup()
    setpos(-300, taille_gazon - 300)
    begin_fill()
    pendown()
    setpos(-300, 300)
    setpos(300, 300)
    setpos(300, taille_gazon - 300)
    end_fill()
    penup()


if __name__ == '__main__':
    nombre_maisons = 0
    while nombre_maisons >= 15 or nombre_maisons <= 0:
        nombre_maisons = int(input("Combien de maisons voulez-vous ?  (<15)  "))  # <- ne pas modifier !!!
    nombre_etoiles = int(input("Combien d'étoiles voulez-vous ?  "))  # <- ne pas modifier !!!

    speed(0)
    colormode(255)
    setup(600, 600)  # <- ne pas modifier !!!
    # Compléter le programme ici

    hideturtle()
    penup()

    gazon()
    ciel()

    ciel_etoile(nombre_etoiles)
    draw_moon()

    for i in range(1, nombre_maisons):
        position = -300 + i * int(600 / nombre_maisons);
        make_tree(15, position)

    rue(nombre_maisons)

    # maison(100)

    exitonclick()  # <- ne pas modifier !!!
