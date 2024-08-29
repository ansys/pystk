StkCentralBody
==============

.. py:class:: ansys.stk.core.stkobjects.StkCentralBody

   A central body coclass.

.. py:currentmodule:: StkCentralBody

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBody.name`
              - A name of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBody.ellipsoid`
              - The central body ellipsoid.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBody.vgt`
              - Returns the central body's Vector Geometry Tool provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBody.gravitational_parameter`
              - The gravitational parameter of the central body in distance units cubed per time units squared (i.e. m^3*s^-2).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StkCentralBody


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.StkCentralBody.name
    :type: str

    A name of the central body.

.. py:property:: ellipsoid
    :canonical: ansys.stk.core.stkobjects.StkCentralBody.ellipsoid
    :type: StkCentralBodyEllipsoid

    The central body ellipsoid.

.. py:property:: vgt
    :canonical: ansys.stk.core.stkobjects.StkCentralBody.vgt
    :type: IAnalysisWorkbenchProvider

    Returns the central body's Vector Geometry Tool provider.

.. py:property:: gravitational_parameter
    :canonical: ansys.stk.core.stkobjects.StkCentralBody.gravitational_parameter
    :type: float

    The gravitational parameter of the central body in distance units cubed per time units squared (i.e. m^3*s^-2).


