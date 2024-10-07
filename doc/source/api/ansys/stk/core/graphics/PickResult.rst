PickResult
==========

.. py:class:: ansys.stk.core.graphics.PickResult

   A single result from Pick.

.. py:currentmodule:: PickResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PickResult.objects`
              - Gets a collection of objects that were on the pick stack for the picked object.
            * - :py:attr:`~ansys.stk.core.graphics.PickResult.depth`
              - Gets the depth of the picked location in the 3D scene.
            * - :py:attr:`~ansys.stk.core.graphics.PickResult.position`
              - Gets the position of the picked location in the central body's fixed reference frame. The array contains the components of the position arranged in the order x, y, z.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PickResult


Property detail
---------------

.. py:property:: objects
    :canonical: ansys.stk.core.graphics.PickResult.objects
    :type: ObjectCollection

    Gets a collection of objects that were on the pick stack for the picked object.

.. py:property:: depth
    :canonical: ansys.stk.core.graphics.PickResult.depth
    :type: float

    Gets the depth of the picked location in the 3D scene.

.. py:property:: position
    :canonical: ansys.stk.core.graphics.PickResult.position
    :type: list

    Gets the position of the picked location in the central body's fixed reference frame. The array contains the components of the position arranged in the order x, y, z.


