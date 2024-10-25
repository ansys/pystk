CentralBody
===========

.. py:class:: ansys.stk.core.stkobjects.CentralBody

   A central body coclass.

.. py:currentmodule:: CentralBody

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBody.name`
              - A name of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBody.ellipsoid`
              - The central body ellipsoid.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBody.analysis_workbench_components`
              - Returns the central body's Vector Geometry Tool provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBody.gravitational_parameter`
              - The gravitational parameter of the central body in distance units cubed per time units squared (i.e. m^3*s^-2).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CentralBody


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.CentralBody.name
    :type: str

    A name of the central body.

.. py:property:: ellipsoid
    :canonical: ansys.stk.core.stkobjects.CentralBody.ellipsoid
    :type: CentralBodyEllipsoid

    The central body ellipsoid.

.. py:property:: analysis_workbench_components
    :canonical: ansys.stk.core.stkobjects.CentralBody.analysis_workbench_components
    :type: IAnalysisWorkbenchComponentProvider

    Returns the central body's Vector Geometry Tool provider.

.. py:property:: gravitational_parameter
    :canonical: ansys.stk.core.stkobjects.CentralBody.gravitational_parameter
    :type: float

    The gravitational parameter of the central body in distance units cubed per time units squared (i.e. m^3*s^-2).


