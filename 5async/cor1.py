import asyncio

async def diz_oi():
    print('Diz oi...')
    

el = asyncio.get_event_loop()
el.run_until_complete(diz_oi())
el.close()