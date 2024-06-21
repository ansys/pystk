ICatalogSource
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.ICatalogSource

   object
   
   Interface used to access options for a source in the Aviator Catalog. Examples of sources include User Aircraft Models, ARINC424runways, User Runways, etc.

.. py:currentmodule:: ICatalogSource

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogSource.contains`
              - Check whether the catalog source contains the catalog item with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogSource.remove_child`
              - Remove the child with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogSource.save`
              - Save the catalog item.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogSource.child_names`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ICatalogSource


Property detail
---------------

.. py:property:: child_names
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogSource.child_names
    :type: list

    Returns the child names.


Method detail
-------------


.. py:method:: contains(self, aircraftName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogSource.contains

    Check whether the catalog source contains the catalog item with the given name.

    :Parameters:

    **aircraftName** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove_child(self, childName: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogSource.remove_child

    Remove the child with the given name.

    :Parameters:

    **childName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: save(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogSource.save

    Save the catalog item.

    :Returns:

        :obj:`~None`

