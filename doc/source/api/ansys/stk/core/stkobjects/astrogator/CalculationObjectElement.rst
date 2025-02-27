CalculationObjectElement
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CalculationObjectElement

   IntEnum


.. py:currentmodule:: CalculationObjectElement

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BROUWER_LYDDANE_MEAN_LONG`
              - Brouwer-Lyddane mean elements considering both the short and long period terms (i.e. resulting from averaging over the rotation of periapse). The perturbation terms are the J2, J3, J4 and J5 oblateness terms and it considers the term involving J2^2.

            * - :py:attr:`~BROUWER_LYDDANE_MEAN_SHORT`
              - Brouwer-Lyddane Mean Short - Brouwer-Lyddane mean elements considering only the short period terms (i.e. those involving averaging over the period of the orbit) where the only perturbation force is the oblateness arising from the J2 gravity term.

            * - :py:attr:`~KOZAI_IZSAK_MEAN`
              - Kozai-Izsak Mean - Kozai-Izsak mean elements for which only the short period terms (i.e. those involving averaging over the period of the orbit) are considered. The only perturbation force considered is the oblateness arising from the J2 gravity term.

            * - :py:attr:`~OSCULATING`
              - Osculating.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CalculationObjectElement


