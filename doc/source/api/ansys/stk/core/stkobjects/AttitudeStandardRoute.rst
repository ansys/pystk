AttitudeStandardRoute
=====================

.. py:class:: ansys.stk.core.stkobjects.AttitudeStandardRoute

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeStandard`, :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitude`

   Standard attitude profile for aircraft.

.. py:currentmodule:: AttitudeStandardRoute

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardRoute.basic`
              - Get the basic attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardRoute.external`
              - Get the precomputed (external) attitude properties.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AttitudeStandardRoute


Property detail
---------------

.. py:property:: basic
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardRoute.basic
    :type: AttitudeStandardBasic

    Get the basic attitude properties.

.. py:property:: external
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardRoute.external
    :type: VehicleAttitudeExternal

    Get the precomputed (external) attitude properties.


