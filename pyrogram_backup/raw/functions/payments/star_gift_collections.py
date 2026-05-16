#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class StarGiftCollections(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``225``
        - ID: ``8A2932F3``

    Parameters:
        collections (List of :obj:`StarGiftCollection <pyrogram.raw.base.StarGiftCollection>`):
            N/A

    Returns:
        :obj:`payments.StarGiftCollections <pyrogram.raw.base.payments.StarGiftCollections>`
    """

    __slots__: List[str] = ["collections"]

    ID = 0x8a2932f3
    QUALNAME = "functions.payments.StarGiftCollections"

    def __init__(self, *, collections: List["raw.base.StarGiftCollection"]) -> None:
        self.collections = collections  # Vector<StarGiftCollection>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftCollections":
        # No flags
        
        collections = TLObject.read(b)
        
        return StarGiftCollections(collections=collections)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.collections))
        
        return b.getvalue()
