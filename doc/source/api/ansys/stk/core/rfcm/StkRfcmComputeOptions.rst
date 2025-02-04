StkRfcmComputeOptions
=====================

.. py:class:: ansys.stk.core.rfcm.StkRfcmComputeOptions

   The options for computing RF Channel Modeler.

.. py:currentmodule:: StkRfcmComputeOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmComputeOptions.ray_density`
              - Gets or sets the ray density.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmComputeOptions.geometrical_optics_blockage`
              - Gets or sets the geometrical optics blockage.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmComputeOptions.geometrical_optics_blockage_starting_bounce`
              - Gets or sets the geometrical optics blockage starting bounce.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmComputeOptions.maximum_reflections`
              - Gets or sets the maximum number of reflections.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmComputeOptions.maximum_transmissions`
              - Gets or sets the maximum number of transmissions.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmComputeOptions.bounding_box_mode`
              - Gets or sets the bounding box.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmComputeOptions.bounding_box_side_length`
              - Gets or sets the bounding box side length.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.rfcm import StkRfcmComputeOptions


Property detail
---------------

.. py:property:: ray_density
    :canonical: ansys.stk.core.rfcm.StkRfcmComputeOptions.ray_density
    :type: float

    Gets or sets the ray density.

.. py:property:: geometrical_optics_blockage
    :canonical: ansys.stk.core.rfcm.StkRfcmComputeOptions.geometrical_optics_blockage
    :type: bool

    Gets or sets the geometrical optics blockage.

.. py:property:: geometrical_optics_blockage_starting_bounce
    :canonical: ansys.stk.core.rfcm.StkRfcmComputeOptions.geometrical_optics_blockage_starting_bounce
    :type: int

    Gets or sets the geometrical optics blockage starting bounce.

.. py:property:: maximum_reflections
    :canonical: ansys.stk.core.rfcm.StkRfcmComputeOptions.maximum_reflections
    :type: int

    Gets or sets the maximum number of reflections.

.. py:property:: maximum_transmissions
    :canonical: ansys.stk.core.rfcm.StkRfcmComputeOptions.maximum_transmissions
    :type: int

    Gets or sets the maximum number of transmissions.

.. py:property:: bounding_box_mode
    :canonical: ansys.stk.core.rfcm.StkRfcmComputeOptions.bounding_box_mode
    :type: RfcmAnalysisSolverBoundingBoxMode

    Gets or sets the bounding box.

.. py:property:: bounding_box_side_length
    :canonical: ansys.stk.core.rfcm.StkRfcmComputeOptions.bounding_box_side_length
    :type: float

    Gets or sets the bounding box side length.


