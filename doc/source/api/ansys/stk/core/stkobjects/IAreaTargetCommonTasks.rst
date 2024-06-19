IAreaTargetCommonTasks
======================

.. py:class:: IAreaTargetCommonTasks

   object
   
   AreaTarget common tasks.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_area_type_ellipse`
              - Set the boundary area type to Ellipse.
            * - :py:meth:`~set_area_type_pattern`
              - Set the boundary area type to Pattern.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAreaTargetCommonTasks



Method detail
-------------

.. py:method:: set_area_type_ellipse(self, semiMajorAxis: float, semiMinorAxis: float, bearing: typing.Any) -> IAreaTypeEllipse
    :canonical: ansys.stk.core.stkobjects.IAreaTargetCommonTasks.set_area_type_ellipse

    Set the boundary area type to Ellipse.

    :Parameters:

    **semiMajorAxis** : :obj:`~float`
    **semiMinorAxis** : :obj:`~float`
    **bearing** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IAreaTypeEllipse`

.. py:method:: set_area_type_pattern(self, latLons: list) -> IAreaTypePatternCollection
    :canonical: ansys.stk.core.stkobjects.IAreaTargetCommonTasks.set_area_type_pattern

    Set the boundary area type to Pattern.

    :Parameters:

    **latLons** : :obj:`~list`

    :Returns:

        :obj:`~IAreaTypePatternCollection`

