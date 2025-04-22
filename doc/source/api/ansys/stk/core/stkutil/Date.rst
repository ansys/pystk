Date
====

.. py:class:: ansys.stk.core.stkutil.Date

   Object that contains a date.

.. py:currentmodule:: Date

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.Date.format`
              - Return the value of the date given the unit.
            * - :py:attr:`~ansys.stk.core.stkutil.Date.set_date`
              - Set this date with the given date value and unit type.
            * - :py:attr:`~ansys.stk.core.stkutil.Date.add`
              - Add the value in the given unit and returns a new date interface.
            * - :py:attr:`~ansys.stk.core.stkutil.Date.subtract`
              - Subtracts the value in the given unit and returns a new date interface.
            * - :py:attr:`~ansys.stk.core.stkutil.Date.span`
              - Subtracts the value from the Date interface and returns an Quantity.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.Date.ole_date`
              - Get or set the current time in OLE DATE Format.
            * - :py:attr:`~ansys.stk.core.stkutil.Date.whole_days`
              - Get or set the Julian Day Number of the date of interest.
            * - :py:attr:`~ansys.stk.core.stkutil.Date.sec_into_day`
              - Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0.
            * - :py:attr:`~ansys.stk.core.stkutil.Date.whole_days_utc`
              - Get or set the UTC Day Number of the date of interest.
            * - :py:attr:`~ansys.stk.core.stkutil.Date.sec_into_day_utc`
              - Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import Date


Property detail
---------------

.. py:property:: ole_date
    :canonical: ansys.stk.core.stkutil.Date.ole_date
    :type: datetime

    Get or set the current time in OLE DATE Format.

.. py:property:: whole_days
    :canonical: ansys.stk.core.stkutil.Date.whole_days
    :type: int

    Get or set the Julian Day Number of the date of interest.

.. py:property:: sec_into_day
    :canonical: ansys.stk.core.stkutil.Date.sec_into_day
    :type: float

    Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0.

.. py:property:: whole_days_utc
    :canonical: ansys.stk.core.stkutil.Date.whole_days_utc
    :type: int

    Get or set the UTC Day Number of the date of interest.

.. py:property:: sec_into_day_utc
    :canonical: ansys.stk.core.stkutil.Date.sec_into_day_utc
    :type: float

    Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0.


Method detail
-------------

.. py:method:: format(self, unit: str) -> str
    :canonical: ansys.stk.core.stkutil.Date.format

    Return the value of the date given the unit.

    :Parameters:

    **unit** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: set_date(self, unit: str, value: str) -> None
    :canonical: ansys.stk.core.stkutil.Date.set_date

    Set this date with the given date value and unit type.

    :Parameters:

    **unit** : :obj:`~str`
    **value** : :obj:`~str`

    :Returns:

        :obj:`~None`











.. py:method:: add(self, unit: str, value: float) -> Date
    :canonical: ansys.stk.core.stkutil.Date.add

    Add the value in the given unit and returns a new date interface.

    :Parameters:

    **unit** : :obj:`~str`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~Date`

.. py:method:: subtract(self, unit: str, value: float) -> Date
    :canonical: ansys.stk.core.stkutil.Date.subtract

    Subtracts the value in the given unit and returns a new date interface.

    :Parameters:

    **unit** : :obj:`~str`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~Date`

.. py:method:: span(self, date: Date) -> Quantity
    :canonical: ansys.stk.core.stkutil.Date.span

    Subtracts the value from the Date interface and returns an Quantity.

    :Parameters:

    **date** : :obj:`~Date`

    :Returns:

        :obj:`~Quantity`

