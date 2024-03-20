class Polynomial:
    def __init__(self, coefs):
        """Créer la classe Polynomial

        Args:
            coefs (list): les coefficients dans l'ordre croissant des puissances
        """
        self.coefs = coefs
    
    def __str__(self) -> str:
        """Représente la classe en chaîne de caractère
        """
        s = ""
        for i, coef in enumerate(self.coefs):
            if coef != 0:
                if i == 0:
                    s += f"{coef}"
                else:
                    s += f" + {coef}*X^{i}"
        return s
    
    def __add__(self,other):
        """Additionne deux polynomes
        """
        # On rajoute des 0 pour que les deux polynomes aient la même taille
        s_coefs = self.coefs.copy()
        o_coefs = other.coefs.copy()
        if len(self.coefs) < len(other.coefs):
            s_coefs += [0]*(len(other.coefs) - len(self.coefs))
        if len(self.coefs) > len(other.coefs):
            o_coefs += [0]*(len(self.coefs) - len(other.coefs))
        # On additionne les coefficients deux à deux
        return Polynomial([a+b for a,b in zip(s_coefs,o_coefs)])

    def derivative(self):
        """Dérive le polynome
        """
        return Polynomial([i*coef for i,coef in enumerate(self.coefs)][1:])
    
    def integrate(self):
        """Intègre le polynome
        """
        return Polynomial([0] + [coef/i for i,coef in enumerate(self.coefs,1)])
    
if __name__ == "__main__":
    p = Polynomial([1,0,3,4])
    print(p)
    print(p.derivative())
    print(p.integrate())