IRadarModelBistaticReceiver
===========================

.. py:class:: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver

   object
   
   Provide access to the properties and methods defining a bistatic receiver radar model.

.. py:currentmodule:: IRadarModelBistaticReceiver

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.set_mode`
              - Set the current radar mode by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.supported_modes`
              - Gets an array of supported mode names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.mode`
              - Gets the current radar mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.receiver`
              - Gets the radar receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.clutter_geometry`
              - This property is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.jamming`
              - Gets the radar jamming.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.bistatic_transmitters`
              - Gets the bistatic transmitter collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.antenna_control`
              - Gets the radar antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.clutter`
              - Gets the radar clutter settings.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModelBistaticReceiver


Property detail
---------------

.. py:property:: supported_modes
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.supported_modes
    :type: list

    Gets an array of supported mode names.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.mode
    :type: IRadarModeBistaticReceiver

    Gets the current radar mode.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.receiver
    :type: IRadarReceiver

    Gets the radar receiver.

.. py:property:: clutter_geometry
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.clutter_geometry
    :type: IRadarClutterGeometry

    This property is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.jamming
    :type: IRadarJamming

    Gets the radar jamming.

.. py:property:: bistatic_transmitters
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.bistatic_transmitters
    :type: IObjectLinkCollection

    Gets the bistatic transmitter collection.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.antenna_control
    :type: IAntennaControl

    Gets the radar antenna control.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.clutter
    :type: IRadarClutter

    Gets the radar clutter settings.


Method detail
-------------


.. py:method:: set_mode(self, modeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.set_mode

    Set the current radar mode by name.

    :Parameters:

    **modeName** : :obj:`~str`

    :Returns:

        :obj:`~None`








