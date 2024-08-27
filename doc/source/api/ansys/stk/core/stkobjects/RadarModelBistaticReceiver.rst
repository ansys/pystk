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
              - Set the current radar mode by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.supported_modes`
              - Gets an array of supported mode names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.mode`
              - Gets the current radar mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.receiver`
              - Gets the radar receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.clutter_geometry`
              - This property is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.jamming`
              - Gets the radar jamming.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.bistatic_transmitters`
              - Gets the bistatic transmitter collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.antenna_control`
              - Gets the radar antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver.clutter`
              - Gets the radar clutter settings.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModelBistaticReceiver


Property detail
---------------

.. py:property:: supported_modes
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.supported_modes
    :type: list

    Gets an array of supported mode names.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.mode
    :type: IRadarModeBistaticReceiver

    Gets the current radar mode.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.receiver
    :type: RadarReceiver

    Gets the radar receiver.

.. py:property:: clutter_geometry
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.clutter_geometry
    :type: RadarClutterGeometry

    This property is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.jamming
    :type: RadarJamming

    Gets the radar jamming.

.. py:property:: bistatic_transmitters
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.bistatic_transmitters
    :type: ObjectLinkCollection

    Gets the bistatic transmitter collection.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.antenna_control
    :type: AntennaControl

    Gets the radar antenna control.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.clutter
    :type: RadarClutter

    Gets the radar clutter settings.


Method detail
-------------


.. py:method:: set_mode(self, modeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticReceiver.set_mode

    Set the current radar mode by name.

    :Parameters:

    **modeName** : :obj:`~str`

    :Returns:

        :obj:`~None`








