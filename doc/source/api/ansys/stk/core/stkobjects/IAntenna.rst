IAntenna
========

.. py:class:: IAntenna

   object
   
   Provide access to the properties and methods defining an Antenna object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_model`
              - Set the current antenna model by name.
            * - :py:meth:`~is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~supported_models`
            * - :py:meth:`~model`
            * - :py:meth:`~orientation`
            * - :py:meth:`~refraction`
            * - :py:meth:`~refraction_supported_types`
            * - :py:meth:`~refraction_model`
            * - :py:meth:`~use_refraction_in_access`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~graphics`
            * - :py:meth:`~rf_environment`
            * - :py:meth:`~laser_environment`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntenna


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.IAntenna.supported_models
    :type: list

    Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IAntenna.model
    :type: IAgAntennaModel

    Gets the current antenna model.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.IAntenna.orientation
    :type: IAgOrientation

    Gets the antenna orientation.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.IAntenna.refraction
    :type: SENSOR_REFRACTION_TYPE

    Refraction method, a member of the AgESnRefractionType enumeration.

.. py:property:: refraction_supported_types
    :canonical: ansys.stk.core.stkobjects.IAntenna.refraction_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: refraction_model
    :canonical: ansys.stk.core.stkobjects.IAntenna.refraction_model
    :type: IAgRfModelBase

    Gets a refraction model.

.. py:property:: use_refraction_in_access
    :canonical: ansys.stk.core.stkobjects.IAntenna.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IAntenna.graphics_3d
    :type: IAgAntennaVO

    Get the 3D Graphics properties for the antenna.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IAntenna.graphics
    :type: IAgAntennaGraphics

    Get the 2D Graphics properties for the antenna.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.IAntenna.rf_environment
    :type: IAgObjectRFEnvironment

    Gets the object RF environment settings.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.IAntenna.laser_environment
    :type: IAgObjectLaserEnvironment

    Gets the object laser environment settings.


Method detail
-------------


.. py:method:: set_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IAntenna.set_model

    Set the current antenna model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`






.. py:method:: is_refraction_type_supported(self, model: SENSOR_REFRACTION_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.IAntenna.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **model** : :obj:`~SENSOR_REFRACTION_TYPE`

    :Returns:

        :obj:`~bool`









