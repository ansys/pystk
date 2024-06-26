IProjectionStream
=================

.. py:class:: ansys.stk.core.graphics.IProjectionStream

   object
   
   A projection that is updated dynamically at the specified update delta. The class can be used to stream projection data to projection clients, like projected raster overlay...

.. py:currentmodule:: IProjectionStream

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IProjectionStream.update`
              - When overridden in a derived class, updates the projection data associated with the projection stream at the specified time. When the Update method is called, the projection stream contains the current projection data...

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IProjectionStream.update_delta`
              - Gets or sets the update delta of the projection stream in seconds. The update delta defines the interval at which the Update method will be called...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IProjectionStream


Property detail
---------------

.. py:property:: update_delta
    :canonical: ansys.stk.core.graphics.IProjectionStream.update_delta
    :type: float

    Gets or sets the update delta of the projection stream in seconds. The update delta defines the interval at which the Update method will be called...


Method detail
-------------



.. py:method:: update(self, time: IDate, nextTime: IDate) -> bool
    :canonical: ansys.stk.core.graphics.IProjectionStream.update

    When overridden in a derived class, updates the projection data associated with the projection stream at the specified time. When the Update method is called, the projection stream contains the current projection data...

    :Parameters:

    **time** : :obj:`~IDate`
    **nextTime** : :obj:`~IDate`

    :Returns:

        :obj:`~bool`

