SceneDisplayConditionFactory
============================

.. py:class:: ansys.stk.core.graphics.SceneDisplayConditionFactory

   Bases: 

   A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

.. py:currentmodule:: SceneDisplayConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SceneDisplayConditionFactory.initialize`
              - Initialize a default scene display condition. When this display condition is assigned to an object, such as a primitive, the object can be restricted to only render in certain scenes. Call set display in scene or display only in scene to limit the scenes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SceneDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> SceneDisplayCondition
    :canonical: ansys.stk.core.graphics.SceneDisplayConditionFactory.initialize

    Initialize a default scene display condition. When this display condition is assigned to an object, such as a primitive, the object can be restricted to only render in certain scenes. Call set display in scene or display only in scene to limit the scenes.

    :Returns:

        :obj:`~SceneDisplayCondition`

