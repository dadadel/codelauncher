codelauncher
============

A Flask Python server to launch C code and Python code online.

This is a simple, light Flask server that allows you to quickly run C code or Python code.
It uses only HTML5 and CSS3. No Javascript is needed.

The only dependency is Flask.

WARNING: Be careful, this is intended to run in local as there is no sandbox, no security management.

How to use
----------

The easy way is to clone it and use it via a virtualenv:

.. code-block:: sh

    $ git clone https://github.com/dadadel/codelauncher.git  # or git@github.com:dadadel/codelauncher.git
    $ cd codelauncher
    $ virtualenv env
    $ . env/bin/activate
    $ pip install Flask

Run the server:

.. code-block:: sh

    $ python webdev.py

Then visite with your web browser the URL: `http://127.0.0.1:5000`.

Screenshot
----------

.. image:: screenshot-codelauncher.png
   :alt: Screenshot


