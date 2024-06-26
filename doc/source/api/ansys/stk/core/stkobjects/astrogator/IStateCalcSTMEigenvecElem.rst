IStateCalcSTMEigenvecElem
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenvecElem

   object
   
   Properties for an STM Eigenvector element calculation object.

.. py:currentmodule:: IStateCalcSTMEigenvecElem

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenvecElem.coord_system_name`
              - Gets or sets the coordinate system within which the element is defined.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenvecElem.eigenvector_number`
              - Gets or sets the number identifying one of the six Eigenvectors.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenvecElem.state_variable`
              - Gets or sets the variable identifying the component within an Eigenvector.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenvecElem.eigenvector_complex_part`
              - Whether this value represents the real or imaginary part of an Eigenvector element.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcSTMEigenvecElem


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenvecElem.coord_system_name
    :type: str

    Gets or sets the coordinate system within which the element is defined.

.. py:property:: eigenvector_number
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenvecElem.eigenvector_number
    :type: STM_EIGEN_NUMBER

    Gets or sets the number identifying one of the six Eigenvectors.

.. py:property:: state_variable
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenvecElem.state_variable
    :type: STM_PERT_VARIABLES

    Gets or sets the variable identifying the component within an Eigenvector.

.. py:property:: eigenvector_complex_part
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenvecElem.eigenvector_complex_part
    :type: COMPLEX_NUMBER

    Whether this value represents the real or imaginary part of an Eigenvector element.


