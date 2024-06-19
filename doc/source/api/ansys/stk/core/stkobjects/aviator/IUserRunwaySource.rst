IUserRunwaySource
=================

.. py:class:: IUserRunwaySource

   object
   
   Interface used to access the user runways in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_user_runway`
              - Get the user runway with the given name.
            * - :py:meth:`~add_user_runway`
              - Create a new user runway with the given name.
            * - :py:meth:`~get_as_catalog_source`
              - Get the catalog source interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IUserRunwaySource



Method detail
-------------

.. py:method:: get_user_runway(self, name: str) -> IUserRunway
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunwaySource.get_user_runway

    Get the user runway with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUserRunway`

.. py:method:: add_user_runway(self, name: str) -> IUserRunway
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunwaySource.add_user_runway

    Create a new user runway with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUserRunway`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunwaySource.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

