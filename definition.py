# Precision secant method:
# Cette methode ne semble a priori pas
# très précise car elle est basee sur une
# approximation, d'autant moins valable que
# X1 est eloigne de X0. La recherche est
# en genéral longue et moyennement precise.
# Il faut donc prendre X0 et X1 assez
# proches. Au final, c'est une methode qui,
# a cette condition, peut tout à fait bien
# fonctionner, et elle est indispensable
# pour une fonction de derivee inconnue ou
# trop lourde a calculer.


# Avantage et Incovenient de la methode de
# Halley:
# L'inconvénient majeur est de connaitre
# f′'(x) en plus de la connaissance de f(x)
# et f′(x) dans Newton-Raphson. Un avantage
# est de ne pas avoir a connaitre l'ordre
# p de la racine.

# Comparaison Halley et Newton-Raphson:
# On a obtenu la meme precision
# (10 decimales de justes) en le meme
# nombre exactement d’iterations avec la
# methode de Halley ou la methode de Newton,
# alors que la methode de Halley est ici
# beaucoup plus consommatrice de calculs !
# Elle etait donc inutile a priori, la
# methode de Newton, moins consommatrice
# de calculs, est suffisante... Elle peut
# rendre cependant de bons services dans
# certains cas ou la precision recherchee
# est superieure (il existe des situation
# dans certains domaines ou des valeurs
# doivent etre connues avec 64 decimales
# justes...), donc elle reste valable a
# connaitre car elle peut s’averer tres
# precieuse dans ces cas la

# Methode de Horner (Clenshaw):
# Les deux méthodes donnent bien entendu
# le même résultat, mais la méthode de
# Hörner est bien plus économe en termes
# de calculs réalisés. Sur les petits
# degrés de polynômes cela ne se ressent
# pas trop, mais cet algorithme est
# recommandé pour les polynômes de
# grand degré... !

# Runge-Kutta 2:
# Il existe une infinite de methode de
# Runge-Kutta 2, selon la valeur de beta
# (beta = 1/2, beta = 1, beta = 3/4, etc.)
# La fonction ci-dessous est la forme
# generale de la methode de Runge-Kutta 2
# (1-beta)f(x,y) +
#     beta*f(x+h/2beta,y+(h/2beta)*f(x,y))

# Runge-Kutta 4 est nomme ainsi car il
# l'erreur de troncation est de
# l'ordre de h^4

# La methode de Rumberg:
# permet de calculer la valeur
# numerique d'une integrale definie


# Comparaison RK2 et Euler:
# RK2 plus precis que Euler, pour
# ameliorer la precision on peut
# dimuer h, ou utiliser RK4 par
# exemple