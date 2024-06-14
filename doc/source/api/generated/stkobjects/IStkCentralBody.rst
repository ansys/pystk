IStkCentralBody
===============

.. py:class:: IStkCentralBody

   object
   
   A central body interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~ellipsoid`
            * - :py:meth:`~vgt`
            * - :py:meth:`~gravitational_parameter`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkCentralBody


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IStkCentralBody.name
    :type: str

    A name of the central body.

.. py:property:: ellipsoid
    :canonical: ansys.stk.core.stkobjects.IStkCentralBody.ellipsoid
    :type: "IAgStkCentralBodyEllipsoid"

    The central body ellipsoid.

.. py:property:: vgt
    :canonical: ansys.stk.core.stkobjects.IStkCentralBody.vgt
    :type: "IAgCrdnProvider"

    Returns the central body's Vector Geometry Tool provider.

.. py:property:: gravitational_parameter
    :canonical: ansys.stk.core.stkobjects.IStkCentralBody.gravitational_parameter
    :type: float

    The gravitational parameter of the central body in distance units cubed per time units squared (i.e. m^3*s^-2).


