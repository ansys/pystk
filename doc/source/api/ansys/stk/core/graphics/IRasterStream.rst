IRasterStream
=============

.. py:class:: ansys.stk.core.graphics.IRasterStream

   A raster, the data of which, is updated dynamically at the specified update delta. The class can be used to stream video and other dynamic raster data to textures and other raster clients...

.. py:currentmodule:: IRasterStream

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IRasterStream.update`
              - When overridden in a derived class, updates the raster data associated with the raster stream at the specified time...

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IRasterStream.update_delta`
              - Gets or sets the update delta of the raster stream in seconds. The update delta defines the interval at which the Update method will be called. The default update delta is 0, which will call the Update method every time the scene manager time changes...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IRasterStream


Property detail
---------------

.. py:property:: update_delta
    :canonical: ansys.stk.core.graphics.IRasterStream.update_delta
    :type: float

    Gets or sets the update delta of the raster stream in seconds. The update delta defines the interval at which the Update method will be called. The default update delta is 0, which will call the Update method every time the scene manager time changes...


Method detail
-------------



.. py:method:: update(self, time: IDate, nextTime: IDate) -> bool
    :canonical: ansys.stk.core.graphics.IRasterStream.update

    When overridden in a derived class, updates the raster data associated with the raster stream at the specified time...

    :Parameters:

    **time** : :obj:`~IDate`
    **nextTime** : :obj:`~IDate`

    :Returns:

        :obj:`~bool`

