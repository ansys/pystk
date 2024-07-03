IRotorcraftModels
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.IRotorcraftModels

   object
   
   Interface for the User Rotorcraft Models in the Aviator Catalog.

.. py:currentmodule:: IRotorcraftModels

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IRotorcraftModels.get_rotorcraft`
              - Get the rotorcraft with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IRotorcraftModels.add_rotorcraft`
              - Create a new rotorcraft with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IRotorcraftModels.get_as_catalog_source`
              - Get the catalog source interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IRotorcraftModels



Method detail
-------------

.. py:method:: get_rotorcraft(self, name: str) -> IRotorcraftModel
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModels.get_rotorcraft

    Get the rotorcraft with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IRotorcraftModel`

.. py:method:: add_rotorcraft(self, name: str) -> IRotorcraftModel
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModels.add_rotorcraft

    Create a new rotorcraft with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IRotorcraftModel`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModels.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

