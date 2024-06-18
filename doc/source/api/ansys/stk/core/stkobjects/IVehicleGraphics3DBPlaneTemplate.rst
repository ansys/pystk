IVehicleGraphics3DBPlaneTemplate
================================

.. py:class:: IVehicleGraphics3DBPlaneTemplate

   object
   
   An element of IAgVeVOBPlaneTemplatesCollection.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~description`
            * - :py:meth:`~central_body`
            * - :py:meth:`~available_central_bodies`
            * - :py:meth:`~reference_vector`
            * - :py:meth:`~available_vectors`
            * - :py:meth:`~is_cartesian_grid_visible`
            * - :py:meth:`~is_polar_grid_visible`
            * - :py:meth:`~grid_spacing`
            * - :py:meth:`~display_elements`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DBPlaneTemplate


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplate.name
    :type: str

    Gets or sets the name of the template.

.. py:property:: description
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplate.description
    :type: str

    Gets or sets the description of the template.

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplate.central_body
    :type: str

    Gets or sets the template's central body.

.. py:property:: available_central_bodies
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplate.available_central_bodies
    :type: list

    Gets a list of available central bodies.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplate.reference_vector
    :type: str

    Gets or sets the template's reference vector.

.. py:property:: available_vectors
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplate.available_vectors
    :type: list

    Gets a list of available vectors.

.. py:property:: is_cartesian_grid_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplate.is_cartesian_grid_visible
    :type: bool

    Whether the Cartesian grid is displayed with the template.

.. py:property:: is_polar_grid_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplate.is_polar_grid_visible
    :type: bool

    Whether the Polar grid is displayed with the template.

.. py:property:: grid_spacing
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplate.grid_spacing
    :type: float

    Gets or sets the distance between grid lines. Uses Distance Dimension.

.. py:property:: display_elements
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplate.display_elements
    :type: "IAgVeVOBPlaneTemplateDisplayCollection"

    Returns the 3D BPlane template display collection.


