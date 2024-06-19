IPerformanceModelOptions
========================

.. py:class:: IPerformanceModelOptions

   object
   
   Interface used to change the active performance model in a phase for a given model type.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~link_to_catalog`
              - Link to the performance model in the catalog with the given name.
            * - :py:meth:`~copy_from_catalog`
              - Create a copy of the performance model in the catalog with the given name.
            * - :py:meth:`~create_new`
              - Create a new performance model of the given type.
            * - :py:meth:`~rename`
              - Rename the performance model.
            * - :py:meth:`~delete`
              - Delete the performance model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~is_linked_to_catalog`
            * - :py:meth:`~properties`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IPerformanceModelOptions


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.IPerformanceModelOptions.name
    :type: str

    Get the name of the performance model.

.. py:property:: is_linked_to_catalog
    :canonical: ansys.stk.core.stkobjects.aviator.IPerformanceModelOptions.is_linked_to_catalog
    :type: bool

    Get whether the performance model is linked to the catalog.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.aviator.IPerformanceModelOptions.properties
    :type: IAgAvtrPerformanceModel

    Get the properties of the performance model.


Method detail
-------------

.. py:method:: link_to_catalog(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPerformanceModelOptions.link_to_catalog

    Link to the performance model in the catalog with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: copy_from_catalog(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPerformanceModelOptions.copy_from_catalog

    Create a copy of the performance model in the catalog with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: create_new(self, type: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPerformanceModelOptions.create_new

    Create a new performance model of the given type.

    :Parameters:

    **type** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: rename(self, type: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPerformanceModelOptions.rename

    Rename the performance model.

    :Parameters:

    **type** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: delete(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPerformanceModelOptions.delete

    Delete the performance model.

    :Returns:

        :obj:`~None`




