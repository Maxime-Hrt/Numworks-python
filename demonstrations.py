# Methode de Halley:
# on a x = alpha + h <=> alpha= x - h
# f(alpha) = f(x - h) = f(x) - h*f'(x)
#           + h^2/2*f''(x) - ...
# a l'ordre 2:
# et f(alpha) = 0 <=> f(x)-h*f'(x)+h^2/2*f''(x)=0
# <=> h=-f(x)/(-f'(x)+h/2*f''(x))
# <=> h~=-f(x)/f'(x) et h est petit
# <=> h = -f(x)/(-f'(x)+(f(x)/2f'(x))*f'(x))
# <=> h = (-2f(x)f'(x))/(2f'(x)^2-f(x)f''(x))
# reccurence defini par alpha = x - h
# alpha = x - (-2f(x)f'(x))/(2f'(x)^2-f(x)f''(x))
# remplacer alpha par xn+1 et x par xn

# Methode de Newton-Raphson:
# f(x) = cst.h^p = cst.(x-alpha)^p
# donc f'(x) = cst.p.(x-alpha)^(p-1)
# s1 = f'(x)/f(x) = p/(x-alpha)
# <=> alpha = x - p*f(x)/f'(x)

# Methode de Euler:
# on sait que l'approximation de
# la derivee par la difference est
# y'(xn) = (y(xn+1)-y(xn))/h
# <=> y(xn+1) = y(xn) + h*f(xn,y(xn))
# avec f(xn,y(xn)) = y'(xn)

