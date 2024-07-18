VehicleGPSAutoUpdateFileSource
==============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGPSAutoUpdateFileSource

   Bases: 

   GPS automatic updates using almanac file(s).

.. py:currentmodule:: VehicleGPSAutoUpdateFileSource

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdateFileSource.preview`
              - Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdateFileSource.filename`
              - Gets or sets the name of the source file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGPSAutoUpdateFileSource


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.VehicleGPSAutoUpdateFileSource.filename
    :type: str

    Gets or sets the name of the source file.


Method detail
-------------



.. py:method:: preview(self) -> VehicleGPSElementCollection
    :canonical: ansys.stk.core.stkobjects.VehicleGPSAutoUpdateFileSource.preview

    Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.

    :Returns:

        :obj:`~VehicleGPSElementCollection`

