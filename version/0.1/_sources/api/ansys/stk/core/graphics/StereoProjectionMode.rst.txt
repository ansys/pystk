StereoProjectionMode
====================

.. py:class:: ansys.stk.core.graphics.StereoProjectionMode

   IntEnum


.. py:currentmodule:: StereoProjectionMode

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~PARALLEL`
              - Parallel projection. Parallel projection will ignore any projection distance that has been set and instead use a parallel projection for each eye. In parallel mode all objects will appear to go into the screen...

            * - :py:attr:`~FIXED_DISTANCE`
              - Fixed distance projection. Objects at the fixed distance will appear to have no depth. Objects further than the distance will appear to go into the screen. Objects nearer than the distance will appear to pop out of the screen.

            * - :py:attr:`~AUTOMATIC`
              - Automatic distance projection. Automatic distance projection will ignore any projection distance that has been set and instead automatically calculates the projection distance based on the distance between the camera and the center of the scene.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import StereoProjectionMode


