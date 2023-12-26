Welcome to wacc documentation!
==============================

Wacc is a compiler for a small, fictional language that is a sort of cross between Lua and C. It is written entirely in Python,
and is designed to a toy compiler so it isn't really optimised for speed or anything like that. It is designed to be a learning
experience and a stepping stone for implementing a more complex compiler in the future.

Installation
------------

To run the wacc compiler on your local machine,
run this command in your terminal:

.. code-block:: console

   $ git clone https://gitlab.com/pn320/wacc.git
   $ cd wacc
   $ pip install -e .
   $ poetry run wacc --help


Usage
-----

Wacc's compiler comes with a command line interface. A quick overview of the most common functions is provided below.

.. code-block:: console

   $ wacc

.. option:: -l <language>, --language <language>

   The Wikipedia language edition,
   as identified by its subdomain on
   `wikipedia.org <https://www.wikipedia.org/>`_.
   By default, the English Wikipedia is selected.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.
