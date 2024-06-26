IStkCentralBody
===============

.. py:class:: ansys.stk.core.stkobjects.IStkCentralBody

   object
   
   A central body interface.

.. py:currentmodule:: IStkCentralBody

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkCentralBody.name`
              - A name of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkCentralBody.ellipsoid`
              - The central body ellipsoid.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkCentralBody.vgt`
              - Returns the central body's Vector Geometry Tool provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkCentralBody.gravitational_parameter`
              - The gravitational parameter of the central body in distance units cubed per time units squared (i.e. m^3*s^-2).


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
    :type: IStkCentralBodyEllipsoid

    The central body ellipsoid.

.. py:property:: vgt
    :canonical: ansys.stk.core.stkobjects.IStkCentralBody.vgt
    :type: IAnalysisWorkbenchProvider

    Returns the central body's Vector Geometry Tool provider.

.. py:property:: gravitational_parameter
    :canonical: ansys.stk.core.stkobjects.IStkCentralBody.gravitational_parameter
    :type: float

    The gravitational parameter of the central body in distance units cubed per time units squared (i.e. m^3*s^-2).


