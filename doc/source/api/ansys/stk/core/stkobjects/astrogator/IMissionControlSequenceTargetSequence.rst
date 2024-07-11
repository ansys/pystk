IMissionControlSequenceTargetSequence
=====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence

   object
   
   General properties of a TargetSequence segment.

.. py:currentmodule:: IMissionControlSequenceTargetSequence

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.apply_profiles`
              - Apply Changes - applies the current values of search profiles' controls and the changes specified by the segment configuration profiles to the segments within the target sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.reset_profiles`
              - Reset - resets the controls of the search profiles to the segments' values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.apply_profile`
              - Apply Changes - applies the current values of specified profile to the segments within the target sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.reset_profile`
              - Reset - resets the current values of specified profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.apply_profile_by_name`
              - Apply Changes - applies the current values of specified profile to the segments within the target sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.reset_profile_by_name`
              - Reset - resets the current values of specified profile.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.action`
              - Whether to run the sequence nominally or using profiles.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.when_profiles_finish`
              - When Profiles Converge - the action to be carried out if targeting has converged.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.continue_on_failure`
              - Continue if profiles don't converge - if true, the target sequence continues if a profile fails to converge; otherwise, the MCS will stop upon the failure of a search profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.segments`
              - Returns the segments contained within the target sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.profiles`
              - Returns the profiles used within the target sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.reset_inner_targeters`
              - If true, inner target sequences will have their profiles reset before each run.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceTargetSequence


Property detail
---------------

.. py:property:: action
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.action
    :type: TARGET_SEQ_ACTION

    Whether to run the sequence nominally or using profiles.

.. py:property:: when_profiles_finish
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.when_profiles_finish
    :type: PROFILES_FINISH

    When Profiles Converge - the action to be carried out if targeting has converged.

.. py:property:: continue_on_failure
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.continue_on_failure
    :type: bool

    Continue if profiles don't converge - if true, the target sequence continues if a profile fails to converge; otherwise, the MCS will stop upon the failure of a search profile.

.. py:property:: segments
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.segments
    :type: IMissionControlSequenceSegmentCollection

    Returns the segments contained within the target sequence.

.. py:property:: profiles
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.profiles
    :type: IProfileCollection

    Returns the profiles used within the target sequence.

.. py:property:: reset_inner_targeters
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.reset_inner_targeters
    :type: bool

    If true, inner target sequences will have their profiles reset before each run.


Method detail
-------------









.. py:method:: apply_profiles(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.apply_profiles

    Apply Changes - applies the current values of search profiles' controls and the changes specified by the segment configuration profiles to the segments within the target sequence.

    :Returns:

        :obj:`~None`

.. py:method:: reset_profiles(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.reset_profiles

    Reset - resets the controls of the search profiles to the segments' values.

    :Returns:

        :obj:`~None`

.. py:method:: apply_profile(self, profile: IProfile) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.apply_profile

    Apply Changes - applies the current values of specified profile to the segments within the target sequence.

    :Parameters:

    **profile** : :obj:`~IProfile`

    :Returns:

        :obj:`~None`

.. py:method:: reset_profile(self, profile: IProfile) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.reset_profile

    Reset - resets the current values of specified profile.

    :Parameters:

    **profile** : :obj:`~IProfile`

    :Returns:

        :obj:`~None`

.. py:method:: apply_profile_by_name(self, profile: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.apply_profile_by_name

    Apply Changes - applies the current values of specified profile to the segments within the target sequence.

    :Parameters:

    **profile** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: reset_profile_by_name(self, profile: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence.reset_profile_by_name

    Reset - resets the current values of specified profile.

    :Parameters:

    **profile** : :obj:`~str`

    :Returns:

        :obj:`~None`



