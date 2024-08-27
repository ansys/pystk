FrameRate
=========

.. py:class:: ansys.stk.core.graphics.FrameRate

   Keeps track of how many times the scenes are rendered per second.

.. py:currentmodule:: FrameRate

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.FrameRate.reset`
              - Reset the frame rate counter back to zero. The frame rate computation begins anew.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.FrameRate.frames_per_second`
              - Gets the current frame rate in frames per second.
            * - :py:attr:`~ansys.stk.core.graphics.FrameRate.maximum_number_of_frames`
              - Gets or sets the maximum number of frames used to determine frame rate. More frames means that the frame rate is averaged over a longer period of time and will fluctuate less than fewer frames would. The minimum value is 2.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import FrameRate


Property detail
---------------

.. py:property:: frames_per_second
    :canonical: ansys.stk.core.graphics.FrameRate.frames_per_second
    :type: float

    Gets the current frame rate in frames per second.

.. py:property:: maximum_number_of_frames
    :canonical: ansys.stk.core.graphics.FrameRate.maximum_number_of_frames
    :type: int

    Gets or sets the maximum number of frames used to determine frame rate. More frames means that the frame rate is averaged over a longer period of time and will fluctuate less than fewer frames would. The minimum value is 2.


Method detail
-------------




.. py:method:: reset(self) -> None
    :canonical: ansys.stk.core.graphics.FrameRate.reset

    Reset the frame rate counter back to zero. The frame rate computation begins anew.

    :Returns:

        :obj:`~None`

