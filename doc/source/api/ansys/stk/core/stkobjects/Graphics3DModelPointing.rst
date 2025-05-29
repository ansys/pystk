Graphics3DModelPointing
=======================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DModelPointing

   List of pointable model elements.

.. py:currentmodule:: Graphics3DModelPointing

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelPointing.add_interval`
              - Add a new element to the collection using specified pointable model part, target name and the time period during which the pointable part targets the specified object.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelPointing.remove_interval`
              - Remove a pointable element from the collection of pointable elements using specified pointable model part and target name.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelPointing.load_intervals`
              - Add the intervals from the given file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelPointing.pointable_elements`
              - Get the list of pointable model elements.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DModelPointing


Property detail
---------------

.. py:property:: pointable_elements
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelPointing.pointable_elements
    :type: Graphics3DPointableElementsCollection

    Get the list of pointable model elements.


Method detail
-------------


.. py:method:: add_interval(self, attach_point_name: str, target_name: str, start: typing.Any, stop: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelPointing.add_interval

    Add a new element to the collection using specified pointable model part, target name and the time period during which the pointable part targets the specified object.

    :Parameters:

        **attach_point_name** : :obj:`~str`

        **target_name** : :obj:`~str`

        **start** : :obj:`~typing.Any`

        **stop** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: remove_interval(self, attach_point_name: str, target_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelPointing.remove_interval

    Remove a pointable element from the collection of pointable elements using specified pointable model part and target name.

    :Parameters:

        **attach_point_name** : :obj:`~str`

        **target_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: load_intervals(self, file_name: str, attach_point: str) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelPointing.load_intervals

    Add the intervals from the given file.

    :Parameters:

        **file_name** : :obj:`~str`

        **attach_point** : :obj:`~str`


    :Returns:

        :obj:`~None`

