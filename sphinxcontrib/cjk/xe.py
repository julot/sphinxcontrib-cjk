from docutils import nodes


class XeCnJpKr(nodes.General, nodes.Element):
    pass


def on_visit_html(self, node):
    self.body.append('<span>')
    self.body.append(node['text'])


def on_depart_html(self, node):
    _ = node
    self.body.append('</span>')


def on_visit_latex(self, node):
    self.body.append(r'\textsf{%s}' % node['text'])


def on_depart_latex(self, node):
    _ = self
    _ = node


def role(name, raw, text, lineno, inliner, options=None, content=None):
    _ = name
    _ = raw
    _ = lineno
    _ = inliner
    _ = options
    _ = content

    el = XeCnJpKr()
    el['text'] = text
    return [el], []
