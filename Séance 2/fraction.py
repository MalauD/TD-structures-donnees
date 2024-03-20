class Fraction:
    """ Classe représentant une fraction
    """
    def __init__(self,numerateur,denominateur):
        """Créer la classe Fraction

        Args:
            numerateur (number): le numérateur
            denominateur (number): le dénominateur
        """
        if denominateur == 0:
            raise ValueError("Le dénominateur ne peut pas être nul")
        self.numerateur = numerateur
        self.denominateur = denominateur
    def __str__(self) -> str:
        """Représente la classe en chaîne de caractère

        Returns:
            str: la représentation en chaîne de caractère
        """
        return f"({self.numerateur} / {self.denominateur})"
    def __add__(self,other):
        """Additionne deux fractions

        Args:
            other (Fraction): l'autre fraction

        Returns:
            Fraction: la somme des deux fractions
        """
        return Fraction(self.numerateur*other.denominateur + other.numerateur*self.denominateur,self.denominateur*other.denominateur)
    def __mul__(self,other):
        """Multiplie deux fractions

        Args:
            other (Fraction): l'autre fraction

        Returns:
            Fraction: le produit des deux fractions
        """
        return Fraction(self.numerateur*other.numerateur,self.denominateur*other.denominateur)
    def __eq__(self, other) -> bool:
        """Compare deux fractions
        Args:
            other (Fraction): l'autre fraction
        Returns:
            bool: True si les deux fractions sont égales, False sinon
        """
        l = self.simplify()
        r = other.simplify()
        return l.numerateur == r.numerateur and l.denominateur == r.denominateur
    def simplify(self):
        """Simplifie la fraction
        """
        a = self.numerateur
        b = self.denominateur
        while b != 0:
            a, b = b, a % b
        return Fraction(self.numerateur // a,self.denominateur // a)
    def float(self):
        """Convertit la fraction
        """
        return self.numerateur / self.denominateur

if __name__ == '__main__':
    def Hn(iter):
        h = Fraction(1,1)
        for i in range(2,iter+1):
            h = h + Fraction(1,i)
        return h
    
    def Leibniz(iter):
        l = Fraction(0,1)
        for i in range(iter+1):
            l = l + Fraction((-1)**i,2*i + 1)
        return l

    test = Hn(10000)
    print(test.float())

    test2 = Leibniz(10000)
    print(test2.float())

