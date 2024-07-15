OrbitStateCoordinateSystem
==========================

.. py:class:: ansys.stk.core.stkobjects.OrbitStateCoordinateSystem

   Bases: 

   Selection of coordinate epoch for coordinate systems that do not have pre-established epochs.

.. py:currentmodule:: OrbitStateCoordinateSystem

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCoordinateSystem.type`
              - Get the coordinate system being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCoordinateSystem.coordinate_system_epoch`
              - Smart epoch component representing the coordinate epoch. Disabled for coordinate systems with pre-established epochs (e.g. J2000, B1950).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OrbitStateCoordinateSystem


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.OrbitStateCoordinateSystem.type
    :type: COORDINATE_SYSTEM

    Get the coordinate system being used.

.. py:property:: coordinate_system_epoch
    :canonical: ansys.stk.core.stkobjects.OrbitStateCoordinateSystem.coordinate_system_epoch
    :type: ITimeToolEventSmartEpoch

    Smart epoch component representing the coordinate epoch. Disabled for coordinate systems with pre-established epochs (e.g. J2000, B1950).


