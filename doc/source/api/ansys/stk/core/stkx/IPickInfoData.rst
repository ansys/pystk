IPickInfoData
=============

.. py:class:: ansys.stk.core.stkx.IPickInfoData

   object
   
   Mouse pick details.

.. py:currentmodule:: IPickInfoData

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IPickInfoData.obj_path`
            * - :py:attr:`~ansys.stk.core.stkx.IPickInfoData.lat`
            * - :py:attr:`~ansys.stk.core.stkx.IPickInfoData.lon`
            * - :py:attr:`~ansys.stk.core.stkx.IPickInfoData.altitude`
            * - :py:attr:`~ansys.stk.core.stkx.IPickInfoData.is_obj_path_valid`
            * - :py:attr:`~ansys.stk.core.stkx.IPickInfoData.is_lat_lon_altitude_valid`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IPickInfoData


Property detail
---------------

.. py:property:: obj_path
    :canonical: ansys.stk.core.stkx.IPickInfoData.obj_path
    :type: str

    Path of the STK object picked if any (or empty string).

.. py:property:: lat
    :canonical: ansys.stk.core.stkx.IPickInfoData.lat
    :type: float

    Latitude of point clicked (if available).

.. py:property:: lon
    :canonical: ansys.stk.core.stkx.IPickInfoData.lon
    :type: float

    Longitude of point clicked (if available).

.. py:property:: altitude
    :canonical: ansys.stk.core.stkx.IPickInfoData.altitude
    :type: float

    Altitude of point clicked (if available).

.. py:property:: is_obj_path_valid
    :canonical: ansys.stk.core.stkx.IPickInfoData.is_obj_path_valid
    :type: bool

    Indicate if the ObjPath property is valid.

.. py:property:: is_lat_lon_altitude_valid
    :canonical: ansys.stk.core.stkx.IPickInfoData.is_lat_lon_altitude_valid
    :type: bool

    Indicate if the Lat/Lon/Alt properties are valid.


