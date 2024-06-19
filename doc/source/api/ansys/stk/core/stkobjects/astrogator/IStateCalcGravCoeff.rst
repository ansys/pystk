IStateCalcGravCoeff
===================

.. py:class:: IStateCalcGravCoeff

   object
   
   Properties for a gravity coefficient calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~gravity_filename`
            * - :py:meth:`~coefficient_type`
            * - :py:meth:`~degree`
            * - :py:meth:`~order`
            * - :py:meth:`~normalization_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcGravCoeff


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcGravCoeff.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: gravity_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcGravCoeff.gravity_filename
    :type: str

    Source for the gravity coefficient.

.. py:property:: coefficient_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcGravCoeff.coefficient_type
    :type: GRAV_COEFF_COEFFICIENT_TYPE

    Coefficient type.

.. py:property:: degree
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcGravCoeff.degree
    :type: int

    Degree of the coefficient.

.. py:property:: order
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcGravCoeff.order
    :type: int

    Order of the coefficient.

.. py:property:: normalization_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcGravCoeff.normalization_type
    :type: GRAV_COEFF_NORMALIZATION_TYPE

    Normalization type.


