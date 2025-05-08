MeanElementTheory
=================

.. py:class:: ansys.stk.core.analysis_workbench.MeanElementTheory

   IntEnum


.. py:currentmodule:: MeanElementTheory

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~OSCULATING_ELEMENTS`
              - Osculating elements (six standard Keplerian orbital elements).

            * - :py:attr:`~KOZAI`
              - The Kozai-Iszak (KI) mean elements are based upon the paper \"The Motion of a Close earth satellite,\" Y. Kozai, The Astronomical Journal, Nov 1959, pp.367-377.

            * - :py:attr:`~BROUWER_LYDDANE`
              - Refers to the BL mean elements considering both the short and long period terms (resulting from averaging over the rotation of periapse). The perturbation terms are the J2, J3, J4 and J5 oblateness terms and it considers the term involving J2^2.

            * - :py:attr:`~BROUWER_LYDDANE_SHORT_PERIODIC_TERMS_ONLY`
              - Refers to the BL mean elements considering only the short period terms (i.e. those involving averaging over the period of the orbit) where the only perturbation force is the oblateness arising from the J2 gravity term.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import MeanElementTheory


