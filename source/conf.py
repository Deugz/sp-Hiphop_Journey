# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Hiphop Journey'
copyright = '2023, Vincent Deguin'
author = 'Vincent Deguin'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

comments_config = {
   "utterances": {
      "repo": "https://github.com/Deugz/sp-Hiphop_Journey",
      "optional": "config",
   }
}

comments_config = {
   "hypothesis": True
}




extensions = [
  
  "myst_parser",
  "sphinx_design",
  "sphinx_comments",
  "sphinx_new_tab_link",
  "sphinx_book_theme",
  "sphinx_togglebutton",
  "sphinx_thebe",
]

myst_enable_extensions = ["colon_fence", "linkify", "substitution", "html_image"]
myst_heading_anchors = 2



templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/Logo/HLA-Logo.png"
html_favicon = "_static/Logo/HLA-Logo.png"
html_static_path = ['_static']

html_theme_options = {
    "analytics": {"google_analytics_id": "G-N80S8Q5VH7"},    
    "external_links": [
        {
            "url": "https://deugz.github.io/nb-hiphop/_build/html/intro.html",
            "name": " &nbsp 💽 DJ's",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/nb-hiphop/_build/html/intro.html",
            "name": " &nbsp 🎤 MC's",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-dance-hh/_build/html/intro.html",
            "name": " &nbsp 🤸 Breakdancers",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-graff/_build/html/intro.html",
            "name": "&nbsp 🎨 Graffers",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-graff/_build/html/intro.html",
            "name": "&nbsp ☝ 5th Elements",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-hiphop-research/_build/html/intro.html",
            "name": "&nbsp 🔧 Research (Accademia)",
            "attributes": {"target": "_blank"},
        },
        {
            "url": " https://deugz.github.io/jb-society-hh/_build/html/intro.html",
            "name": "&nbsp 🌍 Societal Impact &nbsp",
            "attributes": {"target": "_blank"},
        },

    ],
    "header_links_before_dropdown": 6,    
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Deugz/sp-Hiphop_Journey",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Home",
            "url": "https://deugz.github.io/Encyclopedia-Home/build/html/index.html",
            "icon": "fa-solid fa-house",
        },
        {
            "name": "Profile",
            "url": "https://deugz.github.io/nb-profile/_build/html/intro.html",
            "icon": "fa-solid fa-user",
        },
        {
            "name": "Blog",
            "url": "https://deugz.github.io/ab-blog/_website/index.html",
            "icon": "fa-solid fa-blog",
        },
        {
            "name": "Tools",
            "url": "https://deugz.github.io/nb-tools/_build/html/intro.html",
            "icon": "fa-solid fa-screwdriver-wrench",
        },
        {
            "name": "Forum",
            "url": "https://deugz.github.io",
            "icon": "fa-solid fa-comments",
        },
    ],
    

    "logo": {
        "text": "&nbsp Hiphop Living Arxiv &nbsp &nbsp",
        "image_dark": "_static/Logo/HLA-Logo.png",
        "alt_text": "V. Deguin",
    },
    
    
    "navbar_start": ["navbar-logo"],
    
}


html_css_files = ["css/custom_style.css", "css/Cube.css", "css/coffee_cup.css", "css/kittons.css", "css/style_book_shell.css", "css/style_flipping_card.css", "css/style_wheel.css"]
html_js_files = ["assets/script/kittons.js", "assets/script/script_flipping_card.js", "assets/script/script_wheel.js", "assets/script/scriptvideo.js", "assets/script/slideshow.js"]

    
