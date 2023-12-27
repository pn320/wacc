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

   $ pip install -i https://test.pypi.org/simple/ wacc


Usage
-----

Wacc's compiler comes with a command line interface. A quick overview of the most common functions is provided below.

.. option:: source

    The source file to compile

.. option:: --output-file

    The output file for the compiled program

.. option:: --o1

    Enable basic optimisations for the compiler

.. option:: --o2

    Enable advanced optimisations for the compiler

.. option:: --version

    Display the version and exit.

.. option:: --help

    Display a short usage message and exit.
