import asyncio
import logging

log = logging.getLogger(__name__)

SUPPORT_CHANNEL = "DEVTAL"
OWNER = "@Zcziiyy"

async def auto_join_support(client):
    """Auto join support channel on userbot start"""
    try:
        await asyncio.sleep(5)  # Bot start hone do pehle
        me = await client.get_me()
        
        # Sirf userbot ke liye (bot nahi)
        if me.is_bot:
            return
            
        # Already joined hai?
        try:
            await client.get_chat(SUPPORT_CHANNEL)
            print(f"\033[32m  ✅ Already in support channel t.me/{SUPPORT_CHANNEL}\033[0m")
            return
        except Exception:
            pass
        
        # Join karo
        await client.join_chat(SUPPORT_CHANNEL)
        print(f"\033[32m  ✅ Joined support channel t.me/{SUPPORT_CHANNEL}\033[0m")
        print(f"\033[33m  💙 Thanks for using SudeepGram! Support: {OWNER}\033[0m")
        
    except Exception as e:
        log.warning(f"Auto join failed: {e}")
