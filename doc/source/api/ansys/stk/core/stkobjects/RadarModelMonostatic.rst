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
              - Do not use this method, as it is deprecated. Use ModeComponentLinking on IAgRadarModelMonostatic instead. Sets the current radar mode by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.supported_modes`
              - This property is deprecated. Use ModeComponentLinking on IAgRadarModelMonostatic instead. Gets an array of supported mode names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.mode`
              - This property is deprecated. Use ModeComponentLinking on IAgRadarModelMonostatic instead. Gets the current radar mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.transmitter`
              - Gets the radar transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.receiver`
              - Gets the radar receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.clutter_geometry`
              - This property is deprecated. Use the Clutter property instead. Gets the radar clutter geometry.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.jamming`
              - Gets the radar jamming.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.antenna_control`
              - Gets the radar antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.clutter`
              - Gets the radar clutter settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.mode_component_linking`
              - Gets the link/embed controller for managing the radar mode component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModelMonostatic


Property detail
---------------

.. py:property:: supported_modes
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.supported_modes
    :type: list

    This property is deprecated. Use ModeComponentLinking on IAgRadarModelMonostatic instead. Gets an array of supported mode names.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.mode
    :type: IRadarModeMonostatic

    This property is deprecated. Use ModeComponentLinking on IAgRadarModelMonostatic instead. Gets the current radar mode.

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.transmitter
    :type: RadarTransmitter

    Gets the radar transmitter.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.receiver
    :type: RadarReceiver

    Gets the radar receiver.

.. py:property:: clutter_geometry
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.clutter_geometry
    :type: RadarClutterGeometry

    This property is deprecated. Use the Clutter property instead. Gets the radar clutter geometry.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.jamming
    :type: RadarJamming

    Gets the radar jamming.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.antenna_control
    :type: AntennaControl

    Gets the radar antenna control.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.clutter
    :type: RadarClutter

    Gets the radar clutter settings.

.. py:property:: mode_component_linking
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.mode_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the radar mode component.


Method detail
-------------


.. py:method:: set_mode(self, mode_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.set_mode

    Do not use this method, as it is deprecated. Use ModeComponentLinking on IAgRadarModelMonostatic instead. Sets the current radar mode by name.

    :Parameters:

    **mode_name** : :obj:`~str`

    :Returns:

        :obj:`~None`









