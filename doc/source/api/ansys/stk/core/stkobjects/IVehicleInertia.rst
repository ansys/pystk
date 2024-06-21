IVehicleInertia
===============

.. py:class:: ansys.stk.core.stkobjects.IVehicleInertia

   object
   
   Satellite inertia matrix parameters.

.. py:currentmodule:: IVehicleInertia

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleInertia.ixx`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleInertia.iyy`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleInertia.izz`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleInertia.ixy`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleInertia.ixz`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleInertia.iyz`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleInertia


Property detail
---------------

.. py:property:: ixx
    :canonical: ansys.stk.core.stkobjects.IVehicleInertia.ixx
    :type: float

    Moment of Inertia about the X body axis. Uses MomentOfInertia Dimension.

.. py:property:: iyy
    :canonical: ansys.stk.core.stkobjects.IVehicleInertia.iyy
    :type: float

    Moment of Inertia about the Y body axis. Uses MomentOfInertia Dimension.

.. py:property:: izz
    :canonical: ansys.stk.core.stkobjects.IVehicleInertia.izz
    :type: float

    Moment of Inertia about the Z body axis. Uses MomentOfInertia Dimension.

.. py:property:: ixy
    :canonical: ansys.stk.core.stkobjects.IVehicleInertia.ixy
    :type: float

    Product of Inertia between the X and Y body axes. Uses MomentOfInertia Dimension.

.. py:property:: ixz
    :canonical: ansys.stk.core.stkobjects.IVehicleInertia.ixz
    :type: float

    Product of Inertia between the X and Z body axes. Uses MomentOfInertia Dimension.

.. py:property:: iyz
    :canonical: ansys.stk.core.stkobjects.IVehicleInertia.iyz
    :type: float

    Product of Inertia between the Y and Z body axes. Uses MomentOfInertia Dimension.


