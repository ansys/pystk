RenderingEventArgs
==================

.. py:class:: ansys.stk.core.graphics.RenderingEventArgs

   The event is raised when the scene is rendered.

.. py:currentmodule:: RenderingEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.RenderingEventArgs.time`
              - The time of the rendering event.
            * - :py:attr:`~ansys.stk.core.graphics.RenderingEventArgs.time_in_ep_secs`
              - The time of the rendering event (in STK's scenario epoch units).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import RenderingEventArgs


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.graphics.RenderingEventArgs.time
    :type: IDate

    The time of the rendering event.

.. py:property:: time_in_ep_secs
    :canonical: ansys.stk.core.graphics.RenderingEventArgs.time_in_ep_secs
    :type: float

    The time of the rendering event (in STK's scenario epoch units).


