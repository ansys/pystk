IDAFIFSource
============

.. py:class:: IDAFIFSource

   object
   
   Interface used to access the options for any DAFIF source in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_dafif_item`
              - Get the DAFIF item with the given name.
            * - :py:meth:`~get_as_catalog_source`
              - Get the catalog source interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~data_path`
            * - :py:meth:`~effective_date`
            * - :py:meth:`~expiration_date`
            * - :py:meth:`~spec_revision`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IDAFIFSource


Property detail
---------------

.. py:property:: data_path
    :canonical: ansys.stk.core.stkobjects.aviator.IDAFIFSource.data_path
    :type: str

    Gets or sets the DAFIF data path.

.. py:property:: effective_date
    :canonical: ansys.stk.core.stkobjects.aviator.IDAFIFSource.effective_date
    :type: str

    Get the effective date of the DAFIF catalog.

.. py:property:: expiration_date
    :canonical: ansys.stk.core.stkobjects.aviator.IDAFIFSource.expiration_date
    :type: str

    Get the expiration date of the DAFIF catalog.

.. py:property:: spec_revision
    :canonical: ansys.stk.core.stkobjects.aviator.IDAFIFSource.spec_revision
    :type: str

    Get the DAFIF edition.


Method detail
-------------

.. py:method:: get_dafif_item(self, name:str) -> "IDAFIFItem"

    Get the DAFIF item with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IDAFIFItem"`






.. py:method:: get_as_catalog_source(self) -> "ICatalogSource"

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~"ICatalogSource"`

