RadarModelBistaticTransmitter
=============================

.. py:class:: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a bistatic transmitter radar model.

.. py:currentmodule:: RadarModelBistaticTransmitter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.antenna_control`
              - Get the radar antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.bistatic_receivers`
              - Get the bistatic receiver collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.mode_component_linking`
              - Get the link/embed controller for managing the radar mode component.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.transmitter`
              - Get the radar transmitter.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModelBistaticTransmitter


Property detail
---------------

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.antenna_control
    :type: AntennaControl

    Get the radar antenna control.

.. py:property:: bistatic_receivers
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.bistatic_receivers
    :type: ObjectLinkCollection

    Get the bistatic receiver collection.

.. py:property:: mode_component_linking
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.mode_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar mode component.

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.RadarModelBistaticTransmitter.transmitter
    :type: RadarTransmitter

    Get the radar transmitter.


