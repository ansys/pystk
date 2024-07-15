AntennaControl
==============

.. py:class:: ansys.stk.core.stkobjects.AntennaControl

   Bases: 

   Class defining the properties for a antenna control.

.. py:currentmodule:: AntennaControl

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaControl.set_embedded_model`
              - Set the current antenna model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaControl.reference_type`
              - Gets or sets the antenna control reference type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaControl.supported_linked_antenna_objects`
              - Gets an array of available antenna objects that this object can link to and use.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaControl.linked_antenna_object`
              - Gets or sets the linked antenna object.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaControl.supported_embedded_models`
              - Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaControl.embedded_model`
              - Gets the current antenna model.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaControl.embedded_model_orientation`
              - Gets or sets the antenna orientation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaControl


Property detail
---------------

.. py:property:: reference_type
    :canonical: ansys.stk.core.stkobjects.AntennaControl.reference_type
    :type: ANTENNA_CONTROL_REFERENCE_TYPE

    Gets or sets the antenna control reference type.

.. py:property:: supported_linked_antenna_objects
    :canonical: ansys.stk.core.stkobjects.AntennaControl.supported_linked_antenna_objects
    :type: list

    Gets an array of available antenna objects that this object can link to and use.

.. py:property:: linked_antenna_object
    :canonical: ansys.stk.core.stkobjects.AntennaControl.linked_antenna_object
    :type: str

    Gets or sets the linked antenna object.

.. py:property:: supported_embedded_models
    :canonical: ansys.stk.core.stkobjects.AntennaControl.supported_embedded_models
    :type: list

    Gets an array of supported model names.

.. py:property:: embedded_model
    :canonical: ansys.stk.core.stkobjects.AntennaControl.embedded_model
    :type: IAntennaModel

    Gets the current antenna model.

.. py:property:: embedded_model_orientation
    :canonical: ansys.stk.core.stkobjects.AntennaControl.embedded_model_orientation
    :type: IOrientation

    Gets or sets the antenna orientation.


Method detail
-------------







.. py:method:: set_embedded_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaControl.set_embedded_model

    Set the current antenna model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`




