PerformanceModelOptions
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions

   Bases: 

   Class defining the options for the active performance model in a phase.

.. py:currentmodule:: PerformanceModelOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.link_to_catalog`
              - Link to the performance model in the catalog with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.copy_from_catalog`
              - Create a copy of the performance model in the catalog with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.create_new`
              - Create a new performance model of the given type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.rename`
              - Rename the performance model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.delete`
              - Delete the performance model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.name`
              - Get the name of the performance model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.is_linked_to_catalog`
              - Get whether the performance model is linked to the catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.properties`
              - Get the properties of the performance model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import PerformanceModelOptions


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.name
    :type: str

    Get the name of the performance model.

.. py:property:: is_linked_to_catalog
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.is_linked_to_catalog
    :type: bool

    Get whether the performance model is linked to the catalog.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.properties
    :type: IPerformanceModel

    Get the properties of the performance model.


Method detail
-------------

.. py:method:: link_to_catalog(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.link_to_catalog

    Link to the performance model in the catalog with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: copy_from_catalog(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.copy_from_catalog

    Create a copy of the performance model in the catalog with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: create_new(self, type: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.create_new

    Create a new performance model of the given type.

    :Parameters:

    **type** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: rename(self, type: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.rename

    Rename the performance model.

    :Parameters:

    **type** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: delete(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.delete

    Delete the performance model.

    :Returns:

        :obj:`~None`




