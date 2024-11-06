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
              - Set the current radar mode by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.supported_modes`
              - Gets an array of supported mode names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.mode`
              - Gets the current radar mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.transmitter`
              - Gets the radar transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.bistatic_receivers`
              - Gets the bistatic receiver collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.antenna_control`
              - Gets the radar antenna control.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModelBistaticTransmitter


Property detail
---------------

.. py:property:: supported_modes
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.supported_modes
    :type: list

    Gets an array of supported mode names.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.mode
    :type: IRadarModeBistaticTransmitter

    Gets the current radar mode.

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.transmitter
    :type: RadarTransmitter

    Gets the radar transmitter.

.. py:property:: bistatic_receivers
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.bistatic_receivers
    :type: ObjectLinkCollection

    Gets the bistatic receiver collection.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.antenna_control
    :type: AntennaControl

    Gets the radar antenna control.


Method detail
-------------


.. py:method:: set_mode(self, mode_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.set_mode

    Set the current radar mode by name.

    :Parameters:

    **mode_name** : :obj:`~str`

    :Returns:

        :obj:`~None`





