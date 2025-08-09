RotorcraftModels
================

.. py:class:: ansys.stk.core.stkobjects.aviator.RotorcraftModels

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogSource`

   Class defining the User Rotorcraft Models in the Aviator Catalog.

.. py:currentmodule:: RotorcraftModels

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftModels.get_rotorcraft`
              - Get the rotorcraft with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftModels.add_rotorcraft`
              - Create a new rotorcraft with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftModels.get_as_catalog_source`
              - Get the catalog source interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import RotorcraftModels



Method detail
-------------

.. py:method:: get_rotorcraft(self, name: str) -> RotorcraftModel
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftModels.get_rotorcraft

    Get the rotorcraft with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~RotorcraftModel`

.. py:method:: add_rotorcraft(self, name: str) -> RotorcraftModel
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftModels.add_rotorcraft

    Create a new rotorcraft with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~RotorcraftModel`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftModels.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

