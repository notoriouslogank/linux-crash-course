from sphinxawesome_theme.postprocess import Icons

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Coastal Crypto Knowledge Base"
copyright = "2024, notoriouslogank"
author = "notoriouslogank"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_title = "Coastal Crypto Knowledge Base"
html_theme = "sphinxawesome_theme"
html_static_path = ["_static"]
html_logo = "https://static.wixstatic.com/media/27c6a6_62ba63aad329460b868b5e9ede26f848~mv2.png/v1/fill/w_84,h_84,al_c,q_85,usm_1.20_1.00_0.01,enc_auto/COASTAL%20CRYPTO%20wht.png"
pygments_style = "sphinx"
highlight_language = "bash"
html_last_updated_fmt = ""
html_permalinks_icon = Icons.permalinks_icon
