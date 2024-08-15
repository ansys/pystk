PickInfoData
============

.. py:class:: ansys.stk.core.stkx.PickInfoData

   Single mouse pick result.

.. py:currentmodule:: PickInfoData

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.PickInfoData.obj_path`
              - Path of the STK object picked if any (or empty string).
            * - :py:attr:`~ansys.stk.core.stkx.PickInfoData.lat`
              - Latitude of point clicked (if available).
            * - :py:attr:`~ansys.stk.core.stkx.PickInfoData.lon`
              - Longitude of point clicked (if available).
            * - :py:attr:`~ansys.stk.core.stkx.PickInfoData.altitude`
              - Altitude of point clicked (if available).
            * - :py:attr:`~ansys.stk.core.stkx.PickInfoData.is_obj_path_valid`
              - Indicate if the ObjPath property is valid.
            * - :py:attr:`~ansys.stk.core.stkx.PickInfoData.is_lat_lon_altitude_valid`
              - Indicate if the Lat/Lon/Alt properties are valid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import PickInfoData


Property detail
---------------

.. py:property:: obj_path
    :canonical: ansys.stk.core.stkx.PickInfoData.obj_path
    :type: str

    Path of the STK object picked if any (or empty string).

.. py:property:: lat
    :canonical: ansys.stk.core.stkx.PickInfoData.lat
    :type: float

    Latitude of point clicked (if available).

.. py:property:: lon
    :canonical: ansys.stk.core.stkx.PickInfoData.lon
    :type: float

    Longitude of point clicked (if available).

.. py:property:: altitude
    :canonical: ansys.stk.core.stkx.PickInfoData.altitude
    :type: float

    Altitude of point clicked (if available).

.. py:property:: is_obj_path_valid
    :canonical: ansys.stk.core.stkx.PickInfoData.is_obj_path_valid
    :type: bool

    Indicate if the ObjPath property is valid.

.. py:property:: is_lat_lon_altitude_valid
    :canonical: ansys.stk.core.stkx.PickInfoData.is_lat_lon_altitude_valid
    :type: bool

    Indicate if the Lat/Lon/Alt properties are valid.


