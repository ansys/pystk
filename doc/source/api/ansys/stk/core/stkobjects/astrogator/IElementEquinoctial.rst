IElementEquinoctial
===================

.. py:class:: IElementEquinoctial

   IElement
   
   Properties for Equinoctial elements.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~semi_major_axis`
            * - :py:meth:`~mean_motion`
            * - :py:meth:`~h`
            * - :py:meth:`~k`
            * - :py:meth:`~p`
            * - :py:meth:`~q`
            * - :py:meth:`~mean_longitude`
            * - :py:meth:`~formulation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IElementEquinoctial


Property detail
---------------

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementEquinoctial.semi_major_axis
    :type: float

    Half the length of the major axis of the orbital ellipse. Uses Distance Dimension.

.. py:property:: mean_motion
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementEquinoctial.mean_motion
    :type: float

    Gets or sets the average angular rate of the satellite based on 2 body motion. Uses Rate Dimension.

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementEquinoctial.h
    :type: float

    h/k collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.

.. py:property:: k
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementEquinoctial.k
    :type: float

    h/k collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.

.. py:property:: p
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementEquinoctial.p
    :type: float

    p/q collectively describe the orientation of the satellite's orbit plane. Dimensionless.

.. py:property:: q
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementEquinoctial.q
    :type: float

    p/q collectively describe the orientation of the satellite's orbit plane. Dimensionless.

.. py:property:: mean_longitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementEquinoctial.mean_longitude
    :type: typing.Any

    Specifies a satellite's position within its orbit at epoch and equals the sum of the classical Right Ascension of the Ascending Node, Argument of Perigee, and Mean Anomaly. Uses Angle Dimension.

.. py:property:: formulation
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementEquinoctial.formulation
    :type: FORMULATION

    Retrograde, which has its singularity at an inclination of 0 deg. Posigrade, which has its singularity at an inclination of 180 deg.


