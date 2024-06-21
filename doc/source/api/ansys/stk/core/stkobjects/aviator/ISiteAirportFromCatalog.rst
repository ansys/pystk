ISiteAirportFromCatalog
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ISiteAirportFromCatalog

   object
   
   Interface used to access the options for a airport From Catalog site type.

.. py:currentmodule:: ISiteAirportFromCatalog

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteAirportFromCatalog.get_catalog_airport`
              - Get the catalog airport.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteAirportFromCatalog.set_catalog_airport`
              - Set the catalog airport.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteAirportFromCatalog.get_as_site`
              - Get the site interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteAirportFromCatalog



Method detail
-------------

.. py:method:: get_catalog_airport(self) -> ICatalogAirport
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteAirportFromCatalog.get_catalog_airport

    Get the catalog airport.

    :Returns:

        :obj:`~ICatalogAirport`

.. py:method:: set_catalog_airport(self, pVal: ICatalogAirport) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteAirportFromCatalog.set_catalog_airport

    Set the catalog airport.

    :Parameters:

    **pVal** : :obj:`~ICatalogAirport`

    :Returns:

        :obj:`~None`

.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteAirportFromCatalog.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

