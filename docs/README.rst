.. Note, requirements.txt should be up-to-date for Read the Docs


Description
===========

Implement the :meth:`~pcfg.PCFG.generate_sentences` method for NLTK's `probabilistic context-free grammar`_ to probabilistically generate valid sentences. (NLTK stands for Natural Language Toolkit.)

Installation
============

The source code for **pcfg** hosted on `Github`_.

.. code-block:: zsh

    pip install pcfg

.. Documentation
   =============
   Read the latest documentation for **pcfg** `here <https


Example usage
=============

A :class:`~pcfg.PCFG` can be initialized in the same way that an NLTK `probabilistic context-free grammar`_ is initialized:

.. code-block:: python3

   >>> from pcfg import PCFG
   >>> grammar = PCFG.fromstring("""
   ... S -> Subject Action [1.0]
   ... Subject -> "a cow" [0.7] | "some guy" [0.1] | "the woman" [0.2]
   ... Action -> "eats lunch" [0.5] | "was here" [0.5]
   ... """)

To generate sentences, simply use the :meth:`~pcfg.PCFG.generate_sentences` method:

.. code-block:: python3

   >>> for sentence in grammar.generate_sentences(3):
   ...     print(sentence)

The output could be the following:

.. code-block::

   the woman eats lunch
   the woman was here
   a cow was here

Of course, your output may be different because the sentences are generated probabilistically.

License
=======
MIT_

.. _MIT: https://github.com/thomasbreydo/pcfg/blob/master/LICENSE
.. _probabilistic context-free grammar: https://www.nltk.org/api/nltk.html#nltk.grammar.PCFG
.. _Github: https://github.com/thomasbreydo/pcfg