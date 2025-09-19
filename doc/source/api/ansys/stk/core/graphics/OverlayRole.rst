OverlayRole
===========

.. py:class:: ansys.stk.core.graphics.OverlayRole

   IntEnum


.. py:currentmodule:: OverlayRole

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BASE`
              - The globe overlay is a base image.

            * - :py:attr:`~NIGHT`
              - The globe overlay is a base image that is only displayed on the area of the central body that is not lit by the sun.

            * - :py:attr:`~SPECULAR`
              - The globe overlay is a base image that shows the glint of the sun on the central body.

            * - :py:attr:`~NORMAL`
              - The globe overlay is a normal overlay without a special role.

            * - :py:attr:`~NONE`
              - The role of the globe overlay isn't set.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import OverlayRole


