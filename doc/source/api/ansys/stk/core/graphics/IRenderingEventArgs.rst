IRenderingEventArgs
===================

.. py:class:: IRenderingEventArgs

   object
   
   The event is raised when the scene is rendered.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~time`
            * - :py:meth:`~time_in_ep_secs`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IRenderingEventArgs


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.graphics.IRenderingEventArgs.time
    :type: IAgDate

    The time of the rendering event.

.. py:property:: time_in_ep_secs
    :canonical: ansys.stk.core.graphics.IRenderingEventArgs.time_in_ep_secs
    :type: float

    The time of the rendering event (in STK's scenario epoch units).


