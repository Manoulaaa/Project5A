from gamma_classifier import classify_gamma_ray_by_mass, main
import pytest
from io import StringIO
import sys

def test_classify_gamma_ray_by_mass():
    # Tests pour la classification par masse
    assert classify_gamma_ray_by_mass(15) == "trou noir", "Devrait être classé comme trou noir."
    assert classify_gamma_ray_by_mass(8) == "pulsar", "Devrait être classé comme pulsar."
    assert classify_gamma_ray_by_mass(0.5) == "autre source", "Devrait être classé comme autre source."
    
    # Tests des entrées invalides
    with pytest.raises(TypeError):
        classify_gamma_ray_by_mass("high")
    with pytest.raises(TypeError):
        classify_gamma_ray_by_mass("low")

def test_main_trou_noir(monkeypatch):
    # Simuler les entrées pour un trou noir (masse > 10 M☉)
    inputs = iter(['15'])  # Masse = 15 M☉
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    assert "Le rayon gamma est classifié comme : trou noir" in captured_output.getvalue()

def test_main_pulsar(monkeypatch):
    # Simuler les entrées pour un pulsar (masse entre 1 et 10 M☉)
    inputs = iter(['8'])  # Masse = 8 M☉
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    assert "Le rayon gamma est classifié comme : pulsar" in captured_output.getvalue()

def test_main_autre_source(monkeypatch):
    # Simuler les entrées pour une autre source (masse <= 1 M☉)
    inputs = iter(['0.5'])  # Masse = 0.5 M☉
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    assert "Le rayon gamma est classifié comme : autre source" in captured_output.getvalue()

def test_main_invalid_input(monkeypatch):
    # Simuler une entrée invalide
    inputs = iter(['invalid'])  # Entrée non valide
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    assert "Erreur : veuillez entrer une valeur numérique valide pour la masse." in captured_output.getvalue()

