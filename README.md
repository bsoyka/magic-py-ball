# Magic Py Ball

**Magic Py Ball** is a simple Python implementation of a random magic 8 ball.

```py
>>> answer()
'Without a doubt.'
```

[![Downloads](https://pepy.tech/badge/magic_py_ball)](https://pepy.tech/project/magic_py_ball)
[![Supported Versions](https://img.shields.io/pypi/pyversions/magic_py_ball.svg)](https://pypi.org/project/magic_py_ball)
[![License](https://img.shields.io/pypi/l/magic_py_ball)](https://github.com/bsoyka/magic-py-ball/blob/master/LICENSE)
[![Version](https://img.shields.io/pypi/v/magic_py_ball?label=latest)](https://pypi.org/project/magic_py_ball)

## Installation

Magic Py Ball is available on PyPI:

```console
$ python -m pip install magic_py_ball
```

Magic Py Ball officially supports Python 2.7 and 3.5+.

## API Reference

### `magic_py_ball.ANSWERS`

A `list` of `str` objects representing all possible magic 8 ball answers

### `magic_py_ball.answer()`

Gets a random magic 8 ball answer using `random.choice()`.
