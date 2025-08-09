CalculationToolScalarPlugin
===========================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Use a scalar calculation plugin.

.. py:currentmodule:: CalculationToolScalarPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.reset`
              - Reset the plugin.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.set_property`
              - Set the plugin properties. This method throws an exception if the specified property does not exist, an invalid value was specified or the specified property is read-only.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.get_property`
              - Read a value of the specified plugin property. This method throws an exception if the property does not exist.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.prog_id`
              - A programmatic ID associated with the component.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.display_name`
              - The plugin's Display Name associated with the COM plugin.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.available_properties`
              - An array of names of the properties that can be used to configure the plugin.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarPlugin


Property detail
---------------

.. py:property:: prog_id
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.prog_id
    :type: str

    A programmatic ID associated with the component.

.. py:property:: display_name
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.display_name
    :type: str

    The plugin's Display Name associated with the COM plugin.

.. py:property:: available_properties
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.available_properties
    :type: list

    An array of names of the properties that can be used to configure the plugin.


Method detail
-------------




.. py:method:: reset(self) -> None
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.reset

    Reset the plugin.

    :Returns:

        :obj:`~None`

.. py:method:: set_property(self, name: str, value: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.set_property

    Set the plugin properties. This method throws an exception if the specified property does not exist, an invalid value was specified or the specified property is read-only.

    :Parameters:

        **name** : :obj:`~str`

        **value** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: get_property(self, name: str) -> str
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin.get_property

    Read a value of the specified plugin property. This method throws an exception if the property does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~str`

