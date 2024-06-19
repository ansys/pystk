ICalculationToolScalarFactory
=============================

.. py:class:: ICalculationToolScalarFactory

   object
   
   The factory creates scalar calculation components.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create`
              - Create and registers a scalar calculation using specified name, description, and type.
            * - :py:meth:`~create_calc_scalar_angle`
              - Create a scalar calculation equal to angular displacement obtained from any angle in VGT.
            * - :py:meth:`~create_calc_scalar_fixed_at_time_instant`
              - Create a scalar calculation defined by evaluating the input scalar calculation at the specified reference time instant.
            * - :py:meth:`~create_calc_scalar_constant`
              - Create a scalar calculation of constant value of the specified dimension.
            * - :py:meth:`~create_calc_scalar_data_element`
              - Create a scalar calculation defined from a time-dependent data element from STK data providers available for parent STK object.
            * - :py:meth:`~create_calc_scalar_data_element_with_group`
              - Create a scalar calculation defined from a time-dependent data element from STK data providers available for parent STK object.
            * - :py:meth:`~create_calc_scalar_derivative`
              - Create a scalar calculation that is the derivative of an input scalar calculation.
            * - :py:meth:`~create_calc_scalar_elapsed_time`
              - Create a scalar calculation that is the time elapsed since a reference time instant.
            * - :py:meth:`~create_calc_scalar_file`
              - Create scalar calculation specified by external data file.
            * - :py:meth:`~create_calc_scalar_function`
              - Create a scalar calculation that is defined by performing the specified function on the input scalar or time instant.
            * - :py:meth:`~create_calc_scalar_integral`
              - Create a scalar calculation that is the integral of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.
            * - :py:meth:`~create_calc_scalar_function2_var`
              - Create a scalar calculation that is defined by performing a function(x,y) on two scalar arguments.
            * - :py:meth:`~create_calc_scalar_vector_magnitude`
              - Create a scalar calculation equal to the magnitude of a specified vector.
            * - :py:meth:`~create_calc_scalar_plugin_from_display_name`
              - Create a scalar calculation based on a COM plugin. For information how to implement and register VGT plugins, see <topic name='Engine Plugins: COM-based Engine Plugin Components'>COM-based Engine Plugins.</topic>.
            * - :py:meth:`~is_type_supported`
              - Return whether the specified type is supported.
            * - :py:meth:`~create_calc_scalar_from_custom_script`
              - Create a calc scalar calculation that uses scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.
            * - :py:meth:`~create_calc_scalar_surface_distance_between_points`
              - Create a calc scalar calculation that is surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).
            * - :py:meth:`~create_calc_scalar_dot_product`
              - Create a scalar calculation that is defined by a dot product between two vectors.
            * - :py:meth:`~create_calc_scalar_vector_component`
              - Create a scalar calculation that is defined by a specified component of a vector when resolved in specified axes.
            * - :py:meth:`~create_calc_scalar_average`
              - Create a scalar calculation that is the average of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.
            * - :py:meth:`~create_calc_scalar_standard_deviation`
              - Create a scalar calculation that is the standard deviation of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.
            * - :py:meth:`~create_calc_scalar_point_in_volume_calc`
              - Create a scalar calculation along trajectory.
            * - :py:meth:`~create_calc_scalar_custom_inline_script`
              - Create a custom inline script scalar.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~available_calc_scalar_plugin_display_names`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarFactory


Property detail
---------------

.. py:property:: available_calc_scalar_plugin_display_names
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.available_calc_scalar_plugin_display_names
    :type: list

    An array of display names associated with available scalar calculation plugins. The elements of the array are strings. Display names are used to create Calc scalars based on COM plugins using CreateCalcScalarPluginFromDisplayName method.


Method detail
-------------


.. py:method:: create(self, name: str, description: str, type: CRDN_CALC_SCALAR_TYPE) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create

    Create and registers a scalar calculation using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CRDN_CALC_SCALAR_TYPE`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_angle(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_angle

    Create a scalar calculation equal to angular displacement obtained from any angle in VGT.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_fixed_at_time_instant(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_fixed_at_time_instant

    Create a scalar calculation defined by evaluating the input scalar calculation at the specified reference time instant.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_constant(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_constant

    Create a scalar calculation of constant value of the specified dimension.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_data_element(self, name: str, description: str, dataProvider: str, elementName: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_data_element

    Create a scalar calculation defined from a time-dependent data element from STK data providers available for parent STK object.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **dataProvider** : :obj:`~str`
    **elementName** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_data_element_with_group(self, name: str, description: str, dataProvider: str, groupName: str, elementName: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_data_element_with_group

    Create a scalar calculation defined from a time-dependent data element from STK data providers available for parent STK object.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **dataProvider** : :obj:`~str`
    **groupName** : :obj:`~str`
    **elementName** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_derivative(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_derivative

    Create a scalar calculation that is the derivative of an input scalar calculation.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_elapsed_time(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_elapsed_time

    Create a scalar calculation that is the time elapsed since a reference time instant.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_file(self, name: str, description: str, filepath: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_file

    Create scalar calculation specified by external data file.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_function(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_function

    Create a scalar calculation that is defined by performing the specified function on the input scalar or time instant.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_integral(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_integral

    Create a scalar calculation that is the integral of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_function2_var(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_function2_var

    Create a scalar calculation that is defined by performing a function(x,y) on two scalar arguments.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_vector_magnitude(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_vector_magnitude

    Create a scalar calculation equal to the magnitude of a specified vector.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_plugin_from_display_name(self, name: str, description: str, displayName: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_plugin_from_display_name

    Create a scalar calculation based on a COM plugin. For information how to implement and register VGT plugins, see <topic name='Engine Plugins: COM-based Engine Plugin Components'>COM-based Engine Plugins.</topic>.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **displayName** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: is_type_supported(self, eType: CRDN_CALC_SCALAR_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~CRDN_CALC_SCALAR_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_calc_scalar_from_custom_script(self, name: str, description: str, filepath: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_from_custom_script

    Create a calc scalar calculation that uses scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_surface_distance_between_points(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_surface_distance_between_points

    Create a calc scalar calculation that is surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_dot_product(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_dot_product

    Create a scalar calculation that is defined by a dot product between two vectors.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_vector_component(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_vector_component

    Create a scalar calculation that is defined by a specified component of a vector when resolved in specified axes.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_average(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_average

    Create a scalar calculation that is the average of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_standard_deviation(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_standard_deviation

    Create a scalar calculation that is the standard deviation of an input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_point_in_volume_calc(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_point_in_volume_calc

    Create a scalar calculation along trajectory.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: create_calc_scalar_custom_inline_script(self, name: str, description: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFactory.create_calc_scalar_custom_inline_script

    Create a custom inline script scalar.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolScalar`

