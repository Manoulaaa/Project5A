import inspect
import gamma_classifier  # Remplacez cela par le nom de votre module, par exemple `gamma_classifier`

def generate_readme(module, output_file="README.md"):
    """Génère un fichier README.md à partir des docstrings d'un module."""
    with open(output_file, "w") as f:
        f.write("# Documentation du projet\n\n")
        
        # Ajouter la documentation du module (docstring principal)
        f.write(inspect.getdoc(module) + "\n\n")
        
        # Parcourir toutes les fonctions et classes du module et ajouter leurs docstrings
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) or inspect.isclass(obj):
                f.write(f"## {name}\n\n")
                f.write(inspect.getdoc(obj) + "\n\n")

# Appeler la fonction avec votre module
generate_readme(gamma_classifier)  # Remplacez `gamma_classifier` par le nom de votre module
