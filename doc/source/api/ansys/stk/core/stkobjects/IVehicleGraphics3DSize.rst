IVehicleGraphics3DSize
======================

.. py:class:: IVehicleGraphics3DSize

   object
   
   3D graphics vector size interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~scale_to_attitude_sphere`
            * - :py:meth:`~scale_value`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DSize


Property detail
---------------

.. py:property:: scale_to_attitude_sphere
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSize.scale_to_attitude_sphere
    :type: bool

    Opt whether to scale the size of the vector to the attitude sphere.

.. py:property:: scale_value
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSize.scale_value
    :type: float

    A scale value for the vector (either absolute or relative to the model scale). Dimensionless.


