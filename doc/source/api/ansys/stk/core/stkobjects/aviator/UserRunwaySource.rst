UserRunwaySource
================

.. py:class:: ansys.stk.core.stkobjects.aviator.UserRunwaySource

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogSource`

   Class defining the user runways in the Aviator catalog.

.. py:currentmodule:: UserRunwaySource

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunwaySource.get_user_runway`
              - Get the user runway with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunwaySource.add_user_runway`
              - Create a new user runway with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunwaySource.get_as_catalog_source`
              - Get the catalog source interface for this object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import UserRunwaySource



Method detail
-------------

.. py:method:: get_user_runway(self, name: str) -> UserRunway
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunwaySource.get_user_runway

    Get the user runway with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~UserRunway`

.. py:method:: add_user_runway(self, name: str) -> UserRunway
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunwaySource.add_user_runway

    Create a new user runway with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~UserRunway`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunwaySource.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

