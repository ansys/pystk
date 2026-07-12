RadarModelMonostatic
====================

.. py:class:: ansys.stk.core.stkobjects.RadarModelMonostatic

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a monostatic radar model.

.. py:currentmodule:: RadarModelMonostatic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.antenna_control`
              - Get the radar antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.clutter`
              - Get the radar clutter settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.jamming`
              - Get the radar jamming.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.mode_component_linking`
              - Get the link/embed controller for managing the radar mode component.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.receiver`
              - Get the radar receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMonostatic.transmitter`
              - Get the radar transmitter.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModelMonostatic


Property detail
---------------

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.antenna_control
    :type: AntennaControl

    Get the radar antenna control.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.clutter
    :type: RadarClutter

    Get the radar clutter settings.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.jamming
    :type: RadarJamming

    Get the radar jamming.

.. py:property:: mode_component_linking
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.mode_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar mode component.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.receiver
    :type: RadarReceiver

    Get the radar receiver.

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.RadarModelMonostatic.transmitter
    :type: RadarTransmitter

    Get the radar transmitter.


