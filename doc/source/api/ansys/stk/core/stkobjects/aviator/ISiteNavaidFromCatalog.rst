ISiteNavaidFromCatalog
======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ISiteNavaidFromCatalog

   object
   
   Interface used to access the options for a navaid From Catalog site type.

.. py:currentmodule:: ISiteNavaidFromCatalog

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteNavaidFromCatalog.get_catalog_navaid`
              - Get the catalog navaid.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteNavaidFromCatalog.set_catalog_navaid`
              - Set the catalog navaid.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteNavaidFromCatalog.get_as_site`
              - Get the site interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteNavaidFromCatalog



Method detail
-------------

.. py:method:: get_catalog_navaid(self) -> ICatalogNavaid
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteNavaidFromCatalog.get_catalog_navaid

    Get the catalog navaid.

    :Returns:

        :obj:`~ICatalogNavaid`

.. py:method:: set_catalog_navaid(self, pVal: ICatalogNavaid) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteNavaidFromCatalog.set_catalog_navaid

    Set the catalog navaid.

    :Parameters:

    **pVal** : :obj:`~ICatalogNavaid`

    :Returns:

        :obj:`~None`

.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteNavaidFromCatalog.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

