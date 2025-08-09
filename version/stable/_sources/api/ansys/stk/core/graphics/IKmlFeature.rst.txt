IKmlFeature
===========

.. py:class:: ansys.stk.core.graphics.IKmlFeature

   A KML feature.

.. py:currentmodule:: IKmlFeature

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeature.fly_to`
              - Move the camera to the area encompassing this feature.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeature.is_loaded`
              - Get whether the document associated with this feature is loaded.
            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeature.display`
              - Get or set whether this feature will be displayed in the Scene.
            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeature.content`
              - Get the content associated with this feature.
            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeature.name`
              - Get the name of this feature.
            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeature.description`
              - Get the description associated with this feature.
            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeature.snippet`
              - Get the snippet associated with this feature.
            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeature.bounding_sphere`
              - The bounding sphere encompassing the area associated with this feature.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IKmlFeature


Property detail
---------------

.. py:property:: is_loaded
    :canonical: ansys.stk.core.graphics.IKmlFeature.is_loaded
    :type: bool

    Get whether the document associated with this feature is loaded.

.. py:property:: display
    :canonical: ansys.stk.core.graphics.IKmlFeature.display
    :type: bool

    Get or set whether this feature will be displayed in the Scene.

.. py:property:: content
    :canonical: ansys.stk.core.graphics.IKmlFeature.content
    :type: str

    Get the content associated with this feature.

.. py:property:: name
    :canonical: ansys.stk.core.graphics.IKmlFeature.name
    :type: str

    Get the name of this feature.

.. py:property:: description
    :canonical: ansys.stk.core.graphics.IKmlFeature.description
    :type: str

    Get the description associated with this feature.

.. py:property:: snippet
    :canonical: ansys.stk.core.graphics.IKmlFeature.snippet
    :type: str

    Get the snippet associated with this feature.

.. py:property:: bounding_sphere
    :canonical: ansys.stk.core.graphics.IKmlFeature.bounding_sphere
    :type: BoundingSphere

    The bounding sphere encompassing the area associated with this feature.


Method detail
-------------









.. py:method:: fly_to(self) -> None
    :canonical: ansys.stk.core.graphics.IKmlFeature.fly_to

    Move the camera to the area encompassing this feature.

    :Returns:

        :obj:`~None`

