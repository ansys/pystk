IDate
=====

.. py:class:: ansys.stk.core.stkutil.IDate

   object
   
   Provide helper methods for a date.

.. py:currentmodule:: IDate

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IDate.format`
              - Return the value of the date given the unit.
            * - :py:attr:`~ansys.stk.core.stkutil.IDate.set_date`
              - Set this date with the given date value and unit type.
            * - :py:attr:`~ansys.stk.core.stkutil.IDate.add`
              - Add the value in the given unit and returns a new date interface.
            * - :py:attr:`~ansys.stk.core.stkutil.IDate.subtract`
              - Subtracts the value in the given unit and returns a new date interface.
            * - :py:attr:`~ansys.stk.core.stkutil.IDate.span`
              - Subtracts the value from the IAgDate interface and returns an IAgQuantity.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IDate.ole_date`
              - Gets or sets the current time in OLE DATE Format.
            * - :py:attr:`~ansys.stk.core.stkutil.IDate.whole_days`
              - Gets or sets the Julian Day Number of the date of interest.
            * - :py:attr:`~ansys.stk.core.stkutil.IDate.sec_into_day`
              - Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0.
            * - :py:attr:`~ansys.stk.core.stkutil.IDate.whole_days_utc`
              - Gets or sets the UTC Day Number of the date of interest.
            * - :py:attr:`~ansys.stk.core.stkutil.IDate.sec_into_day_utc`
              - Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IDate


Property detail
---------------

.. py:property:: ole_date
    :canonical: ansys.stk.core.stkutil.IDate.ole_date
    :type: datetime

    Gets or sets the current time in OLE DATE Format.

.. py:property:: whole_days
    :canonical: ansys.stk.core.stkutil.IDate.whole_days
    :type: int

    Gets or sets the Julian Day Number of the date of interest.

.. py:property:: sec_into_day
    :canonical: ansys.stk.core.stkutil.IDate.sec_into_day
    :type: float

    Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0.

.. py:property:: whole_days_utc
    :canonical: ansys.stk.core.stkutil.IDate.whole_days_utc
    :type: int

    Gets or sets the UTC Day Number of the date of interest.

.. py:property:: sec_into_day_utc
    :canonical: ansys.stk.core.stkutil.IDate.sec_into_day_utc
    :type: float

    Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0.


Method detail
-------------

.. py:method:: format(self, unit: str) -> str
    :canonical: ansys.stk.core.stkutil.IDate.format

    Return the value of the date given the unit.

    :Parameters:

    **unit** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: set_date(self, unit: str, value: str) -> None
    :canonical: ansys.stk.core.stkutil.IDate.set_date

    Set this date with the given date value and unit type.

    :Parameters:

    **unit** : :obj:`~str`
    **value** : :obj:`~str`

    :Returns:

        :obj:`~None`











.. py:method:: add(self, unit: str, value: float) -> IDate
    :canonical: ansys.stk.core.stkutil.IDate.add

    Add the value in the given unit and returns a new date interface.

    :Parameters:

    **unit** : :obj:`~str`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~IDate`

.. py:method:: subtract(self, unit: str, value: float) -> IDate
    :canonical: ansys.stk.core.stkutil.IDate.subtract

    Subtracts the value in the given unit and returns a new date interface.

    :Parameters:

    **unit** : :obj:`~str`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~IDate`

.. py:method:: span(self, date: IDate) -> IQuantity
    :canonical: ansys.stk.core.stkutil.IDate.span

    Subtracts the value from the IAgDate interface and returns an IAgQuantity.

    :Parameters:

    **date** : :obj:`~IDate`

    :Returns:

        :obj:`~IQuantity`

