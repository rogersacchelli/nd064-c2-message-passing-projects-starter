from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionDataRequest(_message.Message):
    __slots__ = ["id", "start_date", "end_date", "distance"]
    ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    id: int
    start_date: str
    end_date: str
    distance: int
    def __init__(self, id: _Optional[int] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., distance: _Optional[int] = ...) -> None: ...

class ConnectionDataReply(_message.Message):
    __slots__ = ["id", "location_id", "coord_x", "coord_y", "creation_time"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    COORD_X_FIELD_NUMBER: _ClassVar[int]
    COORD_Y_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    location_id: int
    coord_x: float
    coord_y: float
    creation_time: str
    def __init__(self, id: _Optional[int] = ..., location_id: _Optional[int] = ..., coord_x: _Optional[float] = ..., coord_y: _Optional[float] = ..., creation_time: _Optional[str] = ...) -> None: ...
