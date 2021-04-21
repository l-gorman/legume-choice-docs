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
import sphinx_rtd_theme
import sphinx_markdown_tables
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
import myst_parser
# -- Project information -----------------------------------------------------

project = 'LegumeCHOICE'
copyright = '2021, Leo Gorman'
author = 'Leo Gorman'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    #'recommonmark',
    'sphinx_markdown_tables',
    'myst_parser'
]


github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)


# source_parsers = {
#     '.md': CommonMarkParser,
# }

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown'
# }


myst_enable_extensions = [
    "substitution"
]

### All of the main substitutions to add to the sphinx documentation
# To reference any of these, use either {{key}}, to reference in text.
# Or use {{ '[here]({})'.format(key) }} to link in text
# For multiple component links simply build on this
# {{ '[NEW LINK]({}{})'.format(key1,key2) }}
# See here for documentation on these types of substitution https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html

# Personal urls
# myst_substitutions = {
#   "githubBase":"https://github.com/l-gorman/",  
#   "frontEndRepo": "legume-choice-client",
#   "apiRepo": "legume-choice-api",
#   "docsRepo": "legume-choice-docs",
#   "serverConfRepo": "legume-choice-conf",
#   "dataProcessingRepo": "legume-choice-data-processing",
   
#   "appURL": "https://l-gorman.github.io/legume-choice-client/",
#   "apiUrl": "https://l-gorman.com/",
#   "publicData": "LegumeCHOICE",
#   "adminData": "AdminLegumeCHOICE"
# }

# ILRI URLS
myst_substitutions = {
  "githubBase":"https://github.com/ilri/",  
  "frontEndRepo": "legume-choice-client",
  "apiRepo": "legume-choice-api",
  "docsRepo": "legume-choice-docs",
  "serverConfRepo": "legume-choice-conf",
  "dataProcessingRepo": "legume-choice-data-processing",
   
  "appURL": "https://legumechoice.ilri.org/",
  "apiUrl": "https://api.legumechoice.ilri.org/",
  "publicData": "LegumeCHOICE",
  "adminData": "AdminLegumeCHOICE"
}




latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']