# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'NerdyLib'
copyright = '2022, VEX 687: The Nerd Herd'
author = 'Miguel Villa Floran'

# The full version, including alpha/beta/rc tags
release = '2-30-2022'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'myst_parser', 'sphinx-favicon'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'

# Disable showing the sourcelink option for each page
html_show_sourcelink = False

html_context = {
  'default_description': 'Resources on DeepWater Exploration Documentation',
}

source_suffix = ['.rst', '.md']

html_css_files = [
  'css/custom.css'
]

html_favicon = 'img/wave.png'

html_title = "NerdyLib Docs"

# html_logo = 'nerd_herd_2.svg'
html_theme_options = {
  'dark_logo': '687_logo_dark.svg',
  'light_logo': '687_logo_light_1.svg'
}

language = "en"
myst_html_meta = {
  "description": "NerdyLib Documentation Site",
  "keywords": "pros, vex-robotics, vex-v5"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']