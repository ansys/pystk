RFFilterModelFir
================

.. py:class:: ansys.stk.core.stkobjects.RFFilterModelFir

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRFFilterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a FIR filter model.

.. py:currentmodule:: RFFilterModelFir

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RFFilterModelFir.sampling_frequency`
              - Gets or sets the sampling frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RFFilterModelFir.numerator_complex_polynomial`
              - Gets the numerator complex polynomial.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RFFilterModelFir


Property detail
---------------

.. py:property:: sampling_frequency
    :canonical: ansys.stk.core.stkobjects.RFFilterModelFir.sampling_frequency
    :type: float

    Gets or sets the sampling frequency.

.. py:property:: numerator_complex_polynomial
    :canonical: ansys.stk.core.stkobjects.RFFilterModelFir.numerator_complex_polynomial
    :type: ICRComplexCollection

    Gets the numerator complex polynomial.


