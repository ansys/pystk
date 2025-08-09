CalculationToolParameterSetFactory
==================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory

   The factory is used to create instances of available parameter set types.

.. py:currentmodule:: CalculationToolParameterSetFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create`
              - Create and registers a parameter set using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create_attitude`
              - Create a parameter set defined by identifying one set of axes in reference to another.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create_ground_trajectory`
              - Create a parameter set defined by identifying location in reference central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create_trajectory`
              - Create a parameter set defined by identifying location in reference coordinate system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create_orbit`
              - Create a parameter set defined by identifying orbiting point and its central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create_vector`
              - Create a parameter set defined by identifying vector in reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.is_type_supported`
              - Return whether the specified type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolParameterSetFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: ParameterSetType) -> ICalculationToolParameterSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create

    Create and registers a parameter set using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`

        **type** : :obj:`~ParameterSetType`


    :Returns:

        :obj:`~ICalculationToolParameterSet`

.. py:method:: create_attitude(self, name: str, description: str) -> ICalculationToolParameterSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create_attitude

    Create a parameter set defined by identifying one set of axes in reference to another.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ICalculationToolParameterSet`

.. py:method:: create_ground_trajectory(self, name: str, description: str) -> ICalculationToolParameterSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create_ground_trajectory

    Create a parameter set defined by identifying location in reference central body.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ICalculationToolParameterSet`

.. py:method:: create_trajectory(self, name: str, description: str) -> ICalculationToolParameterSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create_trajectory

    Create a parameter set defined by identifying location in reference coordinate system.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ICalculationToolParameterSet`

.. py:method:: create_orbit(self, name: str, description: str) -> ICalculationToolParameterSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create_orbit

    Create a parameter set defined by identifying orbiting point and its central body.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ICalculationToolParameterSet`

.. py:method:: create_vector(self, name: str, description: str) -> ICalculationToolParameterSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.create_vector

    Create a parameter set defined by identifying vector in reference axes.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ICalculationToolParameterSet`

.. py:method:: is_type_supported(self, type: ParameterSetType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

        **type** : :obj:`~ParameterSetType`


    :Returns:

        :obj:`~bool`

