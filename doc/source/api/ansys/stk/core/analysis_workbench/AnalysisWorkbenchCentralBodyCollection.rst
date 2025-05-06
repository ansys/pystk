AnalysisWorkbenchCentralBodyCollection
======================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection

   A collection of central body names.

.. py:currentmodule:: AnalysisWorkbenchCentralBodyCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection.item`
              - Return a central body name at a specified index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection.add`
              - Add a central body to the collection of central bodies. True indicates success.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection.remove`
              - Remove a central body with the specified name from the collection of the central bodies.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection.count`
              - Return a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchCentralBodyCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection.count
    :type: int

    Return a number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection.item

    Return a central body name at a specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: add(self, central_body_name: str) -> bool
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection.add

    Add a central body to the collection of central bodies. True indicates success.

    :Parameters:

    **central_body_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, central_body_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection.remove

    Remove a central body with the specified name from the collection of the central bodies.

    :Parameters:

    **central_body_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

