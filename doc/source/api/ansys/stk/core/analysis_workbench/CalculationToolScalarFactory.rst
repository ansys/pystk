CalculationToolScalarFactory
============================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory

   The factory creates scalar calculation components.

.. py:currentmodule:: CalculationToolScalarFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create`
              - Create and registers a scalar calculation using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_angle`
              - Create a scalar calculation equal to angular displacement obtained from any angle in VGT.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_fixed_at_time_instant`
              - Create a scalar calculation defined by evaluating the input scalar calculation at the specified reference time instant.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_constant`
              - Create a scalar calculation of constant value of the specified dimension.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_data_element`
              - Create a scalar calculation defined from a time-dependent data element from STK data providers available for parent STK object.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_data_element_within_group`
              - Create a scalar calculation defined from a time-dependent data element from STK data providers available for parent STK object.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_derivative`
              - Create a scalar calculation that is the derivative of an input scalar calculation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_elapsed_time`
              - Create a scalar calculation that is the time elapsed since a reference time instant.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_from_file`
              - Create scalar calculation specified by external data file.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_function`
              - Create a scalar calculation that is defined by performing the specified function on the input scalar or time instant.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_integral`
              - Create a scalar calculation that is the integral of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_function_of_2_variables`
              - Create a scalar calculation that is defined by performing a function(x,y) on two scalar arguments.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_vector_magnitude`
              - Create a scalar calculation equal to the magnitude of a specified vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_plugin_from_display_name`
              - Create a scalar calculation based on a COM plugin. For information how to implement and register VGT plugins, see <topic name='Engine Plugins: COM-based Engine Plugin Components'>COM-based Engine Plugins.</topic>.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.is_type_supported`
              - Return whether the specified type is supported.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_from_custom_script`
              - Create a calc scalar calculation that uses scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_surface_distance_between_points`
              - Create a calc scalar calculation that is surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_dot_product`
              - Create a scalar calculation that is defined by a dot product between two vectors.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_vector_component`
              - Create a scalar calculation that is defined by a specified component of a vector when resolved in specified axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_average`
              - Create a scalar calculation that is the average of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_standard_deviation`
              - Create a scalar calculation that is the standard deviation of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_calculation_along_trajectory`
              - Create a scalar calculation along trajectory.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_custom_inline_script`
              - Create a custom inline script scalar.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.available_plugin_display_names`
              - An array of display names associated with available scalar calculation plugins. The elements of the array are strings. Display names are used to create Calc scalars based on COM plugins using CreateCalcScalarPluginFromDisplayName method.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarFactory


Property detail
---------------

.. py:property:: available_plugin_display_names
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.available_plugin_display_names
    :type: list

    An array of display names associated with available scalar calculation plugins. The elements of the array are strings. Display names are used to create Calc scalars based on COM plugins using CreateCalcScalarPluginFromDisplayName method.


Method detail
-------------


.. py:method:: create(self, name: str, description: str, type: CalculationScalarType) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create

    Create and registers a scalar calculation using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CalculationScalarType`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_angle(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_angle

    Create a scalar calculation equal to angular displacement obtained from any angle in VGT.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_fixed_at_time_instant(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_fixed_at_time_instant

    Create a scalar calculation defined by evaluating the input scalar calculation at the specified reference time instant.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_constant(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_constant

    Create a scalar calculation of constant value of the specified dimension.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_data_element(self, name: str, description: str, data_provider: str, element_name: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_data_element

    Create a scalar calculation defined from a time-dependent data element from STK data providers available for parent STK object.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **data_provider** : :obj:`~str`
    **element_name** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_data_element_within_group(self, name: str, description: str, data_provider: str, group_name: str, element_name: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_data_element_within_group

    Create a scalar calculation defined from a time-dependent data element from STK data providers available for parent STK object.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **data_provider** : :obj:`~str`
    **group_name** : :obj:`~str`
    **element_name** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_derivative(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_derivative

    Create a scalar calculation that is the derivative of an input scalar calculation.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_elapsed_time(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_elapsed_time

    Create a scalar calculation that is the time elapsed since a reference time instant.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_from_file(self, name: str, description: str, filepath: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_from_file

    Create scalar calculation specified by external data file.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_function(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_function

    Create a scalar calculation that is defined by performing the specified function on the input scalar or time instant.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_integral(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_integral

    Create a scalar calculation that is the integral of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_function_of_2_variables(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_function_of_2_variables

    Create a scalar calculation that is defined by performing a function(x,y) on two scalar arguments.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_vector_magnitude(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_vector_magnitude

    Create a scalar calculation equal to the magnitude of a specified vector.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_plugin_from_display_name(self, name: str, description: str, display_name: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_plugin_from_display_name

    Create a scalar calculation based on a COM plugin. For information how to implement and register VGT plugins, see <topic name='Engine Plugins: COM-based Engine Plugin Components'>COM-based Engine Plugins.</topic>.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **display_name** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: is_type_supported(self, type: CalculationScalarType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **type** : :obj:`~CalculationScalarType`

    :Returns:

        :obj:`~bool`

.. py:method:: create_from_custom_script(self, name: str, description: str, filepath: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_from_custom_script

    Create a calc scalar calculation that uses scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_surface_distance_between_points(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_surface_distance_between_points

    Create a calc scalar calculation that is surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_dot_product(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_dot_product

    Create a scalar calculation that is defined by a dot product between two vectors.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_vector_component(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_vector_component

    Create a scalar calculation that is defined by a specified component of a vector when resolved in specified axes.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_average(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_average

    Create a scalar calculation that is the average of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_standard_deviation(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_standard_deviation

    Create a scalar calculation that is the standard deviation of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calculation_along_trajectory(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_calculation_along_trajectory

    Create a scalar calculation along trajectory.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_custom_inline_script(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFactory.create_custom_inline_script

    Create a custom inline script scalar.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

