pcfg
====
[![Documentation Status](https://readthedocs.org/projects/pcfg/badge/?version=latest)](https://pcfg.readthedocs.io/en/latest/?badge=latest)


Description
-----------

Implement the ``generate()`` method for NLTK's [probabilistic context-free grammar](https://www.nltk.org/api/nltk.html#nltk.grammar.PCFG) to probabilistically generate valid sentences. (NLTK stands for Natural Language Toolkit.)

Installation
------------

```zsh
pip install pcfg
```

Documentation
-------------

Read the latest documentation for **pcfg** [here](https://pcfg.readthedocs.io/).


Example usage
-------------

A ``PCFG`` can be initialized in the same way that an NLTK [probabilistic context-free grammar](https://www.nltk.org/api/nltk.html#nltk.grammar.PCFG) is initialized:

```python3
>>> from pcfg import PCFG
>>> grammar = PCFG.fromstring("""
... S -> Subject Action [1.0]
... Subject -> "a cow" [0.7] | "some guy" [0.1] | "the woman" [0.2]
... Action -> "eats lunch" [0.5] | "was here" [0.5]
... """)
```

To generate sentences, simply use the ``generate()`` method:

```python3
>> > for sentence in grammar.generate(3):
    ...
print(sentence)
```

The output could be the following:

```text
the woman eats lunch
the woman was here
a cow was here
```

Of course, your output may be different because the sentences are generated probabilistically.

License
-------
[MIT](https://github.com/thomasbreydo/pcfg/blob/master/LICENSE)
