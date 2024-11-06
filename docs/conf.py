import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = 'LanoValoPy'
copyright = '2024, Valorant API Wrapper'
author = 'Lanxre'
release = '0.8.0'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "autodocsumm",
]

add_module_names = False
templates_path = ["templates"]
source_suffix = ".rst"
html_extra_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"
todo_include_todos = True

html_codeblock_linenos_style = "table"
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
