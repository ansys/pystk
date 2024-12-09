SceneDisplayCondition
=====================

.. py:class:: ansys.stk.core.graphics.SceneDisplayCondition

   Bases: :py:class:`~ansys.stk.core.graphics.IDisplayCondition`

   A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

.. py:currentmodule:: SceneDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SceneDisplayCondition.set_display_in_scene`
              - Allow or disallows rendering for in a particular scene for.
            * - :py:attr:`~ansys.stk.core.graphics.SceneDisplayCondition.get_display_in_scene`
              - Determine whether the display condition allows rendering rendering in the given scene.
            * - :py:attr:`~ansys.stk.core.graphics.SceneDisplayCondition.display_only_in_scene`
              - Allow rendering only in the given scene. The display condition will not allow rendering in other scenes, including newly created ones.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SceneDisplayCondition



Method detail
-------------

.. py:method:: set_display_in_scene(self, scene: Scene, on: bool) -> None
    :canonical: ansys.stk.core.graphics.SceneDisplayCondition.set_display_in_scene

    Allow or disallows rendering for in a particular scene for.

    :Parameters:

    **scene** : :obj:`~Scene`
    **on** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: get_display_in_scene(self, scene: Scene) -> bool
    :canonical: ansys.stk.core.graphics.SceneDisplayCondition.get_display_in_scene

    Determine whether the display condition allows rendering rendering in the given scene.

    :Parameters:

    **scene** : :obj:`~Scene`

    :Returns:

        :obj:`~bool`

.. py:method:: display_only_in_scene(self, scene: Scene) -> None
    :canonical: ansys.stk.core.graphics.SceneDisplayCondition.display_only_in_scene

    Allow rendering only in the given scene. The display condition will not allow rendering in other scenes, including newly created ones.

    :Parameters:

    **scene** : :obj:`~Scene`

    :Returns:

        :obj:`~None`

