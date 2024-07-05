IVehicleGPSAutoUpdateFileSource
===============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateFileSource

   object
   
   Interface to configure the GPS automatic updates using almanac file(s).

.. py:currentmodule:: IVehicleGPSAutoUpdateFileSource

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateFileSource.preview`
              - Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateFileSource.filename`
              - Gets or sets the name of the source file.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGPSAutoUpdateFileSource


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateFileSource.filename
    :type: str

    Gets or sets the name of the source file.


Method detail
-------------



.. py:method:: preview(self) -> IVehicleGPSElementCollection
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateFileSource.preview

    Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.

    :Returns:

        :obj:`~IVehicleGPSElementCollection`

