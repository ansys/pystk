Antenna
=======

.. py:class:: ansys.stk.core.stkobjects.Antenna

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining the antenna object.

.. py:currentmodule:: Antenna

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.set_model`
              - Set the current antenna model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.supported_models`
              - Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.model`
              - Gets the current antenna model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.orientation`
              - Gets the antenna orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.refraction`
              - Refraction method, a member of the AgESnRefractionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.refraction_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.refraction_model`
              - Gets a refraction model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.graphics_3d`
              - Get the 3D Graphics properties for the antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.graphics`
              - Get the 2D Graphics properties for the antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.rf_environment`
              - Gets the object RF environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.laser_environment`
              - Gets the object laser environment settings.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Antenna


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.Antenna.supported_models
    :type: list

    Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.Antenna.model
    :type: IAntennaModel

    Gets the current antenna model.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.Antenna.orientation
    :type: IOrientation

    Gets the antenna orientation.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.Antenna.refraction
    :type: SENSOR_REFRACTION_TYPE

    Refraction method, a member of the AgESnRefractionType enumeration.

.. py:property:: refraction_supported_types
    :canonical: ansys.stk.core.stkobjects.Antenna.refraction_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: refraction_model
    :canonical: ansys.stk.core.stkobjects.Antenna.refraction_model
    :type: IRefractionModelBase

    Gets a refraction model.

.. py:property:: use_refraction_in_access
    :canonical: ansys.stk.core.stkobjects.Antenna.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Antenna.graphics_3d
    :type: IAntennaGraphics3D

    Get the 3D Graphics properties for the antenna.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Antenna.graphics
    :type: IAntennaGraphics

    Get the 2D Graphics properties for the antenna.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Antenna.rf_environment
    :type: IObjectRFEnvironment

    Gets the object RF environment settings.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Antenna.laser_environment
    :type: IObjectLaserEnvironment

    Gets the object laser environment settings.


Method detail
-------------


.. py:method:: set_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.Antenna.set_model

    Set the current antenna model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`






.. py:method:: is_refraction_type_supported(self, model: SENSOR_REFRACTION_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.Antenna.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **model** : :obj:`~SENSOR_REFRACTION_TYPE`

    :Returns:

        :obj:`~bool`









