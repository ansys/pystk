IRFFilterModelIir
=================

.. py:class:: IRFFilterModelIir

   object
   
   Provide access to the properties and methods defining a IIR RF filter model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~sampling_frequency`
            * - :py:meth:`~numerator_complex_polynomial`
            * - :py:meth:`~denominator_complex_polynomial`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRFFilterModelIir


Property detail
---------------

.. py:property:: sampling_frequency
    :canonical: ansys.stk.core.stkobjects.IRFFilterModelIir.sampling_frequency
    :type: float

    Gets or sets the sampling frequency.

.. py:property:: numerator_complex_polynomial
    :canonical: ansys.stk.core.stkobjects.IRFFilterModelIir.numerator_complex_polynomial
    :type: "IAgCRComplexCollection"

    Gets the numerator complex polynomial.

.. py:property:: denominator_complex_polynomial
    :canonical: ansys.stk.core.stkobjects.IRFFilterModelIir.denominator_complex_polynomial
    :type: "IAgCRComplexCollection"

    Gets the denominator complex polynomial.


