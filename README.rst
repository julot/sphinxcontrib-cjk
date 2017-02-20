#################
sphinxcontrib.cjk
#################

This module adds kanji (Chinese and Japanese) and hangul (Korean) character
for latex.


Basic Usage
===========


XeLaTeX
-------

::

  LATEX_PREAMBLE = r'''
  \usepackage{xeCJK}
  \setCJKmainfont{MS Mincho} % for \rmfamily
  \setCJKsansfont{MS Gothic} % for \sffamily
  '''

  latex_elements = {
      ...
      'preamble': LATEX_PREAMBLE,
      ...
  }

Somewhere in the document:

::

  :xecjk:`漢字`

Generate pdf:

::

  > make latex
  > xelatex doc.tex


PdfLaTeX
--------

::

  latex_elements = {
      ...
      'preamble': r'\usepackage{CJKutf8}',
      ...
  }

Somewhere in the document:

::

  :cjk:`漢字`

  or

  :cjk:`漢字 <font>`

Available value for font:

- gbsn (简体宋体, simplified Chinese)
- gkai (简体楷体, simplified Chinese )
- bsmi (繁体细上海宋体, traditional Chinese)
- bkai (繁体标楷体, traditional Chinese)

- min (明朝 Mincho)
- goth (ゴシック Gothic)
- maru (丸ゴシック Maru Gothic)

- song (宋体, simsun.ttc, default)
- fs (仿宋, simfant.ttf)
- kai (楷书, simkai.ttf)
- hei (黑体, simhei.ttf)
- li (隶书, simli.ttf)
- you (幼圆, simyou.ttf)

Example:

::

  :cjk:`漢字 <min>`

If you didn't supply the font, it will be fall back to 'song'.

Generate pdf:

::

  > make latex
  > pdflatex doc.tex


Reference
---------

- http://tex.stackexchange.com/questions/15516/how-to-write-japanese-with-latex
- http://latex-my.blogspot.co.id/2010/06/cjk-support-in-latex.html


History
=======

0.1
---

First public release.
