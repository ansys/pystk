IVehicleThirdBodyGravityElement
===============================

.. py:class:: IVehicleThirdBodyGravityElement

   object
   
   Third-body gravity interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~source`
            * - :py:meth:`~gravity_value`
            * - :py:meth:`~central_body`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleThirdBodyGravityElement


Property detail
---------------

.. py:property:: source
    :canonical: ansys.stk.core.stkobjects.IVehicleThirdBodyGravityElement.source
    :type: THIRD_BODY_GRAV_SOURCE_TYPE

    Source of 3rd-body gravity data.

.. py:property:: gravity_value
    :canonical: ansys.stk.core.stkobjects.IVehicleThirdBodyGravityElement.gravity_value
    :type: float

    Gravity value (if the source is user-specified. Uses Gravity Parameter Dimension.

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.IVehicleThirdBodyGravityElement.central_body
    :type: str

    Name of the central body.


