VehicleGraphics3DBPlaneTemplate
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate

   An element of VehicleGraphics3DBPlaneTemplatesCollection.

.. py:currentmodule:: VehicleGraphics3DBPlaneTemplate

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.name`
              - Get or set the name of the template.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.description`
              - Get or set the description of the template.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.central_body`
              - Get or set the template's central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.available_central_bodies`
              - Get a list of available central bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.reference_vector`
              - Get or set the template's reference vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.available_vectors`
              - Get a list of available vectors.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.show_cartesian_grid`
              - Whether the Cartesian grid is displayed with the template.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.show_polar_grid`
              - Whether the Polar grid is displayed with the template.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.grid_spacing`
              - Get or set the distance between grid lines. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.display_elements`
              - Return the 3D BPlane template display collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DBPlaneTemplate


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.name
    :type: str

    Get or set the name of the template.

.. py:property:: description
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.description
    :type: str

    Get or set the description of the template.

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.central_body
    :type: str

    Get or set the template's central body.

.. py:property:: available_central_bodies
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.available_central_bodies
    :type: list

    Get a list of available central bodies.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.reference_vector
    :type: str

    Get or set the template's reference vector.

.. py:property:: available_vectors
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.available_vectors
    :type: list

    Get a list of available vectors.

.. py:property:: show_cartesian_grid
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.show_cartesian_grid
    :type: bool

    Whether the Cartesian grid is displayed with the template.

.. py:property:: show_polar_grid
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.show_polar_grid
    :type: bool

    Whether the Polar grid is displayed with the template.

.. py:property:: grid_spacing
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.grid_spacing
    :type: float

    Get or set the distance between grid lines. Uses Distance Dimension.

.. py:property:: display_elements
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate.display_elements
    :type: VehicleGraphics3DBPlaneTemplateDisplayCollection

    Return the 3D BPlane template display collection.


