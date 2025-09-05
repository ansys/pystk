RadarModelBistaticReceiver
==========================

.. py:class:: ansys.stk.core.stkobjects.RadarModelBistaticReceiver

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a bistatic receiver radar model.

.. py:currentmodule:: RadarModelBistaticReceiver

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.set_mode`
              - Do not use this method, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticReceiver instead. Sets the current radar mode by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.antenna_control`
              - Get the radar antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.bistatic_transmitters`
              - Get the bistatic transmitter collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.clutter`
              - Get the radar clutter settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.clutter_geometry`
              - Do not use this property, as it is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.jamming`
              - Get the radar jamming.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.mode`
              - Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticReceiver instead. Gets the current radar mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.mode_component_linking`
              - Get the link/embed controller for managing the radar mode component.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.receiver`
              - Get the radar receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.supported_modes`
              - Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticReceiver instead. Gets an array of supported mode names.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModelBistaticReceiver


Property detail
---------------

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.antenna_control
    :type: AntennaControl

    Get the radar antenna control.

.. py:property:: bistatic_transmitters
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.bistatic_transmitters
    :type: ObjectLinkCollection

    Get the bistatic transmitter collection.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.clutter
    :type: RadarClutter

    Get the radar clutter settings.

.. py:property:: clutter_geometry
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.clutter_geometry
    :type: RadarClutterGeometry

    Do not use this property, as it is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.jamming
    :type: RadarJamming

    Get the radar jamming.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.mode
    :type: IRadarModeBistaticReceiver

    Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticReceiver instead. Gets the current radar mode.

.. py:property:: mode_component_linking
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.mode_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar mode component.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.receiver
    :type: RadarReceiver

    Get the radar receiver.

.. py:property:: supported_modes
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.supported_modes
    :type: list

    Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticReceiver instead. Gets an array of supported mode names.


Method detail
-------------









.. py:method:: set_mode(self, mode_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.set_mode

    Do not use this method, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticReceiver instead. Sets the current radar mode by name.

    :Parameters:

        **mode_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


