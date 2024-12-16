VehicleAttitudeExternal
=======================

.. py:class:: ansys.stk.core.stkobjects.VehicleAttitudeExternal

   External attitude (.a) file.

.. py:currentmodule:: VehicleAttitudeExternal

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.reload`
              - Reload the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.load`
              - Load the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.disable`
              - Unload the file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.enabled`
              - Opt whether to use an external attitude file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.start_time`
              - Get the start time for the external attitude data. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.stop_time`
              - Get the stop time for the external attitude data. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.filename`
              - External (.a) file name containing attitude data.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.file_path`
              - External (.a) full file name and path containing attitude data.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.override`
              - Opt whether to override times contained in the external file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.attitude_start_epoch`
              - If overriding the times contained in the external file, specifies the time of the first attitude point.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal.message_level`
              - Message level used to report messages during file loading.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleAttitudeExternal


Property detail
---------------

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.enabled
    :type: bool

    Opt whether to use an external attitude file.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.start_time
    :type: typing.Any

    Get the start time for the external attitude data. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.stop_time
    :type: typing.Any

    Get the stop time for the external attitude data. Uses DateFormat Dimension.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.filename
    :type: str

    External (.a) file name containing attitude data.

.. py:property:: file_path
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.file_path
    :type: str

    External (.a) full file name and path containing attitude data.

.. py:property:: override
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.override
    :type: bool

    Opt whether to override times contained in the external file.

.. py:property:: attitude_start_epoch
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.attitude_start_epoch
    :type: ITimeToolInstantSmartEpoch

    If overriding the times contained in the external file, specifies the time of the first attitude point.

.. py:property:: message_level
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.message_level
    :type: ExternalFileMessageLevelType

    Message level used to report messages during file loading.


Method detail
-------------





.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.reload

    Reload the file.

    :Returns:

        :obj:`~None`

.. py:method:: load(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.load

    Load the file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: disable(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExternal.disable

    Unload the file.

    :Returns:

        :obj:`~None`







