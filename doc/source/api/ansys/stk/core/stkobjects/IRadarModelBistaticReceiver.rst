IRadarModelBistaticReceiver
===========================

.. py:class:: IRadarModelBistaticReceiver

   object
   
   Provide access to the properties and methods defining a bistatic receiver radar model.

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
            * - :py:meth:`~receiver`
            * - :py:meth:`~clutter_geometry`
            * - :py:meth:`~jamming`
            * - :py:meth:`~bistatic_transmitters`
            * - :py:meth:`~antenna_control`
            * - :py:meth:`~clutter`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModelBistaticReceiver


Property detail
---------------

.. py:property:: supported_modes
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.supported_modes
    :type: list

    Gets an array of supported mode names.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.mode
    :type: "IAgRadarModeBistaticReceiver"

    Gets the current radar mode.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.receiver
    :type: "IAgRadarReceiver"

    Gets the radar receiver.

.. py:property:: clutter_geometry
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.clutter_geometry
    :type: "IAgRadarClutterGeometry"

    This property is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.jamming
    :type: "IAgRadarJamming"

    Gets the radar jamming.

.. py:property:: bistatic_transmitters
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.bistatic_transmitters
    :type: "IAgObjectLinkCollection"

    Gets the bistatic transmitter collection.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.antenna_control
    :type: "IAgAntennaControl"

    Gets the radar antenna control.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.IRadarModelBistaticReceiver.clutter
    :type: "IAgRadarClutter"

    Gets the radar clutter settings.


Method detail
-------------


.. py:method:: set_mode(self, modeName:str) -> None

    Set the current radar mode by name.

    :Parameters:

    **modeName** : :obj:`~str`

    :Returns:

        :obj:`~None`








