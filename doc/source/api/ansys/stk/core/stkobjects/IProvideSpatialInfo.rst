IProvideSpatialInfo
===================

.. py:class:: ansys.stk.core.stkobjects.IProvideSpatialInfo

   object
   
   Provide methods for accessing spatial information for an object.

.. py:currentmodule:: IProvideSpatialInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IProvideSpatialInfo.get_spatial_info`
              - Return the spatial information for an object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IProvideSpatialInfo



Method detail
-------------

.. py:method:: get_spatial_info(self, recycle: bool) -> VehicleSpatialInfo
    :canonical: ansys.stk.core.stkobjects.IProvideSpatialInfo.get_spatial_info

    Return the spatial information for an object.

    :Parameters:

    **recycle** : :obj:`~bool`

    :Returns:

        :obj:`~VehicleSpatialInfo`

