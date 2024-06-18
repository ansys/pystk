IAntennaControl
===============

.. py:class:: IAntennaControl

   object
   
   Provide access to the properties and methods of the antenna control.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_embedded_model`
              - Set the current antenna model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_type`
            * - :py:meth:`~supported_linked_antenna_objects`
            * - :py:meth:`~linked_antenna_object`
            * - :py:meth:`~supported_embedded_models`
            * - :py:meth:`~embedded_model`
            * - :py:meth:`~embedded_model_orientation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaControl


Property detail
---------------

.. py:property:: reference_type
    :canonical: ansys.stk.core.stkobjects.IAntennaControl.reference_type
    :type: "ANTENNA_CONTROL_REFERENCE_TYPE"

    Gets or sets the antenna control reference type.

.. py:property:: supported_linked_antenna_objects
    :canonical: ansys.stk.core.stkobjects.IAntennaControl.supported_linked_antenna_objects
    :type: list

    Gets an array of available antenna objects that this object can link to and use.

.. py:property:: linked_antenna_object
    :canonical: ansys.stk.core.stkobjects.IAntennaControl.linked_antenna_object
    :type: str

    Gets or sets the linked antenna object.

.. py:property:: supported_embedded_models
    :canonical: ansys.stk.core.stkobjects.IAntennaControl.supported_embedded_models
    :type: list

    Gets an array of supported model names.

.. py:property:: embedded_model
    :canonical: ansys.stk.core.stkobjects.IAntennaControl.embedded_model
    :type: "IAgAntennaModel"

    Gets the current antenna model.

.. py:property:: embedded_model_orientation
    :canonical: ansys.stk.core.stkobjects.IAntennaControl.embedded_model_orientation
    :type: "IAgOrientation"

    Gets or sets the antenna orientation.


Method detail
-------------







.. py:method:: set_embedded_model(self, modelName:str) -> None

    Set the current antenna model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`




