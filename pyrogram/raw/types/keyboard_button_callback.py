from io import BytesIO
from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

class KeyboardButtonCallback(TLObject):
    """
    - ID: E62BC960
    - Layer: 225
    """
    __slots__: List[str] = ["text", "data", "requires_password", "style"]
    ID = 0xe62bc960
    QUALNAME = "types.KeyboardButtonCallback"

    def __init__(self, *, text: str, data: bytes, requires_password: Optional[bool] = None, style=None) -> None:
        self.text = text
        self.data = data
        self.requires_password = requires_password
        self.style = style

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonCallback":
        flags = Int.read(b)
        requires_password = True if flags & (1 << 0) else False
        has_style = bool(flags & (1 << 10))
        style = raw.types.KeyboardButtonStyle.read(b) if has_style else None  # ✅ BEFORE text/data
        text = String.read(b)
        data = Bytes.read(b)
        return KeyboardButtonCallback(text=text, data=data, requires_password=requires_password, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        flags = 0
        flags |= (1 << 0) if self.requires_password else 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))
        if self.style is not None:         # ✅ BEFORE text/data
            b.write(self.style.write())
        b.write(String(self.text))
        b.write(Bytes(self.data))
        return b.getvalue()
