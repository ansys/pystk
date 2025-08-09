RadarModelBistaticTransmitter
=============================

.. py:class:: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a bistatic transmitter radar model.

.. py:currentmodule:: RadarModelBistaticTransmitter

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.set_mode`
              - Do not use this method, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticTransmitter instead. Sets the current radar mode by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.supported_modes`
              - Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticTransmitter instead. Gets an array of supported mode names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.mode`
              - Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticTransmitter instead. Gets the current radar mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.transmitter`
              - Get the radar transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.bistatic_receivers`
              - Get the bistatic receiver collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.antenna_control`
              - Get the radar antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.mode_component_linking`
              - Get the link/embed controller for managing the radar mode component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModelBistaticTransmitter


Property detail
---------------

.. py:property:: supported_modes
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.supported_modes
    :type: list

    Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticTransmitter instead. Gets an array of supported mode names.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.mode
    :type: IRadarModeBistaticTransmitter

    Do not use this property, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticTransmitter instead. Gets the current radar mode.

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.transmitter
    :type: RadarTransmitter

    Get the radar transmitter.

.. py:property:: bistatic_receivers
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.bistatic_receivers
    :type: ObjectLinkCollection

    Get the bistatic receiver collection.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.antenna_control
    :type: AntennaControl

    Get the radar antenna control.

.. py:property:: mode_component_linking
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.mode_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar mode component.


Method detail
-------------


.. py:method:: set_mode(self, mode_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.set_mode

    Do not use this method, as it is deprecated. Use ModeComponentLinking on RadarModelBistaticTransmitter instead. Sets the current radar mode by name.

    :Parameters:

        **mode_name** : :obj:`~str`


    :Returns:

        :obj:`~None`






