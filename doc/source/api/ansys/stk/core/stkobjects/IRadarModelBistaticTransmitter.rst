IRadarModelBistaticTransmitter
==============================

.. py:class:: IRadarModelBistaticTransmitter

   object
   
   Provide access to the properties and methods defining a bistatic transmitter radar model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_mode`
              - Set the current radar mode by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~supported_modes`
            * - :py:meth:`~mode`
            * - :py:meth:`~transmitter`
            * - :py:meth:`~bistatic_receivers`
            * - :py:meth:`~antenna_control`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModelBistaticTransmitter


Property detail
---------------

.. py:property:: supported_modes
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticTransmitter.supported_modes
    :type: list

    Gets an array of supported mode names.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticTransmitter.mode
    :type: IAgRadarModeBistaticTransmitter

    Gets the current radar mode.

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticTransmitter.transmitter
    :type: IAgRadarTransmitter

    Gets the radar transmitter.

.. py:property:: bistatic_receivers
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticTransmitter.bistatic_receivers
    :type: IAgObjectLinkCollection

    Gets the bistatic receiver collection.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticTransmitter.antenna_control
    :type: IAgAntennaControl

    Gets the radar antenna control.


Method detail
-------------


.. py:method:: set_mode(self, modeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticTransmitter.set_mode

    Set the current radar mode by name.

    :Parameters:

    **modeName** : :obj:`~str`

    :Returns:

        :obj:`~None`





