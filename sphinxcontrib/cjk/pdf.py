from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title


class CnJpKr(nodes.General, nodes.Element):
    pass


def on_visit_html(self, node):
    self.body.append('<span>')
    self.body.append(node['text'])


def on_depart_html(self, node):
    _ = node
    self.body.append('</span>')


def on_visit_latex(self, node):
    self.body.append(r'\begin{CJK}{UTF8}{%s}' % node['font'])
    self.body.append(node['text'])


def on_depart_latex(self, node):
    _ = node
    self.body.append(r'\end{CJK}')


def role(name, raw, text, lineno, inliner, options=None, content=None):
    _ = name
    _ = raw
    _ = lineno
    _ = inliner
    _ = options
    _ = content

    text = utils.unescape(text)
    has_explicit, text, font = split_explicit_title(text)

    if not has_explicit:
        font = 'song'

    el = CnJpKr()
    el['text'] = text
    el['font'] = font
    return [el], []
