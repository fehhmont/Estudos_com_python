import asyncio

async def diz_oi_demorado():
    print('oi....')
    await asyncio.sleep(2)
    print('todos....')
    
    
el = asyncio.get_event_loop()
el.run_until_complete(diz_oi_demorado())
el.close()