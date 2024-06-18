IVehiclePointing
================

.. py:class:: IVehiclePointing

   object
   
   Interface for target pointing attitude profiles, which override the basic attitude profile for a satellite and have a selected axis point in the direction of one or more selected targets, subject to applicable access constraints.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_target_pointing`
            * - :py:meth:`~targets`
            * - :py:meth:`~target_times`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePointing


Property detail
---------------

.. py:property:: use_target_pointing
    :canonical: ansys.stk.core.stkobjects.IVehiclePointing.use_target_pointing
    :type: bool

    Opt whether to use a target pointing attitude.

.. py:property:: targets
    :canonical: ansys.stk.core.stkobjects.IVehiclePointing.targets
    :type: "IAgVeTargetPointingCollection"

    Get the targets used for the attitude profile.

.. py:property:: target_times
    :canonical: ansys.stk.core.stkobjects.IVehiclePointing.target_times
    :type: "IAgVeTargetTimes"

    Get the target times.


