IDirectionProviderObject
========================

.. py:class:: IDirectionProviderObject

   object
   
   Provide access to the properties and methods defining an object direction provider.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~directions`
            * - :py:meth:`~enabled`
            * - :py:meth:`~limits_exceeded_behavior_type`
            * - :py:meth:`~use_default_direction`
            * - :py:meth:`~azimuth_steering_limit_a`
            * - :py:meth:`~azimuth_steering_limit_b`
            * - :py:meth:`~elevation_steering_limit_a`
            * - :py:meth:`~elevation_steering_limit_b`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDirectionProviderObject


Property detail
---------------

.. py:property:: directions
    :canonical: ansys.stk.core.stkobjects.IDirectionProviderObject.directions
    :type: "IAgObjectLinkCollection"

    Gets the beam steering list.

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.IDirectionProviderObject.enabled
    :type: bool

    Gets or set the option for enabling steering.

.. py:property:: limits_exceeded_behavior_type
    :canonical: ansys.stk.core.stkobjects.IDirectionProviderObject.limits_exceeded_behavior_type
    :type: "LIMITS_EXCEEDED_BEHAVIOR_TYPE"

    Gets or sets the Limits Exceeded Behavior type.

.. py:property:: use_default_direction
    :canonical: ansys.stk.core.stkobjects.IDirectionProviderObject.use_default_direction
    :type: bool

    Gets or set the option to use default direction when there are zero objects in the field of view.

.. py:property:: azimuth_steering_limit_a
    :canonical: ansys.stk.core.stkobjects.IDirectionProviderObject.azimuth_steering_limit_a
    :type: float

    Gets or sets Azimuth Steering Limit A.

.. py:property:: azimuth_steering_limit_b
    :canonical: ansys.stk.core.stkobjects.IDirectionProviderObject.azimuth_steering_limit_b
    :type: float

    Gets or sets Azimuth Steering Limit B.

.. py:property:: elevation_steering_limit_a
    :canonical: ansys.stk.core.stkobjects.IDirectionProviderObject.elevation_steering_limit_a
    :type: float

    Gets or sets Elevation Steering Limit A.

.. py:property:: elevation_steering_limit_b
    :canonical: ansys.stk.core.stkobjects.IDirectionProviderObject.elevation_steering_limit_b
    :type: float

    Gets or sets Elevation Steering Limit B.


