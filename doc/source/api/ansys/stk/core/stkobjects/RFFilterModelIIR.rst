RFFilterModelIIR
================

.. py:class:: ansys.stk.core.stkobjects.RFFilterModelIIR

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRFFilterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a IIR box car filter model.

.. py:currentmodule:: RFFilterModelIIR

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RFFilterModelIIR.sampling_frequency`
              - Get or set the sampling frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RFFilterModelIIR.numerator_complex_polynomial`
              - Get the numerator complex polynomial.
            * - :py:attr:`~ansys.stk.core.stkobjects.RFFilterModelIIR.denominator_complex_polynomial`
              - Get the denominator complex polynomial.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RFFilterModelIIR


Property detail
---------------

.. py:property:: sampling_frequency
    :canonical: ansys.stk.core.stkobjects.RFFilterModelIIR.sampling_frequency
    :type: float

    Get or set the sampling frequency.

.. py:property:: numerator_complex_polynomial
    :canonical: ansys.stk.core.stkobjects.RFFilterModelIIR.numerator_complex_polynomial
    :type: CommRadComplexNumberCollection

    Get the numerator complex polynomial.

.. py:property:: denominator_complex_polynomial
    :canonical: ansys.stk.core.stkobjects.RFFilterModelIIR.denominator_complex_polynomial
    :type: CommRadComplexNumberCollection

    Get the denominator complex polynomial.


