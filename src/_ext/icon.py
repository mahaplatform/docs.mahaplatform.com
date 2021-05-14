from docutils import nodes

def icon(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.raw('', '<i class="fa fa-'+text+'"></i>', format='html')
    return [node],[]

def setup(app):
    app.add_role("icon", icon)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
