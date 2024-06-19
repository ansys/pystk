ISceneDisplayCondition
======================

.. py:class:: ISceneDisplayCondition

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

            * - :py:meth:`~set_display_in_scene`
              - Allow or disallows rendering for in a particular scene for.
            * - :py:meth:`~get_display_in_scene`
              - Determine whether the display condition allows rendering rendering in the given scene.
            * - :py:meth:`~display_only_in_scene`
              - Allow rendering only in the given scene. The display condition will not allow rendering in other scenes, including newly created ones.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISceneDisplayCondition



Method detail
-------------

.. py:method:: set_display_in_scene(self, scene: IScene, on: bool) -> None
    :canonical: ansys.stk.core.graphics.ISceneDisplayCondition.set_display_in_scene

    Allow or disallows rendering for in a particular scene for.

    :Parameters:

    **scene** : :obj:`~IScene`
    **on** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: get_display_in_scene(self, scene: IScene) -> bool
    :canonical: ansys.stk.core.graphics.ISceneDisplayCondition.get_display_in_scene

    Determine whether the display condition allows rendering rendering in the given scene.

    :Parameters:

    **scene** : :obj:`~IScene`

    :Returns:

        :obj:`~bool`

.. py:method:: display_only_in_scene(self, scene: IScene) -> None
    :canonical: ansys.stk.core.graphics.ISceneDisplayCondition.display_only_in_scene

    Allow rendering only in the given scene. The display condition will not allow rendering in other scenes, including newly created ones.

    :Parameters:

    **scene** : :obj:`~IScene`

    :Returns:

        :obj:`~None`

