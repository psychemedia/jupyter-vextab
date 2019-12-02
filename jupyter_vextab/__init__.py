from string import Template
from typing import List, Dict

from pkg_resources import resource_listdir


def find_vextabjs() -> str:
    """Find the vextabjs JavaScript file bundled with jupyter_vextab
    The first file matching ``vextab*.js`` in the ``static`` directory of the
    package is used. This way we can just replace the library with a newer
    version without updating the file name in Python code.
    :return: The HTTP path for the ``vextabjs`` library inside the Jupyter server
    """
    static_files = resource_listdir('jupyter_vextab', 'static')
    vextabjs_filename = next(name for name in static_files
                          if name.startswith('vextab') and name.endswith('.js'))
    return ('require.toUrl("nbextensions/jupyter-vextab/{}")'.format(vextabjs_filename))

def get_requirejs_configuration() -> str:
    """Generate configuration to use for ``require.config()``
    This is required for loading the ``vextabjs`` Javascript library. The library
    is loaded using the ``requirejs`` library included in Jupyter Notebook.
    ``abcjs`` is bundled and minified using Webpack and can't be loaded
    directly with ``requirejs`` without specifying the path and the name of the
    exported global object.
    :return: The configuration object for ``require.config()`` as JavaScript
             code
    """
    return Template("""
        {paths: {vextabjs: ${vextabjs_url}},
         shim: {vextabjs: {exports: 'VEXTABJS'}}}
    """).substitute(vextabjs_url=find_vextabjs())

INIT_JAVASCRIPT_TEMPLATE = Template(
    '<script type="text/javascript">'
    '    require.config(${requirejs_config});'
    '</script>')

def _jupyter_nbextension_paths() -> List[Dict[str, str]]:
    return [{'section': 'notebook',
             'src': 'static',
             'dest': 'jupyter-vextab',
             'require': 'jupyter-vextab/index'}]


def load_ipython_extension(ipython: 'IPython.InteractiveShell') -> None:
    """Initialize magics commands and load the ``vextabjs`` library
    :param ipython: The active IPython instance
    """
    from IPython.core.display import display, HTML
    from jupyter_vextab.magics import JupyterVextabMagics
    ipython.register_magics(JupyterVextabMagics)
    init_script = INIT_JAVASCRIPT_TEMPLATE.substitute(
        requirejs_config=get_requirejs_configuration())
    display(HTML(init_script))
