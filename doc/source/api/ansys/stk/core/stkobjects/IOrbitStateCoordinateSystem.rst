IOrbitStateCoordinateSystem
===========================

.. py:class:: ansys.stk.core.stkobjects.IOrbitStateCoordinateSystem

   object
   
   Interface for selecting coordinate epoch for coordinate systems that do not have pre-established epochs.

.. py:currentmodule:: IOrbitStateCoordinateSystem

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCoordinateSystem.type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCoordinateSystem.coordinate_system_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOrbitStateCoordinateSystem


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCoordinateSystem.type
    :type: COORDINATE_SYSTEM

    Get the coordinate system being used.

.. py:property:: coordinate_system_epoch
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCoordinateSystem.coordinate_system_epoch
    :type: ITimeToolEventSmartEpoch

    Smart epoch component representing the coordinate epoch. Disabled for coordinate systems with pre-established epochs (e.g. J2000, B1950).


