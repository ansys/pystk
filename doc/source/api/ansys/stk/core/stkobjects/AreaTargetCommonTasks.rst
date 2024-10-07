AreaTargetCommonTasks
=====================

.. py:class:: ansys.stk.core.stkobjects.AreaTargetCommonTasks

   Class defining the Area Target Common class.

.. py:currentmodule:: AreaTargetCommonTasks

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetCommonTasks.set_area_type_ellipse`
              - Set the boundary area type to Ellipse.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetCommonTasks.set_area_type_pattern`
              - Set the boundary area type to Pattern.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AreaTargetCommonTasks



Method detail
-------------

.. py:method:: set_area_type_ellipse(self, semiMajorAxis: float, semiMinorAxis: float, bearing: typing.Any) -> AreaTypeEllipse
    :canonical: ansys.stk.core.stkobjects.AreaTargetCommonTasks.set_area_type_ellipse

    Set the boundary area type to Ellipse.

    :Parameters:

    **semiMajorAxis** : :obj:`~float`
    **semiMinorAxis** : :obj:`~float`
    **bearing** : :obj:`~typing.Any`

    :Returns:

        :obj:`~AreaTypeEllipse`

.. py:method:: set_area_type_pattern(self, latLons: list) -> AreaTypePatternCollection
    :canonical: ansys.stk.core.stkobjects.AreaTargetCommonTasks.set_area_type_pattern

    Set the boundary area type to Pattern.

    :Parameters:

    **latLons** : :obj:`~list`

    :Returns:

        :obj:`~AreaTypePatternCollection`

