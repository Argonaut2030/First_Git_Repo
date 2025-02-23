import sys
import os
from dotenv import load_dotenv

load_dotenv(os.path.abspath('../.env'))
sys.path.append(os.path.abspath('..'))
# sys.path.insert(0, os.path.abspath('..'))

project = 'Rest API'
copyright = '2023, Krabat'
author = 'Krabat'

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'nature'
html_static_path = ['_static']






 # Configuration file for the Sphinx documentation builder.
# #
# # For the full list of built-in configuration values, see the documentation:
# # https://www.sphinx-doc.org/en/master/usage/configuration.html

# # -- Project information -----------------------------------------------------
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# project = 'Contacts App'
# copyright = '2025, Alex'
# author = 'Alex'

# # -- General configuration ---------------------------------------------------
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []

# templates_path = ['_templates']
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# # -- Options for HTML output -------------------------------------------------
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_static_path = ['_static']


