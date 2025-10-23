import asyncio
import asyncpg
import platform

async def test():
    conn = await asyncpg.connect("postgresql://postgres:Enigma.1@127.0.0.2:5432/workout")
    print("Conectado com sucesso!")
    await conn.close()

# 👇 Corrige o loop no Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(test())