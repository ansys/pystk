ISiteRunwayFromCatalog
======================

.. py:class:: ISiteRunwayFromCatalog

   object
   
   Interface used to access the options for a Runway From Catalog site type.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_catalog_runway`
              - Get the catalog runway.
            * - :py:meth:`~set_catalog_runway`
              - Set the catalog runway.
            * - :py:meth:`~get_as_site`
              - Get the site interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteRunwayFromCatalog



Method detail
-------------

.. py:method:: get_catalog_runway(self) -> "ICatalogRunway"

    Get the catalog runway.

    :Returns:

        :obj:`~"ICatalogRunway"`

.. py:method:: set_catalog_runway(self, pVal:"ICatalogRunway") -> None

    Set the catalog runway.

    :Parameters:

    **pVal** : :obj:`~"ICatalogRunway"`

    :Returns:

        :obj:`~None`

.. py:method:: get_as_site(self) -> "ISite"

    Get the site interface.

    :Returns:

        :obj:`~"ISite"`

