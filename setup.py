from setuptools import setup

setup(
    data_files=[('share/jupyter/nbextensions/jupyter-vextab',
                 ['jupyter_vextab/static/vextab-div.js'])]
    # The rest of the setuptools configuration comes from `setup.cfg`. The
    # `data_files` argument is here since it's not yet supported in
    # `setup.cfg`
)
