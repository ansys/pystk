UserVTOLPointSource
===================

.. py:class:: ansys.stk.core.stkobjects.aviator.UserVTOLPointSource

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogSource`

   Class defining the user VTOL Point source in the Aviator catalog.

.. py:currentmodule:: UserVTOLPointSource

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserVTOLPointSource.get_user_vtol_point`
              - Get the user VTOL Point with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserVTOLPointSource.add_user_vtol_point`
              - Create a new user VTOL Point with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserVTOLPointSource.get_as_catalog_source`
              - Get the catalog source interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import UserVTOLPointSource



Method detail
-------------

.. py:method:: get_user_vtol_point(self, name: str) -> UserVTOLPoint
    :canonical: ansys.stk.core.stkobjects.aviator.UserVTOLPointSource.get_user_vtol_point

    Get the user VTOL Point with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~UserVTOLPoint`

.. py:method:: add_user_vtol_point(self, name: str) -> UserVTOLPoint
    :canonical: ansys.stk.core.stkobjects.aviator.UserVTOLPointSource.add_user_vtol_point

    Create a new user VTOL Point with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~UserVTOLPoint`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.UserVTOLPointSource.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

