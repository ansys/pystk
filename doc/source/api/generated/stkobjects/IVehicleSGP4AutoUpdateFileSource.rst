IVehicleSGP4AutoUpdateFileSource
================================

.. py:class:: IVehicleSGP4AutoUpdateFileSource

   object
   
   Interface to configure the SGP4 automatic updates using file(s).

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~preview`
              - Preview the elements.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filename`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSGP4AutoUpdateFileSource


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4AutoUpdateFileSource.filename
    :type: str

    Gets or sets the name of the source file containing GP data (either TLEs or CCSDS OMM content).


Method detail
-------------



.. py:method:: preview(self) -> list

    Preview the elements.

    :Returns:

        :obj:`~list`

