ElementEquinoctial
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ElementEquinoctial

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IElement`

   Equinoctial elements.

.. py:currentmodule:: ElementEquinoctial

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.formulation`
              - Retrograde, which has its singularity at an inclination of 0 deg. Posigrade, which has its singularity at an inclination of 180 deg.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.h`
              - h/k collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.k`
              - h/k collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.mean_longitude`
              - Specify a satellite's position within its orbit at epoch and equals the sum of the classical Right Ascension of the Ascending Node, Argument of Perigee, and Mean Anomaly. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.mean_motion`
              - Get or set the average angular rate of the satellite based on 2 body motion. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.p`
              - p/q collectively describe the orientation of the satellite's orbit plane. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.q`
              - p/q collectively describe the orientation of the satellite's orbit plane. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.semimajor_axis`
              - Half the length of the major axis of the orbital ellipse. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ElementEquinoctial


Property detail
---------------

.. py:property:: formulation
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.formulation
    :type: Formulation

    Retrograde, which has its singularity at an inclination of 0 deg. Posigrade, which has its singularity at an inclination of 180 deg.

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.h
    :type: float

    h/k collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.

.. py:property:: k
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.k
    :type: float

    h/k collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.

.. py:property:: mean_longitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.mean_longitude
    :type: typing.Any

    Specify a satellite's position within its orbit at epoch and equals the sum of the classical Right Ascension of the Ascending Node, Argument of Perigee, and Mean Anomaly. Uses Angle Dimension.

.. py:property:: mean_motion
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.mean_motion
    :type: float

    Get or set the average angular rate of the satellite based on 2 body motion. Uses Rate Dimension.

.. py:property:: p
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.p
    :type: float

    p/q collectively describe the orientation of the satellite's orbit plane. Dimensionless.

.. py:property:: q
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.q
    :type: float

    p/q collectively describe the orientation of the satellite's orbit plane. Dimensionless.

.. py:property:: semimajor_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementEquinoctial.semimajor_axis
    :type: float

    Half the length of the major axis of the orbital ellipse. Uses Distance Dimension.


