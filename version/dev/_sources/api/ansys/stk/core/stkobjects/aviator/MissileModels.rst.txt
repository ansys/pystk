MissileModels
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.MissileModels

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogSource`

   Class defining the User Missile Models in the Aviator Catalog.

.. py:currentmodule:: MissileModels

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModels.add_missile`
              - Create a new missile with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModels.get_as_catalog_source`
              - Get the catalog source interface for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModels.get_missile`
              - Get the missile with the given name.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import MissileModels



Method detail
-------------

.. py:method:: add_missile(self, name: str) -> MissileModel
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModels.add_missile

    Create a new missile with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~MissileModel`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModels.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

.. py:method:: get_missile(self, name: str) -> MissileModel
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModels.get_missile

    Get the missile with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~MissileModel`

