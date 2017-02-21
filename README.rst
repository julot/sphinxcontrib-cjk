#################
sphinxcontrib.cjk
#################

This module adds kanji (Chinese and Japanese) and hangul (Korean) character
support in latex.


Basic Usage
===========

Installation:

::

  > pip install sphinxcontrib-cjk


Using XeLaTeX
-------------

In ``conf.py``:

::

  extensions = ['sphinxcontrib.cjk']

  LATEX_PREAMBLE = r'''
  \usepackage{xeCJK}
  \setCJKmainfont{MS Mincho}
  \setCJKsansfont{MS Gothic}
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


Using PdfLaTeX
--------------

In ``conf.py``:

::

  extensions = ['sphinxcontrib.cjk']

  latex_elements = {
      ...
      'preamble': r'\usepackage{CJKutf8}',
      ...
  }

Somewhere in the document:

::

  :cjk:`漢字`

or specify the style to use:

::

  :cjk:`漢字 <min>`

Available value for style:

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
=========

- http://tex.stackexchange.com/questions/15516/how-to-write-japanese-with-latex
- http://latex-my.blogspot.co.id/2010/06/cjk-support-in-latex.html


Disclaimer
==========

I only test this module in the following condition:

- Windows 10 x64
- Document encoding in UTF-8
- Kanji only
- Generate PDF using `MiKTeX <https://miktex.org/>`__


History
=======

0.1
---

First public release.
