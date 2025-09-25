pyboleto
========
|ci| |pypi|

.. |ci| image:: https://github.com/GilbertoAbrao/pyboleto/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/GilbertoAbrao/pyboleto/actions
.. |pypi| image:: https://img.shields.io/pypi/v/pyboleto.svg
   :target: https://pypi.python.org/pypi/pyboleto/

.. _pyboleto-synopsis:

``pyboleto`` provides a Python toolbox for generating *boletos de cobrança*,
the Brazilian equivalent of invoices. It remains easy to extend for new banks
and custom issuing rules.

Recent Highlights
=================
- Atualizei o cálculo do fator de vencimento para refletir a orientação da
  FEBRABAN: a contagem reinicia em 1000 a partir de 22/02/2025 sem quebrar os
  boletos anteriores a essa data.
- Restabeleci a data base original (07/10/1997) e adicionei validações mais
  claras nas mensagens de erro para facilitar a depuração.
- Introduzi constantes nomeadas para controlar o reset do fator de vencimento,
  preparando o código para futuras revisões pelas instituições financeiras.

.. contents::
   :local:

.. _pyboleto-implemented-bank:

Implemented Banks
=================
You can help by implementing additional banks or by testing the current ones.

For now here's where we are.

+----------------------+----------------+-----------------+------------+
| **Bank**             | **Carteira /** | **Implemented** | **Tested** |
|                      | **Convênio**   |                 |            |
+======================+================+=================+============+
| **Banco do Brasil**  | 18             | Yes             | Yes        |
+----------------------+----------------+-----------------+------------+
| **Banrisul**         | x              | Yes             | Yes        |
+----------------------+----------------+-----------------+------------+
| **Bradesco**         | 06, 03         | Yes             | Yes        |
+----------------------+----------------+-----------------+------------+
| **Caixa Econômica**  | SR             | Yes             | No         |
+----------------------+----------------+-----------------+------------+
| **HSBC**             | CNR, CSB       | Yes             | No         |
+----------------------+----------------+-----------------+------------+
| **Itaú**             | 157            | Yes             | Yes        |
+----------------------+----------------+-----------------+------------+
| **Itaú**             | 175, 174, 178, | Yes             | No         |
|                      | 104, 109       |                 |            |
+----------------------+----------------+-----------------+------------+
| **Real**             | 57             | Yes             | No         |
+----------------------+----------------+-----------------+------------+
| **Santander**        | 102            | Yes             | Yes        |
+----------------------+----------------+-----------------+------------+
| **Santander**        | 101, 201       | Yes             | No         |
+----------------------+----------------+-----------------+------------+

.. _pyboleto-docs:

Documentation
=============
https://github.com/GilbertoAbrao/pyboleto/wiki

The quickest way to learn how to create boletos is to review the examples in
``bin/pdf_pyboleto_sample.py`` or ``bin/html_pyboleto_sample.py`` inside this
repository.

.. _pyboleto-installation:

Installation
============
You can install ``pyboleto`` either via the Python Package Index (PyPI) or from
source.

To install using pip::

    $ pip install pyboleto

To install using easy_install::

    $ easy_install pyboleto

.. _pyboleto-installing-from-source:

Downloading and installing from source
--------------------------------------
Download the latest version of ``pyboleto`` from
https://pypi.python.org/pypi/pyboleto/ or clone the repository::

    $ git clone https://github.com/GilbertoAbrao/pyboleto.git
    $ cd pyboleto
    $ python -m venv .venv && source .venv/bin/activate
    $ pip install -e .

If you prefer the source distribution::

    $ tar xvfz pyboleto-<version>.tar.gz
    $ cd pyboleto-<version>
    $ python setup.py build
    # python setup.py install  # as root

.. _pyboleto-unittests:

Executing tests
===============
You need ``setuptools`` (or ``distribute``) in order to execute the tests.
``pdftohtml``_ is required for the PDF fixtures used by the sample suite::

    $ cd pyboleto
    $ python setup.py test

.. _pdftohtml: http://poppler.freedesktop.org/

.. _pyboleto-license:

License
=======
This software is licensed under the `New BSD License`. See the ``LICENSE`` file
in the root of the repository for the full license text.

