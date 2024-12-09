def plus_grand_den_commun(a, b):
    if b == 0:
        raise ValueError("den ne peut pas être 0")
    while b != 0:
        a, b = b, a % b
    return abs(a)

class Fraction:
    """Class representing a fraction and operations on it


    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.


    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : - num : numérateur doit être un entier
                -den : denominateur doit etre un entier non nul

        POST : - self.__num et self.__den est initialisé à la valeurs réspectives
                - la fraction est automatiquement simplfiiée

        RAISES: -TypeError: si num ou den sont pas des entiers
                -ValueError: si den est nul
        """
        if not isinstance(num, int):
            raise TypeError('Numerator doit etre un entier')
        if not isinstance(den, int):
            raise TypeError('Denominator doit etre un entier')
        if den == 0:
            raise ValueError("Denominator ne peut pas être 0")
        self.__num = num
        self.__den = den
        if self.__num < 0 < self.__den:
            self.__den = abs(self.__den)
        elif self.__den < 0 < self.__num:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        elif self.__den < 0 and self.__num < 0:
            self.__num = abs(self.__num)
            self.__den = abs(self.__den)
        self.simplifie()

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den


    def simplifie(self):

        pgdc = plus_grand_den_commun(self.__num, self.__den)
        self.__num //= pgdc
        self.__den //= pgdc

# ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : -

        POST : -retourne le resultat sous chaine de caractère "num/den"
                - la fraction est automatiquement simplifiée
                - retourne un entier si le denominatuer est 1

        """
        if self.is_integer():
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -

        POST : -retourne une chaine "quotient + num/den"
                - retourne  "num/den" si la fraction est propre
                - retourne le quotient si la fraction est un entier


        """

        q = abs(self.numerator) // self.denominator
        r = abs(self.numerator) % self.denominator

        if self.numerator < 0:
            return f"{-q} {r}/{self.denominator}"
        if r == 0:
            return str(q)
        if q == 0:
            return f"{r}/{self.denominator}"

        return f"{q} {r}/{self.denominator}"



    # ------------------ Operators overloading ------------------


    def __add__(self, other):
        """Overloading of the + operator for fractions


         PRE : - self doit être une instance Fraction
                - other peut être une Fraction ou un entier
         POST : - retourne une fraction qui est le resultat de l'addition simplifié
                - si other n'est pas une Fraction, il sera converti automatiquement


         """
        if isinstance(other, Fraction):
            num1 = self.numerator * other.denominator
            num2 = other.numerator * self.denominator
            num_somme = num1 + num2
            den_somme = self.denominator * other.denominator

        elif isinstance(other, int):

            num1 = self.numerator
            num2 = other * self.denominator
            num_somme = num1 + num2
            den_somme = self.denominator

        else:
            raise TypeError('opération possible que entre une Fraction et une Fraction ou un entier')

        return Fraction(num_somme, den_somme)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE : - self doit être une instance Fraction
                - other peut être une Fraction ou un entier
         POST : - retourne une fraction qui est le resultat de l'sustraction simplifié
                - si other n'est pas une Fraction, il sera converti automatiquement
        """

        if isinstance(other, Fraction):
            num1 = self.numerator * other.denominator
            num2 = other.numerator * self.denominator
            den_diff = self.denominator * other.denominator
            num_diff = num1 - num2
        elif isinstance(other, int):
            other_frac = Fraction(other)
            num1 = self.numerator * other_frac.denominator
            num2 = other_frac.numerator * self.denominator
            num_diff = num1 - num2
            den_diff = self.denominator * other_frac.denominator
        else:
            raise TypeError('opération possible que entre une Fraction et une Fraction ou un entier')
        return Fraction(num_diff, den_diff)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

         PRE : - self doit être une instance Fraction
                - other peut être une Fraction ou un entier
         POST : - retourne une fraction qui est le resultat de la miltiplication  simplifié
                - si other n'est pas une Fraction, il sera converti automatiquement
        """
        if isinstance(other, Fraction):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
        elif isinstance(other, int):
            other_frac = Fraction(other)
            num = self.numerator * other_frac.numerator
            den = self.denominator * other_frac.denominator
        else:
            raise TypeError('opération possible que entre une Fraction et une Fraction ou un entier')
        return Fraction(num, den)


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

         PRE : - self doit être une instance Fraction
                - other peut être une Fraction ou un entier
         POST : - retourne une fraction qui est le resultat de la division  simplifié
                - si other n'est pas une Fraction, il sera converti automatiquement
        """

        if isinstance(other, Fraction):
            o_num = other.numerator
            o_den = other.denominator
        elif isinstance(other, int):
            other_frac = Fraction(other)
            return self / other_frac
        else:
            raise TypeError('opération possible que entre une Fraction et une Fraction ou un entier')
        num = self.numerator * o_den
        den = self.denominator * o_num

        return Fraction(num, den)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

         PRE : -self et other doivent etre des  entiers
        POST : - si other est un int , simple multiplication
                - si other est 0, resultat 1
                -si other est 1, resultat self lui meme
                -si other est negatif, il inverse la fraction self
                -si other est une fraction, raise Value Error ne prend que des entiers en tant que other
        """

        if other == 0:
            return Fraction(1)
        elif other > 0:
            result = self
            for i in range(other - 1):
                result *= self
            return result
        elif other < 0:
            new_num = self.denominator
            new_den = self.numerator
            new = Fraction(new_num, new_den)
            return new * -other
        else:
            raise ValueError("other doit être un entier")

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : -self et other doivent etre des Fractions

        POST : la fraction est considérée comme égale si leur produit croisé et identique

        """
        if isinstance(other, Fraction):
            prod1 = self.numerator * other.denominator
            prod2 = other.numerator * self.denominator
            return prod1 == prod2
        elif isinstance(other, int):
            return self.numerator == other * self.denominator
        elif isinstance(other, float):
            return self.__float__() == other
        return False

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : -
        POST : retour du resultat en decimales de la fraction
        """
        return self.numerator / self.denominator

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------
    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : - un denominator doit etre non nul
        POST : - retourne True si la fraction est bien 0, sinon False
        """

        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -self.den ne peut pas etre nul
        POST : -retourne True si si la fraction est divisible par le den sans reste ,sinon False
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : le self.num doit etre plus petit que le den non nul en valeur absolues
        POST : retourne True si c'est bien une fraction propre, sinon false
        """
        return abs(self.numerator) < abs(self.denominator)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : -
        POST : retorune True si le num est egal à un ,sinon false

        """
        return self.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : -self et other doivent etre des objets de fraction valides
        POST : retourne True si la valeur absolue de la différene est une fraction unitaire (1/n)
        RAISE :  TypeError si other n'est pas instance de Fraction
        """

        if not isinstance(other, Fraction):
            raise TypeError("other n'est pas une fraction")

        num_diff = abs(self.numerator * other.denominator - other.numerator * self.denominator)
        den_diff = self.denominator * other.denominator
        return num_diff == 1 and den_diff > 1


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(-2, 4)

    print(x)
    print(f"{x} + {y} = {x+y}")
    print(f"{x} - {y} = {x-y}")
    print(f"{x} * {y} = {x*y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} ** {6} = {x ** 6}")
    print(f"fraction {x}  est zéro : {x.is_zero()}")
    print(f"fraction {x} est un entier : {x.is_integer()}")
    print(f'fraction {x} est un mixed nnumber : {x.as_mixed_number()}')
    print(f"fraction {x} est adjacents à {y}: {x.is_adjacent_to(y)}")
    print(f" {x} = {y} : {x == y}")
    print(f" {x} = {float(x)}")

    try:
        z = Fraction(1, "2")
    except TypeError as e:
        print(e)

    try:
        w = Fraction(1, 0)
    except ValueError as e:
        print(e)
