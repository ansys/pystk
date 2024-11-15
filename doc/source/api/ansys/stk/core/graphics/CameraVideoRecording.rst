CameraVideoRecording
====================

.. py:class:: ansys.stk.core.graphics.CameraVideoRecording

   Records the 3D window to either a movie file or to consecutively ordered image files each time the scene is rendered.

.. py:currentmodule:: CameraVideoRecording

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CameraVideoRecording.start_recording`
              - Do not use this method, as it is deprecated. Use the overload taking a video format instead. Starts recording a file in the WMV format at the specified bit and frame rate.
            * - :py:attr:`~ansys.stk.core.graphics.CameraVideoRecording.start_recording_frame_stack`
              - Start recording a frame stack. Each frame is saved as a separate image file. The filename of each frame is defined by a prefix followed by a frame number.
            * - :py:attr:`~ansys.stk.core.graphics.CameraVideoRecording.stop_recording`
              - Stop recording.
            * - :py:attr:`~ansys.stk.core.graphics.CameraVideoRecording.start_recording_video`
              - Start recording a video file at the specified bit and frame rate.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CameraVideoRecording.is_recording`
              - Gets if recording is occurring or not.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CameraVideoRecording


Property detail
---------------

.. py:property:: is_recording
    :canonical: ansys.stk.core.graphics.CameraVideoRecording.is_recording
    :type: bool

    Gets if recording is occurring or not.


Method detail
-------------


.. py:method:: start_recording(self, wmv_filename: str, video_bit_rate: int, video_frame_rate: int) -> None
    :canonical: ansys.stk.core.graphics.CameraVideoRecording.start_recording

    Do not use this method, as it is deprecated. Use the overload taking a video format instead. Starts recording a file in the WMV format at the specified bit and frame rate.

    :Parameters:

    **wmv_filename** : :obj:`~str`
    **video_bit_rate** : :obj:`~int`
    **video_frame_rate** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: start_recording_frame_stack(self, file_directory: str, file_prefix: str, camera_snapshot_file_format: SNAPSHOT_FILE_FORMAT, starting_frame_number: int, number_of_frame_digits: int) -> None
    :canonical: ansys.stk.core.graphics.CameraVideoRecording.start_recording_frame_stack

    Start recording a frame stack. Each frame is saved as a separate image file. The filename of each frame is defined by a prefix followed by a frame number.

    :Parameters:

    **file_directory** : :obj:`~str`
    **file_prefix** : :obj:`~str`
    **camera_snapshot_file_format** : :obj:`~SNAPSHOT_FILE_FORMAT`
    **starting_frame_number** : :obj:`~int`
    **number_of_frame_digits** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: stop_recording(self) -> None
    :canonical: ansys.stk.core.graphics.CameraVideoRecording.stop_recording

    Stop recording.

    :Returns:

        :obj:`~None`

.. py:method:: start_recording_video(self, file_directory: str, file_prefix: str, video_format: VIDEO_FORMAT, video_bit_rate: int, video_frame_rate: int) -> None
    :canonical: ansys.stk.core.graphics.CameraVideoRecording.start_recording_video

    Start recording a video file at the specified bit and frame rate.

    :Parameters:

    **file_directory** : :obj:`~str`
    **file_prefix** : :obj:`~str`
    **video_format** : :obj:`~VIDEO_FORMAT`
    **video_bit_rate** : :obj:`~int`
    **video_frame_rate** : :obj:`~int`

    :Returns:

        :obj:`~None`

