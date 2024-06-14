IVehicleAttitudeExternal
========================

.. py:class:: IVehicleAttitudeExternal

   object
   
   Interface for using an external attitude (.a) file.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reload`
              - Reload the file.
            * - :py:meth:`~load`
              - Load the file.
            * - :py:meth:`~disable`
              - Unload the file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enabled`
            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~filename`
            * - :py:meth:`~file_path`
            * - :py:meth:`~override`
            * - :py:meth:`~attitude_start_epoch`
            * - :py:meth:`~message_level`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudeExternal


Property detail
---------------

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExternal.enabled
    :type: bool

    Opt whether to use an external attitude file.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExternal.start_time
    :type: typing.Any

    Get the start time for the external attitude data. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExternal.stop_time
    :type: typing.Any

    Get the stop time for the external attitude data. Uses DateFormat Dimension.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExternal.filename
    :type: str

    External (.a) file name containing attitude data.

.. py:property:: file_path
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExternal.file_path
    :type: str

    External (.a) full file name and path containing attitude data.

.. py:property:: override
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExternal.override
    :type: bool

    Opt whether to override times contained in the external file.

.. py:property:: attitude_start_epoch
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExternal.attitude_start_epoch
    :type: "IAgCrdnEventSmartEpoch"

    If overriding the times contained in the external file, specifies the time of the first attitude point.

.. py:property:: message_level
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExternal.message_level
    :type: "STK_EXTERNAL_FILE_MESSAGE_LEVEL"

    Message level used to report messages during file loading.


Method detail
-------------





.. py:method:: reload(self) -> None

    Reload the file.

    :Returns:

        :obj:`~None`

.. py:method:: load(self, filename:str) -> None

    Load the file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: disable(self) -> None

    Unload the file.

    :Returns:

        :obj:`~None`







