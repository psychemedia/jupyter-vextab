# Jupyter Vextab

A simple jupyter magic, based heavily on [jupyter_abc](https://github.com/akaihola/jupyter_abc), for rendering [Vextab](http://vexflow.com/vextab/) music scores in a Jupyter notebook.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyter-vextab/master)

Current status: *mostly broken*

The magic will render the score if you reload the notebook using the vextab auto parser of suitably classed div elements, but I can't seem to get the parser to run on demand?

The brokenness is currently in `render.py`.