from typing import List


def classify_gamma_ray_by_mass(mass: float) -> str:
    """
    Classification d'un rayon gamma en fonction de la masse de sa source (trou noir, pulsar, ou autre).

    - Si la masse > 10 M☉ (masse solaire), classé comme trou noir.
    - Si la masse est entre 10 M☉ et 1 M☉, classé comme pulsar.
    - Sinon, classé comme autre source.
    Ces ordres de grandeur sont pris de façon arbitrairement pour illustrer un exemple de code.
    :param mass: Masse de la source du rayon gamma en unités de masse solaire (M☉).
    :return: La classification du rayon gamma.
    """
    if not isinstance(mass, (int, float)):
        raise TypeError("La masse doit être un nombre.")

    if mass > 10:
        return "trou noir"
    elif 1 < mass <= 10:
        return "pulsar"
    else:
        return "autre source"


def main():
    """Fonction principale pour classifier un rayon gamma selon la masse de sa source."""
    print("Bienvenue dans le classificateur de rayons gamma!")
    try:
        mass = float(input("Entrez la masse de la source du rayon gamma (en M☉) : "))
        classification = classify_gamma_ray_by_mass(mass)
        print(f"Le rayon gamma est classifié comme : {classification}")
    except ValueError:
        print("Erreur : veuillez entrer une valeur numérique valide pour la masse.")
    except TypeError as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()


def classify_gamma_ray(data: List[float]) -> str:
    # Implémentation de la fonction
    if len(data) > 5:
        return "Pulsar"
    return "Black Hole"


1
