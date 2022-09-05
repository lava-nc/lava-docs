project = "Lava"
copyright = "2021, Intel Corporation"
author = "Intel Corporation"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
    'sphinx.ext.imgmath',
    "sphinx.ext.mathjax",
    "nbsphinx",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram"
]

mathjax_path = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"

inheritance_graph_attrs = dict(rankdir="TB", size='""')
autosectionlabel_prefix_document = True

napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "_templates"]

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": False,
}

html_static_path = ["_static"]

autosummary_generate = True

latex_elements = {
    'preamble': r'''
\usepackage{amsmath}
''',
}
