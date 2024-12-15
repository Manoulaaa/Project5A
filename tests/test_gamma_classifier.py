from projet_github.gamma_classifier_model import (
    classify_gamma_ray_by_mass,
    main,
    classify_gamma_ray,
)
import pytest
from io import StringIO
import sys


def test_classify_gamma_ray_by_mass():
    # Tests pour la classification par masse
    assert (
        classify_gamma_ray_by_mass(15) == "trou noir"
    ), "Devrait être classé comme trou noir."
    assert (
        classify_gamma_ray_by_mass(8) == "pulsar"
    ), "Devrait être classé comme pulsar."
    assert (
        classify_gamma_ray_by_mass(0.5) == "autre source"
    ), "Devrait être classé comme autre source."

    # Tests des entrées invalides
    with pytest.raises(TypeError):
        classify_gamma_ray_by_mass("high")
    with pytest.raises(TypeError):
        classify_gamma_ray_by_mass("low")
    with pytest.raises(TypeError):
        classify_gamma_ray_by_mass([1, 2, 3])  # Liste non autorisée


# Test de la fonction main pour différentes classifications
def test_main_trou_noir(monkeypatch):
    # Simuler les entrées pour un trou noir (masse > 10 M☉)
    inputs = iter(["15"])  # Masse = 15 M☉
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    assert (
        "Le rayon gamma est classifié comme : trou noir" in captured_output.getvalue()
    )


def test_main_pulsar(monkeypatch):
    # Simuler les entrées pour un pulsar (masse entre 1 et 10 M☉)
    inputs = iter(["8"])  # Masse = 8 M☉
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    assert "Le rayon gamma est classifié comme : pulsar" in captured_output.getvalue()


def test_main_autre_source(monkeypatch):
    # Simuler les entrées pour une autre source (masse <= 1 M☉)
    inputs = iter(["0.5"])  # Masse = 0.5 M☉
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    assert (
        "Le rayon gamma est classifié comme : autre source"
        in captured_output.getvalue()
    )


def test_main_value_error(monkeypatch):
    # Simuler une entrée invalide pour lever une ValueError
    inputs = iter(["invalid"])  # Chaîne non convertible en float
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    assert (
        "Erreur : veuillez entrer une valeur numérique valide pour la masse."
        in captured_output.getvalue()
    )


def test_main_type_error_with_list(monkeypatch):
    # Simuler une entrée qui lève explicitement ValueError
    inputs = iter(["[1, 2, 3]"])  # Liste passée comme chaîne
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    # Tester que le message d'erreur attendu est maintenant correct pour ValueError
    assert (
        "Erreur : veuillez entrer une valeur numérique valide pour la masse."
        in captured_output.getvalue()
    )


# Tests pour la fonction classify_gamma_ray
def test_classify_gamma_ray():
    # Cas où la longueur de la liste > 5
    assert classify_gamma_ray([1, 2, 3, 4, 5, 6]) == "Pulsar"
    # Cas où la longueur de la liste <= 5
    assert classify_gamma_ray([1, 2, 3]) == "Black Hole"
