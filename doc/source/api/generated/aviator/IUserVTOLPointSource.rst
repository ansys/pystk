IUserVTOLPointSource
====================

.. py:class:: IUserVTOLPointSource

   object
   
   Interface used to access the user VTOL Points in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_user_vtol_point`
              - Get the user VTOL Point with the given name.
            * - :py:meth:`~add_user_vtol_point`
              - Create a new user VTOL Point with the given name.
            * - :py:meth:`~get_as_catalog_source`
              - Get the catalog source interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IUserVTOLPointSource



Method detail
-------------

.. py:method:: get_user_vtol_point(self, name:str) -> "IUserVTOLPoint"

    Get the user VTOL Point with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IUserVTOLPoint"`

.. py:method:: add_user_vtol_point(self, name:str) -> "IUserVTOLPoint"

    Create a new user VTOL Point with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IUserVTOLPoint"`

.. py:method:: get_as_catalog_source(self) -> "ICatalogSource"

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~"ICatalogSource"`

