RadarModelMonostatic
====================

.. py:class:: ansys.stk.core.stkobjects.RadarModelMonostatic

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a monostatic radar model.

.. py:currentmodule:: RadarModelMonostatic

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.set_mode`
              - Do not use this method, as it is deprecated. Use ModeComponentLinking on RadarModelMonostatic instead. Sets the current radar mode by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.supported_modes`
              - Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelMonostatic instead. Gets an array of supported mode names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.mode`
              - Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelMonostatic instead. Gets the current radar mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.transmitter`
              - Get the radar transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.receiver`
              - Get the radar receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.clutter_geometry`
              - Do not use this property, as it is deprecated. Use the Clutter property instead. Gets the radar clutter geometry.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.jamming`
              - Get the radar jamming.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.antenna_control`
              - Get the radar antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.clutter`
              - Get the radar clutter settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.mode_component_linking`
              - Get the link/embed controller for managing the radar mode component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModelMonostatic


Property detail
---------------

.. py:property:: supported_modes
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.supported_modes
    :type: list

    Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelMonostatic instead. Gets an array of supported mode names.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.mode
    :type: IRadarModeMonostatic

    Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelMonostatic instead. Gets the current radar mode.

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.transmitter
    :type: RadarTransmitter

    Get the radar transmitter.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.receiver
    :type: RadarReceiver

    Get the radar receiver.

.. py:property:: clutter_geometry
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.clutter_geometry
    :type: RadarClutterGeometry

    Do not use this property, as it is deprecated. Use the Clutter property instead. Gets the radar clutter geometry.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.jamming
    :type: RadarJamming

    Get the radar jamming.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.antenna_control
    :type: AntennaControl

    Get the radar antenna control.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.clutter
    :type: RadarClutter

    Get the radar clutter settings.

.. py:property:: mode_component_linking
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.mode_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar mode component.


Method detail
-------------


.. py:method:: set_mode(self, mode_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.set_mode

    Do not use this method, as it is deprecated. Use ModeComponentLinking on RadarModelMonostatic instead. Sets the current radar mode by name.

    :Parameters:

        **mode_name** : :obj:`~str`


    :Returns:

        :obj:`~None`









