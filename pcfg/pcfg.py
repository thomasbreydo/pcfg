from typing import Iterator, List, Tuple, Union
import random
import nltk  # type: ignore
from nltk.grammar import ProbabilisticProduction  # type: ignore
from nltk.grammar import Nonterminal  # type: ignore

Symbol = Union[str, Nonterminal]


class PCFG(nltk.grammar.PCFG):
    def generate(self, n: int) -> Iterator[str]:
        """Probabilistically, recursively reduce the start symbol `n` times,
        yielding a valid sentence each time.

        Args:
            n: The number of sentences to generate.

        Yields:
            The next generated sentence.
        """
        for _ in range(n):
            yield self._generate_derivation(self.start())

    def _generate_derivation(self, nonterminal: Nonterminal) -> str:
        """Probabilistically, recursively reduce `nonterminal` to generate a
        derivation of `nonterminal`.

        Args:
            nonterminal: The non-terminal nonterminal to reduce.

        Returns:
            The derived sentence.
        """
        sentence: List[str] = []
        symbol: Symbol
        derivation: str
        for symbol in self._reduce_once(nonterminal):
            if isinstance(symbol, str):
                derivation = symbol
            else:
                derivation = self._generate_derivation(symbol)
            if derivation != "":
                sentence.append(derivation)
        return " ".join(sentence)

    def _reduce_once(self, nonterminal: Nonterminal) -> Tuple[Symbol]:
        """Probabilistically choose a production to reduce `nonterminal`, then
        return the right-hand side.

        Args:
            nonterminal: The non-terminal symbol to derive.

        Returns:
            The right-hand side of the chosen production.
        """
        return self._choose_production_reducing(nonterminal).rhs()

    def _choose_production_reducing(
        self, nonterminal: Nonterminal
    ) -> ProbabilisticProduction:
        """Probabilistically choose a production that reduces `nonterminal`.

        Args:
            nonterminal: The non-terminal symbol for which to choose a production.

        Returns:
            The chosen production.
        """
        productions: List[ProbabilisticProduction] = self._lhs_index[nonterminal]
        probabilities: List[float] = [production.prob() for production in productions]
        return random.choices(productions, weights=probabilities)[0]
