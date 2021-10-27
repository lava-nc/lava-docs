import os
import sys
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath("../lava/lava"))
sys.path.insert(0, os.path.abspath("../lava-dl"))
sys.path.insert(0, os.path.abspath("../lava-dnf"))
sys.path.insert(0, os.path.abspath("../lava-optimization"))

project = "Lava"
copyright = "2021, Intel Corporation"
author = "Intel Corporation"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme"
]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": False,
}

html_static_path = ["_static"]

autosummary_generate = True
