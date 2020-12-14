""" Logic """
def print_truth_table():
    blank1 = "____________________________________"
    blank2 = "__________"
    print("\n")
    print(("Truth Table").center(len(blank1)))
    print(blank1)
    print("|   |   |     |     |      |       |")
    print("| p | q | p^q | pvq | p->q | p<->q |")
    print("|___|___|_____|_____|______|_______|")
    print("| T | T |  T  |  T  |  T   |   T   |")
    print("| T | F |  F  |  T  |  F   |   F   |")
    print("| F | T |  F  |  T  |  T   |   F   |")
    print("| F | F |  F  |  F  |  T   |   T   |")
    print("|___|___|_____|_____|______|_______|")
    print("\n")
    print(("Negation").center(len(blank2)))
    print(blank2)
    print("|   |    |")
    print("| p | !p |")
    print("|___|____|")
    print("| T |  F |")
    print("| F |  T |")
    print("|___|____|")
would = input("Would you like to see a Truth Table? (yes/no) : ")
if would == "yes":
    print_truth_table()
else:
    pass

def all_sombat():
    print("\n")
    print("True = T")
    print("False = F\n")
    print("Commutative Property\n")
    print("p ∧ q ≡ q ∧ p")
    print("p ∨ q ≡ q ∨ p")
    print("p ↔ q ≡ q ↔ p\n")
    print("Associative Property\n")
    print("p ∧ ( q ∧ r ) ≡  ( p ∧  q ) ∧ r  ≡ p ∧  q ∧ r")
    print("p ∨ ( q ∨ r ) ≡  ( p ∨  q ) ∨ r  ≡ p ∨  q ∨ r")
    print("p ↔ ( q ↔ r ) ≡  ( p ↔  q ) ↔ r  ≡ p ↔ q ↔ r\n")
    print("Distributive Property\n")
    print("p ∧ ( q ∨ r ) ≡ ( p ∧ q ) ∨ ( p ∧ r )")
    print("p ∨ ( q ∧ r ) ≡ ( p ∨ q ) ∧ ( p ∨ r )")
    print("p → ( q ∨ r ) ≡ ( p → q ) ∨ ( p → r )")
    print("p → ( q ∧ r ) ≡ ( p → q ) ∧ ( p → r )")
    print("( p ∨ q ) → r  ≡ ( p → r ) ∧ ( p → r )")
    print("( p ∧ q ) → r  ≡ ( p → r ) ∨ ( p → r )\n")
    print("If...Then Property ( → )\n")
    print("p → q ≡ !q → !p ≡ !p ∨ q\n")
    print("Mean the same as Property ( ↔ )\n")
    print("p ↔ q ≡ ( p → q ) ∧ (q → p )\n")
    print("Nigetion Property ( ! )\n")
    print("!(!p) ≡ p")
    print("!(p ∧ q) ≡ !p ∨ !q")
    print("!(p ∨ q) ≡ !p ∧ !q")
    print("!(p → q) ≡ p ∧ !q")
    print("!(p ↔ q) ≡ !p ↔ q ≡ p ↔ !q\n")
equivalence = input("Would you like to see a Equivalence Property? (yes/no) : ")
if equivalence == "yes":
    all_sombat()
else:
    pass

def tautology():
    """ Tautology is everything is always true """
    print("Tautology")
    print("The statement \" ⊤rue \" is unconditionally true.\n")
    print("1. Using the Truth Table")
    print("Create truth tables of every conceivable form, to know that there is a chance that the proposition has a false value?\n")
    print("2. Check for conflicts")
    print("Used with symbols v, → but if used with ^, ↔ it may have to be done several times.")
    print("Do this by make the answer is false. And then look back to that Can it really be done?")
    print("If you can't do this, then this proposition is tautology\n")
    print("3. Used Equivalence")
    print("=> Popularly used with ↔")
    print("=> In case Δ ↔ Ο if Δ ≡ Ο")
    print("=> So that Δ ↔ Ο is an tautology\n")
tautologys = input("Would you like to see a Tautology? (yes/no) : ")
if tautologys == "yes":
    tautology()
else:
    pass

def justification():
    """ Justification is reasonable """
    print("Justification")
    print("There are 2 methods\n")
    print("1. Bring the reason together with ^ and bring → to connect with the result. After that, check that it is an tautology.")
    print("=> If it is tautology, it reasonable.")
    print("=> If it isn't tautology, it unreasonable.\n")
    print("2. Make every reason are T, find the truth value and substitute the result.")
    print("=> If the result is T, then it is reasonable.")
    print("=> If the result is F, then it is unreasonable.\n")
justifications = input("Would you like to see a Justification? (yes/no) : ")
if justifications == "yes":
    justification()
else:
    pass

def quantifier():
    """ Quantifier is something is developer don't know, you should find by yourself """
    print(" Quantifier")
    print(" => ∀x is all x, if \"F\" is \"F\" at all")
    print(" => ∃x is some x, if \"T\" is \"T\" at all")
    print(" => ∃x[P(x)] Have T at least one T will has a truth value of T.")
    print(" => ∀x[P(x)] Have F at least one F will has a truth value of F.")
    print(" => ∃x∃y[P(x,y)] Have (x, y) at least one pair that is T will has a truth value of T.")
    print(" => ∃x∀y[P(x,y)] Have x at least one x and pair with all y that is T will has a truth value of T")
    print(" => ∀x∃y[P(x,y)] Have all x and pair with some y that is T will has a truth value of T")
    print(" => ∀x∀y[P(x,y)] Have (x,y) at least one pair is F will has a truth value of F\n")
quantifiers = input("Would you like to see a Quantifier? (yes/no) : ")
if quantifiers == "yes":
    quantifier()
else:
    pass
