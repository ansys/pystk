ISceneDisplayConditionFactory
=============================

.. py:class:: ISceneDisplayConditionFactory

   object
   
   A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default scene display condition. When this display condition is assigned to an object, such as a primitive, the object can be restricted to only render in certain scenes. Call set display in scene or display only in scene to limit the scenes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISceneDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> ISceneDisplayCondition
    :canonical: ansys.stk.core.graphics.ISceneDisplayConditionFactory.initialize

    Initialize a default scene display condition. When this display condition is assigned to an object, such as a primitive, the object can be restricted to only render in certain scenes. Call set display in scene or display only in scene to limit the scenes.

    :Returns:

        :obj:`~ISceneDisplayCondition`

