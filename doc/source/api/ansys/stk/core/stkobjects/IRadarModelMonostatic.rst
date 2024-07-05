IRadarModelMonostatic
=====================

.. py:class:: ansys.stk.core.stkobjects.IRadarModelMonostatic

   object
   
   Provide access to the properties and methods defining a monostatic radar model.

.. py:currentmodule:: IRadarModelMonostatic

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMonostatic.set_mode`
              - Set the current radar mode by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMonostatic.supported_modes`
              - Gets an array of supported mode names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMonostatic.mode`
              - Gets the current radar mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMonostatic.transmitter`
              - Gets the radar transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMonostatic.receiver`
              - Gets the radar receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMonostatic.clutter_geometry`
              - This property is deprecated. Use the Clutter property instead. Gets the radar clutter geometry.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMonostatic.jamming`
              - Gets the radar jamming.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMonostatic.antenna_control`
              - Gets the radar antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMonostatic.clutter`
              - Gets the radar clutter settings.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModelMonostatic


Property detail
---------------

.. py:property:: supported_modes
    :canonical: ansys.stk.core.stkobjects.IRadarModelMonostatic.supported_modes
    :type: list

    Gets an array of supported mode names.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.IRadarModelMonostatic.mode
    :type: IRadarModeMonostatic

    Gets the current radar mode.

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.IRadarModelMonostatic.transmitter
    :type: IRadarTransmitter

    Gets the radar transmitter.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.IRadarModelMonostatic.receiver
    :type: IRadarReceiver

    Gets the radar receiver.

.. py:property:: clutter_geometry
    :canonical: ansys.stk.core.stkobjects.IRadarModelMonostatic.clutter_geometry
    :type: IRadarClutterGeometry

    This property is deprecated. Use the Clutter property instead. Gets the radar clutter geometry.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.IRadarModelMonostatic.jamming
    :type: IRadarJamming

    Gets the radar jamming.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.IRadarModelMonostatic.antenna_control
    :type: IAntennaControl

    Gets the radar antenna control.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.IRadarModelMonostatic.clutter
    :type: IRadarClutter

    Gets the radar clutter settings.


Method detail
-------------


.. py:method:: set_mode(self, modeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarModelMonostatic.set_mode

    Set the current radar mode by name.

    :Parameters:

    **modeName** : :obj:`~str`

    :Returns:

        :obj:`~None`








