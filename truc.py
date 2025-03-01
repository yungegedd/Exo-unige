import sympy as sp

def latex_to_text(latex_str):
    # Utiliser sympy pour interpréter l'expression LaTeX
    expr = sp.sympify(latex_str)
    # Convertir l'expression en texte lisible
    readable_text = sp.pretty(expr, use_unicode=True)
    return readable_text

# Exemple d'utilisation
latex_expression = r"\left( \frac{2}{n} \right) ^n"
print("Expression LaTeX:", latex_expression)
print("Texte lisible:", latex_to_text(latex_expression))
