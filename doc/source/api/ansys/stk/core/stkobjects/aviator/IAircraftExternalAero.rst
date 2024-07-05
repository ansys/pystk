IAircraftExternalAero
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero

   object
   
   Interface used to access the External File Aerodynamics options for the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: IAircraftExternalAero

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.set_forward_flight_filepath`
              - Set the filepath for the forward flight aero file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.reload_forward_flight_file`
              - Reload the forward flight aero file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.set_takeoff_landing_filepath`
              - Set the filepath for the takeoff and landing aero file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.reload_takeoff_landing_file`
              - Reload the takeoff and landing aero file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.forward_flight_filepath`
              - Get the filepath for the forward flight aero file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.forward_flight_reference_area`
              - Gets or sets the area of the lifting surface of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.can_set_forward_flight_reference_area`
              - Check whether you can set the reference area or whether it is specified in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.is_forward_flight_valid`
              - Check whether the forward flight file is valid.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.takeoff_landing_filepath`
              - Get the filepath for the takeoff and landing aero file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.takeoff_landing_reference_area`
              - Gets or sets the area of the lifting surface of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.can_set_takeoff_landing_reference_area`
              - Check whether you can set the reference area or whether it is specified in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.is_takeoff_landing_valid`
              - Check whether the takeoff and landing file is valid.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftExternalAero


Property detail
---------------

.. py:property:: forward_flight_filepath
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.forward_flight_filepath
    :type: str

    Get the filepath for the forward flight aero file.

.. py:property:: forward_flight_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.forward_flight_reference_area
    :type: float

    Gets or sets the area of the lifting surface of the aircraft.

.. py:property:: can_set_forward_flight_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.can_set_forward_flight_reference_area
    :type: bool

    Check whether you can set the reference area or whether it is specified in the file.

.. py:property:: is_forward_flight_valid
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.is_forward_flight_valid
    :type: bool

    Check whether the forward flight file is valid.

.. py:property:: takeoff_landing_filepath
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.takeoff_landing_filepath
    :type: str

    Get the filepath for the takeoff and landing aero file.

.. py:property:: takeoff_landing_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.takeoff_landing_reference_area
    :type: float

    Gets or sets the area of the lifting surface of the aircraft.

.. py:property:: can_set_takeoff_landing_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.can_set_takeoff_landing_reference_area
    :type: bool

    Check whether you can set the reference area or whether it is specified in the file.

.. py:property:: is_takeoff_landing_valid
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.is_takeoff_landing_valid
    :type: bool

    Check whether the takeoff and landing file is valid.


Method detail
-------------


.. py:method:: set_forward_flight_filepath(self, filepath: str) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.set_forward_flight_filepath

    Set the filepath for the forward flight aero file.

    :Parameters:

    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: reload_forward_flight_file(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.reload_forward_flight_file

    Reload the forward flight aero file.

    :Returns:

        :obj:`~str`






.. py:method:: set_takeoff_landing_filepath(self, filepath: str) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.set_takeoff_landing_filepath

    Set the filepath for the takeoff and landing aero file.

    :Parameters:

    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: reload_takeoff_landing_file(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalAero.reload_takeoff_landing_file

    Reload the takeoff and landing aero file.

    :Returns:

        :obj:`~str`





