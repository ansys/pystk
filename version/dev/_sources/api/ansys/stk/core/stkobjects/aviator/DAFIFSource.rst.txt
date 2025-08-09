DAFIFSource
===========

.. py:class:: ansys.stk.core.stkobjects.aviator.DAFIFSource

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogSource`

   Class defining an DAFIF source in the Aviator catalog.

.. py:currentmodule:: DAFIFSource

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.DAFIFSource.get_as_catalog_source`
              - Get the catalog source interface for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.DAFIFSource.get_dafif_item`
              - Get the DAFIF item with the given name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.DAFIFSource.data_path`
              - Get or set the DAFIF data path.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.DAFIFSource.effective_date`
              - Get the effective date of the DAFIF catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.DAFIFSource.expiration_date`
              - Get the expiration date of the DAFIF catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.DAFIFSource.spec_revision`
              - Get the DAFIF edition.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import DAFIFSource


Property detail
---------------

.. py:property:: data_path
    :canonical: ansys.stk.core.stkobjects.aviator.DAFIFSource.data_path
    :type: str

    Get or set the DAFIF data path.

.. py:property:: effective_date
    :canonical: ansys.stk.core.stkobjects.aviator.DAFIFSource.effective_date
    :type: str

    Get the effective date of the DAFIF catalog.

.. py:property:: expiration_date
    :canonical: ansys.stk.core.stkobjects.aviator.DAFIFSource.expiration_date
    :type: str

    Get the expiration date of the DAFIF catalog.

.. py:property:: spec_revision
    :canonical: ansys.stk.core.stkobjects.aviator.DAFIFSource.spec_revision
    :type: str

    Get the DAFIF edition.


Method detail
-------------





.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.DAFIFSource.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

.. py:method:: get_dafif_item(self, name: str) -> IDAFIFItem
    :canonical: ansys.stk.core.stkobjects.aviator.DAFIFSource.get_dafif_item

    Get the DAFIF item with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IDAFIFItem`


