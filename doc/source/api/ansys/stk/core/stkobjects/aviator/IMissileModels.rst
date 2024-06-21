IMissileModels
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.IMissileModels

   object
   
   Interface for the User Missile Models in the Aviator Catalog.

.. py:currentmodule:: IMissileModels

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModels.get_missile`
              - Get the missile with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModels.add_missile`
              - Create a new missile with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModels.get_as_catalog_source`
              - Get the catalog source interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileModels



Method detail
-------------

.. py:method:: get_missile(self, name: str) -> IMissileModel
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModels.get_missile

    Get the missile with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IMissileModel`

.. py:method:: add_missile(self, name: str) -> IMissileModel
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModels.add_missile

    Create a new missile with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IMissileModel`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModels.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

