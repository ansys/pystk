IStateCalcSTMEigenval
=====================

.. py:class:: IStateCalcSTMEigenval

   object
   
   Properties for an STM Eigenvalue calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~coord_system_name`
            * - :py:meth:`~eigenvalue_number`
            * - :py:meth:`~eigenvalue_complex_part`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcSTMEigenval


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenval.coord_system_name
    :type: str

    Gets or sets the coordinate system within which the element is defined.

.. py:property:: eigenvalue_number
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenval.eigenvalue_number
    :type: "STM_EIGEN_NUMBER"

    Gets or sets the number identifying one of the six Eigenvalues.

.. py:property:: eigenvalue_complex_part
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenval.eigenvalue_complex_part
    :type: "COMPLEX_NUMBER"

    Whether this value represents the real or imaginary part of the Eigenvalue.


