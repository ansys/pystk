RFFilterModelIir
================

.. py:class:: ansys.stk.core.stkobjects.RFFilterModelIir

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRFFilterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a IIR box car filter model.

.. py:currentmodule:: RFFilterModelIir

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RFFilterModelIir.sampling_frequency`
              - Gets or sets the sampling frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RFFilterModelIir.numerator_complex_polynomial`
              - Gets the numerator complex polynomial.
            * - :py:attr:`~ansys.stk.core.stkobjects.RFFilterModelIir.denominator_complex_polynomial`
              - Gets the denominator complex polynomial.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RFFilterModelIir


Property detail
---------------

.. py:property:: sampling_frequency
    :canonical: ansys.stk.core.stkobjects.RFFilterModelIir.sampling_frequency
    :type: float

    Gets or sets the sampling frequency.

.. py:property:: numerator_complex_polynomial
    :canonical: ansys.stk.core.stkobjects.RFFilterModelIir.numerator_complex_polynomial
    :type: ICRComplexCollection

    Gets the numerator complex polynomial.

.. py:property:: denominator_complex_polynomial
    :canonical: ansys.stk.core.stkobjects.RFFilterModelIir.denominator_complex_polynomial
    :type: ICRComplexCollection

    Gets the denominator complex polynomial.


