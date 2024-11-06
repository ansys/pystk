AnalysisWorkbenchCentralBodyCollection
======================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection

   A collection of central body names.

.. py:currentmodule:: AnalysisWorkbenchCentralBodyCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection.item`
              - Return a central body name at a specified index.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection.add`
              - Add a central body to the collection of central bodies. True indicates success.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection.remove`
              - Remove a central body with the specified name from the collection of the central bodies.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection.count`
              - Returns a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection._NewEnum`
              - Returns a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchCentralBodyCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection.item

    Return a central body name at a specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: add(self, central_body_name: str) -> bool
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection.add

    Add a central body to the collection of central bodies. True indicates success.

    :Parameters:

    **central_body_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, central_body_name: str) -> None
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection.remove

    Remove a central body with the specified name from the collection of the central bodies.

    :Parameters:

    **central_body_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

