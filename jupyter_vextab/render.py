def render_vextab(vextab: str, show_source: bool = False) -> str:
    """Create Javascript code for rendering VExflow music notation
    :param vextab: The Vexflow source code to render into music notation
    :param show_source: ``True`` to include the original Vexflow music notation
                        source code in the cell output
    :return: The Javascript code as a single string
    """
    import time

    vextab_js = vextab.replace('\n', r'\n')
    cid='vextab-{}'.format(int(round(time.time() * 1000)))
    output = [
        'require(["vextabjs"], function(VEXTABJS) {',
            #This  works if we reload the notebook page
            'element.prepend("<div class=\'vex-tabdiv\'>{}</div>");'.format(vextab_js),
            #This doesn't seem to work?
            #'element.prepend("<div id=\'{}\', class=\'vex-tabdiv\'></div>");'.format(cid),
            #'VexTab = VEXTABJS.VexTab;',
            #'Artist = VEXTABJS.Artist;',
            #'Renderer = VEXTABJS.Vex.Flow.Renderer;',
            #  '// Create VexFlow Renderer from canvas element with id #boo and a random component.',
            #'renderer = new Renderer($(\'#{}\')[0], Renderer.Backends.CANVAS);'.format(cid),
            # '// For SVG, you can use Renderer.Backends.SVG',
            #'// Initialize VexTab artist and parser.',
            #'artist = new Artist(10, 10, 600, {scale: 0.8});',
            #'vextab = new VexTab(artist);',
            #'// Parse VexTab music notation passed in as a string.',
            #'vextab.parse("{}")'.format(vextab_js),
            #'vextab.parse("tabstave notation=true\n notes :q 4/4\n");'.replace('\n', r'\n'),
            #'// Render notation onto canvas.',
            #'artist.render(renderer);',
        '});']
    if show_source:
        output.insert(3,
                      'element.prepend("<pre>{}</pre>");'
                      .format(vextab).replace('\n', '<br />'))
        
    return ''.join(output)
