IOrbitStateCoordinateSystem
===========================

.. py:class:: IOrbitStateCoordinateSystem

   object
   
   Interface for selecting coordinate epoch for coordinate systems that do not have pre-established epochs.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~coordinate_system_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOrbitStateCoordinateSystem


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCoordinateSystem.type
    :type: "COORDINATE_SYSTEM"

    Get the coordinate system being used.

.. py:property:: coordinate_system_epoch
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCoordinateSystem.coordinate_system_epoch
    :type: "IAgCrdnEventSmartEpoch"

    Smart epoch component representing the coordinate epoch. Disabled for coordinate systems with pre-established epochs (e.g. J2000, B1950).


