import matplotlib.pyplot as plt

def init():
    #global fig, ax, texte_affiche, elements, nombre_trouves
    width, height = 9.8, 9.8 / 2
    fig, ax = plt.subplots(figsize = (width, height))
    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figure.html
    #fig.figsize = (width, height) ## inefficient
    plt.cla()
    xmin, xmax, ymin, ymax = -75, 25, 0, 40
    #plt.figure(figsize = (width, height))
    ax.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], color = 'lightgrey')
    ax.axis('off')
    ax.axis('equal')
    plt.tight_layout()

    frame = ax.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], color ='lightgrey')
    liste_fig = []
    base = ax.plot([-10, 10], [0, 0], linewidth = 5, color = 'black')
    pilier = ax.plot([5, 5], [0, 40], linewidth = 5, color = 'black')
    etais_pilier = ax.plot([2.5, 5, 7.5], [0, 5, 0], linewidth = 5, color = 'black')
    bras_potence = ax.plot([-5, 5], [40, 40], linewidth = 5, color = 'black')
    etai_bras = ax.plot([0, 5], [40, 35], linewidth = 5, color = 'black')
    corde = ax.plot([-5, -5], [40, 35.5], linewidth = 5, color = 'black')
    #https://stackoverflow.com/questions/9215658/plot-a-circle-with-pyplot
    tete = (plt.Circle((-5, 32.5), 2.5, edgecolor='k', facecolor = 'w', linewidth = 2.5), 0)
    ax.add_artist(tete[0])
    tronc = ax.plot([-5, -5], [30, 17.5], linewidth = 2.5, color = 'black')
    brasdroit = ax.plot([-5, 0], [27, 25], linewidth = 2.5, color = 'black')
    brasgauche = ax.plot([-5, -10], [27, 25], linewidth = 2.5, color = 'black')
    jambedroite = ax.plot([-5, 0], [17.5, 10], linewidth = 2.5, color = 'black')
    jambegauche = ax.plot([-5, -10], [17.5, 10], linewidth = 2.5, color = 'black')
    
    #https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.text.html
    texte_affiche = ax.text(-50, 20, '',
                            fontsize = 24, horizontalalignment='center', verticalalignment='center',
       bbox=dict(facecolor='red', alpha=0.5))
    
    elements_dessin = [base, pilier, etais_pilier, bras_potence, etai_bras, corde,
                 tete, tronc, brasdroit, brasgauche, jambedroite, jambegauche
                ]
    for k in range(len(elements_dessin)):
        elements_dessin[k][0].set_visible(False)
    return fig, ax, texte_affiche, elements_dessin

def update_texte(fig, texte_affiche, new_text):
    #global texte_affiche
    # https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib
    new_text = ' '.join(list(new_text))
    texte_affiche.set_text(new_text)
    fig.canvas.draw()
    fig.canvas.flush_events()

def update_fig(fig, elements, nombre_echecs):
    # global elements, nombre_trouves
    # https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib
    elements[nombre_echecs][0].set_visible(True)
    fig.canvas.draw()
    fig.canvas.flush_events()

def update_final(fig, ax, mot, elements, nombre_echecs):
    texte_final = ax.text(-75, 5, '',
                            fontsize = 20, horizontalalignment='left', verticalalignment='center',
       bbox=dict(facecolor='blue', alpha=0.5))
    if nombre_echecs == len(elements):
        text_final = "Perdu ! Le mot était " + mot
    else:
        text_final = "Bravo ! Vous avez gagné !"
    texte_final.set_text(text_final)
    fig.canvas.draw()
    fig.canvas.flush_events()
