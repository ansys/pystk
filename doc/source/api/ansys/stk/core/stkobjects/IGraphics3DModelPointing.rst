IGraphics3DModelPointing
========================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DModelPointing

   object
   
   List of pointable model elements.

.. py:currentmodule:: IGraphics3DModelPointing

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelPointing.add_interval`
              - Add a new element to the collection using specified pointable model part, target name and the time period during which the pointable part targets the specified object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelPointing.remove_interval`
              - Remove a pointable element from the collection of pointable elements using specified pointable model part and target name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelPointing.load_intervals`
              - Add the intervals from the given file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelPointing.pointable_elements`
              - Get the list of pointable model elements.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DModelPointing


Property detail
---------------

.. py:property:: pointable_elements
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelPointing.pointable_elements
    :type: IGraphics3DPointableElementsCollection

    Get the list of pointable model elements.


Method detail
-------------


.. py:method:: add_interval(self, attachPointName: str, targetName: str, start: typing.Any, stop: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelPointing.add_interval

    Add a new element to the collection using specified pointable model part, target name and the time period during which the pointable part targets the specified object.

    :Parameters:

    **attachPointName** : :obj:`~str`
    **targetName** : :obj:`~str`
    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_interval(self, attachPointName: str, targetName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelPointing.remove_interval

    Remove a pointable element from the collection of pointable elements using specified pointable model part and target name.

    :Parameters:

    **attachPointName** : :obj:`~str`
    **targetName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_intervals(self, fileName: str, attachPoint: str) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelPointing.load_intervals

    Add the intervals from the given file.

    :Parameters:

    **fileName** : :obj:`~str`
    **attachPoint** : :obj:`~str`

    :Returns:

        :obj:`~None`

