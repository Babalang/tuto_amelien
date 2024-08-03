# pylint: skip-file
from datetime import datetime

author = "Bastian Langouet"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "recommonmark",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_automodapi.automodapi",
    "sphinx_copybutton",
]
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
    ".txt": "markdown",
}
master_doc = "index"
exclude_patterns = ["Thumbs.db"]
templates_path = []
add_module_names = False
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_ivar = True
numpydoc_show_class_members = False
todo_include_todos = True
