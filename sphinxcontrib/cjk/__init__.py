from . import pdf, xe


VERSION = '0.1'


def setup(app):
    app.info('Initializing CJK extension.')

    app.add_node(
        pdf.CnJpKr,
        html=(pdf.on_visit_html, pdf.on_depart_html),
        latex=(pdf.on_visit_latex, pdf.on_depart_latex),
    )
    app.add_role('cjk', pdf.role)

    app.add_node(
        xe.XeCnJpKr,
        html=(xe.on_visit_html, xe.on_depart_html),
        latex=(xe.on_visit_latex, xe.on_depart_latex),
    )
    app.add_role('xecjk', xe.role)

    return {'version': VERSION}
