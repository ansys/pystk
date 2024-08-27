VehicleGraphics3DBPlaneTemplate
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate

   An element of IAgVeVOBPlaneTemplatesCollection.

.. py:currentmodule:: VehicleGraphics3DBPlaneTemplate

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.name`
              - Gets or sets the name of the template.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.description`
              - Gets or sets the description of the template.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.central_body`
              - Gets or sets the template's central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.available_central_bodies`
              - Gets a list of available central bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.reference_vector`
              - Gets or sets the template's reference vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.available_vectors`
              - Gets a list of available vectors.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.is_cartesian_grid_visible`
              - Whether the Cartesian grid is displayed with the template.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.is_polar_grid_visible`
              - Whether the Polar grid is displayed with the template.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.grid_spacing`
              - Gets or sets the distance between grid lines. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.display_elements`
              - Returns the 3D BPlane template display collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DBPlaneTemplate


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.name
    :type: str

    Gets or sets the name of the template.

.. py:property:: description
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.description
    :type: str

    Gets or sets the description of the template.

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.central_body
    :type: str

    Gets or sets the template's central body.

.. py:property:: available_central_bodies
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.available_central_bodies
    :type: list

    Gets a list of available central bodies.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.reference_vector
    :type: str

    Gets or sets the template's reference vector.

.. py:property:: available_vectors
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.available_vectors
    :type: list

    Gets a list of available vectors.

.. py:property:: is_cartesian_grid_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.is_cartesian_grid_visible
    :type: bool

    Whether the Cartesian grid is displayed with the template.

.. py:property:: is_polar_grid_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.is_polar_grid_visible
    :type: bool

    Whether the Polar grid is displayed with the template.

.. py:property:: grid_spacing
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.grid_spacing
    :type: float

    Gets or sets the distance between grid lines. Uses Distance Dimension.

.. py:property:: display_elements
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.display_elements
    :type: VehicleGraphics3DBPlaneTemplateDisplayCollection

    Returns the 3D BPlane template display collection.


