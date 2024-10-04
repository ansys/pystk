DisplayTimesTimeComponent
=========================

.. py:class:: ansys.stk.core.stkobjects.DisplayTimesTimeComponent

   Bases: :py:class:`~ansys.stk.core.stkobjects.IDisplayTimesData`

   Provide methods to configure the display times using Timeline API components.

.. py:currentmodule:: DisplayTimesTimeComponent

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DisplayTimesTimeComponent.set_time_component`
              - Configure the display times using the specified time component. Allowed are only intervals and interval lists.
            * - :py:attr:`~ansys.stk.core.stkobjects.DisplayTimesTimeComponent.set_qualified_path`
              - Configure the display times using the specified time component. Allowed are only intervals and interval lists. QualifiedPath format adheres to the format used throughout VGT API (i.e. \"Scenario/Scenario1 AnalysisInterval EventInterval\").
            * - :py:attr:`~ansys.stk.core.stkobjects.DisplayTimesTimeComponent.get_time_component`
              - Return a time component used to configure the display times or null if component has not been configured yet.
            * - :py:attr:`~ansys.stk.core.stkobjects.DisplayTimesTimeComponent.get_qualified_path`
              - Return the time component' qualified path or null if no component has been configured yet.
            * - :py:attr:`~ansys.stk.core.stkobjects.DisplayTimesTimeComponent.reset`
              - Remove and resets the display configuration by unsetting currently set time component (if any).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DisplayTimesTimeComponent



Method detail
-------------

.. py:method:: set_time_component(self, component: IAnalysisWorkbenchComponent) -> None
    :canonical: ansys.stk.core.stkobjects.DisplayTimesTimeComponent.set_time_component

    Configure the display times using the specified time component. Allowed are only intervals and interval lists.

    :Parameters:

    **component** : :obj:`~IAnalysisWorkbenchComponent`

    :Returns:

        :obj:`~None`

.. py:method:: set_qualified_path(self, qualifiedPath: str) -> None
    :canonical: ansys.stk.core.stkobjects.DisplayTimesTimeComponent.set_qualified_path

    Configure the display times using the specified time component. Allowed are only intervals and interval lists. QualifiedPath format adheres to the format used throughout VGT API (i.e. \"Scenario/Scenario1 AnalysisInterval EventInterval\").

    :Parameters:

    **qualifiedPath** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_time_component(self) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.stkobjects.DisplayTimesTimeComponent.get_time_component

    Return a time component used to configure the display times or null if component has not been configured yet.

    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`

.. py:method:: get_qualified_path(self) -> str
    :canonical: ansys.stk.core.stkobjects.DisplayTimesTimeComponent.get_qualified_path

    Return the time component' qualified path or null if no component has been configured yet.

    :Returns:

        :obj:`~str`

.. py:method:: reset(self) -> None
    :canonical: ansys.stk.core.stkobjects.DisplayTimesTimeComponent.reset

    Remove and resets the display configuration by unsetting currently set time component (if any).

    :Returns:

        :obj:`~None`

