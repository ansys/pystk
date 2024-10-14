AXES_TYPE
=========

.. py:class:: ansys.stk.core.vgt.AXES_TYPE

   IntEnum


.. py:currentmodule:: AXES_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported type.

            * - :py:attr:`~LAGRANGE_LIBRATION`
              - Libration point axes using one primary and multiple secondary central bodies. Set primary and secondary bodies, and point type.

            * - :py:attr:`~ANGULAR_OFFSET`
              - Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

            * - :py:attr:`~FIXED_AT_EPOCH`
              - Axes based on another set fixed at a specified epoch.

            * - :py:attr:`~B_PLANE`
              - B-Plane axes using the selected target body and reference vector.

            * - :py:attr:`~CUSTOM_SCRIPT`
              - Customized axes offset with respect to a set of reference Axes.

            * - :py:attr:`~FIXED`
              - Axes fixed in reference axes.

            * - :py:attr:`~ALIGNED_AND_CONSTRAINED`
              - Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

            * - :py:attr:`~MODEL_ATTACHMENT`
              - Axes aligned with the specified pointable element of the object's 3D model. The axes follow the model as well as any articulations that affect the specified pointable element.

            * - :py:attr:`~SPINNING`
              - Axes created by spinning the Reference axes about the Spin vector with the specified rate. The axes are aligned with the Reference axes at the specified epoch plus the additional rotational offset.

            * - :py:attr:`~ON_SURFACE`
              - Projection of the reference point onto the central body.

            * - :py:attr:`~TRAJECTORY`
              - Axes based on trajectory of the point relative to the reference coordinate system.

            * - :py:attr:`~TEMPLATE`
              - Represents a VGT axes created from a template. This type of axes is not creatable.

            * - :py:attr:`~AT_TIME_INSTANT`
              - Axes orientation fixed relative to reference axes based on orientation of another set of axes evaluated at specified time instant.

            * - :py:attr:`~PLUGIN`
              - An axes plugin point.

            * - :py:attr:`~FILE`
              - Axes specified by data from a file.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AXES_TYPE


