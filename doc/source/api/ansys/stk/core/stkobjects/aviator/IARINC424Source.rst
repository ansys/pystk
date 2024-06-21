IARINC424Source
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.IARINC424Source

   object
   
   Interface used to access the options for any ARINC424 source in the Aviator catalog.

.. py:currentmodule:: IARINC424Source

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IARINC424Source.get_arinc424_item`
              - Get the ARINC-424 item with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IARINC424Source.get_as_catalog_source`
              - Get the catalog source interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IARINC424Source.use_master_data_file`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IARINC424Source.master_data_filepath`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IARINC424Source.override_data_filepath`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IARINC424Source


Property detail
---------------

.. py:property:: use_master_data_file
    :canonical: ansys.stk.core.stkobjects.aviator.IARINC424Source.use_master_data_file
    :type: bool

    Opt whether to use the master data file.

.. py:property:: master_data_filepath
    :canonical: ansys.stk.core.stkobjects.aviator.IARINC424Source.master_data_filepath
    :type: str

    Gets or sets the master data file path.

.. py:property:: override_data_filepath
    :canonical: ansys.stk.core.stkobjects.aviator.IARINC424Source.override_data_filepath
    :type: str

    Gets or sets the file path to the data overriding the mader data file.


Method detail
-------------

.. py:method:: get_arinc424_item(self, name: str) -> IARINC424Item
    :canonical: ansys.stk.core.stkobjects.aviator.IARINC424Source.get_arinc424_item

    Get the ARINC-424 item with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IARINC424Item`







.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.IARINC424Source.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

