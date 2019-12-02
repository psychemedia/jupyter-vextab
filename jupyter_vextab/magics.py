from IPython.core.display import display, Javascript
from IPython.core.magic import cell_magic, Magics, magics_class

from jupyter_vextab.render import render_vextab


@magics_class
class JupyterVextabMagics(Magics):
    """Jupyter notebook magic commands for rendering music notation"""
    @cell_magic
    def vextab(self, line: str, cell: str):
        """The ``%%vextab`` magic command for rendering Vextab music notation
        If the first line of a cell starts with ``%%vextab``, subsequent lines are
        interpreted as Vextab notation and rendered as music using the ``vextabjs``
        JavaScript library.
        :param line: The first line of the cell
        :param cell: The rest of the text in the cell
        :return: The Javascript code for rendering the music
        """
        arguments = line.split()
        show_source = '--source' in arguments or '-s' in arguments
        return Javascript(render_vextab(cell, show_source=show_source))
