RFFilterModelFIR
================

.. py:class:: ansys.stk.core.stkobjects.RFFilterModelFIR

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRFFilterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a FIR filter model.

.. py:currentmodule:: RFFilterModelFIR

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RFFilterModelFIR.sampling_frequency`
              - Get or set the sampling frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RFFilterModelFIR.numerator_complex_polynomial`
              - Get the numerator complex polynomial.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RFFilterModelFIR


Property detail
---------------

.. py:property:: sampling_frequency
    :canonical: ansys.stk.core.stkobjects.RFFilterModelFIR.sampling_frequency
    :type: float

    Get or set the sampling frequency.

.. py:property:: numerator_complex_polynomial
    :canonical: ansys.stk.core.stkobjects.RFFilterModelFIR.numerator_complex_polynomial
    :type: CommRadComplexNumberCollection

    Get the numerator complex polynomial.


