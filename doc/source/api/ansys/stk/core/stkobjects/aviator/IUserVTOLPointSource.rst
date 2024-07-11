IUserVTOLPointSource
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IUserVTOLPointSource

   object
   
   Interface used to access the user VTOL Points in the Aviator catalog.

.. py:currentmodule:: IUserVTOLPointSource

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IUserVTOLPointSource.get_user_vtol_point`
              - Get the user VTOL Point with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IUserVTOLPointSource.add_user_vtol_point`
              - Create a new user VTOL Point with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IUserVTOLPointSource.get_as_catalog_source`
              - Get the catalog source interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IUserVTOLPointSource



Method detail
-------------

.. py:method:: get_user_vtol_point(self, name: str) -> IUserVTOLPoint
    :canonical: ansys.stk.core.stkobjects.aviator.IUserVTOLPointSource.get_user_vtol_point

    Get the user VTOL Point with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUserVTOLPoint`

.. py:method:: add_user_vtol_point(self, name: str) -> IUserVTOLPoint
    :canonical: ansys.stk.core.stkobjects.aviator.IUserVTOLPointSource.add_user_vtol_point

    Create a new user VTOL Point with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUserVTOLPoint`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.IUserVTOLPointSource.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

